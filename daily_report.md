# Telegram-First EGX Scanner Report

Scan phase: Open liquidity confirmation
Generated UTC: 2026-06-29T11:26:06.278173+00:00
Generated Cairo: 2026-06-29 14:26
Run timing: target 09:15 Cairo | generated Cairo 2026-06-29 14:26 | cron 15 6 * * 0-4
Trigger: scheduled cron=15 6 * * 0-4 mapped to open_confirm; Cairo now 2026-06-29 14:22

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 0
- Tradeable price/liquidity tickers: 179/190
- Top sector: Tourism & Leisure

## Market Context
- Market trend: Bearish
- Source: Mubasher EGX market page (delayed public data)
- As of: Monday, June 29
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 15.0% / above MA50 25.0%
- EGX70 regime: BEARISH / above MA20 27.5% / above MA50 60.0%
- Sector breadth: 9.52%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- COMI.CA: liquidity=591497088.0 spike=1.04 score=14.24
- ORAS.CA: liquidity=217008752.0 spike=1.0 score=4.6
- CCAP.CA: liquidity=210739504.0 spike=0.31 score=8.67
- TMGH.CA: liquidity=175654608.0 spike=0.44 score=14.89
- PHDC.CA: liquidity=149173152.0 spike=0.37 score=17.89

## AI Narrative
- Provider: OpenRouter OK
- Model: nvidia/nemotron-3-super-120b-a12b-20230311:free
- Summary: EGX30 and EGX70 stay bearish with weak breadth (≈9.5%), keeping risk mode defensive; the scanner flags a few stocks with relatively strong outlook and liquidity but advises no new buys.
- Scanner ranked MHOT.CA, RUBX.CA and CSAG.CA highest due to their scores, sector leadership (Tourism & Leisure, Automotive & Distribution, Transportation & Logistics) and favorable outlook scores despite the bearish marke
- Liquidity varies: MHOT.CA shows tradeable flow, RUBX.CA exhibits an accumulation spike but with overheated RSI, while CSAG.CA offers tradeable liquidity and tight support/resistance bands suggesting a near‑term range.
- Support and resistance distances are generally tight (single‑digit to low‑teens percent), indicating limited upside/downside movement expected over the next 1‑3 days unless the regime shifts.
- Overall bearish EGX30/EGX70 trends and low sector breadth maintain a DEFENSIVE_NO_NEW_BUY risk mode, so any bullish bias remains uncertain and could reverse quickly.

## Top Liquidity Spikes
- AMES.CA: spike=12.12 liquidity=32827604.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- DTPP.CA: spike=8.76 liquidity=12713925.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- GTWL.CA: spike=6.42 liquidity=119795744.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- CPCI.CA: spike=5.57 liquidity=10545195.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- RUBX.CA: spike=4.3 liquidity=65188108.0 outlook=CONSTRUCTIVE score=68.83 buy_ready=False

## Sector Leaderboard
- #1 Tourism & Leisure: score=9.46 5d=2.1% 20d=8.17% aboveMA50=100.0%
- #2 Automotive & Distribution: score=8.74 5d=1.75% 20d=7.28% aboveMA50=100.0%
- #3 Transportation & Logistics: score=3.81 5d=-0.49% 20d=-1.76% aboveMA50=50.0%
- #4 Real Estate: score=2.23 5d=-4.04% 20d=1.47% aboveMA50=76.92%
- #5 Food, Beverages & Tobacco: score=1.83 5d=-3.6% 20d=0.24% aboveMA50=57.14%
- #6 Technology & Distribution: score=1.56 5d=-4.17% 20d=-4.81% aboveMA50=100.0%
- #7 Industrial Goods & Construction: score=1.5 5d=0.0% 20d=0.0% aboveMA50=0.0%
- #8 Agriculture & Food Production: score=1.17 5d=-4.74% 20d=3.32% aboveMA50=50.0%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- CSAG.CA: BULLISH_WATCH score=94.81 liquidity=TRADEABLE sector=LEADING risk=No major short-term scanner risk flags.
- MTIE.CA: BULLISH_WATCH score=93.74 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=below MA20
- MHOT.CA: BULLISH_WATCH score=89.46 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- LCSW.CA: BULLISH_WATCH score=88.49 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- MENA.CA: BULLISH_WATCH score=78.23 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- CNFN.CA: BULLISH_WATCH score=71.95 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; sector is not leading
- CLHO.CA: BULLISH_WATCH score=70.49 liquidity=TRADEABLE sector=IMPROVING risk=sector is not leading
- DOMT.CA: CONSTRUCTIVE score=69.83 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; momentum is extended
- RUBX.CA: CONSTRUCTIVE score=68.83 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=overheated RSI; sector is not leading
- OCPH.CA: CONSTRUCTIVE score=66.83 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=overheated RSI; sector is not leading

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- No provider failures.

## Ranked Scanner Results
- AALR.CA: score=16.83 buy_ready=False sector_rank=13 price=200.95 support=196.0 resistance=231.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:08 PM market time freshness=DELAYED_CURRENT RSI=35.98 liquidity=12852189.0 spike=2.25
- ABUK.CA: score=8.19 buy_ready=False sector_rank=20 price=67.46 support=67.69 resistance=84.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=9.15 liquidity=58929592.0 spike=0.44
- ACAMD.CA: score=14.33 buy_ready=False sector_rank=13 price=2.16 support=2.14 resistance=2.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:08 PM market time freshness=DELAYED_CURRENT RSI=41.18 liquidity=46977048.0 spike=0.38
- ACGC.CA: score=14.35 buy_ready=False sector_rank=12 price=9.12 support=9.11 resistance=10.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=38.76 liquidity=13427519.0 spike=0.32
- ADCI.CA: score=18.93 buy_ready=False sector_rank=13 price=242.31 support=211.0 resistance=244.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=84.03 liquidity=21178762.0 spike=2.3
- ADIB.CA: score=14.16 buy_ready=False sector_rank=17 price=44.91 support=44.01 resistance=48.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=43.59 liquidity=25000190.0 spike=0.26
- ADPC.CA: score=13.25 buy_ready=False sector_rank=13 price=3.37 support=3.38 resistance=3.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=37.5 liquidity=9914032.0 spike=0.43
- AFDI.CA: score=13.78 buy_ready=False sector_rank=13 price=42.42 support=40.15 resistance=48.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=46.07 liquidity=6445303.0 spike=0.43
- AFMC.CA: score=0.03 buy_ready=False sector_rank=13 price=67.35 support=66.66 resistance=74.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:55 PM market time freshness=DELAYED_CURRENT RSI=29.03 liquidity=699139.06 spike=0.27
- AJWA.CA: score=11.0 buy_ready=False sector_rank=13 price=175.05 support=131.5 resistance=188.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:08 PM market time freshness=DELAYED_CURRENT RSI=83.3 liquidity=4665481.0 spike=0.17
- ALCN.CA: score=7.88 buy_ready=False sector_rank=3 price=27.7 support=25.51 resistance=33.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=32.2 liquidity=6351106.5 spike=0.51
- ALUM.CA: score=2.82 buy_ready=False sector_rank=13 price=20.71 support=20.55 resistance=26.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=16.11 liquidity=3486196.75 spike=0.36
- AMER.CA: score=9.89 buy_ready=False sector_rank=4 price=2.33 support=2.3 resistance=3.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=25.56 liquidity=21805072.0 spike=0.29
- AMES.CA: score=9.33 buy_ready=False sector_rank=13 price=55.28 support=45.15 resistance=55.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:08 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=32827604.0 spike=12.12
- AMIA.CA: score=8.52 buy_ready=False sector_rank=13 price=8.49 support=8.4 resistance=9.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:08 PM market time freshness=DELAYED_CURRENT RSI=38.81 liquidity=4191531.75 spike=0.3
- AMOC.CA: score=9.43 buy_ready=False sector_rank=10 price=7.51 support=7.42 resistance=8.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=10.0 liquidity=21292902.0 spike=0.43
- ANFI.CA: score=5.66 buy_ready=False sector_rank=13 price=26.5 support=13.73 resistance=41.4 source=Yahoo Finance as_of=2026-06-22T21:00:00+00:00 freshness=STALE RSI=64.45 liquidity=3331182.5 spike=0.04
- APSW.CA: score=4.42 buy_ready=False sector_rank=13 price=8.05 support=8.24 resistance=9.21 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=12.5 liquidity=2266191.5 spike=2.91
- ARAB.CA: score=14.89 buy_ready=False sector_rank=4 price=0.21 support=0.2 resistance=0.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=55.88 liquidity=59606416.0 spike=0.7
- ARCC.CA: score=9.2 buy_ready=False sector_rank=14 price=53.89 support=53.0 resistance=60.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=31.02 liquidity=13770335.0 spike=0.4
- AREH.CA: score=19.33 buy_ready=False sector_rank=13 price=1.53 support=1.32 resistance=1.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:08 PM market time freshness=DELAYED_CURRENT RSI=54.39 liquidity=12447600.0 spike=0.37
- ARVA.CA: score=17.33 buy_ready=False sector_rank=13 price=10.9 support=8.2 resistance=13.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:08 PM market time freshness=DELAYED_CURRENT RSI=46.55 liquidity=15281609.0 spike=0.48
- ASCM.CA: score=19.33 buy_ready=False sector_rank=13 price=57.79 support=47.5 resistance=73.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:08 PM market time freshness=DELAYED_CURRENT RSI=53.76 liquidity=41518668.0 spike=0.45
- ASPI.CA: score=9.74 buy_ready=False sector_rank=13 price=0.3 support=0.27 resistance=0.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:08 PM market time freshness=DELAYED_CURRENT RSI=36.92 liquidity=6403444.0 spike=0.09
- ATLC.CA: score=8.82 buy_ready=False sector_rank=11 price=4.99 support=4.7 resistance=5.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=49.44 liquidity=1442690.5 spike=0.23
- ATQA.CA: score=12.19 buy_ready=False sector_rank=20 price=9.39 support=9.02 resistance=10.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:08 PM market time freshness=DELAYED_CURRENT RSI=41.31 liquidity=13794311.0 spike=0.42
- AXPH.CA: score=6.03 buy_ready=False sector_rank=13 price=1117.31 support=1073.0 resistance=1174.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=31.18 liquidity=1562786.38 spike=1.07
- BINV.CA: score=8.51 buy_ready=False sector_rank=19 price=45.32 support=42.97 resistance=49.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:08 PM market time freshness=DELAYED_CURRENT RSI=50.05 liquidity=1842541.63 spike=0.18
- BIOC.CA: score=1.46 buy_ready=False sector_rank=13 price=68.17 support=66.75 resistance=75.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=31.39 liquidity=2123255.25 spike=0.86
- BTFH.CA: score=13.38 buy_ready=False sector_rank=11 price=2.98 support=2.96 resistance=3.23 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=47.83 liquidity=104635608.0 spike=0.56
- CAED.CA: score=5.28 buy_ready=False sector_rank=13 price=69.34 support=67.21 resistance=78.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:08 PM market time freshness=DELAYED_CURRENT RSI=43.65 liquidity=947931.75 spike=0.19
- CANA.CA: score=2.04 buy_ready=False sector_rank=17 price=35.18 support=34.5 resistance=39.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=31.12 liquidity=3884915.75 spike=0.36
- CCAP.CA: score=8.67 buy_ready=False sector_rank=19 price=4.68 support=4.72 resistance=5.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:08 PM market time freshness=DELAYED_CURRENT RSI=17.05 liquidity=210739504.0 spike=0.31
- CCRS.CA: score=14.33 buy_ready=False sector_rank=13 price=2.23 support=2.28 resistance=2.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:08 PM market time freshness=DELAYED_CURRENT RSI=35.09 liquidity=13993861.0 spike=0.8
- CEFM.CA: score=1.31 buy_ready=False sector_rank=13 price=96.83 support=98.0 resistance=109.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=20.82 liquidity=2297352.25 spike=1.34
- CERA.CA: score=11.86 buy_ready=False sector_rank=13 price=1.2 support=1.15 resistance=1.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:08 PM market time freshness=DELAYED_CURRENT RSI=53.85 liquidity=5531854.5 spike=0.33
- CFGH.CA: score=-0.3 buy_ready=False sector_rank=13 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance as_of=2026-06-27T21:00:00+00:00 freshness=FRESH RSI=0.0 liquidity=11200.0 spike=1.68
- CICH.CA: score=8.23 buy_ready=False sector_rank=11 price=11.75 support=11.1 resistance=13.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=46.3 liquidity=1853259.25 spike=0.57
- CIEB.CA: score=10.75 buy_ready=False sector_rank=17 price=23.32 support=23.27 resistance=24.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=49.09 liquidity=6554639.0 spike=1.02
- CIRA.CA: score=16.21 buy_ready=False sector_rank=9 price=27.87 support=25.23 resistance=31.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=62.1 liquidity=6775626.5 spike=0.38
- CLHO.CA: score=21.74 buy_ready=False sector_rank=15 price=16.11 support=14.25 resistance=17.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=61.84 liquidity=44767880.0 spike=1.27
- CNFN.CA: score=21.38 buy_ready=False sector_rank=11 price=4.67 support=4.36 resistance=5.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=52.53 liquidity=15170708.0 spike=0.37
- COMI.CA: score=14.24 buy_ready=False sector_rank=17 price=126.43 support=129.8 resistance=137.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=49.33 liquidity=591497088.0 spike=1.04
- COPR.CA: score=16.33 buy_ready=False sector_rank=13 price=0.35 support=0.35 resistance=0.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:08 PM market time freshness=DELAYED_CURRENT RSI=50.85 liquidity=13345917.0 spike=0.45
- COSG.CA: score=9.33 buy_ready=False sector_rank=13 price=1.5 support=1.48 resistance=1.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=29.73 liquidity=19347110.0 spike=0.36
- CPCI.CA: score=9.33 buy_ready=False sector_rank=13 price=390.83 support=370.1 resistance=434.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=10545195.0 spike=5.57
- CSAG.CA: score=24.12 buy_ready=False sector_rank=3 price=32.12 support=30.08 resistance=33.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=60.25 liquidity=20533522.0 spike=1.3
- DAPH.CA: score=8.95 buy_ready=False sector_rank=13 price=79.29 support=76.6 resistance=87.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=44.51 liquidity=3615516.0 spike=0.35
- DEIN.CA: score=5.33 buy_ready=False sector_rank=13 price=11.38 support=11.38 resistance=13.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 June 12:11 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=40.95 spike=0.01
- DOMT.CA: score=12.2 buy_ready=False sector_rank=5 price=26.36 support=23.7 resistance=27.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=70.0 liquidity=2468315.0 spike=0.64
- DSCW.CA: score=13.33 buy_ready=False sector_rank=13 price=1.72 support=1.71 resistance=1.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:08 PM market time freshness=DELAYED_CURRENT RSI=36.11 liquidity=13120489.0 spike=0.34
- DTPP.CA: score=9.33 buy_ready=False sector_rank=13 price=138.38 support=120.0 resistance=138.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=12713925.0 spike=8.76
- EALR.CA: score=6.57 buy_ready=False sector_rank=13 price=341.31 support=332.0 resistance=380.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=38.22 liquidity=2241368.25 spike=0.71
- EASB.CA: score=21.39 buy_ready=False sector_rank=13 price=7.69 support=4.66 resistance=10.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:08 PM market time freshness=DELAYED_CURRENT RSI=74.07 liquidity=23828006.0 spike=2.03
- EAST.CA: score=13.73 buy_ready=False sector_rank=5 price=36.91 support=37.0 resistance=40.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=36.67 liquidity=25885232.0 spike=0.64
- EBSC.CA: score=4.92 buy_ready=False sector_rank=13 price=1.74 support=1.66 resistance=2.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:08 PM market time freshness=DELAYED_CURRENT RSI=37.5 liquidity=585549.06 spike=0.22
- ECAP.CA: score=13.15 buy_ready=False sector_rank=13 price=31.91 support=29.8 resistance=34.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:09 PM market time freshness=DELAYED_CURRENT RSI=55.96 liquidity=5816806.5 spike=0.67
- EDFM.CA: score=-0.4 buy_ready=False sector_rank=13 price=330.59 support=320.29 resistance=355.0 source=Yahoo Finance as_of=2026-06-27T21:00:00+00:00 freshness=FRESH RSI=26.96 liquidity=272406.16 spike=0.51
- EEII.CA: score=8.94 buy_ready=False sector_rank=13 price=2.35 support=2.3 resistance=2.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:08 PM market time freshness=DELAYED_CURRENT RSI=44.07 liquidity=4604019.0 spike=0.34
- EFIC.CA: score=-1.91 buy_ready=False sector_rank=20 price=189.13 support=192.0 resistance=213.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=13.84 liquidity=898450.25 spike=0.46
- EFID.CA: score=9.99 buy_ready=False sector_rank=5 price=27.06 support=25.5 resistance=29.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=25.19 liquidity=83515744.0 spike=1.13
- EFIH.CA: score=12.86 buy_ready=False sector_rank=21 price=20.27 support=20.0 resistance=22.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=42.16 liquidity=10663245.0 spike=0.24
- EGAL.CA: score=8.19 buy_ready=False sector_rank=20 price=274.01 support=273.1 resistance=334.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=10.52 liquidity=20162504.0 spike=0.3
- EGAS.CA: score=9.95 buy_ready=False sector_rank=10 price=48.46 support=46.51 resistance=55.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=51.34 liquidity=2526651.0 spike=0.27
- EGBE.CA: score=11.19 buy_ready=False sector_rank=17 price=0.45 support=0.43 resistance=0.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:46 PM market time freshness=DELAYED_CURRENT RSI=52.31 liquidity=37603.03 spike=0.41
- EGCH.CA: score=8.19 buy_ready=False sector_rank=20 price=12.14 support=12.15 resistance=15.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=21.54 liquidity=22766888.0 spike=0.41
- EGSA.CA: score=7.18 buy_ready=False sector_rank=16 price=8.75 support=8.55 resistance=9.1 source=Yahoo Finance as_of=2026-06-27T21:00:00+00:00 freshness=FRESH RSI=36.0 liquidity=1767.5 spike=0.19
- EGTS.CA: score=17.89 buy_ready=False sector_rank=4 price=16.87 support=16.11 resistance=22.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:08 PM market time freshness=DELAYED_CURRENT RSI=41.49 liquidity=22939256.0 spike=0.25
- EHDR.CA: score=17.33 buy_ready=False sector_rank=13 price=2.41 support=2.27 resistance=2.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:08 PM market time freshness=DELAYED_CURRENT RSI=36.36 liquidity=18968092.0 spike=0.33
- EKHO.CA: score=9.43 buy_ready=False sector_rank=10 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-06-27T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=12.98 buy_ready=False sector_rank=18 price=2.07 support=2.06 resistance=2.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:08 PM market time freshness=DELAYED_CURRENT RSI=40.74 liquidity=14298049.0 spike=0.74
- ELKA.CA: score=16.33 buy_ready=False sector_rank=13 price=1.2 support=1.16 resistance=1.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:08 PM market time freshness=DELAYED_CURRENT RSI=43.75 liquidity=13230741.0 spike=0.33
- ELNA.CA: score=-1.24 buy_ready=False sector_rank=13 price=36.03 support=35.55 resistance=41.51 source=Yahoo Finance as_of=2026-06-27T21:00:00+00:00 freshness=FRESH RSI=33.43 liquidity=425190.02 spike=1.0
- ELSH.CA: score=12.33 buy_ready=False sector_rank=13 price=11.47 support=8.29 resistance=14.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=30.95 liquidity=37741152.0 spike=0.2
- ELWA.CA: score=8.18 buy_ready=False sector_rank=13 price=1.97 support=2.0 resistance=2.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=36.36 liquidity=850831.19 spike=0.27
- EMFD.CA: score=17.89 buy_ready=False sector_rank=4 price=11.5 support=10.8 resistance=12.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=41.44 liquidity=38726180.0 spike=0.14
- ENGC.CA: score=21.33 buy_ready=False sector_rank=13 price=36.33 support=32.9 resistance=38.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=63.41 liquidity=10150130.0 spike=0.72
- EOSB.CA: score=11.4 buy_ready=False sector_rank=13 price=1.48 support=1.35 resistance=1.55 source=Yahoo Finance as_of=2026-06-27T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=65744.56 spike=0.49
- EPCO.CA: score=7.38 buy_ready=False sector_rank=13 price=8.55 support=8.69 resistance=9.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:08 PM market time freshness=DELAYED_CURRENT RSI=38.82 liquidity=3050709.0 spike=0.34
- EPPK.CA: score=13.64 buy_ready=False sector_rank=13 price=13.03 support=11.67 resistance=13.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:08 PM market time freshness=DELAYED_CURRENT RSI=62.62 liquidity=312988.0 spike=0.28
- ETEL.CA: score=14.18 buy_ready=False sector_rank=16 price=90.3 support=89.61 resistance=98.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=39.04 liquidity=35190168.0 spike=0.48
- ETRS.CA: score=19.33 buy_ready=False sector_rank=13 price=10.37 support=8.01 resistance=11.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:09 PM market time freshness=DELAYED_CURRENT RSI=65.32 liquidity=24636852.0 spike=0.34
- EXPA.CA: score=9.16 buy_ready=False sector_rank=17 price=18.17 support=18.03 resistance=20.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=24.55 liquidity=21485952.0 spike=0.67
- FAIT.CA: score=3.79 buy_ready=False sector_rank=17 price=35.9 support=35.01 resistance=38.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=33.38 liquidity=1630627.88 spike=0.53
- FAITA.CA: score=4.19 buy_ready=False sector_rank=17 price=0.98 support=0.98 resistance=1.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=40.0 liquidity=34943.84 spike=0.89
- FERC.CA: score=1.5 buy_ready=False sector_rank=20 price=73.0 support=74.0 resistance=80.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:08 PM market time freshness=DELAYED_CURRENT RSI=16.06 liquidity=4091605.75 spike=1.11
- FWRY.CA: score=12.86 buy_ready=False sector_rank=21 price=18.31 support=17.71 resistance=20.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=49.05 liquidity=64806876.0 spike=0.26
- GBCO.CA: score=20.78 buy_ready=False sector_rank=2 price=31.06 support=25.25 resistance=31.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:08 PM market time freshness=DELAYED_CURRENT RSI=85.94 liquidity=106237912.0 spike=1.19
- GDWA.CA: score=3.91 buy_ready=False sector_rank=13 price=0.77 support=0.76 resistance=0.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=29.32 liquidity=5574971.0 spike=0.4
- GGCC.CA: score=20.51 buy_ready=False sector_rank=13 price=0.46 support=0.4 resistance=0.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:09 PM market time freshness=DELAYED_CURRENT RSI=66.67 liquidity=11843799.0 spike=1.09
- GIHD.CA: score=11.6 buy_ready=False sector_rank=13 price=40.98 support=35.15 resistance=47.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=49.38 liquidity=5272807.5 spike=0.65
- GMCI.CA: score=13.35 buy_ready=False sector_rank=13 price=1.77 support=1.66 resistance=1.84 source=Yahoo Finance as_of=2026-06-27T21:00:00+00:00 freshness=FRESH RSI=48.39 liquidity=941578.04 spike=2.54
- GRCA.CA: score=7.11 buy_ready=False sector_rank=13 price=52.8 support=50.2 resistance=60.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=39.41 liquidity=2777332.0 spike=0.62
- GSSC.CA: score=0.32 buy_ready=False sector_rank=13 price=241.29 support=228.1 resistance=257.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:09 PM market time freshness=DELAYED_CURRENT RSI=27.12 liquidity=1983839.25 spike=0.63
- GTWL.CA: score=9.33 buy_ready=False sector_rank=13 price=73.5 support=60.3 resistance=73.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:08 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=119795744.0 spike=6.42
- HDBK.CA: score=21.16 buy_ready=False sector_rank=17 price=155.06 support=138.0 resistance=172.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=63.41 liquidity=23002980.0 spike=0.84
- HELI.CA: score=17.89 buy_ready=False sector_rank=4 price=6.38 support=6.28 resistance=6.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=50.61 liquidity=34692872.0 spike=0.29
- HRHO.CA: score=15.38 buy_ready=False sector_rank=11 price=26.48 support=25.54 resistance=27.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=53.83 liquidity=45214892.0 spike=0.32
- ICID.CA: score=10.67 buy_ready=False sector_rank=13 price=7.6 support=5.0 resistance=8.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=73.78 liquidity=1335840.63 spike=0.08
- IDRE.CA: score=10.18 buy_ready=False sector_rank=13 price=41.67 support=42.01 resistance=47.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=41.92 liquidity=5851913.5 spike=0.37
- IFAP.CA: score=11.05 buy_ready=False sector_rank=8 price=18.86 support=16.5 resistance=23.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:08 PM market time freshness=DELAYED_CURRENT RSI=49.12 liquidity=5579586.0 spike=0.85
- INFI.CA: score=1.78 buy_ready=False sector_rank=13 price=88.61 support=89.0 resistance=105.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=14.52 liquidity=3444867.5 spike=0.46
- IRON.CA: score=10.65 buy_ready=False sector_rank=20 price=32.28 support=30.75 resistance=34.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=28.36 liquidity=12420569.0 spike=1.73
- ISMA.CA: score=14.91 buy_ready=False sector_rank=13 price=28.58 support=25.95 resistance=36.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:09 PM market time freshness=DELAYED_CURRENT RSI=56.23 liquidity=7575833.5 spike=0.2
- ISMQ.CA: score=20.67 buy_ready=False sector_rank=20 price=9.08 support=7.39 resistance=9.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:08 PM market time freshness=DELAYED_CURRENT RSI=70.06 liquidity=134235136.0 spike=1.24
- ISPH.CA: score=9.2 buy_ready=False sector_rank=15 price=11.39 support=11.2 resistance=12.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=34.51 liquidity=28392782.0 spike=0.25
- JUFO.CA: score=17.73 buy_ready=False sector_rank=5 price=29.14 support=28.1 resistance=32.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=47.21 liquidity=12589279.0 spike=0.36
- KABO.CA: score=17.35 buy_ready=False sector_rank=12 price=6.2 support=5.96 resistance=6.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=41.43 liquidity=14240770.0 spike=0.9
- KWIN.CA: score=15.13 buy_ready=False sector_rank=13 price=67.78 support=65.75 resistance=79.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:09 PM market time freshness=DELAYED_CURRENT RSI=43.59 liquidity=20202614.0 spike=1.9
- KZPC.CA: score=-0.16 buy_ready=False sector_rank=13 price=8.39 support=8.35 resistance=11.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:09 PM market time freshness=DELAYED_CURRENT RSI=14.05 liquidity=1510251.38 spike=0.24
- LCSW.CA: score=22.38 buy_ready=False sector_rank=14 price=27.43 support=26.0 resistance=31.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=51.03 liquidity=42596864.0 spike=1.59
- LUTS.CA: score=19.33 buy_ready=False sector_rank=13 price=0.71 support=0.55 resistance=0.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:09 PM market time freshness=DELAYED_CURRENT RSI=60.35 liquidity=28110480.0 spike=0.63
- MAAL.CA: score=18.33 buy_ready=False sector_rank=13 price=7.13 support=5.24 resistance=7.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:09 PM market time freshness=DELAYED_CURRENT RSI=78.13 liquidity=12427630.0 spike=0.7
- MASR.CA: score=6.01 buy_ready=False sector_rank=13 price=7.14 support=6.82 resistance=7.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:09 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=98179744.0 spike=1.84
- MBSC.CA: score=9.2 buy_ready=False sector_rank=14 price=229.68 support=228.11 resistance=258.91 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=11.36 liquidity=23121622.0 spike=0.66
- MCQE.CA: score=4.42 buy_ready=False sector_rank=14 price=168.85 support=166.66 resistance=200.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=20.75 liquidity=5219633.5 spike=0.32
- MCRO.CA: score=8.33 buy_ready=False sector_rank=13 price=1.19 support=1.18 resistance=1.31 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:09 PM market time freshness=DELAYED_CURRENT RSI=25.0 liquidity=22853794.0 spike=0.64
- MENA.CA: score=12.63 buy_ready=False sector_rank=4 price=6.82 support=6.22 resistance=7.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:08 PM market time freshness=DELAYED_CURRENT RSI=40.54 liquidity=2738439.25 spike=0.21
- MEPA.CA: score=2.88 buy_ready=False sector_rank=13 price=1.54 support=1.52 resistance=1.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:08 PM market time freshness=DELAYED_CURRENT RSI=17.24 liquidity=4546970.0 spike=0.39
- MFPC.CA: score=8.19 buy_ready=False sector_rank=20 price=34.56 support=34.22 resistance=43.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=5.78 liquidity=51322880.0 spike=0.6
- MFSC.CA: score=14.08 buy_ready=False sector_rank=13 price=47.01 support=43.0 resistance=56.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:09 PM market time freshness=DELAYED_CURRENT RSI=54.08 liquidity=4750733.5 spike=0.54
- MHOT.CA: score=26.4 buy_ready=False sector_rank=1 price=33.9 support=28.83 resistance=38.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=61.67 liquidity=15027352.0 spike=0.66
- MICH.CA: score=11.39 buy_ready=False sector_rank=13 price=36.23 support=35.4 resistance=40.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:08 PM market time freshness=DELAYED_CURRENT RSI=43.14 liquidity=4061793.0 spike=0.27
- MILS.CA: score=7.06 buy_ready=False sector_rank=13 price=127.45 support=128.06 resistance=151.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=35.55 liquidity=2731349.75 spike=0.28
- MIPH.CA: score=5.56 buy_ready=False sector_rank=15 price=651.64 support=630.13 resistance=710.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=38.59 liquidity=1362901.88 spike=0.7
- MOED.CA: score=6.84 buy_ready=False sector_rank=13 price=0.65 support=0.65 resistance=0.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:09 PM market time freshness=DELAYED_CURRENT RSI=37.68 liquidity=1509492.25 spike=0.15
- MOIL.CA: score=4.99 buy_ready=False sector_rank=10 price=0.46 support=0.46 resistance=0.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=41.51 liquidity=226113.75 spike=1.17
- MOIN.CA: score=-1.48 buy_ready=False sector_rank=13 price=23.03 support=22.6 resistance=25.66 source=Yahoo Finance as_of=2026-06-27T21:00:00+00:00 freshness=FRESH RSI=1.0 liquidity=187901.78 spike=0.29
- MOSC.CA: score=7.33 buy_ready=False sector_rank=13 price=282.68 support=250.55 resistance=298.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:09 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=21191550.0 spike=2.5
- MPCI.CA: score=4.37 buy_ready=False sector_rank=13 price=235.86 support=223.51 resistance=243.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:09 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=95689712.0 spike=1.02
- MPCO.CA: score=16.47 buy_ready=False sector_rank=8 price=1.72 support=1.58 resistance=2.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:08 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=36377916.0 spike=0.35
- MPRC.CA: score=19.33 buy_ready=False sector_rank=13 price=38.2 support=31.15 resistance=40.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=74.69 liquidity=29177860.0 spike=0.69
- MTIE.CA: score=22.58 buy_ready=False sector_rank=2 price=9.05 support=8.65 resistance=9.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=46.15 liquidity=24618994.0 spike=1.59
- NAHO.CA: score=5.34 buy_ready=False sector_rank=13 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance as_of=2026-06-27T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=9515.24 spike=0.44
- NCCW.CA: score=16.03 buy_ready=False sector_rank=13 price=5.94 support=5.29 resistance=6.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:09 PM market time freshness=DELAYED_CURRENT RSI=42.78 liquidity=8702716.0 spike=0.26
- NEDA.CA: score=-0.37 buy_ready=False sector_rank=13 price=2.74 support=2.68 resistance=2.84 source=Yahoo Finance as_of=2026-06-27T21:00:00+00:00 freshness=FRESH RSI=33.33 liquidity=298218.86 spike=0.79
- NHPS.CA: score=4.13 buy_ready=False sector_rank=13 price=62.09 support=61.62 resistance=68.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:08 PM market time freshness=DELAYED_CURRENT RSI=40.84 liquidity=801564.94 spike=0.22
- NINH.CA: score=10.99 buy_ready=False sector_rank=13 price=17.85 support=16.8 resistance=18.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:08 PM market time freshness=DELAYED_CURRENT RSI=48.35 liquidity=2654782.75 spike=0.63
- NIPH.CA: score=12.26 buy_ready=False sector_rank=15 price=161.33 support=157.05 resistance=176.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=30.86 liquidity=69903064.0 spike=1.03
- OBRI.CA: score=14.33 buy_ready=False sector_rank=13 price=32.2 support=31.5 resistance=37.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:09 PM market time freshness=DELAYED_CURRENT RSI=39.18 liquidity=10280144.0 spike=0.75
- OCDI.CA: score=19.89 buy_ready=False sector_rank=4 price=24.33 support=20.0 resistance=25.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=70.5 liquidity=57098664.0 spike=0.77
- OCPH.CA: score=21.79 buy_ready=False sector_rank=13 price=351.66 support=337.0 resistance=377.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=36.03 liquidity=13051666.0 spike=2.23
- ODIN.CA: score=9.59 buy_ready=False sector_rank=13 price=2.07 support=1.92 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:08 PM market time freshness=DELAYED_CURRENT RSI=51.67 liquidity=2257338.25 spike=0.21
- OFH.CA: score=4.4 buy_ready=False sector_rank=13 price=0.58 support=0.58 resistance=0.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:09 PM market time freshness=DELAYED_CURRENT RSI=22.89 liquidity=6064927.5 spike=0.32
- OIH.CA: score=15.67 buy_ready=False sector_rank=19 price=1.4 support=1.33 resistance=1.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:08 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=15730004.0 spike=0.2
- OLFI.CA: score=17.73 buy_ready=False sector_rank=5 price=21.9 support=21.1 resistance=23.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=49.31 liquidity=16902364.0 spike=0.84
- ORAS.CA: score=4.6 buy_ready=False sector_rank=7 price=702.0 support=695.0 resistance=718.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=217008752.0 spike=1.0
- ORHD.CA: score=17.89 buy_ready=False sector_rank=4 price=37.71 support=35.01 resistance=39.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=58.12 liquidity=95600760.0 spike=0.53
- ORWE.CA: score=9.35 buy_ready=False sector_rank=12 price=22.14 support=22.07 resistance=24.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:08 PM market time freshness=DELAYED_CURRENT RSI=26.23 liquidity=14500136.0 spike=0.4
- PHAR.CA: score=10.82 buy_ready=False sector_rank=15 price=84.72 support=83.02 resistance=89.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=44.94 liquidity=4622561.5 spike=0.13
- PHDC.CA: score=17.89 buy_ready=False sector_rank=4 price=14.65 support=14.26 resistance=16.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=45.18 liquidity=149173152.0 spike=0.37
- PHTV.CA: score=18.33 buy_ready=False sector_rank=13 price=270.0 support=201.55 resistance=259.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:10 PM market time freshness=DELAYED_CURRENT RSI=89.5 liquidity=12869753.0 spike=0.88
- POUL.CA: score=19.73 buy_ready=False sector_rank=5 price=36.74 support=34.99 resistance=41.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=55.23 liquidity=34985360.0 spike=0.93
- PRCL.CA: score=19.2 buy_ready=False sector_rank=14 price=30.7 support=22.11 resistance=32.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:08 PM market time freshness=DELAYED_CURRENT RSI=65.11 liquidity=20116794.0 spike=0.5
- PRDC.CA: score=19.89 buy_ready=False sector_rank=4 price=7.16 support=5.74 resistance=9.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:08 PM market time freshness=DELAYED_CURRENT RSI=64.47 liquidity=72679040.0 spike=0.63
- PRMH.CA: score=12.33 buy_ready=False sector_rank=13 price=2.47 support=2.26 resistance=3.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:10 PM market time freshness=DELAYED_CURRENT RSI=31.53 liquidity=11455571.0 spike=0.37
- RACC.CA: score=7.64 buy_ready=False sector_rank=13 price=9.53 support=9.38 resistance=10.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:09 PM market time freshness=DELAYED_CURRENT RSI=37.84 liquidity=3305733.75 spike=0.35
- RAKT.CA: score=1.62 buy_ready=False sector_rank=13 price=22.43 support=22.0 resistance=24.1 source=Yahoo Finance as_of=2026-06-27T21:00:00+00:00 freshness=FRESH RSI=30.46 liquidity=371620.25 spike=1.46
- RAYA.CA: score=17.62 buy_ready=False sector_rank=6 price=7.24 support=6.7 resistance=7.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=42.18 liquidity=65372684.0 spike=0.79
- RMDA.CA: score=12.2 buy_ready=False sector_rank=15 price=4.94 support=4.85 resistance=5.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=31.0 liquidity=14162349.0 spike=0.18
- ROTO.CA: score=21.33 buy_ready=False sector_rank=13 price=40.26 support=32.91 resistance=47.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:10 PM market time freshness=DELAYED_CURRENT RSI=64.72 liquidity=20497470.0 spike=0.72
- RREI.CA: score=8.55 buy_ready=False sector_rank=13 price=3.39 support=3.34 resistance=3.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:10 PM market time freshness=DELAYED_CURRENT RSI=38.96 liquidity=4220798.5 spike=0.24
- RTVC.CA: score=1.74 buy_ready=False sector_rank=13 price=3.64 support=3.61 resistance=4.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=26.67 liquidity=3405192.75 spike=0.67
- RUBX.CA: score=26.33 buy_ready=False sector_rank=13 price=11.3 support=9.8 resistance=12.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:09 PM market time freshness=DELAYED_CURRENT RSI=74.26 liquidity=65188108.0 spike=4.3
- SAUD.CA: score=3.34 buy_ready=False sector_rank=17 price=20.41 support=19.99 resistance=23.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=19.03 liquidity=4181385.5 spike=0.48
- SCEM.CA: score=9.08 buy_ready=False sector_rank=14 price=61.05 support=59.3 resistance=67.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=40.78 liquidity=4881259.5 spike=0.27
- SCFM.CA: score=0.83 buy_ready=False sector_rank=13 price=237.01 support=226.5 resistance=276.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=20.69 liquidity=1501863.5 spike=0.31
- SCTS.CA: score=0.35 buy_ready=False sector_rank=9 price=543.18 support=540.0 resistance=630.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:49 PM market time freshness=DELAYED_CURRENT RSI=20.92 liquidity=921780.44 spike=0.28
- SDTI.CA: score=10.66 buy_ready=False sector_rank=13 price=46.02 support=44.03 resistance=49.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=49.61 liquidity=3323733.75 spike=0.28
- SEIG.CA: score=9.59 buy_ready=False sector_rank=13 price=183.92 support=180.0 resistance=205.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=40.65 liquidity=2260380.25 spike=0.55
- SIPC.CA: score=5.92 buy_ready=False sector_rank=13 price=3.29 support=3.35 resistance=3.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:09 PM market time freshness=DELAYED_CURRENT RSI=26.67 liquidity=6587160.5 spike=0.57
- SKPC.CA: score=7.19 buy_ready=False sector_rank=20 price=15.8 support=15.64 resistance=17.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=20.87 liquidity=15952617.0 spike=0.44
- SMFR.CA: score=-0.32 buy_ready=False sector_rank=13 price=190.84 support=187.01 resistance=214.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=27.43 liquidity=343802.88 spike=0.16
- SNFC.CA: score=7.09 buy_ready=False sector_rank=13 price=11.83 support=11.68 resistance=12.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:10 PM market time freshness=DELAYED_CURRENT RSI=48.46 liquidity=2759285.75 spike=0.15
- SPIN.CA: score=13.75 buy_ready=False sector_rank=12 price=14.13 support=13.3 resistance=14.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=57.58 liquidity=5401850.5 spike=0.88
- SPMD.CA: score=17.33 buy_ready=False sector_rank=13 price=0.41 support=0.4 resistance=0.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:10 PM market time freshness=DELAYED_CURRENT RSI=50.68 liquidity=10196855.0 spike=0.43
- SUGR.CA: score=4.28 buy_ready=False sector_rank=5 price=46.04 support=46.25 resistance=51.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=23.45 liquidity=5548632.0 spike=0.72
- SVCE.CA: score=17.33 buy_ready=False sector_rank=13 price=8.85 support=8.11 resistance=9.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:08 PM market time freshness=DELAYED_CURRENT RSI=53.11 liquidity=24462908.0 spike=0.37
- SWDY.CA: score=13.98 buy_ready=False sector_rank=18 price=84.98 support=84.01 resistance=90.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=41.75 liquidity=13361587.0 spike=0.78
- TALM.CA: score=6.24 buy_ready=False sector_rank=9 price=15.66 support=15.38 resistance=16.53 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=36.56 liquidity=1812403.5 spike=0.23
- TMGH.CA: score=14.89 buy_ready=False sector_rank=4 price=92.3 support=92.91 resistance=98.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=38.74 liquidity=175654608.0 spike=0.44
- TRTO.CA: score=5.33 buy_ready=False sector_rank=13 price=0.03 support=0.03 resistance=0.04 source=Yahoo Finance as_of=2026-06-27T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=340.0 spike=0.45
- UEFM.CA: score=7.02 buy_ready=False sector_rank=13 price=469.97 support=460.0 resistance=505.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=44.83 liquidity=1226491.38 spike=1.23
- UEGC.CA: score=4.49 buy_ready=False sector_rank=13 price=1.36 support=1.32 resistance=1.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=33.33 liquidity=5154513.5 spike=0.22
- UNIP.CA: score=5.25 buy_ready=False sector_rank=13 price=0.32 support=0.3 resistance=0.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:09 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=33201150.0 spike=1.46
- UNIT.CA: score=4.22 buy_ready=False sector_rank=4 price=12.44 support=12.5 resistance=15.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=16.0 liquidity=1331694.0 spike=0.2
- WCDF.CA: score=5.23 buy_ready=False sector_rank=13 price=518.05 support=450.0 resistance=547.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=35.83 liquidity=396079.84 spike=1.25
- WKOL.CA: score=1.28 buy_ready=False sector_rank=13 price=279.43 support=273.1 resistance=312.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:08 PM market time freshness=DELAYED_CURRENT RSI=27.71 liquidity=1948125.0 spike=0.7
- ZEOT.CA: score=9.05 buy_ready=False sector_rank=13 price=11.03 support=10.6 resistance=11.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:10 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=88856152.0 spike=3.36
- ZMID.CA: score=19.89 buy_ready=False sector_rank=4 price=6.22 support=5.82 resistance=6.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:08 PM market time freshness=DELAYED_CURRENT RSI=51.03 liquidity=111839816.0 spike=0.54

## Backtesting Lite
- MHOT.CA: 180d return=36.21%, max drawdown=-15.7%, MA20>MA50 days last20=20, as_of=2026-06-27T21:00:00+00:00
- RUBX.CA: 180d return=12.72%, max drawdown=-21.39%, MA20>MA50 days last20=10, as_of=2026-06-27T21:00:00+00:00
- CSAG.CA: 180d return=13.87%, max drawdown=-28.0%, MA20>MA50 days last20=20, as_of=2026-06-27T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- MHOT.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Misr Hotels summary=Misr Hotels’ net profits cross EGP 1.1bn in 9M-25/26; Shareholder buys EGP 3.39m worth of shares in Misr Hotels; Misr Hotels repays EGP 383m of NBE&#39;s loan, unveils estimated profits
  - Misr Hotels’ net profits cross EGP 1.1bn in 9M-25/26: https://english.mubasher.info/news/4602482/Misr-Hotels-net-profits-cross-EGP-1-1bn-in-9M-25-26/
  - Shareholder buys EGP 3.39m worth of shares in Misr Hotels: https://english.mubasher.info/news/4013808/Shareholder-buys-EGP-3-39m-worth-of-shares-in-Misr-Hotels/
  - Misr Hotels repays EGP 383m of NBE&#39;s loan, unveils estimated profits: https://english.mubasher.info/news/3975543/Misr-Hotels-repays-EGP-383m-of-NBE-s-loan-unveils-estimated-profits/
- RUBX.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Rubex International for Plastic and Acrylic Manufacturing summary=Evidence rejected for RUBX.CA: source text did not clearly match RUBX.CA / Rubex International for Plastic and Acrylic Manufacturing.
- CSAG.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Canal Shipping Agencies summary=Canal Shipping Agencies targets EGP 970m net profits in FY26/27; Canal Shipping Agencies’ stock rebounds; Canal Shipping Agencies mulls EGP 100m capital raise
  - Canal Shipping Agencies targets EGP 970m net profits in FY26/27: https://english.mubasher.info/news/4582423/Canal-Shipping-Agencies-targets-EGP-970m-net-profits-in-FY26-27/
  - Canal Shipping Agencies’ stock rebounds: https://english.mubasher.info/news/4564447/Canal-Shipping-Agencies-stock-rebounds/
  - Canal Shipping Agencies mulls EGP 100m capital raise: https://english.mubasher.info/news/4191441/Canal-Shipping-Agencies-mulls-EGP-100m-capital-raise/
- MTIE.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=MM Group For Industry and International Trade summary=Evidence rejected for MTIE.CA: source text did not clearly match MTIE.CA / MM Group For Industry and International Trade.
- LCSW.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Lecico Egypt summary=Evidence rejected for LCSW.CA: source text did not clearly match LCSW.CA / Lecico Egypt.
- OCPH.CA: status=OLD_ACCEPTED latest=2022-01-01 age_days=1640 sources=3 expected=October Pharma S.A.E summary=October Pharma targets EGP 135m net profits in 2022; October Pharma&#39;s profit hikes 65% in nine months; October Pharma’s Q1 profits leap 402%
  - October Pharma targets EGP 135m net profits in 2022: https://english.mubasher.info/news/3895021/October-Pharma-targets-EGP-135m-net-profits-in-2022/
  - October Pharma&#39;s profit hikes 65% in nine months: https://english.mubasher.info/news/3870893/October-Pharma-s-profit-hikes-65-in-nine-months/
  - October Pharma’s Q1 profits leap 402%: https://english.mubasher.info/news/3818864/October-Pharma-s-Q1-profits-leap-402-/
- CLHO.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=544 sources=3 expected=Cleopatra Hospital Group summary=Cleopatra Hospitals unveils EGP 84m dividends to employee for 2025; Cleopatra Hospitals posts higher consolidated profits in 2025; revenues cross EGP 7.2bn; Cleopatra Hospitals launches EGP 3.5bn Sky hospital in East Cairo
  - Cleopatra Hospitals unveils EGP 84m dividends to employee for 2025: https://english.mubasher.info/news/4594702/Cleopatra-Hospitals-unveils-EGP-84m-dividends-to-employee-for-2025/
  - Cleopatra Hospitals posts higher consolidated profits in 2025; revenues cross EGP 7.2bn: https://english.mubasher.info/news/4579844/Cleopatra-Hospitals-posts-higher-consolidated-profits-in-2025-revenues-cross-EGP-7-2bn/
  - Cleopatra Hospitals launches EGP 3.5bn Sky hospital in East Cairo: https://english.mubasher.info/news/4553462/Cleopatra-Hospitals-launches-EGP-3-5bn-Sky-hospital-in-East-Cairo/
- EASB.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Egyptian Arabian Company (Themar) for securities Brokerage EAC summary=Evidence rejected for EASB.CA: source text did not clearly match EASB.CA / Egyptian Arabian Company (Themar) for securities Brokerage EAC.

## Warnings
- Evidence for MHOT.CA matches the company but no source/report date was detected.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence rejected for RUBX.CA: source text did not clearly match RUBX.CA / Rubex International for Plastic and Acrylic Manufacturing.
- Evidence for CSAG.CA matches the company but no source/report date was detected.
- Evidence rejected for MTIE.CA: source text did not clearly match MTIE.CA / MM Group For Industry and International Trade.
- Evidence rejected for LCSW.CA: source text did not clearly match LCSW.CA / Lecico Egypt.
- Evidence for OCPH.CA matches the company but appears old; latest detected date is 2022-01-01.
- Evidence for CLHO.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for EASB.CA: source text did not clearly match EASB.CA / Egyptian Arabian Company (Themar) for securities Brokerage EAC.
