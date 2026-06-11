# Telegram-First EGX Scanner Report

Scan phase: Pre-market risk check
Generated UTC: 2026-06-11T09:55:50.289995+00:00
Generated Cairo: 2026-06-11 12:55
Run timing: target 08:45 Cairo | generated Cairo 2026-06-11 12:55 | cron 45 5 * * 0-4
Trigger: scheduled cron=45 5 * * 0-4 mapped to pre_market; Cairo now 2026-06-11 12:53

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
- EGX70 regime: BEARISH / above MA20 32.5% / above MA50 65.0%
- Sector breadth: 9.52%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- CCAP.CA: liquidity=319702528.0 spike=0.38 score=18.32
- COMI.CA: liquidity=251608384.0 spike=0.38 score=14.34
- FWRY.CA: liquidity=195525808.0 spike=0.69 score=12.4
- ORAS.CA: liquidity=195179968.0 spike=1.0 score=4.6
- ANFI.CA: liquidity=168343687.25 spike=4.63 score=24.26

## AI Narrative
- Provider: OpenRouter OK
- Model: openai/gpt-oss-120b:free
- Summary: The EGX30 and EGX70 indices are both in a bearish regime with weak breadth (≈9.5%). This pushes the scanner into a defensive risk mode that blocks new buys. The top‑ranked tickets show mixed short‑term outlooks but all carry cooling liquidity or over‑extended RSI, so they remain on HOLD until market conditions improve.
- Bearish EGX30/EGX70 trends and low sector breadth keep risk mode at DEFENSIVE_NO_NEW_BUY.
- Real Estate (ZMID, EMFD) and Automotive (GBCO) show bullish watches but face cooling liquidity and high RSI.
- Energy (EGAS) has a clean risk profile but remains a watch in a bearish market context.
- Liquidity spikes are modest; support levels sit 6‑9% below price, resistance 2‑8% above, limiting near‑term upside.
- Uncertainty remains high – any shift in EGX30/EGX70 breadth or a breakout above MA20 could change the risk stance.

## Top Liquidity Spikes
- ANFI.CA: spike=4.63 liquidity=168343687.25 outlook=BULLISH_WATCH score=72.15 buy_ready=False
- ELNA.CA: spike=4.09 liquidity=1348871.87 outlook=BULLISH_WATCH score=90.15 buy_ready=False
- CFGH.CA: spike=2.56 liquidity=16699.85 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- EGSA.CA: spike=2.43 liquidity=35930.8 outlook=NEUTRAL score=36.67 buy_ready=False
- RAKT.CA: spike=2.24 liquidity=562312.53 outlook=WEAK_OR_RISKY score=16.15 buy_ready=False

## Sector Leaderboard
- #1 Automotive & Distribution: score=4.87 5d=2.25% 20d=-5.56% aboveMA50=100.0%
- #2 Real Estate: score=3.76 5d=-3.4% 20d=3.87% aboveMA50=84.62%
- #3 Energy & Petrochemicals: score=3.46 5d=-0.59% 20d=-0.21% aboveMA50=75.0%
- #4 Investment Holding: score=3.31 5d=-5.16% 20d=9.48% aboveMA50=66.67%
- #5 General / Verified EGX Expansion: score=3.15 5d=-0.85% 20d=-1.16% aboveMA50=70.19%
- #6 Agriculture & Food Production: score=2.98 5d=0.3% 20d=-3.26% aboveMA50=50.0%
- #7 Tourism & Leisure: score=2.85 5d=-6.69% 20d=11.23% aboveMA50=100.0%
- #8 Education: score=2.61 5d=-2.04% 20d=-3.92% aboveMA50=100.0%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- EGAS.CA: BULLISH_WATCH score=100 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=No major short-term scanner risk flags.
- ELNA.CA: BULLISH_WATCH score=90.15 liquidity=TRADEABLE sector=IMPROVING risk=No major short-term scanner risk flags.
- MPCI.CA: BULLISH_WATCH score=84.15 liquidity=TRADEABLE sector=IMPROVING risk=No major short-term scanner risk flags.
- MENA.CA: BULLISH_WATCH score=83.76 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- ZMID.CA: BULLISH_WATCH score=81.76 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; momentum is extended
- ORHD.CA: BULLISH_WATCH score=81.76 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; momentum is extended
- ACAMD.CA: BULLISH_WATCH score=79.15 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- MILS.CA: BULLISH_WATCH score=79.15 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- AMIA.CA: BULLISH_WATCH score=79.15 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- COPR.CA: BULLISH_WATCH score=76.15 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- No provider failures.

## Ranked Scanner Results
- AALR.CA: score=14.64 buy_ready=False sector_rank=5 price=205.0 support=195.1 resistance=233.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:31 AM market time freshness=DELAYED_CURRENT RSI=50.99 liquidity=6378130.0 spike=0.78
- ABUK.CA: score=9.0 buy_ready=False sector_rank=19 price=78.2 support=79.0 resistance=90.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=20.62 liquidity=54498220.0 spike=0.46
- ACAMD.CA: score=20.26 buy_ready=False sector_rank=5 price=2.27 support=2.14 resistance=2.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=51.52 liquidity=88352816.0 spike=0.7
- ACGC.CA: score=12.87 buy_ready=False sector_rank=9 price=9.18 support=8.6 resistance=10.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=31.86 liquidity=15384033.0 spike=0.26
- ADCI.CA: score=19.3 buy_ready=False sector_rank=5 price=222.33 support=202.22 resistance=228.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:35 AM market time freshness=DELAYED_CURRENT RSI=70.52 liquidity=8596431.0 spike=1.22
- ADIB.CA: score=14.34 buy_ready=False sector_rank=15 price=44.58 support=44.6 resistance=50.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=43.59 liquidity=31641764.0 spike=0.2
- ADPC.CA: score=10.26 buy_ready=False sector_rank=5 price=3.52 support=3.54 resistance=4.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=25.53 liquidity=10428185.0 spike=0.41
- AFDI.CA: score=12.41 buy_ready=False sector_rank=5 price=41.33 support=40.0 resistance=46.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:34 AM market time freshness=DELAYED_CURRENT RSI=60.02 liquidity=4147819.5 spike=0.23
- AFMC.CA: score=9.45 buy_ready=False sector_rank=5 price=69.45 support=69.33 resistance=80.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=42.35 liquidity=1193716.5 spike=0.16
- AJWA.CA: score=13.08 buy_ready=False sector_rank=5 price=146.54 support=130.01 resistance=154.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:30 AM market time freshness=DELAYED_CURRENT RSI=79.93 liquidity=5823285.0 spike=0.32
- ALCN.CA: score=14.08 buy_ready=False sector_rank=17 price=28.58 support=28.17 resistance=30.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=41.72 liquidity=17214750.0 spike=0.87
- ALUM.CA: score=14.06 buy_ready=False sector_rank=5 price=23.62 support=22.93 resistance=26.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=51.48 liquidity=3799673.75 spike=0.18
- AMER.CA: score=20.5 buy_ready=False sector_rank=2 price=2.61 support=2.43 resistance=3.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=55.67 liquidity=27878774.0 spike=0.24
- AMES.CA: score=2.8 buy_ready=False sector_rank=5 price=48.8 support=48.0 resistance=57.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:33 AM market time freshness=DELAYED_CURRENT RSI=17.32 liquidity=537796.69 spike=0.1
- AMIA.CA: score=18.54 buy_ready=False sector_rank=5 price=9.05 support=8.54 resistance=10.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=53.57 liquidity=8276789.5 spike=0.3
- AMOC.CA: score=16.38 buy_ready=False sector_rank=3 price=8.0 support=8.09 resistance=9.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=36.17 liquidity=44582904.0 spike=0.58
- ANFI.CA: score=24.26 buy_ready=False sector_rank=5 price=19.75 support=13.5 resistance=21.99 source=Yahoo Finance as_of=2026-06-09T21:00:00+00:00 freshness=FRESH RSI=87.25 liquidity=168343687.25 spike=4.63
- APSW.CA: score=1.75 buy_ready=False sector_rank=5 price=8.63 support=8.6 resistance=9.38 source=Yahoo Finance as_of=2026-06-09T21:00:00+00:00 freshness=FRESH RSI=29.21 liquidity=1328726.6 spike=1.58
- ARAB.CA: score=16.5 buy_ready=False sector_rank=2 price=0.2 support=0.19 resistance=0.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=57.69 liquidity=35710684.0 spike=0.43
- ARCC.CA: score=17.07 buy_ready=False sector_rank=18 price=54.77 support=53.35 resistance=60.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=58.09 liquidity=18684658.0 spike=0.43
- AREH.CA: score=17.26 buy_ready=False sector_rank=5 price=1.45 support=1.27 resistance=1.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=80.65 liquidity=13159197.0 spike=0.5
- ARVA.CA: score=12.09 buy_ready=False sector_rank=5 price=11.05 support=7.71 resistance=11.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=76.32 liquidity=4831399.0 spike=0.2
- ASCM.CA: score=20.26 buy_ready=False sector_rank=5 price=54.92 support=47.3 resistance=59.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=71.93 liquidity=16722088.0 spike=0.24
- ASPI.CA: score=22.26 buy_ready=False sector_rank=5 price=0.32 support=0.25 resistance=0.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=56.87 liquidity=22913346.0 spike=0.35
- ATLC.CA: score=4.64 buy_ready=False sector_rank=20 price=4.8 support=4.71 resistance=5.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=59.32 liquidity=1668752.5 spike=0.27
- ATQA.CA: score=13.0 buy_ready=False sector_rank=19 price=9.3 support=9.41 resistance=10.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=54.04 liquidity=20580368.0 spike=0.53
- AXPH.CA: score=8.98 buy_ready=False sector_rank=5 price=1124.2 support=1111.0 resistance=1230.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=43.08 liquidity=721719.88 spike=0.13
- BINV.CA: score=14.06 buy_ready=False sector_rank=4 price=44.8 support=40.8 resistance=49.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:35 AM market time freshness=DELAYED_CURRENT RSI=68.75 liquidity=3740183.75 spike=0.32
- BIOC.CA: score=10.09 buy_ready=False sector_rank=5 price=69.04 support=70.0 resistance=79.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:35 AM market time freshness=DELAYED_CURRENT RSI=48.95 liquidity=1832272.0 spike=0.28
- BTFH.CA: score=11.97 buy_ready=False sector_rank=20 price=3.02 support=3.03 resistance=3.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=49.06 liquidity=77094528.0 spike=0.33
- CAED.CA: score=11.06 buy_ready=False sector_rank=5 price=67.54 support=70.41 resistance=84.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=36.79 liquidity=2803702.75 spike=0.2
- CANA.CA: score=12.54 buy_ready=False sector_rank=15 price=35.81 support=34.07 resistance=39.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:31 AM market time freshness=DELAYED_CURRENT RSI=63.4 liquidity=4200027.0 spike=0.28
- CCAP.CA: score=18.32 buy_ready=False sector_rank=4 price=5.19 support=4.7 resistance=5.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=48.45 liquidity=319702528.0 spike=0.38
- CCRS.CA: score=15.43 buy_ready=False sector_rank=5 price=2.39 support=2.16 resistance=2.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=60.0 liquidity=7167914.5 spike=0.26
- CEFM.CA: score=4.15 buy_ready=False sector_rank=5 price=103.49 support=103.07 resistance=119.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=29.98 liquidity=894505.69 spike=0.21
- CERA.CA: score=12.79 buy_ready=False sector_rank=5 price=1.16 support=1.13 resistance=1.23 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=58.33 liquidity=3527450.5 spike=0.24
- CFGH.CA: score=2.4 buy_ready=False sector_rank=5 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:32 AM market time freshness=DELAYED_CURRENT RSI=0.0 liquidity=16699.85 spike=2.56
- CICH.CA: score=-1.09 buy_ready=False sector_rank=20 price=11.27 support=11.5 resistance=13.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:34 AM market time freshness=DELAYED_CURRENT RSI=23.6 liquidity=942778.13 spike=0.2
- CIEB.CA: score=7.97 buy_ready=False sector_rank=15 price=23.49 support=23.31 resistance=24.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=61.73 liquidity=3632158.0 spike=0.39
- CIRA.CA: score=5.07 buy_ready=False sector_rank=8 price=25.9 support=25.62 resistance=28.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=31.87 liquidity=2023263.0 spike=0.07
- CLHO.CA: score=11.66 buy_ready=False sector_rank=10 price=14.72 support=14.8 resistance=16.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:35 AM market time freshness=DELAYED_CURRENT RSI=40.07 liquidity=3814104.25 spike=0.11
- CNFN.CA: score=5.27 buy_ready=False sector_rank=20 price=4.4 support=4.41 resistance=4.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=36.51 liquidity=3300939.25 spike=0.2
- COMI.CA: score=14.34 buy_ready=False sector_rank=15 price=131.25 support=129.8 resistance=139.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=48.17 liquidity=251608384.0 spike=0.38
- COPR.CA: score=21.26 buy_ready=False sector_rank=5 price=0.36 support=0.32 resistance=0.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=60.0 liquidity=12532731.0 spike=0.31
- COSG.CA: score=20.26 buy_ready=False sector_rank=5 price=1.6 support=1.49 resistance=1.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=68.75 liquidity=34750880.0 spike=0.53
- CPCI.CA: score=6.74 buy_ready=False sector_rank=5 price=355.18 support=340.01 resistance=368.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=79.86 liquidity=1481740.75 spike=0.34
- CSAG.CA: score=12.49 buy_ready=False sector_rank=17 price=30.77 support=30.4 resistance=32.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:35 AM market time freshness=DELAYED_CURRENT RSI=56.74 liquidity=5411898.0 spike=0.33
- DAPH.CA: score=3.28 buy_ready=False sector_rank=5 price=77.89 support=78.6 resistance=96.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=27.7 liquidity=4020452.5 spike=0.13
- DEIN.CA: score=6.26 buy_ready=False sector_rank=5 price=11.38 support=11.38 resistance=13.65 source=Yahoo Finance as_of=2026-06-09T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- DOMT.CA: score=0.82 buy_ready=False sector_rank=11 price=23.96 support=24.03 resistance=26.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=25.68 liquidity=1128890.0 spike=0.44
- DSCW.CA: score=16.17 buy_ready=False sector_rank=5 price=1.75 support=1.71 resistance=1.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=58.33 liquidity=9908438.0 spike=0.18
- DTPP.CA: score=0.58 buy_ready=False sector_rank=5 price=118.06 support=118.03 resistance=137.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=21.74 liquidity=318239.31 spike=0.09
- EALR.CA: score=10.34 buy_ready=False sector_rank=5 price=351.81 support=346.01 resistance=392.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:31 AM market time freshness=DELAYED_CURRENT RSI=52.5 liquidity=2082184.25 spike=0.37
- EASB.CA: score=10.84 buy_ready=False sector_rank=5 price=4.92 support=4.61 resistance=5.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:28 AM market time freshness=DELAYED_CURRENT RSI=57.14 liquidity=581585.81 spike=0.52
- EAST.CA: score=21.69 buy_ready=False sector_rank=11 price=38.77 support=37.01 resistance=39.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=57.19 liquidity=11215177.0 spike=0.17
- EBSC.CA: score=10.76 buy_ready=False sector_rank=5 price=1.78 support=1.64 resistance=2.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:29 AM market time freshness=DELAYED_CURRENT RSI=69.23 liquidity=495635.13 spike=0.18
- ECAP.CA: score=12.93 buy_ready=False sector_rank=5 price=31.98 support=28.7 resistance=32.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=89.66 liquidity=5606764.0 spike=1.03
- EDFM.CA: score=8.75 buy_ready=False sector_rank=5 price=334.11 support=320.2 resistance=355.0 source=Yahoo Finance as_of=2026-06-09T21:00:00+00:00 freshness=FRESH RSI=50.28 liquidity=490807.57 spike=0.85
- EEII.CA: score=18.76 buy_ready=False sector_rank=5 price=2.34 support=2.27 resistance=2.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=63.89 liquidity=8496567.0 spike=0.44
- EFIC.CA: score=0.12 buy_ready=False sector_rank=19 price=199.4 support=203.01 resistance=219.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=9.24 liquidity=2120493.0 spike=0.61
- EFID.CA: score=14.69 buy_ready=False sector_rank=11 price=27.37 support=27.49 resistance=29.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=51.39 liquidity=14279254.0 spike=0.19
- EFIH.CA: score=12.4 buy_ready=False sector_rank=21 price=20.59 support=20.54 resistance=22.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=40.71 liquidity=11790062.0 spike=0.2
- EGAL.CA: score=9.0 buy_ready=False sector_rank=19 price=308.24 support=308.87 resistance=344.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=34.63 liquidity=41499200.0 spike=0.39
- EGAS.CA: score=23.18 buy_ready=False sector_rank=3 price=50.85 support=46.51 resistance=51.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=60.58 liquidity=21183676.0 spike=1.9
- EGBE.CA: score=2.37 buy_ready=False sector_rank=15 price=0.44 support=0.44 resistance=0.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:28 AM market time freshness=DELAYED_CURRENT RSI=28.48 liquidity=29112.63 spike=0.21
- EGCH.CA: score=17.0 buy_ready=False sector_rank=19 price=13.94 support=13.18 resistance=15.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=51.46 liquidity=18464666.0 spike=0.16
- EGSA.CA: score=10.56 buy_ready=False sector_rank=12 price=8.6 support=8.3 resistance=9.19 source=Yahoo Finance as_of=2026-06-09T21:00:00+00:00 freshness=FRESH RSI=45.05 liquidity=35930.8 spike=2.43
- EGTS.CA: score=20.5 buy_ready=False sector_rank=2 price=18.5 support=13.45 resistance=22.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=44.07 liquidity=33206680.0 spike=0.28
- EHDR.CA: score=20.26 buy_ready=False sector_rank=5 price=2.69 support=2.25 resistance=2.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=68.82 liquidity=41994280.0 spike=0.79
- EKHO.CA: score=11.38 buy_ready=False sector_rank=3 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-06-09T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=15.47 buy_ready=False sector_rank=14 price=2.09 support=2.06 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=54.17 liquidity=10671779.0 spike=0.4
- ELKA.CA: score=19.26 buy_ready=False sector_rank=5 price=1.22 support=1.12 resistance=1.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=70.97 liquidity=21009124.0 spike=0.49
- ELNA.CA: score=18.61 buy_ready=False sector_rank=5 price=41.26 support=37.11 resistance=42.79 source=Yahoo Finance as_of=2026-06-09T21:00:00+00:00 freshness=FRESH RSI=60.24 liquidity=1348871.87 spike=4.09
- ELSH.CA: score=19.26 buy_ready=False sector_rank=5 price=13.71 support=8.1 resistance=14.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=84.73 liquidity=136544160.0 spike=0.87
- ELWA.CA: score=7.8 buy_ready=False sector_rank=5 price=2.09 support=1.79 resistance=2.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:34 AM market time freshness=DELAYED_CURRENT RSI=88.57 liquidity=541734.31 spike=0.18
- EMFD.CA: score=22.5 buy_ready=False sector_rank=2 price=11.41 support=9.83 resistance=12.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=70.96 liquidity=61993128.0 spike=0.25
- ENGC.CA: score=17.53 buy_ready=False sector_rank=5 price=33.93 support=32.31 resistance=35.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:33 AM market time freshness=DELAYED_CURRENT RSI=66.59 liquidity=7268708.5 spike=0.52
- EOSB.CA: score=10.37 buy_ready=False sector_rank=5 price=1.42 support=1.34 resistance=1.53 source=Yahoo Finance as_of=2026-06-09T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=114534.36 spike=0.95
- EPCO.CA: score=6.82 buy_ready=False sector_rank=5 price=9.01 support=8.56 resistance=9.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:31 AM market time freshness=DELAYED_CURRENT RSI=60.0 liquidity=1561793.0 spike=0.13
- EPPK.CA: score=5.63 buy_ready=False sector_rank=5 price=12.17 support=11.67 resistance=13.6 source=Yahoo Finance as_of=2026-06-09T21:00:00+00:00 freshness=FRESH RSI=45.77 liquidity=366913.33 spike=0.35
- ETEL.CA: score=14.67 buy_ready=False sector_rank=12 price=90.64 support=92.17 resistance=98.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=35.34 liquidity=49165860.0 spike=0.56
- ETRS.CA: score=17.26 buy_ready=False sector_rank=5 price=9.09 support=7.37 resistance=9.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=84.29 liquidity=16582178.0 spike=0.29
- EXPA.CA: score=17.34 buy_ready=False sector_rank=15 price=18.49 support=18.34 resistance=20.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=51.28 liquidity=13203287.0 spike=0.34
- FAIT.CA: score=4.71 buy_ready=False sector_rank=15 price=35.63 support=34.73 resistance=38.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=33.41 liquidity=2374051.25 spike=0.39
- FAITA.CA: score=7.36 buy_ready=False sector_rank=15 price=0.99 support=0.98 resistance=1.0 source=Yahoo Finance as_of=2026-06-09T21:00:00+00:00 freshness=FRESH RSI=60.0 liquidity=17938.8 spike=0.44
- FERC.CA: score=5.93 buy_ready=False sector_rank=19 price=76.59 support=76.5 resistance=82.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=40.99 liquidity=1937041.0 spike=0.34
- FWRY.CA: score=12.4 buy_ready=False sector_rank=21 price=17.94 support=18.01 resistance=21.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=36.41 liquidity=195525808.0 spike=0.69
- GBCO.CA: score=23.95 buy_ready=False sector_rank=1 price=27.35 support=25.25 resistance=29.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=70.7 liquidity=33105878.0 spike=0.26
- GDWA.CA: score=13.67 buy_ready=False sector_rank=5 price=0.78 support=0.77 resistance=0.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=58.51 liquidity=7407586.0 spike=0.76
- GGCC.CA: score=13.99 buy_ready=False sector_rank=5 price=0.41 support=0.39 resistance=0.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:29 AM market time freshness=DELAYED_CURRENT RSI=56.76 liquidity=4725368.5 spike=0.62
- GIHD.CA: score=5.07 buy_ready=False sector_rank=5 price=39.34 support=35.15 resistance=44.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=44.34 liquidity=808796.81 spike=0.17
- GMCI.CA: score=7.57 buy_ready=False sector_rank=5 price=1.73 support=1.68 resistance=1.84 source=Yahoo Finance as_of=2026-06-09T21:00:00+00:00 freshness=FRESH RSI=51.72 liquidity=305609.69 spike=0.91
- GRCA.CA: score=4.42 buy_ready=False sector_rank=5 price=52.7 support=52.18 resistance=60.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:32 AM market time freshness=DELAYED_CURRENT RSI=26.07 liquidity=4160933.25 spike=0.46
- GSSC.CA: score=2.15 buy_ready=False sector_rank=5 price=247.82 support=228.1 resistance=272.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=10.31 liquidity=1886621.0 spike=0.28
- GTWL.CA: score=2.07 buy_ready=False sector_rank=5 price=47.0 support=45.47 resistance=59.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:33 AM market time freshness=DELAYED_CURRENT RSI=32.04 liquidity=1809089.75 spike=0.25
- HDBK.CA: score=9.82 buy_ready=False sector_rank=15 price=138.77 support=138.75 resistance=147.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=43.16 liquidity=5480260.0 spike=0.38
- HELI.CA: score=20.5 buy_ready=False sector_rank=2 price=6.4 support=6.28 resistance=6.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=51.57 liquidity=46904364.0 spike=0.28
- HRHO.CA: score=11.97 buy_ready=False sector_rank=20 price=26.1 support=26.0 resistance=29.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=48.25 liquidity=30374858.0 spike=0.18
- ICID.CA: score=14.98 buy_ready=False sector_rank=5 price=6.66 support=4.5 resistance=6.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=84.81 liquidity=7716720.5 spike=0.51
- IDRE.CA: score=12.8 buy_ready=False sector_rank=5 price=42.42 support=40.0 resistance=49.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:35 AM market time freshness=DELAYED_CURRENT RSI=59.23 liquidity=4543478.5 spike=0.14
- IFAP.CA: score=7.37 buy_ready=False sector_rank=6 price=19.0 support=16.5 resistance=23.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=44.84 liquidity=3173745.25 spike=0.31
- INFI.CA: score=9.35 buy_ready=False sector_rank=5 price=97.82 support=98.0 resistance=112.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=36.87 liquidity=2086031.38 spike=0.13
- IRON.CA: score=15.78 buy_ready=False sector_rank=19 price=32.94 support=31.83 resistance=35.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=41.37 liquidity=10645013.0 spike=1.39
- ISMA.CA: score=17.26 buy_ready=False sector_rank=5 price=30.2 support=22.08 resistance=30.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=90.3 liquidity=33448076.0 spike=0.82
- ISMQ.CA: score=19.38 buy_ready=False sector_rank=19 price=8.13 support=7.27 resistance=8.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=65.14 liquidity=67734960.0 spike=1.19
- ISPH.CA: score=17.85 buy_ready=False sector_rank=10 price=11.7 support=11.12 resistance=12.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=65.37 liquidity=67050172.0 spike=0.45
- JUFO.CA: score=19.69 buy_ready=False sector_rank=11 price=29.17 support=26.51 resistance=30.82 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=69.52 liquidity=23912768.0 spike=0.5
- KABO.CA: score=9.33 buy_ready=False sector_rank=9 price=6.04 support=5.92 resistance=6.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=57.43 liquidity=5454980.5 spike=0.26
- KWIN.CA: score=9.21 buy_ready=False sector_rank=5 price=70.98 support=69.0 resistance=80.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:00 AM market time freshness=DELAYED_CURRENT RSI=48.21 liquidity=949052.5 spike=0.22
- KZPC.CA: score=13.16 buy_ready=False sector_rank=5 price=10.61 support=10.3 resistance=11.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=64.0 liquidity=4904240.0 spike=0.37
- LCSW.CA: score=6.63 buy_ready=False sector_rank=18 price=26.17 support=26.16 resistance=29.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=51.65 liquidity=2563932.0 spike=0.16
- LUTS.CA: score=17.26 buy_ready=False sector_rank=5 price=0.65 support=0.54 resistance=0.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=75.95 liquidity=14986940.0 spike=0.77
- MAAL.CA: score=13.98 buy_ready=False sector_rank=5 price=5.69 support=4.44 resistance=6.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=90.42 liquidity=6724777.5 spike=0.5
- MASR.CA: score=18.26 buy_ready=False sector_rank=5 price=6.68 support=6.63 resistance=7.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=51.38 liquidity=50082024.0 spike=0.78
- MBSC.CA: score=12.07 buy_ready=False sector_rank=18 price=270.96 support=261.52 resistance=295.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=24.23 liquidity=24777338.0 spike=0.52
- MCQE.CA: score=13.7 buy_ready=False sector_rank=18 price=177.6 support=179.0 resistance=201.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=35.24 liquidity=9636761.0 spike=0.5
- MCRO.CA: score=14.26 buy_ready=False sector_rank=5 price=1.22 support=1.21 resistance=1.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=21909358.0 spike=0.28
- MENA.CA: score=15.6 buy_ready=False sector_rank=2 price=6.7 support=5.83 resistance=7.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=59.57 liquidity=3096041.75 spike=0.19
- MEPA.CA: score=14.21 buy_ready=False sector_rank=5 price=1.68 support=1.63 resistance=1.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=51.85 liquidity=5947379.0 spike=0.32
- MFPC.CA: score=9.0 buy_ready=False sector_rank=19 price=40.37 support=41.05 resistance=46.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=28.94 liquidity=53559680.0 spike=0.66
- MFSC.CA: score=13.01 buy_ready=False sector_rank=5 price=45.7 support=43.0 resistance=65.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=15.3 liquidity=9752411.0 spike=0.63
- MHOT.CA: score=12.1 buy_ready=False sector_rank=7 price=29.45 support=26.3 resistance=34.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=40.87 liquidity=3958707.5 spike=0.19
- MICH.CA: score=19.26 buy_ready=False sector_rank=5 price=37.82 support=35.01 resistance=40.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=83.56 liquidity=12797654.0 spike=0.97
- MILS.CA: score=19.41 buy_ready=False sector_rank=5 price=142.08 support=127.01 resistance=153.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=49.5 liquidity=9151629.0 spike=0.46
- MIPH.CA: score=8.43 buy_ready=False sector_rank=10 price=656.19 support=640.0 resistance=729.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=55.79 liquidity=586622.63 spike=0.19
- MOED.CA: score=4.26 buy_ready=False sector_rank=5 price=0.67 support=0.68 resistance=0.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=33.78 liquidity=5002657.5 spike=0.39
- MOIL.CA: score=9.46 buy_ready=False sector_rank=3 price=0.47 support=0.44 resistance=0.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:28 AM market time freshness=DELAYED_CURRENT RSI=62.86 liquidity=75792.76 spike=0.4
- MOIN.CA: score=9.92 buy_ready=False sector_rank=5 price=25.01 support=24.02 resistance=26.4 source=Yahoo Finance as_of=2026-06-09T21:00:00+00:00 freshness=FRESH RSI=55.47 liquidity=656687.58 spike=0.4
- MOSC.CA: score=5.22 buy_ready=False sector_rank=5 price=250.15 support=252.0 resistance=320.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=21.91 liquidity=1957011.0 spike=0.18
- MPCI.CA: score=22.26 buy_ready=False sector_rank=5 price=215.02 support=197.0 resistance=238.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=60.61 liquidity=85532280.0 spike=0.97
- MPCO.CA: score=19.19 buy_ready=False sector_rank=6 price=1.72 support=1.54 resistance=1.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=65.38 liquidity=27076068.0 spike=0.37
- MPRC.CA: score=14.27 buy_ready=False sector_rank=5 price=31.85 support=30.61 resistance=34.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=62.67 liquidity=4012444.0 spike=0.18
- MTIE.CA: score=21.95 buy_ready=False sector_rank=1 price=8.82 support=8.71 resistance=9.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=52.42 liquidity=10338428.0 spike=0.52
- NAHO.CA: score=4.72 buy_ready=False sector_rank=5 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance as_of=2026-06-09T21:00:00+00:00 freshness=FRESH RSI=40.0 liquidity=40433.27 spike=1.21
- NCCW.CA: score=17.26 buy_ready=False sector_rank=5 price=6.38 support=5.13 resistance=6.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=78.64 liquidity=11004337.0 spike=0.42
- NEDA.CA: score=10.62 buy_ready=False sector_rank=5 price=2.79 support=2.65 resistance=2.87 source=Yahoo Finance as_of=2026-06-09T21:00:00+00:00 freshness=FRESH RSI=57.69 liquidity=357842.61 spike=0.77
- NHPS.CA: score=6.9 buy_ready=False sector_rank=5 price=67.19 support=67.0 resistance=73.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=40.75 liquidity=2636178.25 spike=0.31
- NINH.CA: score=1.15 buy_ready=False sector_rank=5 price=16.87 support=17.0 resistance=20.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=31.1 liquidity=892424.31 spike=0.1
- NIPH.CA: score=17.85 buy_ready=False sector_rank=10 price=159.11 support=155.1 resistance=183.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=57.19 liquidity=28366176.0 spike=0.25
- OBRI.CA: score=13.59 buy_ready=False sector_rank=5 price=34.61 support=33.63 resistance=39.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=45.72 liquidity=6329415.5 spike=0.51
- OCDI.CA: score=17.5 buy_ready=False sector_rank=2 price=20.44 support=20.19 resistance=23.67 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=11936230.0 spike=0.29
- OCPH.CA: score=12.44 buy_ready=False sector_rank=5 price=343.3 support=346.01 resistance=409.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:30 AM market time freshness=DELAYED_CURRENT RSI=40.19 liquidity=4178167.25 spike=0.49
- ODIN.CA: score=15.04 buy_ready=False sector_rank=5 price=2.03 support=1.89 resistance=2.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=66.67 liquidity=4782726.5 spike=0.45
- OFH.CA: score=10.4 buy_ready=False sector_rank=5 price=0.6 support=0.6 resistance=0.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=46.94 liquidity=6143164.0 spike=0.27
- OIH.CA: score=10.32 buy_ready=False sector_rank=4 price=1.36 support=1.35 resistance=1.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=29.63 liquidity=14799135.0 spike=0.14
- OLFI.CA: score=20.67 buy_ready=False sector_rank=11 price=21.92 support=21.0 resistance=22.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=74.37 liquidity=28638762.0 spike=1.49
- ORAS.CA: score=4.6 buy_ready=False sector_rank=13 price=749.99 support=731.0 resistance=761.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=195179968.0 spike=1.0
- ORHD.CA: score=20.5 buy_ready=False sector_rank=2 price=36.48 support=33.0 resistance=39.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=66.67 liquidity=78591808.0 spike=0.41
- ORWE.CA: score=19.87 buy_ready=False sector_rank=9 price=22.81 support=21.6 resistance=24.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=67.82 liquidity=23593728.0 spike=0.52
- PHAR.CA: score=13.11 buy_ready=False sector_rank=10 price=83.67 support=83.96 resistance=92.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:32 AM market time freshness=DELAYED_CURRENT RSI=55.91 liquidity=8260940.0 spike=0.25
- PHDC.CA: score=20.5 buy_ready=False sector_rank=2 price=14.55 support=13.01 resistance=16.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=64.91 liquidity=72778960.0 spike=0.18
- PHTV.CA: score=5.35 buy_ready=False sector_rank=5 price=202.09 support=203.25 resistance=233.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=23.43 liquidity=2089578.13 spike=0.15
- POUL.CA: score=16.44 buy_ready=False sector_rank=11 price=36.04 support=34.8 resistance=39.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=55.22 liquidity=8749312.0 spike=0.19
- PRCL.CA: score=21.07 buy_ready=False sector_rank=18 price=24.58 support=21.01 resistance=28.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=64.89 liquidity=17874114.0 spike=0.61
- PRDC.CA: score=17.28 buy_ready=False sector_rank=2 price=6.0 support=5.3 resistance=6.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:27 AM market time freshness=DELAYED_CURRENT RSI=70.63 liquidity=4773158.5 spike=0.24
- PRMH.CA: score=20.26 buy_ready=False sector_rank=5 price=2.65 support=2.19 resistance=2.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=69.7 liquidity=10346247.0 spike=0.69
- RACC.CA: score=15.19 buy_ready=False sector_rank=5 price=9.78 support=9.54 resistance=10.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=44.06 liquidity=6931035.0 spike=0.47
- RAKT.CA: score=9.3 buy_ready=False sector_rank=5 price=23.11 support=22.1 resistance=25.0 source=Yahoo Finance as_of=2026-06-09T21:00:00+00:00 freshness=FRESH RSI=44.98 liquidity=562312.53 spike=2.24
- RAYA.CA: score=17.13 buy_ready=False sector_rank=16 price=6.85 support=6.9 resistance=8.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=45.3 liquidity=44607476.0 spike=0.41
- RMDA.CA: score=17.85 buy_ready=False sector_rank=10 price=4.99 support=4.95 resistance=5.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=51.7 liquidity=17712750.0 spike=0.17
- ROTO.CA: score=15.02 buy_ready=False sector_rank=5 price=33.43 support=32.66 resistance=36.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=49.82 liquidity=4759109.0 spike=0.36
- RREI.CA: score=9.16 buy_ready=False sector_rank=5 price=3.38 support=3.32 resistance=3.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=51.43 liquidity=3901316.75 spike=0.17
- RTVC.CA: score=8.94 buy_ready=False sector_rank=5 price=3.85 support=3.75 resistance=4.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=54.41 liquidity=1684405.63 spike=0.25
- RUBX.CA: score=7.28 buy_ready=False sector_rank=5 price=9.92 support=9.8 resistance=11.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=42.75 liquidity=3018658.5 spike=0.21
- SAUD.CA: score=14.34 buy_ready=False sector_rank=15 price=21.03 support=21.4 resistance=24.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=39.95 liquidity=11702251.0 spike=0.86
- SCEM.CA: score=9.07 buy_ready=False sector_rank=18 price=60.76 support=61.05 resistance=72.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=32.48 liquidity=11689609.0 spike=0.3
- SCFM.CA: score=4.82 buy_ready=False sector_rank=5 price=254.69 support=255.03 resistance=315.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:34 AM market time freshness=DELAYED_CURRENT RSI=24.26 liquidity=1560665.0 spike=0.09
- SCTS.CA: score=4.61 buy_ready=False sector_rank=8 price=606.73 support=590.01 resistance=690.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=26.34 liquidity=1562365.25 spike=0.14
- SDTI.CA: score=22.26 buy_ready=False sector_rank=5 price=46.5 support=43.4 resistance=47.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:28 AM market time freshness=DELAYED_CURRENT RSI=62.1 liquidity=10943130.0 spike=0.56
- SEIG.CA: score=9.34 buy_ready=False sector_rank=5 price=182.3 support=173.35 resistance=205.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:18 AM market time freshness=DELAYED_CURRENT RSI=58.72 liquidity=1079490.5 spike=0.2
- SIPC.CA: score=9.52 buy_ready=False sector_rank=5 price=3.47 support=3.4 resistance=3.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=62.5 liquidity=4264736.5 spike=0.27
- SKPC.CA: score=13.0 buy_ready=False sector_rank=19 price=16.55 support=16.8 resistance=18.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=40.44 liquidity=37540188.0 spike=0.6
- SMFR.CA: score=7.53 buy_ready=False sector_rank=5 price=196.7 support=201.0 resistance=224.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=37.37 liquidity=2268949.5 spike=0.38
- SNFC.CA: score=13.33 buy_ready=False sector_rank=5 price=12.1 support=11.68 resistance=12.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=43.11 liquidity=5065782.0 spike=0.19
- SPIN.CA: score=0.48 buy_ready=False sector_rank=9 price=13.81 support=13.61 resistance=15.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:22 AM market time freshness=DELAYED_CURRENT RSI=25.23 liquidity=611998.81 spike=0.12
- SPMD.CA: score=14.52 buy_ready=False sector_rank=5 price=0.41 support=0.38 resistance=0.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=62.77 liquidity=6260803.5 spike=0.25
- SUGR.CA: score=7.94 buy_ready=False sector_rank=11 price=48.37 support=48.0 resistance=52.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:32 AM market time freshness=DELAYED_CURRENT RSI=52.18 liquidity=4246054.0 spike=0.27
- SVCE.CA: score=13.26 buy_ready=False sector_rank=5 price=8.35 support=8.41 resistance=9.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=31.52 liquidity=12834780.0 spike=0.12
- SWDY.CA: score=17.47 buy_ready=False sector_rank=14 price=84.6 support=85.25 resistance=90.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=47.96 liquidity=13489384.0 spike=0.51
- TALM.CA: score=16.21 buy_ready=False sector_rank=8 price=15.88 support=15.12 resistance=16.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=62.57 liquidity=4166140.75 spike=0.33
- TMGH.CA: score=15.5 buy_ready=False sector_rank=2 price=93.78 support=91.87 resistance=101.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=32.91 liquidity=141680352.0 spike=0.3
- TRTO.CA: score=7.24 buy_ready=False sector_rank=5 price=0.03 support=0.03 resistance=0.04 source=Yahoo Finance as_of=2026-06-09T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=680.0 spike=1.49
- UEFM.CA: score=-0.21 buy_ready=False sector_rank=5 price=470.21 support=455.6 resistance=500.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:24 AM market time freshness=DELAYED_CURRENT RSI=30.06 liquidity=533659.63 spike=0.48
- UEGC.CA: score=18.26 buy_ready=False sector_rank=5 price=1.37 support=1.3 resistance=1.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=66.67 liquidity=10759139.0 spike=0.39
- UNIP.CA: score=15.8 buy_ready=False sector_rank=5 price=0.32 support=0.28 resistance=0.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=83.02 liquidity=9544023.0 spike=0.5
- UNIT.CA: score=11.61 buy_ready=False sector_rank=2 price=13.52 support=12.07 resistance=15.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:18 AM market time freshness=DELAYED_CURRENT RSI=66.58 liquidity=1110060.5 spike=0.1
- WCDF.CA: score=10.44 buy_ready=False sector_rank=5 price=539.84 support=535.0 resistance=555.0 source=Yahoo Finance as_of=2026-06-09T21:00:00+00:00 freshness=FRESH RSI=38.12 liquidity=577628.83 spike=1.8
- WKOL.CA: score=9.49 buy_ready=False sector_rank=5 price=294.45 support=290.0 resistance=324.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:35 AM market time freshness=DELAYED_CURRENT RSI=58.14 liquidity=1230803.0 spike=0.29
- ZEOT.CA: score=3.68 buy_ready=False sector_rank=5 price=9.16 support=8.69 resistance=9.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=7836386.5 spike=1.29
- ZMID.CA: score=24.5 buy_ready=False sector_rank=2 price=6.12 support=5.77 resistance=6.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=62.1 liquidity=100038992.0 spike=0.43

## Backtesting Lite
- ZMID.CA: 180d return=54.65%, max drawdown=-19.84%, MA20>MA50 days last20=20, as_of=2026-06-09T21:00:00+00:00
- ANFI.CA: 180d return=218.24%, max drawdown=-19.31%, MA20>MA50 days last20=20, as_of=2026-06-09T21:00:00+00:00
- GBCO.CA: 180d return=30.78%, max drawdown=-24.35%, MA20>MA50 days last20=20, as_of=2026-06-09T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- ZMID.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=526 sources=3 expected=Zahraa Maadi Investment and Development summary=Zahraa Maadi unveils distribution date for 2025 cash dividends; Zahraa Maadi to disburse EGP 250m dividends for 2025; Zahraa Maadi’s stock faces key resistance at EGP 5.22
  - Zahraa Maadi unveils distribution date for 2025 cash dividends: https://english.mubasher.info/news/4594804/Zahraa-Maadi-unveils-distribution-date-for-2025-cash-dividends/
  - Zahraa Maadi to disburse EGP 250m dividends for 2025: https://english.mubasher.info/news/4583591/Zahraa-Maadi-to-disburse-EGP-250m-dividends-for-2025/
  - Zahraa Maadi’s stock faces key resistance at EGP 5.22: https://english.mubasher.info/news/4563531/Zahraa-Maadi-s-stock-faces-key-resistance-at-EGP-5-22/
- ANFI.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Tycoon Holding Company For Financial Investments summary=Evidence rejected for ANFI.CA: source text did not clearly match ANFI.CA / Tycoon Holding Company For Financial Investments.
- GBCO.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=GB Corp summary=Evidence rejected for GBCO.CA: source text did not clearly match GBCO.CA / GB Corp.
- EGAS.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Natural Gas and Mining Project summary=Evidence rejected for EGAS.CA: source text did not clearly match EGAS.CA / Natural Gas and Mining Project.
- EMFD.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=526 sources=3 expected=Emaar Misr for Development summary=Emaar Misr posts higher revenues at EGP 19.8bn in 2025; Emaar Misr’s consolidated net profits drop to EGP 4.2bn in 9M-25; Emaar Misr, Golden Coast to establish EGP 900bn project in Red Sea
  - Emaar Misr posts higher revenues at EGP 19.8bn in 2025: https://english.mubasher.info/news/4561643/Emaar-Misr-posts-higher-revenues-at-EGP-19-8bn-in-2025/
  - Emaar Misr’s consolidated net profits drop to EGP 4.2bn in 9M-25: https://english.mubasher.info/news/4525192/Emaar-Misr-s-consolidated-net-profits-drop-to-EGP-4-2bn-in-9M-25/
  - Emaar Misr, Golden Coast to establish EGP 900bn project in Red Sea: https://english.mubasher.info/news/4495287/Emaar-Misr-Golden-Coast-to-establish-EGP-900bn-project-in-Red-Sea/
- ASPI.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Aspire Capital Holding for Financial Investments summary=Aspire Capital records higher consolidated net profits at over EGP 42m in 9M-25; PREDCO, Aspire Holding consider establishing mortgage company; Pioneers Holding gets EGX&#39;s approval for capital cut, name change
  - Aspire Capital records higher consolidated net profits at over EGP 42m in 9M-25: https://english.mubasher.info/news/4541324/Aspire-Capital-records-higher-consolidated-net-profits-at-over-EGP-42m-in-9M-25/
  - PREDCO, Aspire Holding consider establishing mortgage company: https://english.mubasher.info/news/4185438/PREDCO-Aspire-Holding-consider-establishing-mortgage-company/
  - Pioneers Holding gets EGX&#39;s approval for capital cut, name change: https://english.mubasher.info/news/3861454/Pioneers-Holding-gets-EGX-s-approval-for-capital-cut-name-change/
- MPCI.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Memphis Pharmaceuticals & Chemical Industries summary=Evidence rejected for MPCI.CA: source text did not clearly match MPCI.CA / Memphis Pharmaceuticals & Chemical Industries.
- SDTI.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=SHARM DREAMS Co. for Touristic Investment S.A.E summary=Sharm Dreams stock maintains strong uptrend - Analysis; Sharm Dreams stock is experiencing sideways movement amid anticipation of next trend – Analysis; Sharm Dreams stock hits historic level halting driving buying force
  - Sharm Dreams stock maintains strong uptrend - Analysis: https://english.mubasher.info/news/4577977/Sharm-Dreams-stock-maintains-strong-uptrend-Analysis/
  - Sharm Dreams stock is experiencing sideways movement amid anticipation of next trend – Analysis: https://english.mubasher.info/news/4547831/Sharm-Dreams-stock-is-experiencing-sideways-movement-amid-anticipation-of-next-trend-Analysis/
  - Sharm Dreams stock hits historic level halting driving buying force: https://english.mubasher.info/news/4529096/Sharm-Dreams-stock-hits-historic-level-halting-driving-buying-force/

## Warnings
- Evidence for ZMID.CA matches the company but appears old; latest detected date is 2025-01-01.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Mubasher stock-page evidence failed for ANFI.CA: 404 Client Error: Not Found for url: https://english.mubasher.info/markets/EGX/stocks/ANFI
- No Yahoo or Mubasher evidence found for ANFI.CA.
- Evidence rejected for ANFI.CA: source text did not clearly match ANFI.CA / Tycoon Holding Company For Financial Investments.
- Evidence rejected for GBCO.CA: source text did not clearly match GBCO.CA / GB Corp.
- Evidence rejected for EGAS.CA: source text did not clearly match EGAS.CA / Natural Gas and Mining Project.
- Evidence for EMFD.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for ASPI.CA matches the company but no source/report date was detected.
- Evidence rejected for MPCI.CA: source text did not clearly match MPCI.CA / Memphis Pharmaceuticals & Chemical Industries.
- Evidence for SDTI.CA matches the company but no source/report date was detected.
