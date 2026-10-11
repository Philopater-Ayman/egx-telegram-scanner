# Telegram-First EGX Scanner Report

Scan phase: Post-close tomorrow tickets
Generated UTC: 2026-10-11T17:46:44.622614+00:00
Generated Cairo: 2026-10-11 20:46
Run timing: target 15:30 Cairo | generated Cairo 2026-10-11 20:46 | cron 30 12 * * 0-4
Trigger: scheduled cron=30 12 * * 0-4 mapped to post_close; Cairo now 2026-10-11 20:43

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 4
- Tradeable price/liquidity tickers: 173/186
- Top sector: Fintech & Payments

## Market Context
- Market trend: Bearish
- Source: Mubasher EGX market page (delayed public data)
- As of: Sunday, October 11
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 15.79% / above MA50 31.58%
- EGX70 regime: BEARISH / above MA20 25.0% / above MA50 27.5%
- Sector breadth: 23.81%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- CCAP.CA: liquidity=541020544.0 spike=0.7 score=19.13
- ARAB.CA: liquidity=272625024.0 spike=3.46 score=26.08
- SCEM.CA: liquidity=217248688.0 spike=3.61 score=12.4
- ORAS.CA: liquidity=198533728.0 spike=1.0 score=4.6
- AMOC.CA: liquidity=163932304.0 spike=1.18 score=22.9

## AI Narrative
- Provider: OpenRouter OK
- Model: nvidia/nemotron-3-super-120b-a12b:free
- Summary: EGX30 and EGX70 are bearish with weak breadth (sector breadth 23.8%), risk mode defensive (no new buys); scanner highlights a few stocks with bullish‑watch outlook and accumulation‑spike liquidity, but holds due to the prevailing regime.
- Top tickets (EFIH.CA, MBSC.CA, ARCC.CA) show accumulation‑spike liquidity and bullish‑watch outlook yet sit far above 20‑day support, limiting near‑term upside.
- Liquidity is tradeable or spiking for many names, but ETEL.CA, TALM.CA and RUBX.CA show cooling liquidity and extended momentum, adding uncertainty.
- Sector leadership is narrow—Fintech & Payments and Telecommunications lead, while Building Materials shows mixed returns, keeping overall sector breadth low.
- EGX30/EGX70 bearish trend and defensive risk mode override the scanner’s bullish watch, so the recommendation stays HOLD with low confidence.
- Uncertainty persists from weak breadth, cooling liquidity in select stocks, and the chance of a short‑term bounce if support holds.

## Top Liquidity Spikes
- CFGH.CA: spike=91.23 liquidity=717957.2 outlook=WEAK_OR_RISKY score=5.87 buy_ready=False
- SCEM.CA: spike=3.61 liquidity=217248688.0 outlook=WEAK_OR_RISKY score=7.84 buy_ready=False
- OBRI.CA: spike=3.54 liquidity=43389308.0 outlook=CONSTRUCTIVE score=52.87 buy_ready=False
- ARAB.CA: spike=3.46 liquidity=272625024.0 outlook=BULLISH_WATCH score=72.4 buy_ready=False
- AJWA.CA: spike=2.98 liquidity=56764428.0 outlook=NEUTRAL score=49.87 buy_ready=False

## Sector Leaderboard
- #1 Fintech & Payments: score=8.52 5d=9.0% 20d=2.24% aboveMA50=50.0%
- #2 Telecommunications: score=8.5 5d=5.34% 20d=7.79% aboveMA50=100.0%
- #3 Building Materials: score=7.84 5d=9.52% 20d=-8.87% aboveMA50=50.0%
- #4 Investment Holding: score=5.32 5d=-0.15% 20d=8.52% aboveMA50=66.67%
- #5 Education: score=5.1 5d=4.23% 20d=2.76% aboveMA50=33.33%
- #6 Energy & Petrochemicals: score=3.86 5d=2.0% 20d=0.63% aboveMA50=33.33%
- #7 Transportation & Logistics: score=3.77 5d=2.27% 20d=-4.21% aboveMA50=50.0%
- #8 Non-bank Financial Services: score=3.63 5d=7.98% 20d=-6.73% aboveMA50=20.0%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- MBSC.CA: BULLISH_WATCH score=100 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=far above support
- ARCC.CA: BULLISH_WATCH score=100 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=No major short-term scanner risk flags.
- LCSW.CA: BULLISH_WATCH score=98.84 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=No major short-term scanner risk flags.
- EFIH.CA: BULLISH_WATCH score=91.52 liquidity=TRADEABLE sector=LEADING risk=far above support
- AMOC.CA: BULLISH_WATCH score=86.86 liquidity=TRADEABLE sector=IMPROVING risk=No major short-term scanner risk flags.
- ETEL.CA: BULLISH_WATCH score=80.5 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; momentum is extended
- ALCN.CA: BULLISH_WATCH score=79.77 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- BINV.CA: BULLISH_WATCH score=75.32 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- ARAB.CA: BULLISH_WATCH score=72.4 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=far above support; sector is not leading
- TALM.CA: BULLISH_WATCH score=71.1 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; far above support

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- EKHO.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ARVA.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- GTWL.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=7.14 buy_ready=False sector_rank=12 price=254.95 support=230.11 resistance=359.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=24.09 liquidity=7394857.5 spike=0.36
- ABUK.CA: score=17.8 buy_ready=False sector_rank=11 price=87.28 support=83.55 resistance=96.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=43.87 liquidity=63033248.0 spike=0.67
- ACAMD.CA: score=16.75 buy_ready=False sector_rank=12 price=2.01 support=1.87 resistance=2.16 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=45.65 liquidity=26581648.0 spike=0.62
- ACGC.CA: score=16.87 buy_ready=False sector_rank=18 price=13.8 support=13.11 resistance=15.63 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=51.9 liquidity=9551738.0 spike=0.5
- ADCI.CA: score=5.68 buy_ready=False sector_rank=12 price=269.04 support=256.0 resistance=294.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=42.81 liquidity=927693.38 spike=0.4
- ADIB.CA: score=9.85 buy_ready=False sector_rank=10 price=47.09 support=47.45 resistance=54.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=20.97 liquidity=69901656.0 spike=0.97
- ADPC.CA: score=6.43 buy_ready=False sector_rank=12 price=3.48 support=3.4 resistance=4.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=33.33 liquidity=7677665.0 spike=0.5
- AFDI.CA: score=11.87 buy_ready=False sector_rank=12 price=53.0 support=47.7 resistance=56.82 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=44.19 liquidity=3121497.25 spike=0.44
- AFMC.CA: score=13.83 buy_ready=False sector_rank=12 price=146.42 support=131.0 resistance=179.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=43.31 liquidity=7080611.0 spike=0.26
- AJWA.CA: score=20.71 buy_ready=False sector_rank=12 price=199.55 support=176.0 resistance=201.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=79.58 liquidity=56764428.0 spike=2.98
- ALCN.CA: score=22.51 buy_ready=False sector_rank=7 price=33.1 support=30.4 resistance=36.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=48.17 liquidity=12916173.0 spike=0.38
- ALUM.CA: score=2.91 buy_ready=False sector_rank=12 price=22.92 support=21.65 resistance=28.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=26.88 liquidity=3160138.75 spike=0.63
- AMER.CA: score=21.12 buy_ready=False sector_rank=19 price=4.98 support=4.05 resistance=5.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=39.52 liquidity=118015080.0 spike=2.48
- AMES.CA: score=4.75 buy_ready=False sector_rank=12 price=43.92 support=43.7 resistance=46.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=51289156.0 spike=0.39
- AMIA.CA: score=17.75 buy_ready=False sector_rank=12 price=19.04 support=17.12 resistance=19.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=67.0 liquidity=12454425.0 spike=0.73
- AMOC.CA: score=22.9 buy_ready=False sector_rank=6 price=13.79 support=12.18 resistance=14.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=58.76 liquidity=163932304.0 spike=1.18
- APSW.CA: score=6.23 buy_ready=False sector_rank=12 price=8.24 support=7.81 resistance=8.92 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=44.44 liquidity=482042.5 spike=0.7
- ARAB.CA: score=26.08 buy_ready=False sector_rank=19 price=0.28 support=0.2 resistance=0.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=57.94 liquidity=272625024.0 spike=3.46
- ARCC.CA: score=26.28 buy_ready=False sector_rank=3 price=70.65 support=60.01 resistance=76.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=45.84 liquidity=55771296.0 spike=1.94
- AREH.CA: score=6.52 buy_ready=False sector_rank=12 price=1.23 support=1.14 resistance=1.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=31.82 liquidity=5774685.0 spike=0.62
- ASCM.CA: score=12.05 buy_ready=False sector_rank=12 price=56.51 support=53.8 resistance=64.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=35.31 liquidity=5302472.5 spike=0.59
- ASPI.CA: score=9.75 buy_ready=False sector_rank=12 price=0.35 support=0.33 resistance=0.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=24.24 liquidity=21609050.0 spike=0.54
- ATLC.CA: score=3.83 buy_ready=False sector_rank=8 price=6.09 support=5.2 resistance=7.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=34.21 liquidity=3378207.75 spike=0.27
- ATQA.CA: score=17.8 buy_ready=False sector_rank=11 price=11.95 support=10.91 resistance=13.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=44.98 liquidity=15756523.0 spike=0.2
- AXPH.CA: score=5.21 buy_ready=False sector_rank=12 price=1488.27 support=1334.35 resistance=1987.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=29.19 liquidity=5458537.5 spike=0.83
- BINV.CA: score=21.13 buy_ready=False sector_rank=4 price=57.98 support=49.91 resistance=72.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=41.54 liquidity=10914786.0 spike=0.45
- BIOC.CA: score=4.75 buy_ready=False sector_rank=12 price=307.33 support=303.5 resistance=335.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=53834524.0 spike=0.57
- BTFH.CA: score=9.45 buy_ready=False sector_rank=8 price=2.7 support=2.65 resistance=3.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=34.29 liquidity=71705288.0 spike=0.77
- CAED.CA: score=-1.15 buy_ready=False sector_rank=12 price=111.16 support=110.5 resistance=118.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=4101619.0 spike=0.23
- CANA.CA: score=17.85 buy_ready=False sector_rank=10 price=43.02 support=41.35 resistance=52.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=53.49 liquidity=16311818.0 spike=0.73
- CCAP.CA: score=19.13 buy_ready=False sector_rank=4 price=6.53 support=6.1 resistance=7.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=41.54 liquidity=541020544.0 spike=0.7
- CCRS.CA: score=1.43 buy_ready=False sector_rank=12 price=2.2 support=2.18 resistance=2.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=6686174.0 spike=0.47
- CEFM.CA: score=6.51 buy_ready=False sector_rank=12 price=135.24 support=113.0 resistance=154.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=39.8 liquidity=1764073.25 spike=0.54
- CERA.CA: score=16.75 buy_ready=False sector_rank=12 price=1.34 support=1.18 resistance=1.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=43.84 liquidity=90139424.0 spike=0.63
- CFGH.CA: score=4.47 buy_ready=False sector_rank=12 price=0.11 support=0.11 resistance=0.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 12:55 PM market time freshness=DELAYED_CURRENT RSI=0.0 liquidity=717957.2 spike=91.23
- CICH.CA: score=6.44 buy_ready=False sector_rank=8 price=11.78 support=10.75 resistance=13.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:09 PM market time freshness=DELAYED_CURRENT RSI=41.38 liquidity=986362.69 spike=0.26
- CIEB.CA: score=4.06 buy_ready=False sector_rank=10 price=23.69 support=23.0 resistance=25.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=30.26 liquidity=4203809.0 spike=0.46
- CIRA.CA: score=16.04 buy_ready=False sector_rank=5 price=37.53 support=36.8 resistance=41.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=40.89 liquidity=20331838.0 spike=0.57
- CLHO.CA: score=15.79 buy_ready=False sector_rank=20 price=14.99 support=13.9 resistance=16.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=38.27 liquidity=23926922.0 spike=0.58
- CNFN.CA: score=13.74 buy_ready=False sector_rank=8 price=4.19 support=3.84 resistance=4.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=39.57 liquidity=7287722.5 spike=0.95
- COMI.CA: score=8.85 buy_ready=False sector_rank=10 price=123.21 support=124.14 resistance=139.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=22.53 liquidity=160031648.0 spike=0.29
- COPR.CA: score=14.75 buy_ready=False sector_rank=12 price=0.47 support=0.44 resistance=0.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=41.01 liquidity=10891430.0 spike=0.43
- COSG.CA: score=7.9 buy_ready=False sector_rank=12 price=1.57 support=1.46 resistance=1.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=28.57 liquidity=8149580.5 spike=0.51
- CPCI.CA: score=9.18 buy_ready=False sector_rank=12 price=598.88 support=530.0 resistance=619.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=84.08 liquidity=2427414.5 spike=0.63
- CSAG.CA: score=10.1 buy_ready=False sector_rank=7 price=36.77 support=34.52 resistance=41.67 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=42.17 liquidity=4593325.5 spike=0.56
- DAPH.CA: score=9.75 buy_ready=False sector_rank=12 price=102.18 support=89.1 resistance=133.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=31.4 liquidity=26912394.0 spike=0.72
- DEIN.CA: score=7.75 buy_ready=False sector_rank=12 price=10.35 support=10.35 resistance=12.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 09:54 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=37.26 spike=0.01
- DOMT.CA: score=4.51 buy_ready=False sector_rank=21 price=23.94 support=23.81 resistance=28.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=31.24 liquidity=6478794.0 spike=1.27
- DSCW.CA: score=8.18 buy_ready=False sector_rank=12 price=1.67 support=1.58 resistance=1.92 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=24.14 liquidity=7430714.5 spike=0.39
- DTPP.CA: score=4.75 buy_ready=False sector_rank=12 price=283.79 support=283.03 resistance=302.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=25353074.0 spike=0.26
- EALR.CA: score=1.4 buy_ready=False sector_rank=12 price=333.54 support=312.0 resistance=411.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=30.06 liquidity=2655311.0 spike=0.27
- EASB.CA: score=18.79 buy_ready=False sector_rank=12 price=7.81 support=6.04 resistance=9.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=38.81 liquidity=15871777.0 spike=1.52
- EAST.CA: score=7.49 buy_ready=False sector_rank=21 price=28.08 support=27.91 resistance=35.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=17.1 liquidity=18346066.0 spike=0.39
- EBSC.CA: score=-0.23 buy_ready=False sector_rank=12 price=1.76 support=1.61 resistance=2.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=32.91 liquidity=1019328.62 spike=0.32
- ECAP.CA: score=3.11 buy_ready=False sector_rank=12 price=29.86 support=29.13 resistance=33.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=29.16 liquidity=2359737.0 spike=0.54
- EDFM.CA: score=7.52 buy_ready=False sector_rank=12 price=399.81 support=354.0 resistance=425.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=51.1 liquidity=767248.75 spike=0.63
- EEII.CA: score=10.33 buy_ready=False sector_rank=12 price=2.09 support=2.02 resistance=2.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=45.57 liquidity=4577378.5 spike=0.48
- EFIC.CA: score=8.8 buy_ready=False sector_rank=11 price=157.23 support=147.0 resistance=227.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=22.29 liquidity=20435072.0 spike=0.34
- EFID.CA: score=7.49 buy_ready=False sector_rank=21 price=18.81 support=18.1 resistance=32.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=8.88 liquidity=16231692.0 spike=0.3
- EFIH.CA: score=28.4 buy_ready=False sector_rank=1 price=24.53 support=20.2 resistance=25.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=59.12 liquidity=63260440.0 spike=0.99
- EGAL.CA: score=9.8 buy_ready=False sector_rank=11 price=335.02 support=331.5 resistance=378.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=22.5 liquidity=35268616.0 spike=0.66
- EGAS.CA: score=10.58 buy_ready=False sector_rank=6 price=55.01 support=53.62 resistance=60.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=36.57 liquidity=5039356.0 spike=0.45
- EGBE.CA: score=10.26 buy_ready=False sector_rank=10 price=0.54 support=0.49 resistance=0.54 source=Yahoo Finance as_of=2026-10-06T21:00:00+00:00 freshness=FRESH RSI=68.75 liquidity=144017.49 spike=1.13
- EGCH.CA: score=14.8 buy_ready=False sector_rank=11 price=13.14 support=12.88 resistance=14.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=37.3 liquidity=25042696.0 spike=0.28
- EGSA.CA: score=6.4 buy_ready=False sector_rank=2 price=8.87 support=8.82 resistance=9.1 source=Yahoo Finance as_of=2026-10-06T21:00:00+00:00 freshness=FRESH RSI=11.76 liquidity=8.87 spike=0.0
- EGTS.CA: score=14.16 buy_ready=False sector_rank=19 price=16.01 support=15.65 resistance=19.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=43.74 liquidity=34058240.0 spike=0.98
- EHDR.CA: score=8.73 buy_ready=False sector_rank=12 price=2.45 support=2.35 resistance=2.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=29.69 liquidity=8981745.0 spike=0.75
- ELEC.CA: score=10.52 buy_ready=False sector_rank=17 price=1.83 support=1.72 resistance=2.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=29.27 liquidity=16757845.0 spike=0.26
- ELKA.CA: score=15.75 buy_ready=False sector_rank=12 price=1.54 support=1.43 resistance=1.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=37.04 liquidity=13247561.0 spike=0.95
- ELNA.CA: score=0.8 buy_ready=False sector_rank=12 price=35.22 support=33.46 resistance=37.96 source=Yahoo Finance as_of=2026-10-06T21:00:00+00:00 freshness=FRESH RSI=0.0 liquidity=52196.04 spike=0.28
- ELSH.CA: score=11.75 buy_ready=False sector_rank=12 price=11.72 support=10.8 resistance=13.67 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=33.97 liquidity=11411648.0 spike=0.52
- ELWA.CA: score=7.11 buy_ready=False sector_rank=12 price=1.65 support=1.43 resistance=1.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=36.59 liquidity=359885.78 spike=0.49
- EMFD.CA: score=9.16 buy_ready=False sector_rank=19 price=12.4 support=11.7 resistance=15.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=32.19 liquidity=37762728.0 spike=0.46
- ENGC.CA: score=5.83 buy_ready=False sector_rank=12 price=36.04 support=33.33 resistance=45.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=33.49 liquidity=7085649.5 spike=0.4
- EOSB.CA: score=10.91 buy_ready=False sector_rank=12 price=1.57 support=1.58 resistance=1.64 source=Yahoo Finance as_of=2026-10-06T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=78572.22 spike=1.54
- EPCO.CA: score=5.09 buy_ready=False sector_rank=12 price=9.48 support=9.25 resistance=12.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=25.17 liquidity=5345933.0 spike=0.38
- EPPK.CA: score=-4.83 buy_ready=False sector_rank=12 price=10.29 support=10.29 resistance=10.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=8 September 01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=419183.72 spike=0.28
- ETEL.CA: score=23.4 buy_ready=False sector_rank=2 price=144.78 support=124.01 resistance=156.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=69.69 liquidity=115837976.0 spike=0.41
- ETRS.CA: score=12.11 buy_ready=False sector_rank=12 price=10.65 support=9.82 resistance=11.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=42.35 liquidity=5359186.0 spike=0.56
- EXPA.CA: score=8.97 buy_ready=False sector_rank=10 price=15.27 support=15.41 resistance=22.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=16.84 liquidity=40122744.0 spike=1.06
- FAIT.CA: score=9.28 buy_ready=False sector_rank=10 price=44.36 support=38.48 resistance=48.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=38.93 liquidity=1423007.13 spike=0.46
- FAITA.CA: score=6.86 buy_ready=False sector_rank=10 price=0.99 support=0.98 resistance=1.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:00 AM market time freshness=DELAYED_CURRENT RSI=66.67 liquidity=11263.59 spike=0.38
- FERC.CA: score=1.52 buy_ready=False sector_rank=11 price=74.54 support=70.42 resistance=82.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=26.13 liquidity=2717077.0 spike=0.43
- FWRY.CA: score=21.4 buy_ready=False sector_rank=1 price=18.62 support=17.5 resistance=19.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=52.19 liquidity=105861368.0 spike=0.98
- GBCO.CA: score=20.38 buy_ready=False sector_rank=9 price=30.42 support=27.0 resistance=32.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=50.07 liquidity=39813472.0 spike=0.4
- GDWA.CA: score=8.75 buy_ready=False sector_rank=12 price=0.65 support=0.61 resistance=0.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=21.08 liquidity=13500536.0 spike=0.58
- GGCC.CA: score=6.27 buy_ready=False sector_rank=12 price=0.71 support=0.65 resistance=0.91 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=24.38 liquidity=6518570.0 spike=0.43
- GIHD.CA: score=6.87 buy_ready=False sector_rank=12 price=60.06 support=60.9 resistance=78.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=29.07 liquidity=7119987.5 spike=0.31
- GMCI.CA: score=6.56 buy_ready=False sector_rank=12 price=1.61 support=1.49 resistance=1.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:09 PM market time freshness=DELAYED_CURRENT RSI=42.11 liquidity=532865.94 spike=1.14
- GRCA.CA: score=-0.33 buy_ready=False sector_rank=12 price=35.21 support=35.0 resistance=37.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=4917816.5 spike=0.25
- GSSC.CA: score=0.86 buy_ready=False sector_rank=12 price=277.71 support=246.0 resistance=333.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=31.91 liquidity=1114941.25 spike=0.3
- HDBK.CA: score=10.92 buy_ready=False sector_rank=10 price=107.01 support=102.03 resistance=121.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=28.02 liquidity=9064429.0 spike=0.3
- HELI.CA: score=9.16 buy_ready=False sector_rank=19 price=7.12 support=6.94 resistance=8.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=26.07 liquidity=39044900.0 spike=0.34
- HRHO.CA: score=21.45 buy_ready=False sector_rank=8 price=25.9 support=22.81 resistance=27.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=61.05 liquidity=51669192.0 spike=0.39
- ICID.CA: score=11.32 buy_ready=False sector_rank=12 price=17.88 support=16.52 resistance=20.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=44.41 liquidity=3568273.75 spike=0.46
- IDRE.CA: score=-1.25 buy_ready=False sector_rank=12 price=47.37 support=47.06 resistance=50.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=4001548.75 spike=0.27
- IFAP.CA: score=4.6 buy_ready=False sector_rank=13 price=19.08 support=17.17 resistance=21.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=32.55 liquidity=5867817.5 spike=0.72
- INFI.CA: score=13.96 buy_ready=False sector_rank=12 price=123.8 support=104.0 resistance=149.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=44.57 liquidity=7209784.0 spike=0.51
- IRON.CA: score=18.32 buy_ready=False sector_rank=11 price=28.31 support=25.01 resistance=32.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=55.15 liquidity=14568666.0 spike=1.26
- ISMA.CA: score=5.17 buy_ready=False sector_rank=12 price=24.98 support=22.7 resistance=34.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=31.85 liquidity=5425923.5 spike=0.41
- ISMQ.CA: score=17.04 buy_ready=False sector_rank=11 price=8.18 support=7.6 resistance=9.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=35.29 liquidity=22337762.0 spike=1.12
- ISPH.CA: score=12.79 buy_ready=False sector_rank=20 price=11.42 support=11.22 resistance=13.06 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=38.61 liquidity=37729108.0 spike=0.59
- JUFO.CA: score=8.37 buy_ready=False sector_rank=21 price=25.07 support=24.4 resistance=27.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=31.2 liquidity=22843800.0 spike=1.44
- KABO.CA: score=14.32 buy_ready=False sector_rank=18 price=8.67 support=7.97 resistance=10.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=45.52 liquidity=25795216.0 spike=0.83
- KWIN.CA: score=2.36 buy_ready=False sector_rank=12 price=74.28 support=72.21 resistance=95.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=27.44 liquidity=3610822.0 spike=0.32
- KZPC.CA: score=12.85 buy_ready=False sector_rank=12 price=13.23 support=12.15 resistance=14.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=32.01 liquidity=12982693.0 spike=1.05
- LCSW.CA: score=25.48 buy_ready=False sector_rank=3 price=34.35 support=28.86 resistance=35.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=57.61 liquidity=28717632.0 spike=1.54
- LUTS.CA: score=4.75 buy_ready=False sector_rank=12 price=0.86 support=0.85 resistance=0.92 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=35681100.0 spike=0.43
- MAAL.CA: score=16.15 buy_ready=False sector_rank=12 price=10.37 support=8.45 resistance=12.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=72.35 liquidity=6402373.5 spike=0.28
- MASR.CA: score=19.01 buy_ready=False sector_rank=12 price=7.74 support=6.82 resistance=8.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=49.58 liquidity=79996992.0 spike=1.13
- MBSC.CA: score=26.52 buy_ready=False sector_rank=3 price=368.14 support=288.0 resistance=426.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=51.1 liquidity=152830240.0 spike=2.06
- MCQE.CA: score=19.0 buy_ready=False sector_rank=3 price=194.51 support=177.02 resistance=240.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=40.35 liquidity=82710696.0 spike=1.8
- MCRO.CA: score=14.75 buy_ready=False sector_rank=12 price=1.47 support=1.41 resistance=1.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=35.59 liquidity=21863948.0 spike=0.27
- MENA.CA: score=8.28 buy_ready=False sector_rank=19 price=6.55 support=5.8 resistance=7.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=46.21 liquidity=1560143.25 spike=1.28
- MEPA.CA: score=6.94 buy_ready=False sector_rank=12 price=1.67 support=1.56 resistance=2.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=36.0 liquidity=3193426.75 spike=0.24
- MFPC.CA: score=17.8 buy_ready=False sector_rank=11 price=45.06 support=43.0 resistance=51.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=35.39 liquidity=36984324.0 spike=0.38
- MFSC.CA: score=-3.6 buy_ready=False sector_rank=12 price=42.58 support=42.06 resistance=44.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=1656419.88 spike=0.62
- MHOT.CA: score=13.63 buy_ready=False sector_rank=14 price=17.42 support=16.2 resistance=21.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=44.32 liquidity=10424849.0 spike=0.56
- MICH.CA: score=10.64 buy_ready=False sector_rank=12 price=46.53 support=42.01 resistance=50.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=42.65 liquidity=5891980.5 spike=0.59
- MILS.CA: score=1.42 buy_ready=False sector_rank=12 price=177.2 support=165.5 resistance=213.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=33.32 liquidity=1670372.75 spike=0.17
- MIPH.CA: score=5.11 buy_ready=False sector_rank=20 price=798.27 support=739.69 resistance=1000.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=47.42 liquidity=1320311.63 spike=0.15
- MOED.CA: score=7.47 buy_ready=False sector_rank=12 price=0.66 support=0.59 resistance=0.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=28.14 liquidity=8719022.0 spike=0.27
- MOIL.CA: score=5.7 buy_ready=False sector_rank=6 price=0.68 support=0.67 resistance=0.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=57.53 liquidity=160562.36 spike=0.62
- MOIN.CA: score=17.75 buy_ready=False sector_rank=12 price=35.66 support=32.0 resistance=41.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=38.51 liquidity=10934339.0 spike=0.75
- MOSC.CA: score=0.12 buy_ready=False sector_rank=12 price=273.37 support=257.0 resistance=329.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=34.76 liquidity=374195.25 spike=0.1
- MPCI.CA: score=9.75 buy_ready=False sector_rank=12 price=332.18 support=305.45 resistance=455.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=29.8 liquidity=86959312.0 spike=0.84
- MPCO.CA: score=12.73 buy_ready=False sector_rank=13 price=2.33 support=2.25 resistance=3.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=32.69 liquidity=47717024.0 spike=0.25
- MPRC.CA: score=20.27 buy_ready=False sector_rank=12 price=39.39 support=37.65 resistance=42.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=51.43 liquidity=36085796.0 spike=1.76
- MTIE.CA: score=16.38 buy_ready=False sector_rank=9 price=7.86 support=7.5 resistance=8.63 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=35.25 liquidity=14856201.0 spike=0.85
- NAHO.CA: score=4.75 buy_ready=False sector_rank=12 price=0.13 support=0.12 resistance=0.14 source=Yahoo Finance as_of=2026-10-06T21:00:00+00:00 freshness=FRESH RSI=46.43 liquidity=5811.04 spike=0.15
- NCCW.CA: score=17.75 buy_ready=False sector_rank=12 price=6.84 support=6.44 resistance=8.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=35.64 liquidity=14658994.0 spike=0.23
- NEDA.CA: score=5.09 buy_ready=False sector_rank=12 price=2.6 support=2.48 resistance=2.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=36.59 liquidity=339440.75 spike=0.45
- NHPS.CA: score=13.5 buy_ready=False sector_rank=12 price=71.11 support=66.0 resistance=86.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=45.02 liquidity=6754465.0 spike=0.46
- NINH.CA: score=10.35 buy_ready=False sector_rank=12 price=18.84 support=18.53 resistance=24.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=35.43 liquidity=5598166.0 spike=0.38
- NIPH.CA: score=13.79 buy_ready=False sector_rank=20 price=304.13 support=290.0 resistance=368.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=48.72 liquidity=48406808.0 spike=0.38
- OBRI.CA: score=22.75 buy_ready=False sector_rank=12 price=29.01 support=22.8 resistance=33.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=40.5 liquidity=43389308.0 spike=3.54
- OCDI.CA: score=9.16 buy_ready=False sector_rank=19 price=26.49 support=24.2 resistance=33.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=31.43 liquidity=25315472.0 spike=0.49
- OCPH.CA: score=7.81 buy_ready=False sector_rank=12 price=219.7 support=190.0 resistance=256.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=38.14 liquidity=2065902.0 spike=0.56
- ODIN.CA: score=9.65 buy_ready=False sector_rank=12 price=2.47 support=2.35 resistance=3.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=41.38 liquidity=4900609.0 spike=0.53
- OFH.CA: score=14.75 buy_ready=False sector_rank=12 price=0.84 support=0.83 resistance=1.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=36.62 liquidity=21387656.0 spike=0.21
- OIH.CA: score=11.13 buy_ready=False sector_rank=4 price=1.89 support=1.7 resistance=2.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=23.64 liquidity=19314890.0 spike=0.2
- OLFI.CA: score=7.49 buy_ready=False sector_rank=21 price=21.11 support=20.82 resistance=23.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=18.49 liquidity=11022428.0 spike=0.62
- ORAS.CA: score=4.6 buy_ready=False sector_rank=15 price=859.43 support=856.07 resistance=889.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=198533728.0 spike=1.0
- ORHD.CA: score=8.16 buy_ready=False sector_rank=19 price=11.57 support=11.59 resistance=44.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=2.67 liquidity=77984912.0 spike=0.48
- ORWE.CA: score=17.32 buy_ready=False sector_rank=18 price=26.55 support=26.01 resistance=28.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=41.12 liquidity=15968563.0 spike=0.41
- PHAR.CA: score=15.79 buy_ready=False sector_rank=20 price=112.95 support=102.0 resistance=128.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=39.97 liquidity=31055414.0 spike=0.41
- PHDC.CA: score=16.16 buy_ready=False sector_rank=19 price=12.75 support=12.36 resistance=14.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=36.59 liquidity=27382154.0 spike=0.25
- PHTV.CA: score=6.23 buy_ready=False sector_rank=12 price=344.49 support=315.1 resistance=378.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=40.36 liquidity=1364716.75 spike=1.06
- POUL.CA: score=7.49 buy_ready=False sector_rank=21 price=9.7 support=9.12 resistance=41.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=1.89 liquidity=15008413.0 spike=0.45
- PRCL.CA: score=8.21 buy_ready=False sector_rank=3 price=24.8 support=22.8 resistance=33.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=28.66 liquidity=5806256.5 spike=0.47
- PRDC.CA: score=16.16 buy_ready=False sector_rank=19 price=6.93 support=6.81 resistance=8.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=40.17 liquidity=24491650.0 spike=0.69
- PRMH.CA: score=0.44 buy_ready=False sector_rank=12 price=2.17 support=2.03 resistance=2.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=18.06 liquidity=1690054.25 spike=0.42
- RACC.CA: score=9.65 buy_ready=False sector_rank=12 price=9.15 support=8.51 resistance=10.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=35.27 liquidity=3899192.25 spike=0.55
- RAKT.CA: score=14.36 buy_ready=False sector_rank=12 price=23.22 support=20.26 resistance=25.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:08 PM market time freshness=DELAYED_CURRENT RSI=65.9 liquidity=627435.38 spike=1.99
- RAYA.CA: score=14.03 buy_ready=False sector_rank=16 price=6.39 support=5.72 resistance=7.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=35.65 liquidity=9461539.0 spike=0.26
- RMDA.CA: score=8.79 buy_ready=False sector_rank=20 price=5.24 support=4.83 resistance=6.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=22.82 liquidity=11583988.0 spike=0.35
- ROTO.CA: score=21.49 buy_ready=False sector_rank=12 price=41.2 support=35.02 resistance=43.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=48.85 liquidity=18426450.0 spike=2.37
- RREI.CA: score=4.92 buy_ready=False sector_rank=12 price=3.72 support=3.53 resistance=4.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=28.87 liquidity=5169315.0 spike=0.47
- RTVC.CA: score=-0.09 buy_ready=False sector_rank=12 price=3.63 support=3.37 resistance=4.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=33.33 liquidity=1164952.88 spike=0.43
- RUBX.CA: score=23.75 buy_ready=False sector_rank=12 price=17.3 support=12.65 resistance=19.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=64.2 liquidity=71181208.0 spike=0.78
- SAUD.CA: score=7.31 buy_ready=False sector_rank=10 price=22.82 support=21.6 resistance=26.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=45.32 liquidity=2457289.5 spike=0.13
- SCEM.CA: score=12.4 buy_ready=False sector_rank=3 price=90.04 support=85.3 resistance=95.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=217248688.0 spike=3.61
- SCFM.CA: score=-0.43 buy_ready=False sector_rank=12 price=242.98 support=223.11 resistance=290.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=32.37 liquidity=825726.06 spike=0.35
- SCTS.CA: score=2.03 buy_ready=False sector_rank=5 price=529.37 support=520.3 resistance=635.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=31.41 liquidity=989685.88 spike=0.6
- SDTI.CA: score=21.75 buy_ready=False sector_rank=12 price=86.01 support=71.0 resistance=94.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=74.91 liquidity=23903682.0 spike=0.74
- SEIG.CA: score=8.16 buy_ready=False sector_rank=12 price=222.54 support=200.0 resistance=267.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=45.07 liquidity=1414194.0 spike=0.63
- SIPC.CA: score=6.67 buy_ready=False sector_rank=12 price=5.77 support=5.71 resistance=6.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=100273720.0 spike=1.96
- SKPC.CA: score=9.3 buy_ready=False sector_rank=11 price=15.82 support=15.4 resistance=18.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=20.0 liquidity=105941176.0 spike=1.25
- SMFR.CA: score=10.08 buy_ready=False sector_rank=12 price=231.27 support=205.01 resistance=256.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=44.95 liquidity=1330231.13 spike=0.34
- SNFC.CA: score=19.31 buy_ready=False sector_rank=12 price=11.42 support=10.58 resistance=11.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=69.23 liquidity=7562877.0 spike=0.62
- SPIN.CA: score=9.06 buy_ready=False sector_rank=18 price=15.9 support=15.11 resistance=19.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=35.33 liquidity=4744165.0 spike=0.75
- SPMD.CA: score=4.44 buy_ready=False sector_rank=12 price=0.38 support=0.36 resistance=0.62 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=21.88 liquidity=5693092.0 spike=0.08
- SUGR.CA: score=16.65 buy_ready=False sector_rank=21 price=56.01 support=50.5 resistance=64.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=38.09 liquidity=15649352.0 spike=1.08
- SVCE.CA: score=9.75 buy_ready=False sector_rank=12 price=10.17 support=9.24 resistance=12.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=34.39 liquidity=93249544.0 spike=0.95
- SWDY.CA: score=14.52 buy_ready=False sector_rank=17 price=112.43 support=102.31 resistance=132.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=37.0 liquidity=29922326.0 spike=0.46
- TALM.CA: score=23.04 buy_ready=False sector_rank=5 price=21.5 support=17.61 resistance=25.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=46.6 liquidity=23840332.0 spike=0.33
- TMGH.CA: score=8.16 buy_ready=False sector_rank=19 price=86.37 support=84.4 resistance=99.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=18.33 liquidity=100428112.0 spike=0.46
- TRTO.CA: score=11.75 buy_ready=False sector_rank=12 price=0.07 support=0.05 resistance=0.08 source=Yahoo Finance as_of=2026-10-06T21:00:00+00:00 freshness=FRESH RSI=57.69 liquidity=4869.33 spike=0.41
- UEFM.CA: score=14.79 buy_ready=False sector_rank=12 price=515.11 support=407.57 resistance=550.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=50.67 liquidity=5060005.0 spike=1.49
- UEGC.CA: score=10.75 buy_ready=False sector_rank=12 price=1.49 support=1.37 resistance=1.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=31.67 liquidity=16924750.0 spike=0.51
- UNIP.CA: score=11.91 buy_ready=False sector_rank=12 price=0.35 support=0.32 resistance=0.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=38.02 liquidity=5166313.5 spike=0.41
- UNIT.CA: score=7.09 buy_ready=False sector_rank=19 price=17.48 support=16.41 resistance=23.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=35.96 liquidity=2930124.25 spike=0.18
- WCDF.CA: score=4.66 buy_ready=False sector_rank=12 price=657.98 support=575.5 resistance=765.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=24.65 liquidity=1908885.25 spike=0.53
- WKOL.CA: score=1.57 buy_ready=False sector_rank=12 price=282.34 support=266.18 resistance=379.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=22.46 liquidity=2818266.75 spike=0.24
- ZEOT.CA: score=8.98 buy_ready=False sector_rank=12 price=12.09 support=10.6 resistance=14.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=44.72 liquidity=2235765.0 spike=0.41
- ZMID.CA: score=9.16 buy_ready=False sector_rank=19 price=7.3 support=7.07 resistance=9.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=13.88 liquidity=48868248.0 spike=0.44

## Backtesting Lite
- EFIH.CA: 180d return=26.87%, max drawdown=-22.68%, MA20>MA50 days last20=10, as_of=2026-10-06T21:00:00+00:00
- MBSC.CA: 180d return=54.89%, max drawdown=-36.93%, MA20>MA50 days last20=20, as_of=2026-10-06T21:00:00+00:00
- ARCC.CA: 180d return=59.47%, max drawdown=-23.67%, MA20>MA50 days last20=19, as_of=2026-10-06T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- EFIH.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=E-Finance For Digital and Financial Investments summary=Evidence rejected for EFIH.CA: source text did not clearly match EFIH.CA / E-Finance For Digital and Financial Investments.
- MBSC.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=648 sources=3 expected=Misr Beni Suef Cement summary=Misr Beni Suef’s consolidated net profits near EGP 4bn in 2025; Misr Beni Suef’s consolidated net profits hit EGP 953m in H1-25; Misr Beni Suef Cement’s consolidate profits fall to EGP 574m in Q1-25
  - Misr Beni Suef’s consolidated net profits near EGP 4bn in 2025: https://english.mubasher.info/news/4599415/Misr-Beni-Suef-s-consolidated-net-profits-near-EGP-4bn-in-2025/
  - Misr Beni Suef’s consolidated net profits hit EGP 953m in H1-25: https://english.mubasher.info/news/4488249/Misr-Beni-Suef-s-consolidated-net-profits-hit-EGP-953m-in-H1-25/
  - Misr Beni Suef Cement’s consolidate profits fall to EGP 574m in Q1-25: https://english.mubasher.info/news/4455784/Misr-Beni-Suef-Cement-s-consolidate-profits-fall-to-EGP-574m-in-Q1-25/
- ARCC.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=648 sources=3 expected=Arabian Cement Company summary=Arabian Cement to pay out EGP 2bn dividends for 2025; Arabian Cement’s EGM approves nearly EGP 8m capital cut; Arabian Cement’s consolidated profits near EGP 3.6bn in 2025
  - Arabian Cement to pay out EGP 2bn dividends for 2025: https://english.mubasher.info/news/4587912/Arabian-Cement-to-pay-out-EGP-2bn-dividends-for-2025/
  - Arabian Cement’s EGM approves nearly EGP 8m capital cut: https://english.mubasher.info/news/4583762/Arabian-Cement-s-EGM-approves-nearly-EGP-8m-capital-cut/
  - Arabian Cement’s consolidated profits near EGP 3.6bn in 2025: https://english.mubasher.info/news/4562679/Arabian-Cement-s-consolidated-profits-near-EGP-3-6bn-in-2025/
- ARAB.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Arab Developers Holding summary=Arab Developers Holding unveils EGP 1bn expansion plans to improve financial efficiency; FRA gives initial approval for Arab Developers’ rights issue; Arab Developers stock stabilizes after correction
  - Arab Developers Holding unveils EGP 1bn expansion plans to improve financial efficiency: https://english.mubasher.info/news/4601724/Arab-Developers-Holding-unveils-EGP-1bn-expansion-plans-to-improve-financial-efficiency/
  - FRA gives initial approval for Arab Developers’ rights issue: https://english.mubasher.info/news/4582627/FRA-gives-initial-approval-for-Arab-Developers-rights-issue/
  - Arab Developers stock stabilizes after correction: https://english.mubasher.info/news/4564643/Arab-Developers-stock-stabilizes-after-correction/
- LCSW.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Lecico Egypt summary=Evidence rejected for LCSW.CA: source text did not clearly match LCSW.CA / Lecico Egypt.
- RUBX.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Rubex International for Plastic and Acrylic Manufacturing summary=Evidence rejected for RUBX.CA: source text did not clearly match RUBX.CA / Rubex International for Plastic and Acrylic Manufacturing.
- ETEL.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Telecom Egypt summary=Evidence rejected for ETEL.CA: source text did not clearly match ETEL.CA / Telecom Egypt.
- TALM.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Talim Management Services summary=Evidence rejected for TALM.CA: source text did not clearly match TALM.CA / Talim Management Services.

## Warnings
- Evidence rejected for EFIH.CA: source text did not clearly match EFIH.CA / E-Finance For Digital and Financial Investments.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence for MBSC.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for ARCC.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for ARAB.CA matches the company but no source/report date was detected.
- Evidence rejected for LCSW.CA: source text did not clearly match LCSW.CA / Lecico Egypt.
- Evidence rejected for RUBX.CA: source text did not clearly match RUBX.CA / Rubex International for Plastic and Acrylic Manufacturing.
- Evidence rejected for ETEL.CA: source text did not clearly match ETEL.CA / Telecom Egypt.
- Evidence rejected for TALM.CA: source text did not clearly match TALM.CA / Talim Management Services.
