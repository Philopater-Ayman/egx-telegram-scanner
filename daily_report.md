# Telegram-First EGX Scanner Report

Scan phase: Pre-market risk check
Generated UTC: 2026-06-16T10:33:17.333296+00:00
Generated Cairo: 2026-06-16 13:33
Run timing: target 08:45 Cairo | generated Cairo 2026-06-16 13:33 | cron 45 5 * * 0-4
Trigger: scheduled cron=45 5 * * 0-4 mapped to pre_market; Cairo now 2026-06-16 13:30

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 0
- Tradeable price/liquidity tickers: 174/190
- Top sector: Automotive & Distribution

## Market Context
- Market trend: Bearish
- Source: Mubasher EGX market page (delayed public data)
- As of: Tuesday, June 16
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 31.58% / above MA50 57.89%
- EGX70 regime: BEARISH / above MA20 47.37% / above MA50 73.68%
- Sector breadth: 19.05%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- CCAP.CA: liquidity=453453120.0 spike=0.53 score=17.3
- PHDC.CA: liquidity=419891168.0 spike=1.02 score=25.44
- COMI.CA: liquidity=370707360.0 spike=0.56 score=20.13
- HRHO.CA: liquidity=331845184.0 spike=2.38 score=22.42
- MPCO.CA: liquidity=305651072.0 spike=3.97 score=9.88

## AI Narrative
- Provider: OpenRouter OK
- Model: openai/gpt-oss-120b:free
- Summary: The scanner flags a defensive market regime – both EGX30 and EGX70 are bearish with weak breadth (19%). Consequently no new BUY signals are issued. Still, the top‑ranked stocks show bullish watch outlooks, solid liquidity spikes and support above 20‑day levels, especially in the Automotive & Distribution and Real Estate sectors.
- EGX30/EGX70 bearish trends and low sector breadth push the system into DEFENSIVE_NO_NEW_BUY risk mode.
- Automotive & Distribution leads sector breadth; MTIE.CA and GBCO.CA have strong liquidity spikes and are near support, but resistance is close.
- Real Estate shows positive 5‑day returns; PHDC.CA, EMFD.CA and ARAB.CA sit well above 20‑day support but approach resistance levels.
- Liquidity regimes range from accumulation spikes to normal tradeable levels, indicating short‑term buying interest despite overall market weakness.
- Outlook remains uncertain for the next 1‑3 days – bullish watches could reverse if broader market pressure persists.

## Top Liquidity Spikes
- ZEOT.CA: spike=31.92 liquidity=195295408.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- EASB.CA: spike=6.47 liquidity=19114400.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- MOSC.CA: spike=3.99 liquidity=26696894.0 outlook=BULLISH_WATCH score=91.0 buy_ready=False
- MPCO.CA: spike=3.97 liquidity=305651072.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- ANFI.CA: spike=3.88 liquidity=202227615.0 outlook=CONSTRUCTIVE score=61.0 buy_ready=False

## Sector Leaderboard
- #1 Automotive & Distribution: score=10.45 5d=6.42% 20d=-1.19% aboveMA50=100.0%
- #2 Real Estate: score=6.64 5d=2.02% 20d=5.26% aboveMA50=84.62%
- #3 Tourism & Leisure: score=4.09 5d=-3.06% 20d=9.1% aboveMA50=100.0%
- #4 Education: score=4.04 5d=0.22% 20d=-3.69% aboveMA50=100.0%
- #5 General / Verified EGX Expansion: score=4.0 5d=-0.39% 20d=-0.15% aboveMA50=66.35%
- #6 Food, Beverages & Tobacco: score=3.68 5d=-0.73% 20d=0.18% aboveMA50=71.43%
- #7 Industrial Goods & Cables: score=3.31 5d=-2.56% 20d=-3.39% aboveMA50=100.0%
- #8 Textiles: score=3.26 5d=-2.08% 20d=3.81% aboveMA50=75.0%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- MTIE.CA: BULLISH_WATCH score=100 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=No major short-term scanner risk flags.
- MOSC.CA: BULLISH_WATCH score=91.0 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=No major short-term scanner risk flags.
- ELWA.CA: BULLISH_WATCH score=91.0 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=No major short-term scanner risk flags.
- PHDC.CA: BULLISH_WATCH score=89.64 liquidity=TRADEABLE sector=LEADING risk=far above support
- ORHD.CA: BULLISH_WATCH score=86.64 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- MENA.CA: BULLISH_WATCH score=86.64 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- ARAB.CA: BULLISH_WATCH score=85.64 liquidity=TRADEABLE sector=LEADING risk=momentum is extended
- EPCO.CA: BULLISH_WATCH score=85.0 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=close to resistance
- RREI.CA: BULLISH_WATCH score=85.0 liquidity=TRADEABLE sector=IMPROVING risk=No major short-term scanner risk flags.
- COSG.CA: BULLISH_WATCH score=85.0 liquidity=TRADEABLE sector=IMPROVING risk=No major short-term scanner risk flags.

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- No provider failures.

## Ranked Scanner Results
- AALR.CA: score=12.0 buy_ready=False sector_rank=5 price=206.21 support=195.1 resistance=231.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:12 PM market time freshness=DELAYED_CURRENT RSI=53.35 liquidity=1396849.88 spike=0.2
- ABUK.CA: score=9.09 buy_ready=False sector_rank=20 price=71.94 support=72.7 resistance=90.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:15 PM market time freshness=DELAYED_CURRENT RSI=15.03 liquidity=79576368.0 spike=0.61
- ACAMD.CA: score=20.6 buy_ready=False sector_rank=5 price=2.36 support=2.14 resistance=2.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:16 PM market time freshness=DELAYED_CURRENT RSI=58.46 liquidity=73322616.0 spike=0.57
- ACGC.CA: score=13.28 buy_ready=False sector_rank=8 price=9.41 support=8.95 resistance=10.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:15 PM market time freshness=DELAYED_CURRENT RSI=40.88 liquidity=4972908.0 spike=0.09
- ADCI.CA: score=16.06 buy_ready=False sector_rank=5 price=225.25 support=202.22 resistance=230.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:15 PM market time freshness=DELAYED_CURRENT RSI=71.08 liquidity=5459340.0 spike=0.75
- ADIB.CA: score=20.13 buy_ready=False sector_rank=11 price=47.51 support=44.01 resistance=48.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:15 PM market time freshness=DELAYED_CURRENT RSI=35.44 liquidity=44146072.0 spike=0.35
- ADPC.CA: score=12.99 buy_ready=False sector_rank=5 price=3.61 support=3.45 resistance=4.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:16 PM market time freshness=DELAYED_CURRENT RSI=45.76 liquidity=7386818.5 spike=0.29
- AFDI.CA: score=12.26 buy_ready=False sector_rank=5 price=42.3 support=40.15 resistance=46.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:12 PM market time freshness=DELAYED_CURRENT RSI=55.48 liquidity=3658860.75 spike=0.22
- AFMC.CA: score=9.25 buy_ready=False sector_rank=5 price=71.42 support=67.0 resistance=80.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=56.21 liquidity=647269.19 spike=0.11
- AJWA.CA: score=7.94 buy_ready=False sector_rank=5 price=181.02 support=172.98 resistance=188.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=51866272.0 spike=2.17
- ALCN.CA: score=11.02 buy_ready=False sector_rank=17 price=28.5 support=25.51 resistance=33.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:15 PM market time freshness=DELAYED_CURRENT RSI=47.7 liquidity=6574316.0 spike=0.38
- ALUM.CA: score=12.04 buy_ready=False sector_rank=5 price=23.23 support=23.05 resistance=26.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=53.51 liquidity=3435431.5 spike=0.2
- AMER.CA: score=21.4 buy_ready=False sector_rank=2 price=2.57 support=2.52 resistance=3.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:15 PM market time freshness=DELAYED_CURRENT RSI=42.39 liquidity=63975068.0 spike=0.6
- AMES.CA: score=5.4 buy_ready=False sector_rank=5 price=49.63 support=48.0 resistance=55.69 source=Yahoo Finance as_of=2026-06-13T21:00:00+00:00 freshness=FRESH RSI=29.71 liquidity=1801072.74 spike=0.55
- AMIA.CA: score=17.96 buy_ready=False sector_rank=5 price=9.23 support=8.54 resistance=9.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:15 PM market time freshness=DELAYED_CURRENT RSI=70.87 liquidity=7360371.5 spike=0.41
- AMOC.CA: score=10.21 buy_ready=False sector_rank=10 price=7.87 support=7.84 resistance=9.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:15 PM market time freshness=DELAYED_CURRENT RSI=32.67 liquidity=22192666.0 spike=0.29
- ANFI.CA: score=24.6 buy_ready=False sector_rank=5 price=28.75 support=13.73 resistance=28.75 source=Yahoo Finance as_of=2026-06-14T21:00:00+00:00 freshness=FRESH RSI=96.86 liquidity=202227615.0 spike=3.88
- APSW.CA: score=2.47 buy_ready=False sector_rank=5 price=8.51 support=8.24 resistance=9.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=31.58 liquidity=1648923.63 spike=1.61
- ARAB.CA: score=25.4 buy_ready=False sector_rank=2 price=0.22 support=0.19 resistance=0.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:15 PM market time freshness=DELAYED_CURRENT RSI=69.44 liquidity=74270152.0 spike=0.85
- ARCC.CA: score=14.19 buy_ready=False sector_rank=14 price=56.14 support=53.35 resistance=60.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:15 PM market time freshness=DELAYED_CURRENT RSI=53.41 liquidity=6473147.5 spike=0.18
- AREH.CA: score=5.6 buy_ready=False sector_rank=5 price=1.6 support=1.59 resistance=1.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=18514792.0 spike=0.69
- ARVA.CA: score=18.22 buy_ready=False sector_rank=5 price=11.36 support=7.71 resistance=13.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=79.19 liquidity=37112072.0 spike=1.31
- ASCM.CA: score=19.6 buy_ready=False sector_rank=5 price=59.41 support=47.3 resistance=61.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:15 PM market time freshness=DELAYED_CURRENT RSI=80.32 liquidity=33936300.0 spike=0.5
- ASPI.CA: score=22.6 buy_ready=False sector_rank=5 price=0.31 support=0.25 resistance=0.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:16 PM market time freshness=DELAYED_CURRENT RSI=61.57 liquidity=21035168.0 spike=0.31
- ATLC.CA: score=15.91 buy_ready=False sector_rank=15 price=5.12 support=4.7 resistance=5.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:06 PM market time freshness=DELAYED_CURRENT RSI=67.29 liquidity=4256527.0 spike=0.9
- ATQA.CA: score=18.79 buy_ready=False sector_rank=20 price=9.79 support=9.02 resistance=10.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:16 PM market time freshness=DELAYED_CURRENT RSI=49.32 liquidity=49510076.0 spike=1.35
- AXPH.CA: score=9.47 buy_ready=False sector_rank=5 price=1115.52 support=1111.0 resistance=1185.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:12 PM market time freshness=DELAYED_CURRENT RSI=40.02 liquidity=870575.19 spike=0.27
- BINV.CA: score=15.81 buy_ready=False sector_rank=19 price=47.07 support=40.8 resistance=49.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:15 PM market time freshness=DELAYED_CURRENT RSI=66.54 liquidity=6509443.5 spike=0.61
- BIOC.CA: score=10.86 buy_ready=False sector_rank=5 price=72.11 support=68.34 resistance=79.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:11 PM market time freshness=DELAYED_CURRENT RSI=51.09 liquidity=2258375.25 spike=0.43
- BTFH.CA: score=13.66 buy_ready=False sector_rank=15 price=3.02 support=2.96 resistance=3.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:15 PM market time freshness=DELAYED_CURRENT RSI=45.59 liquidity=67824728.0 spike=0.32
- CAED.CA: score=9.73 buy_ready=False sector_rank=5 price=70.86 support=67.21 resistance=79.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=39.83 liquidity=1131376.5 spike=0.17
- CANA.CA: score=13.82 buy_ready=False sector_rank=11 price=37.29 support=34.07 resistance=39.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=56.38 liquidity=1695975.13 spike=0.12
- CCAP.CA: score=17.3 buy_ready=False sector_rank=19 price=5.1 support=4.92 resistance=5.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:15 PM market time freshness=DELAYED_CURRENT RSI=47.49 liquidity=453453120.0 spike=0.53
- CCRS.CA: score=20.6 buy_ready=False sector_rank=5 price=2.48 support=2.22 resistance=2.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:11 PM market time freshness=DELAYED_CURRENT RSI=45.76 liquidity=12083648.0 spike=0.47
- CEFM.CA: score=10.02 buy_ready=False sector_rank=5 price=104.02 support=100.53 resistance=119.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:16 PM market time freshness=DELAYED_CURRENT RSI=51.29 liquidity=1420882.0 spike=0.39
- CERA.CA: score=9.98 buy_ready=False sector_rank=5 price=1.26 support=1.17 resistance=1.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:16 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=43357360.0 spike=3.19
- CFGH.CA: score=-0.4 buy_ready=False sector_rank=5 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance as_of=2026-06-13T21:00:00+00:00 freshness=FRESH RSI=0.0 liquidity=1904.14 spike=0.31
- CICH.CA: score=0.45 buy_ready=False sector_rank=15 price=11.54 support=11.1 resistance=13.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=23.96 liquidity=794181.44 spike=0.23
- CIEB.CA: score=8.47 buy_ready=False sector_rank=11 price=23.5 support=23.27 resistance=24.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=56.74 liquidity=3340568.25 spike=0.45
- CIRA.CA: score=12.49 buy_ready=False sector_rank=4 price=26.25 support=25.23 resistance=28.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:10 PM market time freshness=DELAYED_CURRENT RSI=46.14 liquidity=3873859.0 spike=0.15
- CLHO.CA: score=14.66 buy_ready=False sector_rank=9 price=15.54 support=14.25 resistance=16.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=55.46 liquidity=4388688.5 spike=0.15
- CNFN.CA: score=7.93 buy_ready=False sector_rank=15 price=4.44 support=4.36 resistance=4.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=42.65 liquidity=4278294.5 spike=0.27
- COMI.CA: score=20.13 buy_ready=False sector_rank=11 price=134.0 support=129.8 resistance=136.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=46.42 liquidity=370707360.0 spike=0.56
- COPR.CA: score=17.6 buy_ready=False sector_rank=5 price=0.36 support=0.32 resistance=0.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:15 PM market time freshness=DELAYED_CURRENT RSI=56.25 liquidity=25024784.0 spike=0.61
- COSG.CA: score=20.8 buy_ready=False sector_rank=5 price=1.62 support=1.49 resistance=1.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:16 PM market time freshness=DELAYED_CURRENT RSI=57.14 liquidity=75607400.0 spike=1.1
- CPCI.CA: score=9.76 buy_ready=False sector_rank=5 price=362.74 support=345.0 resistance=368.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:11 PM market time freshness=DELAYED_CURRENT RSI=71.26 liquidity=1160410.75 spike=0.43
- CSAG.CA: score=11.57 buy_ready=False sector_rank=17 price=31.2 support=30.08 resistance=32.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:11 PM market time freshness=DELAYED_CURRENT RSI=53.78 liquidity=4124139.75 spike=0.3
- DAPH.CA: score=15.09 buy_ready=False sector_rank=5 price=80.91 support=76.6 resistance=89.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:15 PM market time freshness=DELAYED_CURRENT RSI=39.56 liquidity=9485008.0 spike=0.32
- DEIN.CA: score=6.6 buy_ready=False sector_rank=5 price=11.38 support=11.38 resistance=13.65 source=Yahoo Finance as_of=2026-06-13T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- DOMT.CA: score=0.95 buy_ready=False sector_rank=6 price=24.47 support=23.7 resistance=26.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=26.34 liquidity=478615.63 spike=0.19
- DSCW.CA: score=18.6 buy_ready=False sector_rank=5 price=1.85 support=1.71 resistance=1.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:16 PM market time freshness=DELAYED_CURRENT RSI=58.06 liquidity=49854924.0 spike=0.97
- DTPP.CA: score=1.41 buy_ready=False sector_rank=5 price=116.53 support=114.0 resistance=137.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT RSI=17.35 liquidity=808134.81 spike=0.4
- EALR.CA: score=13.04 buy_ready=False sector_rank=5 price=358.4 support=346.01 resistance=383.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:12 PM market time freshness=DELAYED_CURRENT RSI=48.61 liquidity=2435687.5 spike=0.55
- EASB.CA: score=10.6 buy_ready=False sector_rank=5 price=7.16 support=5.9 resistance=7.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:16 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=19114400.0 spike=6.47
- EAST.CA: score=20.47 buy_ready=False sector_rank=6 price=39.9 support=37.01 resistance=39.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:10 PM market time freshness=DELAYED_CURRENT RSI=47.08 liquidity=25558188.0 spike=0.39
- EBSC.CA: score=12.23 buy_ready=False sector_rank=5 price=1.93 support=1.64 resistance=2.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=70.37 liquidity=1630157.75 spike=0.61
- ECAP.CA: score=14.02 buy_ready=False sector_rank=5 price=32.41 support=28.7 resistance=32.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=91.4 liquidity=4421772.0 spike=0.85
- EDFM.CA: score=12.12 buy_ready=False sector_rank=5 price=335.82 support=320.2 resistance=355.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:15 PM market time freshness=DELAYED_CURRENT RSI=56.59 liquidity=884312.13 spike=1.32
- EEII.CA: score=17.58 buy_ready=False sector_rank=5 price=2.43 support=2.27 resistance=2.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:16 PM market time freshness=DELAYED_CURRENT RSI=57.45 liquidity=6982687.0 spike=0.36
- EFIC.CA: score=-0.67 buy_ready=False sector_rank=20 price=203.68 support=192.01 resistance=219.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=16.09 liquidity=1236371.13 spike=0.36
- EFID.CA: score=18.47 buy_ready=False sector_rank=6 price=28.31 support=27.06 resistance=29.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:15 PM market time freshness=DELAYED_CURRENT RSI=48.95 liquidity=21711160.0 spike=0.28
- EFIH.CA: score=17.99 buy_ready=False sector_rank=12 price=21.31 support=20.2 resistance=22.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=40.17 liquidity=10339057.0 spike=0.18
- EGAL.CA: score=9.09 buy_ready=False sector_rank=20 price=300.68 support=297.1 resistance=335.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=24.21 liquidity=20547382.0 spike=0.22
- EGAS.CA: score=14.36 buy_ready=False sector_rank=10 price=51.89 support=46.51 resistance=55.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:12 PM market time freshness=DELAYED_CURRENT RSI=73.53 liquidity=2150320.75 spike=0.18
- EGBE.CA: score=8.18 buy_ready=False sector_rank=11 price=0.44 support=0.44 resistance=0.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:07 PM market time freshness=DELAYED_CURRENT RSI=43.01 liquidity=50603.8 spike=0.36
- EGCH.CA: score=17.09 buy_ready=False sector_rank=20 price=13.62 support=13.2 resistance=15.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=43.39 liquidity=32030564.0 spike=0.29
- EGSA.CA: score=2.41 buy_ready=False sector_rank=18 price=8.78 support=8.3 resistance=9.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:11 PM market time freshness=DELAYED_CURRENT RSI=21.87 liquidity=11936.48 spike=0.77
- EGTS.CA: score=21.4 buy_ready=False sector_rank=2 price=17.83 support=14.72 resistance=22.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=48.17 liquidity=28255464.0 spike=0.23
- EHDR.CA: score=20.6 buy_ready=False sector_rank=5 price=2.73 support=2.25 resistance=2.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=73.39 liquidity=17899048.0 spike=0.31
- EKHO.CA: score=10.21 buy_ready=False sector_rank=10 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-06-13T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=19.32 buy_ready=False sector_rank=7 price=2.15 support=2.06 resistance=2.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:15 PM market time freshness=DELAYED_CURRENT RSI=56.67 liquidity=13322131.0 spike=0.5
- ELKA.CA: score=19.6 buy_ready=False sector_rank=5 price=1.31 support=1.12 resistance=1.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:16 PM market time freshness=DELAYED_CURRENT RSI=66.67 liquidity=42447776.0 spike=0.95
- ELNA.CA: score=5.11 buy_ready=False sector_rank=5 price=38.4 support=37.11 resistance=41.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:12 PM market time freshness=DELAYED_CURRENT RSI=39.76 liquidity=414742.16 spike=1.05
- ELSH.CA: score=5.72 buy_ready=False sector_rank=5 price=13.9 support=12.85 resistance=13.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:16 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=184183248.0 spike=1.06
- ELWA.CA: score=19.18 buy_ready=False sector_rank=5 price=2.1 support=1.79 resistance=2.22 source=Yahoo Finance as_of=2026-06-14T21:00:00+00:00 freshness=FRESH RSI=60.61 liquidity=5095299.07 spike=1.74
- EMFD.CA: score=25.4 buy_ready=False sector_rank=2 price=12.45 support=9.83 resistance=12.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:15 PM market time freshness=DELAYED_CURRENT RSI=70.0 liquidity=210003376.0 spike=0.8
- ENGC.CA: score=15.68 buy_ready=False sector_rank=5 price=36.02 support=32.31 resistance=35.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:16 PM market time freshness=DELAYED_CURRENT RSI=65.98 liquidity=5075672.5 spike=0.38
- EOSB.CA: score=14.71 buy_ready=False sector_rank=5 price=1.48 support=1.34 resistance=1.55 source=Yahoo Finance as_of=2026-06-14T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=110727.68 spike=0.93
- EPCO.CA: score=24.32 buy_ready=False sector_rank=5 price=9.53 support=8.56 resistance=9.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:16 PM market time freshness=DELAYED_CURRENT RSI=47.83 liquidity=31935654.0 spike=2.86
- EPPK.CA: score=6.02 buy_ready=False sector_rank=5 price=12.12 support=11.67 resistance=13.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:11 PM market time freshness=DELAYED_CURRENT RSI=45.61 liquidity=424404.13 spike=0.37
- ETEL.CA: score=9.4 buy_ready=False sector_rank=18 price=92.74 support=89.61 resistance=98.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:15 PM market time freshness=DELAYED_CURRENT RSI=31.37 liquidity=44581596.0 spike=0.54
- ETRS.CA: score=19.6 buy_ready=False sector_rank=5 price=10.07 support=7.37 resistance=9.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:16 PM market time freshness=DELAYED_CURRENT RSI=77.99 liquidity=22907930.0 spike=0.39
- EXPA.CA: score=18.13 buy_ready=False sector_rank=11 price=18.69 support=18.31 resistance=20.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:12 PM market time freshness=DELAYED_CURRENT RSI=45.57 liquidity=23944896.0 spike=0.67
- FAIT.CA: score=9.38 buy_ready=False sector_rank=11 price=37.23 support=35.01 resistance=38.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=42.86 liquidity=1251264.0 spike=0.21
- FAITA.CA: score=12.16 buy_ready=False sector_rank=11 price=0.99 support=0.98 resistance=1.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=60.0 liquidity=31802.47 spike=0.71
- FERC.CA: score=1.2 buy_ready=False sector_rank=20 price=75.63 support=75.0 resistance=80.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=28.35 liquidity=3103057.25 spike=0.69
- FWRY.CA: score=9.99 buy_ready=False sector_rank=12 price=19.03 support=17.71 resistance=20.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=29.98 liquidity=188354416.0 spike=0.64
- GBCO.CA: score=24.4 buy_ready=False sector_rank=1 price=28.13 support=25.25 resistance=29.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:15 PM market time freshness=DELAYED_CURRENT RSI=72.42 liquidity=27219790.0 spike=0.23
- GDWA.CA: score=20.16 buy_ready=False sector_rank=5 price=0.82 support=0.77 resistance=0.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:16 PM market time freshness=DELAYED_CURRENT RSI=57.14 liquidity=17109358.0 spike=1.28
- GGCC.CA: score=11.93 buy_ready=False sector_rank=5 price=0.41 support=0.39 resistance=0.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:16 PM market time freshness=DELAYED_CURRENT RSI=57.3 liquidity=4328530.0 spike=0.58
- GIHD.CA: score=12.4 buy_ready=False sector_rank=5 price=41.72 support=35.15 resistance=43.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=58.24 liquidity=1796576.0 spike=0.43
- GMCI.CA: score=11.03 buy_ready=False sector_rank=5 price=1.79 support=1.68 resistance=1.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=52.78 liquidity=407940.94 spike=1.01
- GRCA.CA: score=11.96 buy_ready=False sector_rank=5 price=55.41 support=50.2 resistance=60.5 source=Yahoo Finance as_of=2026-06-14T21:00:00+00:00 freshness=FRESH RSI=35.59 liquidity=5875066.87 spike=1.24
- GSSC.CA: score=1.7 buy_ready=False sector_rank=5 price=247.08 support=228.1 resistance=268.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=22.42 liquidity=1098868.25 spike=0.21
- GTWL.CA: score=17.9 buy_ready=False sector_rank=5 price=48.63 support=45.47 resistance=58.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:16 PM market time freshness=DELAYED_CURRENT RSI=29.05 liquidity=22233018.0 spike=3.15
- HDBK.CA: score=9.59 buy_ready=False sector_rank=11 price=153.04 support=146.2 resistance=154.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:15 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=41443316.0 spike=3.23
- HELI.CA: score=21.4 buy_ready=False sector_rank=2 price=6.45 support=6.28 resistance=6.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=55.42 liquidity=64502968.0 spike=0.42
- HRHO.CA: score=22.42 buy_ready=False sector_rank=15 price=27.66 support=25.8 resistance=28.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:15 PM market time freshness=DELAYED_CURRENT RSI=53.5 liquidity=331845184.0 spike=2.38
- ICID.CA: score=10.18 buy_ready=False sector_rank=5 price=7.11 support=4.5 resistance=7.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=87.09 liquidity=2583473.75 spike=0.16
- IDRE.CA: score=18.6 buy_ready=False sector_rank=5 price=44.05 support=41.01 resistance=47.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:10 PM market time freshness=DELAYED_CURRENT RSI=40.08 liquidity=10345281.0 spike=0.32
- IFAP.CA: score=5.63 buy_ready=False sector_rank=13 price=19.39 support=16.5 resistance=23.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:15 PM market time freshness=DELAYED_CURRENT RSI=35.69 liquidity=1753589.88 spike=0.2
- INFI.CA: score=3.88 buy_ready=False sector_rank=5 price=98.36 support=97.0 resistance=109.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:12 PM market time freshness=DELAYED_CURRENT RSI=24.0 liquidity=1276302.63 spike=0.09
- IRON.CA: score=15.47 buy_ready=False sector_rank=20 price=32.86 support=31.3 resistance=35.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:15 PM market time freshness=DELAYED_CURRENT RSI=43.27 liquidity=9840748.0 spike=1.27
- ISMA.CA: score=23.86 buy_ready=False sector_rank=5 price=29.95 support=23.1 resistance=31.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:17 PM market time freshness=DELAYED_CURRENT RSI=88.93 liquidity=124015640.0 spike=3.13
- ISMQ.CA: score=19.21 buy_ready=False sector_rank=20 price=8.23 support=7.27 resistance=8.62 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:16 PM market time freshness=DELAYED_CURRENT RSI=65.57 liquidity=73102896.0 spike=1.06
- ISPH.CA: score=20.27 buy_ready=False sector_rank=9 price=12.19 support=11.12 resistance=12.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:15 PM market time freshness=DELAYED_CURRENT RSI=60.92 liquidity=31371750.0 spike=0.23
- JUFO.CA: score=22.47 buy_ready=False sector_rank=6 price=30.32 support=26.51 resistance=30.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=70.99 liquidity=13900629.0 spike=0.34
- KABO.CA: score=12.88 buy_ready=False sector_rank=8 price=6.18 support=5.92 resistance=6.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=57.27 liquidity=4578948.5 spike=0.22
- KWIN.CA: score=16.15 buy_ready=False sector_rank=5 price=72.64 support=69.0 resistance=77.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:16 PM market time freshness=DELAYED_CURRENT RSI=65.36 liquidity=3548784.5 spike=0.75
- KZPC.CA: score=11.81 buy_ready=False sector_rank=5 price=10.59 support=10.3 resistance=11.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:17 PM market time freshness=DELAYED_CURRENT RSI=57.05 liquidity=1205351.63 spike=0.11
- LCSW.CA: score=12.08 buy_ready=False sector_rank=14 price=27.22 support=26.0 resistance=28.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:59 AM market time freshness=DELAYED_CURRENT RSI=38.69 liquidity=4365166.0 spike=0.38
- LUTS.CA: score=20.28 buy_ready=False sector_rank=5 price=0.75 support=0.54 resistance=0.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:17 PM market time freshness=DELAYED_CURRENT RSI=88.76 liquidity=44067184.0 spike=1.34
- MAAL.CA: score=5.74 buy_ready=False sector_rank=5 price=6.1 support=5.82 resistance=6.23 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:16 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=13821770.0 spike=1.07
- MASR.CA: score=20.6 buy_ready=False sector_rank=5 price=7.24 support=6.54 resistance=7.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:16 PM market time freshness=DELAYED_CURRENT RSI=52.08 liquidity=45361052.0 spike=0.83
- MBSC.CA: score=19.71 buy_ready=False sector_rank=14 price=253.51 support=251.52 resistance=251.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:15 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=22547086.0 spike=1.0
- MCQE.CA: score=2.89 buy_ready=False sector_rank=14 price=178.74 support=174.0 resistance=201.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:15 PM market time freshness=DELAYED_CURRENT RSI=27.73 liquidity=3181040.75 spike=0.18
- MCRO.CA: score=17.6 buy_ready=False sector_rank=5 price=1.25 support=1.2 resistance=1.31 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:17 PM market time freshness=DELAYED_CURRENT RSI=47.62 liquidity=16001098.0 spike=0.31
- MENA.CA: score=15.05 buy_ready=False sector_rank=2 price=6.74 support=5.91 resistance=7.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=55.67 liquidity=1648757.5 spike=0.1
- MEPA.CA: score=12.12 buy_ready=False sector_rank=5 price=1.7 support=1.63 resistance=1.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=55.56 liquidity=3520191.75 spike=0.2
- MFPC.CA: score=9.09 buy_ready=False sector_rank=20 price=37.17 support=36.9 resistance=46.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=4.92 liquidity=46134884.0 spike=0.53
- MFSC.CA: score=5.28 buy_ready=False sector_rank=5 price=44.56 support=43.0 resistance=65.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=29.01 liquidity=1681488.63 spike=0.11
- MHOT.CA: score=16.8 buy_ready=False sector_rank=3 price=30.01 support=26.3 resistance=34.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:12 PM market time freshness=DELAYED_CURRENT RSI=44.65 liquidity=7166741.5 spike=0.33
- MICH.CA: score=15.26 buy_ready=False sector_rank=5 price=37.62 support=35.05 resistance=40.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=66.34 liquidity=4657984.5 spike=0.32
- MILS.CA: score=18.6 buy_ready=False sector_rank=5 price=142.01 support=127.01 resistance=151.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=69.34 liquidity=11256780.0 spike=0.57
- MIPH.CA: score=11.98 buy_ready=False sector_rank=9 price=665.27 support=640.0 resistance=700.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:15 PM market time freshness=DELAYED_CURRENT RSI=54.88 liquidity=1712915.63 spike=0.59
- MOED.CA: score=16.76 buy_ready=False sector_rank=5 price=0.71 support=0.65 resistance=0.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:17 PM market time freshness=DELAYED_CURRENT RSI=47.15 liquidity=13410677.0 spike=1.08
- MOIL.CA: score=8.22 buy_ready=False sector_rank=10 price=0.47 support=0.44 resistance=0.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:15 PM market time freshness=DELAYED_CURRENT RSI=56.45 liquidity=16456.37 spike=0.1
- MOIN.CA: score=8.86 buy_ready=False sector_rank=5 price=24.31 support=24.1 resistance=26.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:00 PM market time freshness=DELAYED_CURRENT RSI=40.38 liquidity=1257192.88 spike=0.72
- MOSC.CA: score=25.6 buy_ready=False sector_rank=5 price=288.08 support=246.6 resistance=318.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=60.53 liquidity=26696894.0 spike=3.99
- MPCI.CA: score=18.6 buy_ready=False sector_rank=5 price=219.0 support=197.0 resistance=238.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:16 PM market time freshness=DELAYED_CURRENT RSI=67.25 liquidity=54128084.0 spike=0.61
- MPCO.CA: score=9.88 buy_ready=False sector_rank=13 price=1.97 support=1.95 resistance=2.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:15 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=305651072.0 spike=3.97
- MPRC.CA: score=19.75 buy_ready=False sector_rank=5 price=32.41 support=30.61 resistance=34.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:12 PM market time freshness=DELAYED_CURRENT RSI=63.94 liquidity=9154399.0 spike=0.44
- MTIE.CA: score=27.6 buy_ready=False sector_rank=1 price=9.45 support=8.65 resistance=9.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:15 PM market time freshness=DELAYED_CURRENT RSI=54.86 liquidity=49330300.0 spike=2.6
- NAHO.CA: score=4.6 buy_ready=False sector_rank=5 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance as_of=2026-06-13T21:00:00+00:00 freshness=FRESH RSI=42.86 liquidity=682.27 spike=0.02
- NCCW.CA: score=19.43 buy_ready=False sector_rank=5 price=6.29 support=5.13 resistance=6.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:16 PM market time freshness=DELAYED_CURRENT RSI=73.64 liquidity=8828984.0 spike=0.32
- NEDA.CA: score=10.95 buy_ready=False sector_rank=5 price=2.81 support=2.65 resistance=2.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:11 PM market time freshness=DELAYED_CURRENT RSI=53.57 liquidity=348801.72 spike=0.69
- NHPS.CA: score=9.36 buy_ready=False sector_rank=5 price=68.29 support=65.03 resistance=72.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:11 PM market time freshness=DELAYED_CURRENT RSI=40.0 liquidity=1757105.5 spike=0.34
- NINH.CA: score=5.22 buy_ready=False sector_rank=5 price=17.65 support=16.8 resistance=19.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=34.72 liquidity=1623691.75 spike=0.22
- NIPH.CA: score=18.27 buy_ready=False sector_rank=9 price=161.1 support=155.1 resistance=176.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:15 PM market time freshness=DELAYED_CURRENT RSI=52.23 liquidity=30589798.0 spike=0.3
- OBRI.CA: score=17.07 buy_ready=False sector_rank=5 price=36.19 support=33.63 resistance=38.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:17 PM market time freshness=DELAYED_CURRENT RSI=51.18 liquidity=7469964.0 spike=0.57
- OCDI.CA: score=18.4 buy_ready=False sector_rank=2 price=20.77 support=20.0 resistance=22.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=45.76 liquidity=10711219.0 spike=0.3
- OCPH.CA: score=5.01 buy_ready=False sector_rank=5 price=346.93 support=337.0 resistance=389.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=27.26 liquidity=1414380.75 spike=0.2
- ODIN.CA: score=21.28 buy_ready=False sector_rank=5 price=2.2 support=1.89 resistance=2.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=68.75 liquidity=14615859.0 spike=1.34
- OFH.CA: score=14.1 buy_ready=False sector_rank=5 price=0.62 support=0.59 resistance=0.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:16 PM market time freshness=DELAYED_CURRENT RSI=54.78 liquidity=8499612.0 spike=0.37
- OIH.CA: score=8.37 buy_ready=False sector_rank=19 price=1.38 support=1.33 resistance=1.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=34.29 liquidity=9070678.0 spike=0.1
- OLFI.CA: score=20.47 buy_ready=False sector_rank=6 price=21.94 support=21.0 resistance=23.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=74.01 liquidity=15701477.0 spike=0.79
- ORAS.CA: score=4.6 buy_ready=False sector_rank=16 price=783.79 support=780.01 resistance=788.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:15 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=79291128.0 spike=1.0
- ORHD.CA: score=23.4 buy_ready=False sector_rank=2 price=37.51 support=33.09 resistance=39.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:15 PM market time freshness=DELAYED_CURRENT RSI=59.12 liquidity=78170992.0 spike=0.42
- ORWE.CA: score=19.99 buy_ready=False sector_rank=8 price=23.23 support=21.6 resistance=24.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=61.86 liquidity=9688198.0 spike=0.22
- PHAR.CA: score=13.73 buy_ready=False sector_rank=9 price=84.0 support=83.02 resistance=91.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:15 PM market time freshness=DELAYED_CURRENT RSI=49.27 liquidity=8461560.0 spike=0.27
- PHDC.CA: score=25.44 buy_ready=False sector_rank=2 price=16.0 support=13.01 resistance=16.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:15 PM market time freshness=DELAYED_CURRENT RSI=59.77 liquidity=419891168.0 spike=1.02
- PHTV.CA: score=6.26 buy_ready=False sector_rank=5 price=221.5 support=219.0 resistance=224.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:17 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=18530402.0 spike=1.33
- POUL.CA: score=18.47 buy_ready=False sector_rank=6 price=36.19 support=34.8 resistance=38.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:15 PM market time freshness=DELAYED_CURRENT RSI=35.8 liquidity=23265148.0 spike=0.52
- PRCL.CA: score=19.71 buy_ready=False sector_rank=14 price=24.9 support=21.01 resistance=28.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=62.78 liquidity=15086718.0 spike=0.53
- PRDC.CA: score=8.64 buy_ready=False sector_rank=2 price=7.71 support=6.6 resistance=7.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:15 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=100271568.0 spike=1.12
- PRMH.CA: score=6.3 buy_ready=False sector_rank=5 price=2.95 support=2.78 resistance=3.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:17 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=33115886.0 spike=1.35
- RACC.CA: score=5.98 buy_ready=False sector_rank=5 price=9.77 support=9.38 resistance=10.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:17 PM market time freshness=DELAYED_CURRENT RSI=26.09 liquidity=2375514.25 spike=0.21
- RAKT.CA: score=5.81 buy_ready=False sector_rank=5 price=23.1 support=22.1 resistance=25.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:10 PM market time freshness=DELAYED_CURRENT RSI=44.37 liquidity=449619.41 spike=1.38
- RAYA.CA: score=11.57 buy_ready=False sector_rank=21 price=7.09 support=6.7 resistance=8.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=30.28 liquidity=35533508.0 spike=0.36
- RMDA.CA: score=20.06 buy_ready=False sector_rank=9 price=5.12 support=4.92 resistance=5.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=53.61 liquidity=9785191.0 spike=0.11
- ROTO.CA: score=20.6 buy_ready=False sector_rank=5 price=35.19 support=32.66 resistance=35.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:15 PM market time freshness=DELAYED_CURRENT RSI=56.22 liquidity=10889679.0 spike=0.82
- RREI.CA: score=21.5 buy_ready=False sector_rank=5 price=3.6 support=3.32 resistance=3.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:16 PM market time freshness=DELAYED_CURRENT RSI=57.32 liquidity=31172804.0 spike=1.45
- RTVC.CA: score=13.92 buy_ready=False sector_rank=5 price=3.87 support=3.75 resistance=4.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:12 PM market time freshness=DELAYED_CURRENT RSI=49.28 liquidity=4316739.5 spike=0.63
- RUBX.CA: score=9.04 buy_ready=False sector_rank=5 price=9.99 support=9.8 resistance=11.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:17 PM market time freshness=DELAYED_CURRENT RSI=43.87 liquidity=4441574.5 spike=0.38
- SAUD.CA: score=7.87 buy_ready=False sector_rank=11 price=21.89 support=20.82 resistance=23.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=36.86 liquidity=2742647.0 spike=0.2
- SCEM.CA: score=6.34 buy_ready=False sector_rank=14 price=61.86 support=59.3 resistance=67.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:16 PM market time freshness=DELAYED_CURRENT RSI=38.15 liquidity=1627429.88 spike=0.04
- SCFM.CA: score=6.99 buy_ready=False sector_rank=5 price=254.2 support=248.1 resistance=296.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:07 PM market time freshness=DELAYED_CURRENT RSI=35.98 liquidity=1385038.75 spike=0.11
- SCTS.CA: score=6.76 buy_ready=False sector_rank=4 price=587.62 support=590.01 resistance=689.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=29.2 liquidity=3147654.75 spike=0.46
- SDTI.CA: score=15.54 buy_ready=False sector_rank=5 price=47.16 support=43.4 resistance=47.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:16 PM market time freshness=DELAYED_CURRENT RSI=71.43 liquidity=2940944.0 spike=0.18
- SEIG.CA: score=9.69 buy_ready=False sector_rank=5 price=182.28 support=173.35 resistance=205.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:16 PM market time freshness=DELAYED_CURRENT RSI=53.04 liquidity=1086126.13 spike=0.21
- SIPC.CA: score=15.84 buy_ready=False sector_rank=5 price=3.45 support=3.4 resistance=3.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:16 PM market time freshness=DELAYED_CURRENT RSI=45.28 liquidity=13872322.0 spike=1.12
- SKPC.CA: score=13.09 buy_ready=False sector_rank=20 price=16.25 support=16.29 resistance=18.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=36.29 liquidity=14385790.0 spike=0.25
- SMFR.CA: score=9.32 buy_ready=False sector_rank=5 price=204.56 support=192.0 resistance=222.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=39.88 liquidity=717522.88 spike=0.12
- SNFC.CA: score=10.15 buy_ready=False sector_rank=5 price=12.24 support=11.68 resistance=12.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=48.64 liquidity=1553693.25 spike=0.06
- SPIN.CA: score=1.69 buy_ready=False sector_rank=8 price=13.98 support=13.61 resistance=15.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:25 AM market time freshness=DELAYED_CURRENT RSI=30.56 liquidity=1389966.5 spike=0.3
- SPMD.CA: score=10.72 buy_ready=False sector_rank=5 price=0.41 support=0.38 resistance=0.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:16 PM market time freshness=DELAYED_CURRENT RSI=45.56 liquidity=2119815.5 spike=0.09
- SUGR.CA: score=6.2 buy_ready=False sector_rank=6 price=48.58 support=48.0 resistance=52.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=53.03 liquidity=1729177.0 spike=0.11
- SVCE.CA: score=5.6 buy_ready=False sector_rank=5 price=9.28 support=9.0 resistance=9.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:16 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=70361384.0 spike=0.79
- SWDY.CA: score=12.75 buy_ready=False sector_rank=7 price=86.22 support=84.01 resistance=90.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:15 PM market time freshness=DELAYED_CURRENT RSI=47.16 liquidity=4426518.5 spike=0.19
- TALM.CA: score=13.47 buy_ready=False sector_rank=4 price=16.31 support=15.12 resistance=16.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=75.86 liquidity=5850636.5 spike=0.69
- TMGH.CA: score=21.4 buy_ready=False sector_rank=2 price=95.3 support=91.87 resistance=101.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:15 PM market time freshness=DELAYED_CURRENT RSI=47.36 liquidity=223828256.0 spike=0.49
- TRTO.CA: score=9.0 buy_ready=False sector_rank=5 price=0.03 support=0.03 resistance=0.04 source=Yahoo Finance as_of=2026-06-13T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=1849.87 spike=2.2
- UEFM.CA: score=0.07 buy_ready=False sector_rank=5 price=468.67 support=455.6 resistance=500.0 source=Yahoo Finance as_of=2026-06-13T21:00:00+00:00 freshness=FRESH RSI=27.33 liquidity=471482.03 spike=0.75
- UEGC.CA: score=22.6 buy_ready=False sector_rank=5 price=1.46 support=1.3 resistance=1.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:17 PM market time freshness=DELAYED_CURRENT RSI=61.76 liquidity=14005704.0 spike=0.55
- UNIP.CA: score=10.5 buy_ready=False sector_rank=5 price=0.34 support=0.33 resistance=0.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:17 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=69937816.0 spike=3.45
- UNIT.CA: score=15.02 buy_ready=False sector_rank=2 price=13.77 support=12.07 resistance=15.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:12 PM market time freshness=DELAYED_CURRENT RSI=63.0 liquidity=1619425.0 spike=0.15
- WCDF.CA: score=-4.05 buy_ready=False sector_rank=5 price=540.04 support=530.11 resistance=544.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:17 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=349726.56 spike=0.96
- WKOL.CA: score=6.77 buy_ready=False sector_rank=5 price=291.46 support=289.5 resistance=312.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:15 PM market time freshness=DELAYED_CURRENT RSI=46.28 liquidity=1165205.63 spike=0.3
- ZEOT.CA: score=10.6 buy_ready=False sector_rank=5 price=11.28 support=9.47 resistance=11.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:15 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=195295408.0 spike=31.92
- ZMID.CA: score=25.4 buy_ready=False sector_rank=2 price=6.23 support=5.77 resistance=6.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=62.32 liquidity=63211904.0 spike=0.27

## Backtesting Lite
- MTIE.CA: 180d return=40.27%, max drawdown=-20.49%, MA20>MA50 days last20=20, as_of=2026-06-14T21:00:00+00:00
- MOSC.CA: 180d return=62.4%, max drawdown=-30.84%, MA20>MA50 days last20=20, as_of=2026-06-13T21:00:00+00:00
- PHDC.CA: 180d return=119.62%, max drawdown=-15.81%, MA20>MA50 days last20=20, as_of=2026-06-14T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- MTIE.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=MM Group For Industry and International Trade summary=Evidence rejected for MTIE.CA: source text did not clearly match MTIE.CA / MM Group For Industry and International Trade.
- MOSC.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Misr Oils & Soap summary=Misr Oils and Soap not to pay dividends for FY20/21; Misr Oils and Soap&#39;s profit plunges 78% in FY20/21; Misr Oils and Soap swings to loss in 10 months
  - Misr Oils and Soap not to pay dividends for FY20/21: https://english.mubasher.info/news/3856493/Misr-Oils-and-Soap-not-to-pay-dividends-for-FY20-21/
  - Misr Oils and Soap&#39;s profit plunges 78% in FY20/21: https://english.mubasher.info/news/3851183/Misr-Oils-and-Soap-s-profit-plunges-78-in-FY20-21/
  - Misr Oils and Soap swings to loss in 10 months: https://english.mubasher.info/news/3811105/Misr-Oils-and-Soap-swings-to-loss-in-10-months/
- PHDC.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=531 sources=3 expected=Palm Hills Development summary=Palm Hills, UAE’s Miran to launch new development project in Ras Al Hikma; Palm Hills records 30% higher profits in 2025, unveils new project in UAE; Strong momentum pushes Palm Hills toward EGP 10.15
  - Palm Hills, UAE’s Miran to launch new development project in Ras Al Hikma: https://english.mubasher.info/news/4598123/Palm-Hills-UAE-s-Miran-to-launch-new-development-project-in-Ras-Al-Hikma/
  - Palm Hills records 30% higher profits in 2025, unveils new project in UAE: https://english.mubasher.info/news/4580548/Palm-Hills-records-30-higher-profits-in-2025-unveils-new-project-in-UAE/
  - Strong momentum pushes Palm Hills toward EGP 10.15: https://english.mubasher.info/news/4560871/Strong-momentum-pushes-Palm-Hills-toward-EGP-10-15/
- EMFD.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=531 sources=3 expected=Emaar Misr for Development summary=Emaar Misr posts higher revenues at EGP 19.8bn in 2025; Emaar Misr’s consolidated net profits drop to EGP 4.2bn in 9M-25; Emaar Misr, Golden Coast to establish EGP 900bn project in Red Sea
  - Emaar Misr posts higher revenues at EGP 19.8bn in 2025: https://english.mubasher.info/news/4561643/Emaar-Misr-posts-higher-revenues-at-EGP-19-8bn-in-2025/
  - Emaar Misr’s consolidated net profits drop to EGP 4.2bn in 9M-25: https://english.mubasher.info/news/4525192/Emaar-Misr-s-consolidated-net-profits-drop-to-EGP-4-2bn-in-9M-25/
  - Emaar Misr, Golden Coast to establish EGP 900bn project in Red Sea: https://english.mubasher.info/news/4495287/Emaar-Misr-Golden-Coast-to-establish-EGP-900bn-project-in-Red-Sea/
- ARAB.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Arab Developers Holding summary=Arab Developers Holding unveils EGP 1bn expansion plans to improve financial efficiency; FRA gives initial approval for Arab Developers’ rights issue; Arab Developers stock stabilizes after correction
  - Arab Developers Holding unveils EGP 1bn expansion plans to improve financial efficiency: https://english.mubasher.info/news/4601724/Arab-Developers-Holding-unveils-EGP-1bn-expansion-plans-to-improve-financial-efficiency/
  - FRA gives initial approval for Arab Developers’ rights issue: https://english.mubasher.info/news/4582627/FRA-gives-initial-approval-for-Arab-Developers-rights-issue/
  - Arab Developers stock stabilizes after correction: https://english.mubasher.info/news/4564643/Arab-Developers-stock-stabilizes-after-correction/
- ZMID.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=531 sources=3 expected=Zahraa Maadi Investment and Development summary=Zahraa Maadi unveils distribution date for 2025 cash dividends; Zahraa Maadi to disburse EGP 250m dividends for 2025; Zahraa Maadi’s stock faces key resistance at EGP 5.22
  - Zahraa Maadi unveils distribution date for 2025 cash dividends: https://english.mubasher.info/news/4594804/Zahraa-Maadi-unveils-distribution-date-for-2025-cash-dividends/
  - Zahraa Maadi to disburse EGP 250m dividends for 2025: https://english.mubasher.info/news/4583591/Zahraa-Maadi-to-disburse-EGP-250m-dividends-for-2025/
  - Zahraa Maadi’s stock faces key resistance at EGP 5.22: https://english.mubasher.info/news/4563531/Zahraa-Maadi-s-stock-faces-key-resistance-at-EGP-5-22/
- ANFI.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Tycoon Holding Company For Financial Investments summary=Evidence rejected for ANFI.CA: source text did not clearly match ANFI.CA / Tycoon Holding Company For Financial Investments.
- GBCO.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=GB Corp summary=Evidence rejected for GBCO.CA: source text did not clearly match GBCO.CA / GB Corp.

## Warnings
- Evidence rejected for MTIE.CA: source text did not clearly match MTIE.CA / MM Group For Industry and International Trade.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence for MOSC.CA matches the company but no source/report date was detected.
- Evidence for PHDC.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for EMFD.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for ARAB.CA matches the company but no source/report date was detected.
- Evidence for ZMID.CA matches the company but appears old; latest detected date is 2025-01-01.
- Mubasher stock-page evidence failed for ANFI.CA: 404 Client Error: Not Found for url: https://english.mubasher.info/markets/EGX/stocks/ANFI
- No Yahoo or Mubasher evidence found for ANFI.CA.
- Evidence rejected for ANFI.CA: source text did not clearly match ANFI.CA / Tycoon Holding Company For Financial Investments.
- Evidence rejected for GBCO.CA: source text did not clearly match GBCO.CA / GB Corp.
