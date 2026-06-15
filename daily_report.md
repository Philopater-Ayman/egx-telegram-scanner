# Telegram-First EGX Scanner Report

Scan phase: Pre-market risk check
Generated UTC: 2026-06-15T11:38:08.198014+00:00
Generated Cairo: 2026-06-15 14:38
Run timing: target 08:45 Cairo | generated Cairo 2026-06-15 14:38 | cron 45 5 * * 0-4
Trigger: scheduled cron=45 5 * * 0-4 mapped to pre_market; Cairo now 2026-06-15 14:34

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 0
- Tradeable price/liquidity tickers: 180/190
- Top sector: Automotive & Distribution

## Market Context
- Market trend: Bullish
- Source: Mubasher EGX market page (delayed public data)
- As of: Monday, June 15
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 35.0% / above MA50 55.0%
- EGX70 regime: BEARISH / above MA20 52.63% / above MA50 73.68%
- Sector breadth: 23.81%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- CCAP.CA: liquidity=991131328.0 spike=1.18 score=20.74
- COMI.CA: liquidity=810355584.0 spike=1.23 score=21.31
- PHDC.CA: liquidity=788413504.0 spike=2.05 score=25.5
- FWRY.CA: liquidity=555660160.0 spike=2.03 score=11.78
- EMFD.CA: liquidity=410697664.0 spike=1.66 score=24.72

## AI Narrative
- Provider: OpenRouter OK
- Model: openai/gpt-oss-120b:free
- Summary: The local scanner stays on HOLD as EGX30 and EGX70 remain in a bearish regime with weak breadth (23.81%). Liquidity is modest and most sectors, especially Real Estate and Automotive, show limited upside. Risk mode is DEFENSIVE_NO_NEW_BUY, so new entries are discouraged for the next 1‑3 days.
- EGX30/EGX70 trends are bearish; median 5‑day returns are negative and only ~35‑53% of stocks sit above MA20.
- Sector breadth is low; only Real Estate and Automotive show modest bullish watch signals but face resistance or extended momentum.
- Liquidity spikes exist (e.g., ARAB.CA, PHDC.CA) but market regime limits buying; expect sideways or further down pressure.
- Risk mode DEFENSIVE_NO_NEW_BUY reflects uncertainty – hold existing positions, watch for any regime shift before adding.
- Outlook for 1‑3 days remains cautious; monitor sector support levels and any change in EGX30/EGX70 breadth.

## Top Liquidity Spikes
- EASB.CA: spike=10.21 liquidity=20326756.0 outlook=CONSTRUCTIVE score=55.52 buy_ready=False
- MOSC.CA: spike=8.6 liquidity=57611036.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- ATLC.CA: spike=4.7 liquidity=19783046.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- MOED.CA: spike=3.98 liquidity=44293968.0 outlook=WEAK_OR_RISKY score=26.52 buy_ready=False
- KWIN.CA: spike=3.85 liquidity=15877190.0 outlook=BULLISH_WATCH score=85.52 buy_ready=False

## Sector Leaderboard
- #1 Automotive & Distribution: score=9.55 5d=5.54% 20d=-2.23% aboveMA50=100.0%
- #2 Real Estate: score=7.36 5d=1.94% 20d=5.26% aboveMA50=92.31%
- #3 Investment Holding: score=5.95 5d=2.48% 20d=0.96% aboveMA50=66.67%
- #4 Food, Beverages & Tobacco: score=5.26 5d=-0.93% 20d=0.18% aboveMA50=71.43%
- #5 Education: score=4.77 5d=0.22% 20d=-3.69% aboveMA50=100.0%
- #6 Banking & Financials: score=4.63 5d=-0.12% 20d=-1.16% aboveMA50=70.0%
- #7 Energy & Petrochemicals: score=4.2 5d=0.21% 20d=0.53% aboveMA50=75.0%
- #8 Textiles: score=4.12 5d=-2.08% 20d=3.81% aboveMA50=75.0%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- MTIE.CA: BULLISH_WATCH score=100 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=close to resistance
- ORHD.CA: BULLISH_WATCH score=92.36 liquidity=TRADEABLE sector=LEADING risk=No major short-term scanner risk flags.
- EFID.CA: BULLISH_WATCH score=92.26 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=No major short-term scanner risk flags.
- HDBK.CA: BULLISH_WATCH score=91.63 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=No major short-term scanner risk flags.
- OBRI.CA: BULLISH_WATCH score=91.52 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- ARAB.CA: BULLISH_WATCH score=90.36 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=momentum is extended
- MENA.CA: BULLISH_WATCH score=87.36 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- PHDC.CA: BULLISH_WATCH score=86.36 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=momentum is extended; far above support
- EMFD.CA: BULLISH_WATCH score=86.36 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=momentum is extended; far above support
- KWIN.CA: BULLISH_WATCH score=85.52 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- No provider failures.

## Ranked Scanner Results
- AALR.CA: score=10.48 buy_ready=False sector_rank=9 price=205.05 support=195.1 resistance=231.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=56.87 liquidity=2068511.38 spike=0.27
- ABUK.CA: score=9.76 buy_ready=False sector_rank=20 price=72.62 support=72.7 resistance=90.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=15.03 liquidity=189367440.0 spike=1.46
- ACAMD.CA: score=20.41 buy_ready=False sector_rank=9 price=2.3 support=2.14 resistance=2.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=62.69 liquidity=93977984.0 spike=0.72
- ACGC.CA: score=18.65 buy_ready=False sector_rank=8 price=9.36 support=8.95 resistance=10.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=40.88 liquidity=15239236.0 spike=0.26
- ADCI.CA: score=20.74 buy_ready=False sector_rank=9 price=226.87 support=202.22 resistance=230.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=71.08 liquidity=9674931.0 spike=1.33
- ADIB.CA: score=21.51 buy_ready=False sector_rank=6 price=47.37 support=44.01 resistance=48.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=35.44 liquidity=170337584.0 spike=1.33
- ADPC.CA: score=10.93 buy_ready=False sector_rank=9 price=3.55 support=3.45 resistance=4.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=39.71 liquidity=5525578.5 spike=0.22
- AFDI.CA: score=18.41 buy_ready=False sector_rank=9 price=42.32 support=40.15 resistance=46.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=54.95 liquidity=10479114.0 spike=0.62
- AFMC.CA: score=10.23 buy_ready=False sector_rank=9 price=71.35 support=67.0 resistance=80.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=56.21 liquidity=1821077.13 spike=0.3
- AJWA.CA: score=10.41 buy_ready=False sector_rank=9 price=170.69 support=160.0 resistance=179.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=73372952.0 spike=3.53
- ALCN.CA: score=15.3 buy_ready=False sector_rank=10 price=28.85 support=25.51 resistance=33.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=47.7 liquidity=12895700.0 spike=0.74
- ALUM.CA: score=12.7 buy_ready=False sector_rank=9 price=23.55 support=23.05 resistance=26.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=48.53 liquidity=4294864.5 spike=0.21
- AMER.CA: score=21.4 buy_ready=False sector_rank=2 price=2.63 support=2.52 resistance=3.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=46.81 liquidity=65388344.0 spike=0.61
- AMES.CA: score=3.75 buy_ready=False sector_rank=9 price=48.88 support=48.0 resistance=55.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=29.71 liquidity=1342877.63 spike=0.28
- AMIA.CA: score=19.11 buy_ready=False sector_rank=9 price=9.22 support=8.54 resistance=9.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=68.38 liquidity=24588330.0 spike=1.35
- AMOC.CA: score=10.68 buy_ready=False sector_rank=7 price=7.82 support=7.84 resistance=9.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=32.67 liquidity=75162784.0 spike=0.99
- ANFI.CA: score=23.67 buy_ready=False sector_rank=9 price=23.96 support=13.73 resistance=24.3 source=Yahoo Finance as_of=2026-06-13T21:00:00+00:00 freshness=FRESH RSI=92.83 liquidity=138402035.55 spike=3.13
- APSW.CA: score=0.04 buy_ready=False sector_rank=9 price=8.6 support=8.24 resistance=9.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:10 PM market time freshness=DELAYED_CURRENT RSI=31.58 liquidity=635381.31 spike=0.62
- ARAB.CA: score=29.72 buy_ready=False sector_rank=2 price=0.22 support=0.19 resistance=0.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=63.33 liquidity=275771776.0 spike=3.16
- ARCC.CA: score=20.17 buy_ready=False sector_rank=12 price=56.65 support=53.35 resistance=60.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=49.07 liquidity=24559662.0 spike=0.63
- AREH.CA: score=7.11 buy_ready=False sector_rank=9 price=1.61 support=1.53 resistance=1.62 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=49589756.0 spike=1.85
- ARVA.CA: score=6.83 buy_ready=False sector_rank=9 price=11.84 support=11.7 resistance=12.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=46859368.0 spike=1.71
- ASCM.CA: score=21.05 buy_ready=False sector_rank=9 price=60.77 support=47.3 resistance=61.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=80.32 liquidity=123792824.0 spike=1.82
- ASPI.CA: score=22.41 buy_ready=False sector_rank=9 price=0.31 support=0.25 resistance=0.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=63.12 liquidity=24665712.0 spike=0.36
- ATLC.CA: score=9.32 buy_ready=False sector_rank=18 price=5.2 support=4.84 resistance=5.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=19783046.0 spike=4.7
- ATQA.CA: score=12.84 buy_ready=False sector_rank=20 price=9.42 support=9.02 resistance=10.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=49.32 liquidity=23732532.0 spike=0.65
- AXPH.CA: score=9.54 buy_ready=False sector_rank=9 price=1121.32 support=1111.0 resistance=1185.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=40.02 liquidity=1133709.5 spike=0.35
- BINV.CA: score=25.0 buy_ready=False sector_rank=3 price=47.89 support=40.8 resistance=49.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=62.61 liquidity=14885671.0 spike=1.31
- BIOC.CA: score=9.47 buy_ready=False sector_rank=9 price=70.84 support=68.34 resistance=79.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=51.09 liquidity=1061660.0 spike=0.2
- BTFH.CA: score=13.34 buy_ready=False sector_rank=18 price=3.02 support=2.96 resistance=3.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=49.23 liquidity=208146096.0 spike=1.01
- CAED.CA: score=7.61 buy_ready=False sector_rank=9 price=71.04 support=67.21 resistance=79.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=27.09 liquidity=4202823.5 spike=0.46
- CANA.CA: score=6.03 buy_ready=False sector_rank=6 price=38.0 support=36.04 resistance=38.23 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=15355639.0 spike=1.09
- CCAP.CA: score=20.74 buy_ready=False sector_rank=3 price=5.04 support=4.94 resistance=5.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=56.52 liquidity=991131328.0 spike=1.18
- CCRS.CA: score=18.41 buy_ready=False sector_rank=9 price=2.4 support=2.22 resistance=2.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=45.76 liquidity=14356150.0 spike=0.56
- CEFM.CA: score=10.28 buy_ready=False sector_rank=9 price=103.48 support=100.53 resistance=119.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=51.29 liquidity=1875774.88 spike=0.52
- CERA.CA: score=17.64 buy_ready=False sector_rank=9 price=1.18 support=1.13 resistance=1.23 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=61.54 liquidity=8234990.0 spike=0.61
- CFGH.CA: score=-0.59 buy_ready=False sector_rank=9 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance as_of=2026-06-13T21:00:00+00:00 freshness=FRESH RSI=0.0 liquidity=1904.14 spike=0.31
- CICH.CA: score=0.87 buy_ready=False sector_rank=18 price=11.6 support=11.1 resistance=13.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=23.96 liquidity=1549266.5 spike=0.44
- CIEB.CA: score=13.89 buy_ready=False sector_rank=6 price=23.48 support=23.27 resistance=24.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=56.74 liquidity=7914850.5 spike=1.06
- CIRA.CA: score=17.68 buy_ready=False sector_rank=5 price=26.81 support=25.23 resistance=28.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=46.14 liquidity=6767461.5 spike=0.27
- CLHO.CA: score=17.96 buy_ready=False sector_rank=13 price=15.49 support=14.25 resistance=16.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=45.06 liquidity=11005159.0 spike=0.37
- CNFN.CA: score=8.83 buy_ready=False sector_rank=18 price=4.42 support=4.36 resistance=4.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=40.28 liquidity=5509052.5 spike=0.35
- COMI.CA: score=21.31 buy_ready=False sector_rank=6 price=134.95 support=129.8 resistance=136.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=46.42 liquidity=810355584.0 spike=1.23
- COPR.CA: score=17.41 buy_ready=False sector_rank=9 price=0.36 support=0.32 resistance=0.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=56.25 liquidity=16410239.0 spike=0.4
- COSG.CA: score=18.41 buy_ready=False sector_rank=9 price=1.57 support=1.49 resistance=1.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=57.14 liquidity=30665104.0 spike=0.44
- CPCI.CA: score=10.23 buy_ready=False sector_rank=9 price=362.32 support=345.0 resistance=368.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=71.26 liquidity=1820886.75 spike=0.67
- CSAG.CA: score=20.3 buy_ready=False sector_rank=10 price=31.39 support=30.08 resistance=32.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=53.78 liquidity=11060223.0 spike=0.8
- DAPH.CA: score=7.38 buy_ready=False sector_rank=9 price=77.72 support=76.6 resistance=89.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=39.56 liquidity=2973126.25 spike=0.1
- DEIN.CA: score=6.41 buy_ready=False sector_rank=9 price=11.38 support=11.38 resistance=13.65 source=Yahoo Finance as_of=2026-06-13T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- DOMT.CA: score=1.68 buy_ready=False sector_rank=4 price=24.35 support=23.7 resistance=26.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=26.34 liquidity=576830.88 spike=0.23
- DSCW.CA: score=18.61 buy_ready=False sector_rank=9 price=1.8 support=1.71 resistance=1.91 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=55.17 liquidity=55835188.0 spike=1.1
- DTPP.CA: score=3.48 buy_ready=False sector_rank=9 price=117.16 support=117.01 resistance=137.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=22.87 liquidity=2710376.75 spike=1.18
- EALR.CA: score=9.9 buy_ready=False sector_rank=9 price=353.48 support=346.01 resistance=383.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=48.61 liquidity=1492011.25 spike=0.34
- EASB.CA: score=24.41 buy_ready=False sector_rank=9 price=6.11 support=4.61 resistance=6.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=88.89 liquidity=20326756.0 spike=10.21
- EAST.CA: score=21.1 buy_ready=False sector_rank=4 price=39.79 support=37.01 resistance=39.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=47.08 liquidity=46693852.0 spike=0.71
- EBSC.CA: score=12.83 buy_ready=False sector_rank=9 price=1.89 support=1.64 resistance=2.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=70.37 liquidity=2424886.25 spike=0.9
- ECAP.CA: score=12.92 buy_ready=False sector_rank=9 price=31.77 support=28.7 resistance=32.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=91.4 liquidity=3515851.0 spike=0.67
- EDFM.CA: score=8.73 buy_ready=False sector_rank=9 price=334.03 support=320.2 resistance=355.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=56.59 liquidity=317029.5 spike=0.47
- EEII.CA: score=13.28 buy_ready=False sector_rank=9 price=2.37 support=2.27 resistance=2.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=57.45 liquidity=4874558.5 spike=0.25
- EFIC.CA: score=0.2 buy_ready=False sector_rank=20 price=205.05 support=192.01 resistance=219.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=16.09 liquidity=2355921.5 spike=0.68
- EFID.CA: score=23.34 buy_ready=False sector_rank=4 price=28.76 support=27.06 resistance=29.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=47.53 liquidity=154632176.0 spike=2.12
- EFIH.CA: score=18.08 buy_ready=False sector_rank=15 price=21.35 support=20.2 resistance=22.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=37.78 liquidity=67132584.0 spike=1.18
- EGAL.CA: score=9.5 buy_ready=False sector_rank=20 price=299.11 support=305.01 resistance=335.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=28.51 liquidity=135857120.0 spike=1.33
- EGAS.CA: score=22.7 buy_ready=False sector_rank=7 price=51.5 support=46.51 resistance=55.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=73.53 liquidity=12446770.0 spike=1.01
- EGBE.CA: score=8.91 buy_ready=False sector_rank=6 price=0.43 support=0.44 resistance=0.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:09 PM market time freshness=DELAYED_CURRENT RSI=43.01 liquidity=55901.77 spike=0.4
- EGCH.CA: score=16.84 buy_ready=False sector_rank=20 price=13.2 support=13.2 resistance=15.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=43.39 liquidity=47753080.0 spike=0.44
- EGSA.CA: score=2.5 buy_ready=False sector_rank=17 price=8.74 support=8.3 resistance=9.19 source=Yahoo Finance as_of=2026-06-13T21:00:00+00:00 freshness=FRESH RSI=21.87 liquidity=5742.18 spike=0.39
- EGTS.CA: score=21.4 buy_ready=False sector_rank=2 price=17.8 support=14.72 resistance=22.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=48.17 liquidity=43853932.0 spike=0.36
- EHDR.CA: score=20.41 buy_ready=False sector_rank=9 price=2.71 support=2.25 resistance=2.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=73.39 liquidity=52770784.0 spike=0.93
- EKHO.CA: score=10.68 buy_ready=False sector_rank=7 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-06-13T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=13.14 buy_ready=False sector_rank=19 price=2.11 support=2.06 resistance=2.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=56.67 liquidity=10737682.0 spike=0.4
- ELKA.CA: score=19.41 buy_ready=False sector_rank=9 price=1.26 support=1.12 resistance=1.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=66.67 liquidity=35711028.0 spike=0.8
- ELNA.CA: score=8.05 buy_ready=False sector_rank=9 price=37.74 support=37.11 resistance=41.99 source=Yahoo Finance as_of=2026-06-13T21:00:00+00:00 freshness=FRESH RSI=35.15 liquidity=820580.86 spike=2.41
- ELSH.CA: score=17.41 buy_ready=False sector_rank=9 price=12.95 support=8.1 resistance=14.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=76.86 liquidity=107820752.0 spike=0.63
- ELWA.CA: score=15.47 buy_ready=False sector_rank=9 price=2.1 support=1.79 resistance=2.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=77.78 liquidity=4879554.5 spike=1.59
- EMFD.CA: score=24.72 buy_ready=False sector_rank=2 price=12.29 support=9.83 resistance=12.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=68.06 liquidity=410697664.0 spike=1.66
- ENGC.CA: score=23.41 buy_ready=False sector_rank=9 price=35.94 support=32.31 resistance=35.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=65.98 liquidity=33648780.0 spike=2.5
- EOSB.CA: score=13.87 buy_ready=False sector_rank=9 price=1.48 support=1.34 resistance=1.55 source=Yahoo Finance as_of=2026-06-13T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=198135.0 spike=1.63
- EPCO.CA: score=16.58 buy_ready=False sector_rank=9 price=9.25 support=8.56 resistance=9.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=47.83 liquidity=6171765.5 spike=0.55
- EPPK.CA: score=6.75 buy_ready=False sector_rank=9 price=11.86 support=11.67 resistance=13.0 source=Yahoo Finance as_of=2026-06-13T21:00:00+00:00 freshness=FRESH RSI=45.61 liquidity=1064909.37 spike=1.14
- ETEL.CA: score=9.97 buy_ready=False sector_rank=17 price=92.58 support=89.61 resistance=98.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=31.37 liquidity=101668704.0 spike=1.24
- ETRS.CA: score=21.97 buy_ready=False sector_rank=9 price=10.09 support=7.37 resistance=9.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=77.99 liquidity=133732128.0 spike=2.28
- EXPA.CA: score=18.85 buy_ready=False sector_rank=6 price=18.61 support=18.31 resistance=20.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=45.57 liquidity=15120278.0 spike=0.42
- FAIT.CA: score=14.03 buy_ready=False sector_rank=6 price=37.42 support=35.01 resistance=38.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=42.86 liquidity=3179499.0 spike=0.53
- FAITA.CA: score=12.87 buy_ready=False sector_rank=6 price=1.0 support=0.98 resistance=1.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=60.0 liquidity=22158.95 spike=0.5
- FERC.CA: score=0.12 buy_ready=False sector_rank=20 price=76.0 support=75.0 resistance=81.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=23.87 liquidity=1278604.88 spike=0.24
- FWRY.CA: score=11.78 buy_ready=False sector_rank=15 price=18.77 support=17.71 resistance=20.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=33.26 liquidity=555660160.0 spike=2.03
- GBCO.CA: score=24.4 buy_ready=False sector_rank=1 price=28.45 support=25.25 resistance=29.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=72.42 liquidity=102518632.0 spike=0.88
- GDWA.CA: score=18.02 buy_ready=False sector_rank=9 price=0.8 support=0.77 resistance=0.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=55.65 liquidity=8613058.0 spike=0.65
- GGCC.CA: score=12.87 buy_ready=False sector_rank=9 price=0.41 support=0.39 resistance=0.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=57.3 liquidity=5459833.5 spike=0.73
- GIHD.CA: score=13.75 buy_ready=False sector_rank=9 price=41.35 support=35.15 resistance=43.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=58.24 liquidity=3345570.0 spike=0.8
- GMCI.CA: score=13.33 buy_ready=False sector_rank=9 price=1.78 support=1.68 resistance=1.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=39.29 liquidity=765873.25 spike=2.08
- GRCA.CA: score=5.9 buy_ready=False sector_rank=9 price=55.41 support=50.2 resistance=60.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=30.85 liquidity=5493731.0 spike=0.64
- GSSC.CA: score=3.28 buy_ready=False sector_rank=9 price=248.31 support=228.1 resistance=272.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:10 PM market time freshness=DELAYED_CURRENT RSI=21.32 liquidity=2869640.5 spike=0.49
- GTWL.CA: score=3.59 buy_ready=False sector_rank=9 price=46.34 support=45.47 resistance=58.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=29.05 liquidity=3177269.0 spike=0.45
- HDBK.CA: score=25.17 buy_ready=False sector_rank=6 price=146.79 support=138.0 resistance=146.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=49.95 liquidity=40530624.0 spike=3.16
- HELI.CA: score=21.4 buy_ready=False sector_rank=2 price=6.42 support=6.28 resistance=6.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=55.42 liquidity=126627592.0 spike=0.83
- HRHO.CA: score=15.4 buy_ready=False sector_rank=18 price=27.03 support=25.8 resistance=28.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=47.54 liquidity=147303056.0 spike=1.04
- ICID.CA: score=16.6 buy_ready=False sector_rank=9 price=7.0 support=4.5 resistance=7.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=87.09 liquidity=9190246.0 spike=0.57
- IDRE.CA: score=16.37 buy_ready=False sector_rank=9 price=43.08 support=41.01 resistance=47.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=43.87 liquidity=7958462.5 spike=0.25
- IFAP.CA: score=6.67 buy_ready=False sector_rank=14 price=19.51 support=16.5 resistance=23.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=35.69 liquidity=2849172.5 spike=0.33
- INFI.CA: score=9.51 buy_ready=False sector_rank=9 price=98.25 support=97.0 resistance=109.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=24.0 liquidity=7105197.0 spike=0.48
- IRON.CA: score=7.1 buy_ready=False sector_rank=20 price=32.04 support=31.3 resistance=35.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=43.27 liquidity=4260840.0 spike=0.55
- ISMA.CA: score=19.41 buy_ready=False sector_rank=9 price=30.25 support=23.1 resistance=31.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=88.93 liquidity=20891952.0 spike=0.53
- ISMQ.CA: score=21.54 buy_ready=False sector_rank=20 price=8.17 support=7.27 resistance=8.62 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=72.52 liquidity=92630552.0 spike=1.35
- ISPH.CA: score=19.96 buy_ready=False sector_rank=13 price=12.15 support=11.12 resistance=12.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=59.29 liquidity=80720968.0 spike=0.6
- JUFO.CA: score=21.42 buy_ready=False sector_rank=4 price=30.83 support=26.51 resistance=30.82 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=70.29 liquidity=51422992.0 spike=1.16
- KABO.CA: score=17.49 buy_ready=False sector_rank=8 price=6.24 support=5.92 resistance=6.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=57.27 liquidity=6839380.0 spike=0.33
- KWIN.CA: score=25.41 buy_ready=False sector_rank=9 price=75.04 support=69.0 resistance=77.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=58.34 liquidity=15877190.0 spike=3.85
- KZPC.CA: score=13.98 buy_ready=False sector_rank=9 price=10.54 support=10.3 resistance=11.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=57.05 liquidity=5569690.0 spike=0.5
- LCSW.CA: score=12.99 buy_ready=False sector_rank=12 price=26.65 support=26.0 resistance=28.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=38.69 liquidity=4826559.0 spike=0.42
- LUTS.CA: score=23.85 buy_ready=False sector_rank=9 price=0.75 support=0.54 resistance=0.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=86.92 liquidity=92955160.0 spike=3.22
- MAAL.CA: score=9.88 buy_ready=False sector_rank=9 price=5.79 support=4.44 resistance=6.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=78.65 liquidity=2474622.75 spike=0.19
- MASR.CA: score=21.79 buy_ready=False sector_rank=9 price=7.1 support=6.54 resistance=7.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=52.08 liquidity=92981208.0 spike=1.69
- MBSC.CA: score=18.81 buy_ready=False sector_rank=12 price=271.99 support=262.02 resistance=295.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=41.84 liquidity=63298204.0 spike=1.32
- MCQE.CA: score=10.17 buy_ready=False sector_rank=12 price=178.81 support=174.0 resistance=201.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=27.73 liquidity=13185312.0 spike=0.73
- MCRO.CA: score=14.41 buy_ready=False sector_rank=9 price=1.23 support=1.2 resistance=1.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=17257490.0 spike=0.32
- MENA.CA: score=20.35 buy_ready=False sector_rank=2 price=6.73 support=5.91 resistance=7.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=55.67 liquidity=6948906.5 spike=0.41
- MEPA.CA: score=18.41 buy_ready=False sector_rank=9 price=1.7 support=1.63 resistance=1.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=57.69 liquidity=11087726.0 spike=0.61
- MFPC.CA: score=10.34 buy_ready=False sector_rank=20 price=37.51 support=38.15 resistance=46.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=5.34 liquidity=149142768.0 spike=1.75
- MFSC.CA: score=6.1 buy_ready=False sector_rank=9 price=45.52 support=43.0 resistance=65.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=29.01 liquidity=2691249.75 spike=0.17
- MHOT.CA: score=9.1 buy_ready=False sector_rank=11 price=29.73 support=26.3 resistance=34.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=34.99 liquidity=5870786.5 spike=0.27
- MICH.CA: score=20.41 buy_ready=False sector_rank=9 price=37.0 support=35.05 resistance=40.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=66.34 liquidity=10624359.0 spike=0.74
- MILS.CA: score=20.57 buy_ready=False sector_rank=9 price=146.0 support=127.01 resistance=153.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=71.63 liquidity=20681240.0 spike=1.08
- MIPH.CA: score=10.91 buy_ready=False sector_rank=13 price=662.15 support=640.0 resistance=700.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:08 PM market time freshness=DELAYED_CURRENT RSI=54.88 liquidity=947748.19 spike=0.33
- MOED.CA: score=14.41 buy_ready=False sector_rank=9 price=0.71 support=0.65 resistance=0.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=30.85 liquidity=44293968.0 spike=3.98
- MOIL.CA: score=8.75 buy_ready=False sector_rank=7 price=0.47 support=0.44 resistance=0.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=62.12 liquidity=66865.75 spike=0.36
- MOIN.CA: score=8.09 buy_ready=False sector_rank=9 price=24.88 support=24.1 resistance=26.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=40.38 liquidity=682794.0 spike=0.39
- MOSC.CA: score=10.41 buy_ready=False sector_rank=9 price=280.61 support=280.0 resistance=330.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=57611036.0 spike=8.6
- MPCI.CA: score=18.41 buy_ready=False sector_rank=9 price=218.53 support=197.0 resistance=238.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=67.25 liquidity=20802486.0 spike=0.24
- MPCO.CA: score=9.82 buy_ready=False sector_rank=14 price=1.99 support=1.8 resistance=1.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=281222688.0 spike=3.65
- MPRC.CA: score=17.85 buy_ready=False sector_rank=9 price=31.88 support=30.61 resistance=34.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=63.94 liquidity=9442450.0 spike=0.46
- MTIE.CA: score=25.4 buy_ready=False sector_rank=1 price=9.23 support=8.65 resistance=9.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=55.78 liquidity=28317724.0 spike=1.5
- NAHO.CA: score=4.44 buy_ready=False sector_rank=9 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=42.86 liquidity=33520.83 spike=0.94
- NCCW.CA: score=17.41 buy_ready=False sector_rank=9 price=6.44 support=5.13 resistance=6.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=78.22 liquidity=24594750.0 spike=0.91
- NEDA.CA: score=8.56 buy_ready=False sector_rank=9 price=2.75 support=2.65 resistance=2.87 source=Yahoo Finance as_of=2026-06-13T21:00:00+00:00 freshness=FRESH RSI=53.57 liquidity=151602.0 spike=0.37
- NHPS.CA: score=6.37 buy_ready=False sector_rank=9 price=67.72 support=65.03 resistance=72.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=40.0 liquidity=1959093.38 spike=0.38
- NINH.CA: score=5.37 buy_ready=False sector_rank=9 price=17.36 support=16.8 resistance=19.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=34.72 liquidity=1961630.13 spike=0.27
- NIPH.CA: score=17.96 buy_ready=False sector_rank=13 price=162.03 support=155.1 resistance=176.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=52.23 liquidity=27632372.0 spike=0.27
- OBRI.CA: score=24.01 buy_ready=False sector_rank=9 price=36.8 support=33.63 resistance=38.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=51.18 liquidity=23810948.0 spike=1.8
- OCDI.CA: score=18.4 buy_ready=False sector_rank=2 price=20.7 support=20.0 resistance=22.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=45.76 liquidity=16559174.0 spike=0.46
- OCPH.CA: score=5.53 buy_ready=False sector_rank=9 price=344.59 support=337.0 resistance=394.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=28.16 liquidity=2123629.5 spike=0.28
- ODIN.CA: score=21.85 buy_ready=False sector_rank=9 price=2.18 support=1.89 resistance=2.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=68.75 liquidity=18650350.0 spike=1.72
- OFH.CA: score=18.41 buy_ready=False sector_rank=9 price=0.62 support=0.59 resistance=0.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=52.73 liquidity=14229585.0 spike=0.62
- OIH.CA: score=17.38 buy_ready=False sector_rank=3 price=1.37 support=1.33 resistance=1.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=37.5 liquidity=72252392.0 spike=0.75
- OLFI.CA: score=22.98 buy_ready=False sector_rank=4 price=22.47 support=21.0 resistance=22.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=76.16 liquidity=46518716.0 spike=2.44
- ORAS.CA: score=4.6 buy_ready=False sector_rank=16 price=779.75 support=772.0 resistance=785.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=257348032.0 spike=1.0
- ORHD.CA: score=23.4 buy_ready=False sector_rank=2 price=37.23 support=33.09 resistance=39.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=59.12 liquidity=158228128.0 spike=0.84
- ORWE.CA: score=20.65 buy_ready=False sector_rank=8 price=23.13 support=21.6 resistance=24.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=61.86 liquidity=14624994.0 spike=0.33
- PHAR.CA: score=14.96 buy_ready=False sector_rank=13 price=84.02 support=83.02 resistance=91.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=49.27 liquidity=20233196.0 spike=0.65
- PHDC.CA: score=25.5 buy_ready=False sector_rank=2 price=16.09 support=13.01 resistance=16.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=64.33 liquidity=788413504.0 spike=2.05
- PHTV.CA: score=9.31 buy_ready=False sector_rank=9 price=219.5 support=207.0 resistance=223.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=41095176.0 spike=2.95
- POUL.CA: score=19.88 buy_ready=False sector_rank=4 price=36.75 support=34.8 resistance=38.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=35.8 liquidity=61627728.0 spike=1.39
- PRCL.CA: score=20.85 buy_ready=False sector_rank=12 price=24.52 support=21.01 resistance=28.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=59.36 liquidity=38295884.0 spike=1.34
- PRDC.CA: score=22.4 buy_ready=False sector_rank=2 price=6.67 support=5.3 resistance=6.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=81.2 liquidity=26671304.0 spike=0.3
- PRMH.CA: score=19.49 buy_ready=False sector_rank=9 price=2.77 support=2.19 resistance=2.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=75.61 liquidity=24670720.0 spike=1.04
- RACC.CA: score=8.88 buy_ready=False sector_rank=9 price=9.68 support=9.38 resistance=10.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=32.99 liquidity=5473105.5 spike=0.46
- RAKT.CA: score=7.15 buy_ready=False sector_rank=9 price=22.59 support=22.1 resistance=25.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=44.37 liquidity=662938.56 spike=2.04
- RAYA.CA: score=11.75 buy_ready=False sector_rank=21 price=6.98 support=6.7 resistance=8.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=30.28 liquidity=65277968.0 spike=0.66
- RMDA.CA: score=19.96 buy_ready=False sector_rank=13 price=5.1 support=4.92 resistance=5.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=54.63 liquidity=22707772.0 spike=0.25
- ROTO.CA: score=18.23 buy_ready=False sector_rank=9 price=34.47 support=32.66 resistance=35.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=56.22 liquidity=7825696.5 spike=0.59
- RREI.CA: score=20.03 buy_ready=False sector_rank=9 price=3.5 support=3.32 resistance=3.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=57.32 liquidity=9623932.0 spike=0.45
- RTVC.CA: score=9.73 buy_ready=False sector_rank=9 price=3.85 support=3.75 resistance=4.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=49.28 liquidity=2317863.25 spike=0.34
- RUBX.CA: score=11.14 buy_ready=False sector_rank=9 price=9.86 support=9.8 resistance=11.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=43.87 liquidity=6733428.5 spike=0.57
- SAUD.CA: score=15.18 buy_ready=False sector_rank=6 price=22.0 support=20.82 resistance=23.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=36.86 liquidity=9327789.0 spike=0.68
- SCEM.CA: score=14.7 buy_ready=False sector_rank=12 price=62.19 support=59.3 resistance=67.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=38.15 liquidity=6530380.5 spike=0.17
- SCFM.CA: score=11.18 buy_ready=False sector_rank=9 price=253.42 support=248.1 resistance=315.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=37.43 liquidity=5771633.5 spike=0.45
- SCTS.CA: score=7.47 buy_ready=False sector_rank=5 price=605.92 support=590.01 resistance=689.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=29.2 liquidity=3560835.0 spike=0.52
- SDTI.CA: score=15.77 buy_ready=False sector_rank=9 price=46.96 support=43.4 resistance=47.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=71.43 liquidity=3360165.75 spike=0.21
- SEIG.CA: score=9.54 buy_ready=False sector_rank=9 price=181.31 support=173.35 resistance=205.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=53.04 liquidity=1131488.0 spike=0.22
- SIPC.CA: score=11.26 buy_ready=False sector_rank=9 price=3.47 support=3.4 resistance=3.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=45.28 liquidity=5854437.5 spike=0.42
- SKPC.CA: score=12.84 buy_ready=False sector_rank=20 price=16.35 support=16.29 resistance=18.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=36.29 liquidity=32323312.0 spike=0.56
- SMFR.CA: score=11.67 buy_ready=False sector_rank=9 price=204.19 support=192.0 resistance=222.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=39.88 liquidity=3263444.5 spike=0.56
- SNFC.CA: score=20.41 buy_ready=False sector_rank=9 price=12.39 support=11.68 resistance=12.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=45.53 liquidity=10476181.0 spike=0.39
- SPIN.CA: score=1.48 buy_ready=False sector_rank=8 price=14.03 support=13.61 resistance=15.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=30.56 liquidity=835436.13 spike=0.18
- SPMD.CA: score=10.75 buy_ready=False sector_rank=9 price=0.41 support=0.38 resistance=0.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=59.29 liquidity=2337966.75 spike=0.1
- SUGR.CA: score=8.29 buy_ready=False sector_rank=4 price=48.54 support=48.0 resistance=52.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=53.03 liquidity=3188448.75 spike=0.21
- SVCE.CA: score=7.91 buy_ready=False sector_rank=9 price=9.1 support=8.56 resistance=9.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=200865840.0 spike=2.25
- SWDY.CA: score=14.65 buy_ready=False sector_rank=19 price=86.19 support=84.01 resistance=90.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=47.16 liquidity=7511027.5 spike=0.33
- TALM.CA: score=11.13 buy_ready=False sector_rank=5 price=16.12 support=15.12 resistance=16.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=79.41 liquidity=3220752.0 spike=0.28
- TMGH.CA: score=21.4 buy_ready=False sector_rank=2 price=95.03 support=91.87 resistance=101.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=45.24 liquidity=340163264.0 spike=0.75
- TRTO.CA: score=8.81 buy_ready=False sector_rank=9 price=0.03 support=0.03 resistance=0.04 source=Yahoo Finance as_of=2026-06-13T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=1849.87 spike=2.2
- UEFM.CA: score=2.88 buy_ready=False sector_rank=9 price=472.48 support=455.6 resistance=500.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=27.33 liquidity=1734027.88 spike=1.87
- UEGC.CA: score=22.41 buy_ready=False sector_rank=9 price=1.41 support=1.3 resistance=1.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:10 PM market time freshness=DELAYED_CURRENT RSI=61.76 liquidity=10028577.0 spike=0.39
- UNIP.CA: score=13.05 buy_ready=False sector_rank=9 price=0.32 support=0.28 resistance=0.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=81.82 liquidity=6638630.5 spike=0.33
- UNIT.CA: score=14.73 buy_ready=False sector_rank=2 price=13.48 support=12.07 resistance=15.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=63.0 liquidity=1325251.13 spike=0.12
- WCDF.CA: score=1.79 buy_ready=False sector_rank=9 price=507.59 support=450.0 resistance=554.25 source=Yahoo Finance as_of=2026-06-13T21:00:00+00:00 freshness=FRESH RSI=2.97 liquidity=465460.03 spike=1.46
- WKOL.CA: score=7.74 buy_ready=False sector_rank=9 price=290.5 support=290.0 resistance=315.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=45.46 liquidity=2329442.25 spike=0.58
- ZEOT.CA: score=21.73 buy_ready=False sector_rank=9 price=9.4 support=8.41 resistance=9.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=65.99 liquidity=10127466.0 spike=1.66
- ZMID.CA: score=25.4 buy_ready=False sector_rank=2 price=6.16 support=5.77 resistance=6.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=62.32 liquidity=119178112.0 spike=0.5

## Backtesting Lite
- ARAB.CA: 180d return=14.13%, max drawdown=-38.02%, MA20>MA50 days last20=20, as_of=2026-06-13T21:00:00+00:00
- PHDC.CA: 180d return=115.21%, max drawdown=-15.81%, MA20>MA50 days last20=20, as_of=2026-06-13T21:00:00+00:00
- KWIN.CA: 180d return=-0.77%, max drawdown=-34.04%, MA20>MA50 days last20=20, as_of=2026-06-13T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- ARAB.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Arab Developers Holding summary=Arab Developers Holding unveils EGP 1bn expansion plans to improve financial efficiency; FRA gives initial approval for Arab Developers’ rights issue; Arab Developers stock stabilizes after correction
  - Arab Developers Holding unveils EGP 1bn expansion plans to improve financial efficiency: https://english.mubasher.info/news/4601724/Arab-Developers-Holding-unveils-EGP-1bn-expansion-plans-to-improve-financial-efficiency/
  - FRA gives initial approval for Arab Developers’ rights issue: https://english.mubasher.info/news/4582627/FRA-gives-initial-approval-for-Arab-Developers-rights-issue/
  - Arab Developers stock stabilizes after correction: https://english.mubasher.info/news/4564643/Arab-Developers-stock-stabilizes-after-correction/
- PHDC.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=530 sources=3 expected=Palm Hills Development summary=Palm Hills, UAE’s Miran to launch new development project in Ras Al Hikma; Palm Hills records 30% higher profits in 2025, unveils new project in UAE; Strong momentum pushes Palm Hills toward EGP 10.15
  - Palm Hills, UAE’s Miran to launch new development project in Ras Al Hikma: https://english.mubasher.info/news/4598123/Palm-Hills-UAE-s-Miran-to-launch-new-development-project-in-Ras-Al-Hikma/
  - Palm Hills records 30% higher profits in 2025, unveils new project in UAE: https://english.mubasher.info/news/4580548/Palm-Hills-records-30-higher-profits-in-2025-unveils-new-project-in-UAE/
  - Strong momentum pushes Palm Hills toward EGP 10.15: https://english.mubasher.info/news/4560871/Strong-momentum-pushes-Palm-Hills-toward-EGP-10-15/
- KWIN.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=El Kahera El Watania Investment summary=ADIB Egypt&#39;s Cairo National unveils equity reduction transaction worth over EGP 3m; El Kahera El Watania to buy stake in Assiut for Agricultural Development; Tycoon Holding acquires 85% of Alexandria National Investment
  - ADIB Egypt&#39;s Cairo National unveils equity reduction transaction worth over EGP 3m: https://english.mubasher.info/news/4546852/ADIB-Egypt-s-Cairo-National-unveils-equity-reduction-transaction-worth-over-EGP-3m/
  - El Kahera El Watania to buy stake in Assiut for Agricultural Development: https://english.mubasher.info/news/4009433/El-Kahera-El-Watania-to-buy-stake-in-Assiut-for-Agricultural-Development/
  - Tycoon Holding acquires 85% of Alexandria National Investment: https://english.mubasher.info/news/3844623/Tycoon-Holding-acquires-85-of-Alexandria-National-Investment/
- MTIE.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=MM Group For Industry and International Trade summary=Evidence rejected for MTIE.CA: source text did not clearly match MTIE.CA / MM Group For Industry and International Trade.
- ZMID.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=530 sources=3 expected=Zahraa Maadi Investment and Development summary=Zahraa Maadi unveils distribution date for 2025 cash dividends; Zahraa Maadi to disburse EGP 250m dividends for 2025; Zahraa Maadi’s stock faces key resistance at EGP 5.22
  - Zahraa Maadi unveils distribution date for 2025 cash dividends: https://english.mubasher.info/news/4594804/Zahraa-Maadi-unveils-distribution-date-for-2025-cash-dividends/
  - Zahraa Maadi to disburse EGP 250m dividends for 2025: https://english.mubasher.info/news/4583591/Zahraa-Maadi-to-disburse-EGP-250m-dividends-for-2025/
  - Zahraa Maadi’s stock faces key resistance at EGP 5.22: https://english.mubasher.info/news/4563531/Zahraa-Maadi-s-stock-faces-key-resistance-at-EGP-5-22/
- HDBK.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Housing and Development Bank Egypt summary=Evidence rejected for HDBK.CA: source text did not clearly match HDBK.CA / Housing and Development Bank Egypt.
- BINV.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=B Investments Holding summary=Evidence rejected for BINV.CA: source text did not clearly match BINV.CA / B Investments Holding.
- EMFD.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=530 sources=3 expected=Emaar Misr for Development summary=Emaar Misr posts higher revenues at EGP 19.8bn in 2025; Emaar Misr’s consolidated net profits drop to EGP 4.2bn in 9M-25; Emaar Misr, Golden Coast to establish EGP 900bn project in Red Sea
  - Emaar Misr posts higher revenues at EGP 19.8bn in 2025: https://english.mubasher.info/news/4561643/Emaar-Misr-posts-higher-revenues-at-EGP-19-8bn-in-2025/
  - Emaar Misr’s consolidated net profits drop to EGP 4.2bn in 9M-25: https://english.mubasher.info/news/4525192/Emaar-Misr-s-consolidated-net-profits-drop-to-EGP-4-2bn-in-9M-25/
  - Emaar Misr, Golden Coast to establish EGP 900bn project in Red Sea: https://english.mubasher.info/news/4495287/Emaar-Misr-Golden-Coast-to-establish-EGP-900bn-project-in-Red-Sea/

## Warnings
- Evidence for ARAB.CA matches the company but no source/report date was detected.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence for PHDC.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for KWIN.CA matches the company but no source/report date was detected.
- Evidence rejected for MTIE.CA: source text did not clearly match MTIE.CA / MM Group For Industry and International Trade.
- Evidence for ZMID.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for HDBK.CA: source text did not clearly match HDBK.CA / Housing and Development Bank Egypt.
- Evidence rejected for BINV.CA: source text did not clearly match BINV.CA / B Investments Holding.
- Evidence for EMFD.CA matches the company but appears old; latest detected date is 2025-01-01.
