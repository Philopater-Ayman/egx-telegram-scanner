# Telegram-First EGX Scanner Report

Scan phase: Evening tomorrow plan
Generated UTC: 2026-10-12T23:09:22.740292+00:00
Generated Cairo: 2026-10-13 02:09
Run timing: target 19:30 Cairo | generated Cairo 2026-10-13 02:09 | cron 30 16 * * 0-4
Trigger: scheduled cron=30 16 * * 0-4 mapped to evening_plan; Cairo now 2026-10-13 02:05

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 6
- Tradeable price/liquidity tickers: 133/184
- Top sector: Telecommunications

## Market Context
- Market trend: Bearish
- Source: Mubasher EGX market page (delayed public data)
- As of: Monday, October 12
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 15.79% / above MA50 26.32%
- EGX70 regime: BEARISH / above MA20 13.79% / above MA50 17.24%
- Sector breadth: 9.52%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- COMI.CA: liquidity=532364640.0 spike=1.02 score=8.41
- CCAP.CA: liquidity=516032960.0 spike=0.68 score=14.52
- TMGH.CA: liquidity=226872160.0 spike=1.06 score=7.7
- ARAB.CA: liquidity=181132704.0 spike=2.04 score=24.66
- BIOC.CA: liquidity=153443328.0 spike=1.62 score=19.63

## AI Narrative
- Provider: OpenRouter OK
- Model: nvidia/nemotron-3-super-120b-a12b:free
- Summary: EGX30 and EGX70 remain bearish with low sector breadth, keeping the risk mode defensive and blocking new buys despite several tickets showing bullish watch outlooks.
- Liquidity is mostly tradeable but cooling; ARAB.CA and AMIA.CA show accumulation spikes, yet the sustainability of these inflows is uncertain.
- Top tickets sit in leading sectors (Telecom, Fintech & Payments, Investment Holding) that outperform the broader market, providing relative strength.
- Prices are either close to resistance (small resistance distance) or far above support, limiting near‑term upside and raising pullback risk over the next 1‑3 days.
- Scanner outlook flags BULLISH_WATCH for most tickets, but the bearish EGX30/EGX70 regime overrides this, adding uncertainty to short‑term direction.

## Top Liquidity Spikes
- MENA.CA: spike=8.03 liquidity=10051239.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- AJWA.CA: spike=4.52 liquidity=95075272.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- ETRS.CA: spike=3.37 liquidity=32074300.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- CNFN.CA: spike=2.12 liquidity=16354117.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- FAITA.CA: spike=2.05 liquidity=54672.4 outlook=WEAK_OR_RISKY score=0 buy_ready=False

## Sector Leaderboard
- #1 Telecommunications: score=7.25 5d=2.38% 20d=6.78% aboveMA50=100.0%
- #2 Fintech & Payments: score=4.98 5d=1.69% 20d=-0.5% aboveMA50=50.0%
- #3 Investment Holding: score=3.81 5d=-2.95% 20d=4.83% aboveMA50=66.67%
- #4 Transportation & Logistics: score=2.47 5d=-1.47% 20d=0.97% aboveMA50=50.0%
- #5 Education: score=2.13 5d=-2.89% 20d=1.43% aboveMA50=33.33%
- #6 Industrial Goods & Construction: score=1.5 5d=0.0% 20d=0.0% aboveMA50=0.0%
- #7 Non-bank Financial Services: score=1.48 5d=0.0% 20d=-0.69% aboveMA50=0.0%
- #8 Energy & Petrochemicals: score=1.3 5d=-2.21% 20d=0.0% aboveMA50=33.33%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- AMIA.CA: BULLISH_WATCH score=88.98 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- BINV.CA: BULLISH_WATCH score=88.81 liquidity=TRADEABLE sector=LEADING risk=No major short-term scanner risk flags.
- EFIH.CA: BULLISH_WATCH score=84.98 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- ETEL.CA: BULLISH_WATCH score=79.25 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; momentum is extended
- TALM.CA: BULLISH_WATCH score=73.13 liquidity=TRADEABLE sector=IMPROVING risk=far above support
- ARAB.CA: BULLISH_WATCH score=72 liquidity=ACCUMULATION_SPIKE sector=LAGGING risk=momentum is extended; far above support; sector is not leading
- ALCN.CA: CONSTRUCTIVE score=65.47 liquidity=TRADEABLE sector=IMPROVING risk=below MA20
- RUBX.CA: CONSTRUCTIVE score=60.98 liquidity=TRADEABLE sector=IMPROVING risk=far above support; sector is not leading; high short-term volatility
- ICID.CA: CONSTRUCTIVE score=58.98 liquidity=TRADEABLE sector=IMPROVING risk=below MA20; sector is not leading
- BIOC.CA: CONSTRUCTIVE score=56.98 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=below MA50; far above support; sector is not leading

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- EKHO.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ISPH.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ARVA.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- GTWL.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- WCDF.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=5.39 buy_ready=False sector_rank=10 price=245.85 support=230.11 resistance=359.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:27 PM market time freshness=DELAYED_CURRENT RSI=24.49 liquidity=5995844.0 spike=0.3
- ABUK.CA: score=11.85 buy_ready=False sector_rank=13 price=85.1 support=83.55 resistance=96.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:26 PM market time freshness=DELAYED_CURRENT RSI=34.44 liquidity=49501616.0 spike=0.53
- ACAMD.CA: score=15.45 buy_ready=False sector_rank=10 price=1.96 support=1.87 resistance=2.16 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:27 PM market time freshness=DELAYED_CURRENT RSI=40.82 liquidity=44492148.0 spike=1.03
- ACGC.CA: score=13.51 buy_ready=False sector_rank=15 price=13.14 support=13.11 resistance=15.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:27 PM market time freshness=DELAYED_CURRENT RSI=43.84 liquidity=11737359.0 spike=0.62
- ADCI.CA: score=6.35 buy_ready=False sector_rank=10 price=261.65 support=256.0 resistance=293.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:13 PM market time freshness=DELAYED_CURRENT RSI=37.2 liquidity=1955939.63 spike=0.86
- ADIB.CA: score=9.55 buy_ready=False sector_rank=12 price=45.92 support=46.6 resistance=54.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=20.97 liquidity=79119848.0 spike=1.09
- ADPC.CA: score=5.13 buy_ready=False sector_rank=10 price=3.26 support=3.25 resistance=3.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=20344068.0 spike=1.37
- AFDI.CA: score=10.36 buy_ready=False sector_rank=10 price=51.62 support=47.7 resistance=56.82 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:25 PM market time freshness=DELAYED_CURRENT RSI=41.28 liquidity=3969591.25 spike=0.59
- AFMC.CA: score=16.39 buy_ready=False sector_rank=10 price=139.17 support=131.0 resistance=179.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:14 PM market time freshness=DELAYED_CURRENT RSI=38.46 liquidity=10064435.0 spike=0.39
- AJWA.CA: score=9.39 buy_ready=False sector_rank=10 price=212.0 support=198.62 resistance=212.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=95075272.0 spike=4.52
- ALCN.CA: score=17.99 buy_ready=False sector_rank=4 price=32.25 support=30.4 resistance=36.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:28 PM market time freshness=DELAYED_CURRENT RSI=53.5 liquidity=28835314.0 spike=0.83
- ALUM.CA: score=2.14 buy_ready=False sector_rank=10 price=22.15 support=21.65 resistance=27.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=25.42 liquidity=3749517.5 spike=0.77
- AMER.CA: score=16.68 buy_ready=False sector_rank=14 price=4.87 support=4.05 resistance=5.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=40.69 liquidity=79187216.0 spike=1.55
- AMES.CA: score=15.39 buy_ready=False sector_rank=10 price=42.3 support=40.15 resistance=60.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=39.42 liquidity=56220256.0 spike=0.48
- AMIA.CA: score=21.21 buy_ready=False sector_rank=10 price=18.71 support=17.12 resistance=19.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:28 PM market time freshness=DELAYED_CURRENT RSI=60.56 liquidity=33079024.0 spike=1.91
- AMOC.CA: score=17.52 buy_ready=False sector_rank=8 price=13.44 support=12.18 resistance=14.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=45.96 liquidity=105150680.0 spike=0.79
- APSW.CA: score=5.95 buy_ready=False sector_rank=10 price=8.18 support=7.81 resistance=8.92 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:13 PM market time freshness=DELAYED_CURRENT RSI=42.86 liquidity=558064.75 spike=0.81
- ARAB.CA: score=24.66 buy_ready=False sector_rank=14 price=0.28 support=0.2 resistance=0.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:28 PM market time freshness=DELAYED_CURRENT RSI=64.35 liquidity=181132704.0 spike=2.04
- ARCC.CA: score=16.44 buy_ready=False sector_rank=9 price=67.43 support=60.01 resistance=76.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=45.42 liquidity=24848330.0 spike=0.81
- AREH.CA: score=8.83 buy_ready=False sector_rank=10 price=1.17 support=1.14 resistance=1.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=29.17 liquidity=11090098.0 spike=1.22
- ASCM.CA: score=5.17 buy_ready=False sector_rank=10 price=52.46 support=52.02 resistance=56.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=12091961.0 spike=1.39
- ASPI.CA: score=4.39 buy_ready=False sector_rank=10 price=0.33 support=0.33 resistance=0.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=18196268.0 spike=0.49
- ATLC.CA: score=2.34 buy_ready=False sector_rank=7 price=5.51 support=5.46 resistance=6.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=7743776.0 spike=0.68
- ATQA.CA: score=8.85 buy_ready=False sector_rank=13 price=11.5 support=10.91 resistance=13.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:25 PM market time freshness=DELAYED_CURRENT RSI=34.74 liquidity=53137156.0 spike=0.74
- AXPH.CA: score=3.61 buy_ready=False sector_rank=10 price=1439.5 support=1334.35 resistance=1987.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:14 PM market time freshness=DELAYED_CURRENT RSI=29.61 liquidity=4217760.0 spike=0.64
- BINV.CA: score=21.98 buy_ready=False sector_rank=3 price=58.0 support=49.91 resistance=72.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:25 PM market time freshness=DELAYED_CURRENT RSI=41.17 liquidity=29997604.0 spike=1.23
- BIOC.CA: score=19.63 buy_ready=False sector_rank=10 price=302.26 support=225.21 resistance=380.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=57.37 liquidity=153443328.0 spike=1.62
- BTFH.CA: score=8.59 buy_ready=False sector_rank=7 price=2.65 support=2.65 resistance=3.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:28 PM market time freshness=DELAYED_CURRENT RSI=27.4 liquidity=67739144.0 spike=0.72
- CAED.CA: score=5.82 buy_ready=False sector_rank=10 price=107.73 support=103.1 resistance=150.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:26 PM market time freshness=DELAYED_CURRENT RSI=34.22 liquidity=6426440.0 spike=0.4
- CANA.CA: score=14.07 buy_ready=False sector_rank=12 price=44.0 support=41.35 resistance=52.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:27 PM market time freshness=DELAYED_CURRENT RSI=30.43 liquidity=41989108.0 spike=1.85
- CCAP.CA: score=14.52 buy_ready=False sector_rank=3 price=6.28 support=6.25 resistance=7.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=29.38 liquidity=516032960.0 spike=0.68
- CCRS.CA: score=3.45 buy_ready=False sector_rank=10 price=2.08 support=2.06 resistance=2.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=9059062.0 spike=0.64
- CEFM.CA: score=-4.63 buy_ready=False sector_rank=10 price=128.08 support=126.93 resistance=136.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=980436.06 spike=0.3
- CERA.CA: score=16.39 buy_ready=False sector_rank=10 price=1.28 support=1.18 resistance=1.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=42.11 liquidity=81885712.0 spike=0.58
- CFGH.CA: score=-1.08 buy_ready=False sector_rank=10 price=0.11 support=0.11 resistance=0.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:26 PM market time freshness=DELAYED_CURRENT RSI=0.0 liquidity=9940.86 spike=1.26
- CICH.CA: score=6.79 buy_ready=False sector_rank=7 price=11.3 support=10.75 resistance=13.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:28 PM market time freshness=DELAYED_CURRENT RSI=37.06 liquidity=2200725.5 spike=0.63
- CIEB.CA: score=10.27 buy_ready=False sector_rank=12 price=22.95 support=23.0 resistance=25.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=28.05 liquidity=13264116.0 spike=1.45
- CIRA.CA: score=9.85 buy_ready=False sector_rank=5 price=36.62 support=36.8 resistance=41.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:26 PM market time freshness=DELAYED_CURRENT RSI=33.09 liquidity=18126282.0 spike=0.51
- CLHO.CA: score=8.94 buy_ready=False sector_rank=17 price=14.59 support=13.9 resistance=16.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=34.75 liquidity=22581086.0 spike=0.6
- CNFN.CA: score=6.83 buy_ready=False sector_rank=7 price=3.92 support=3.91 resistance=4.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:26 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=16354117.0 spike=2.12
- COMI.CA: score=8.41 buy_ready=False sector_rank=12 price=121.7 support=122.7 resistance=137.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=13.49 liquidity=532364640.0 spike=1.02
- COPR.CA: score=14.39 buy_ready=False sector_rank=10 price=0.46 support=0.44 resistance=0.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=38.26 liquidity=22026636.0 spike=0.88
- COSG.CA: score=4.39 buy_ready=False sector_rank=10 price=1.46 support=1.46 resistance=1.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=10463730.0 spike=0.66
- CPCI.CA: score=8.62 buy_ready=False sector_rank=10 price=592.63 support=530.0 resistance=619.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:14 PM market time freshness=DELAYED_CURRENT RSI=78.97 liquidity=2224939.25 spike=0.57
- CSAG.CA: score=2.7 buy_ready=False sector_rank=4 price=34.88 support=34.52 resistance=37.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=7714466.5 spike=0.98
- DAPH.CA: score=4.57 buy_ready=False sector_rank=10 price=94.59 support=93.82 resistance=103.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=41234460.0 spike=1.09
- DEIN.CA: score=7.39 buy_ready=False sector_rank=10 price=10.35 support=10.35 resistance=12.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 09:54 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=37.26 spike=0.01
- DOMT.CA: score=5.55 buy_ready=False sector_rank=19 price=23.47 support=23.81 resistance=28.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:14 PM market time freshness=DELAYED_CURRENT RSI=35.57 liquidity=3695591.75 spike=0.7
- DSCW.CA: score=8.39 buy_ready=False sector_rank=10 price=1.62 support=1.58 resistance=1.91 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:25 PM market time freshness=DELAYED_CURRENT RSI=23.33 liquidity=11631017.0 spike=0.62
- DTPP.CA: score=9.39 buy_ready=False sector_rank=10 price=276.22 support=250.01 resistance=380.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=31.91 liquidity=27059186.0 spike=0.27
- EALR.CA: score=0.92 buy_ready=False sector_rank=10 price=320.08 support=312.0 resistance=411.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:08 PM market time freshness=DELAYED_CURRENT RSI=28.01 liquidity=2526706.75 spike=0.26
- EASB.CA: score=-0.14 buy_ready=False sector_rank=10 price=7.3 support=7.22 resistance=7.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=5470531.0 spike=0.63
- EAST.CA: score=7.02 buy_ready=False sector_rank=19 price=27.53 support=27.91 resistance=34.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:27 PM market time freshness=DELAYED_CURRENT RSI=16.38 liquidity=49433352.0 spike=1.08
- EBSC.CA: score=-0.47 buy_ready=False sector_rank=10 price=1.69 support=1.61 resistance=2.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:26 PM market time freshness=DELAYED_CURRENT RSI=29.87 liquidity=1142340.62 spike=0.42
- ECAP.CA: score=3.12 buy_ready=False sector_rank=10 price=29.63 support=29.13 resistance=33.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:14 PM market time freshness=DELAYED_CURRENT RSI=27.31 liquidity=2730250.5 spike=0.64
- EDFM.CA: score=7.05 buy_ready=False sector_rank=10 price=393.61 support=354.0 resistance=425.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:09 PM market time freshness=DELAYED_CURRENT RSI=43.38 liquidity=656857.81 spike=0.56
- EEII.CA: score=5.55 buy_ready=False sector_rank=10 price=2.0 support=2.02 resistance=2.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:28 PM market time freshness=DELAYED_CURRENT RSI=31.88 liquidity=5154432.0 spike=0.54
- EFIC.CA: score=7.85 buy_ready=False sector_rank=13 price=155.33 support=147.0 resistance=217.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=20.62 liquidity=24162726.0 spike=0.52
- EFID.CA: score=8.86 buy_ready=False sector_rank=19 price=18.52 support=18.1 resistance=31.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:28 PM market time freshness=DELAYED_CURRENT RSI=27.23 liquidity=28066482.0 spike=0.54
- EFIH.CA: score=24.99 buy_ready=False sector_rank=2 price=24.01 support=20.2 resistance=25.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:27 PM market time freshness=DELAYED_CURRENT RSI=59.2 liquidity=46115320.0 spike=0.71
- EGAL.CA: score=8.85 buy_ready=False sector_rank=13 price=325.61 support=331.5 resistance=378.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=18.13 liquidity=40793856.0 spike=0.78
- EGAS.CA: score=0.48 buy_ready=False sector_rank=8 price=51.1 support=51.0 resistance=56.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=5963725.5 spike=0.53
- EGBE.CA: score=6.39 buy_ready=False sector_rank=12 price=0.53 support=0.49 resistance=0.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:26 PM market time freshness=DELAYED_CURRENT RSI=75.34 liquidity=25699.37 spike=0.2
- EGCH.CA: score=8.85 buy_ready=False sector_rank=13 price=12.79 support=12.88 resistance=14.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:26 PM market time freshness=DELAYED_CURRENT RSI=27.6 liquidity=33852476.0 spike=0.4
- EGSA.CA: score=7.4 buy_ready=False sector_rank=1 price=8.87 support=8.82 resistance=9.08 source=Yahoo Finance as_of=2026-10-10T21:00:00+00:00 freshness=FRESH RSI=11.76 liquidity=691.86 spike=0.12
- EGTS.CA: score=3.58 buy_ready=False sector_rank=14 price=14.5 support=14.02 resistance=16.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=31855116.0 spike=0.88
- EHDR.CA: score=2.62 buy_ready=False sector_rank=10 price=2.31 support=2.31 resistance=2.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=8228117.0 spike=0.71
- ELEC.CA: score=6.72 buy_ready=False sector_rank=20 price=1.74 support=1.72 resistance=2.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=26.67 liquidity=49665640.0 spike=0.81
- ELKA.CA: score=10.39 buy_ready=False sector_rank=10 price=1.5 support=1.43 resistance=1.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:28 PM market time freshness=DELAYED_CURRENT RSI=33.33 liquidity=12918482.0 spike=0.94
- ELNA.CA: score=7.02 buy_ready=False sector_rank=10 price=35.22 support=33.46 resistance=36.98 source=Yahoo Finance as_of=2026-10-10T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=264150.01 spike=1.68
- ELSH.CA: score=4.97 buy_ready=False sector_rank=10 price=11.11 support=11.06 resistance=11.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=27428990.0 spike=1.29
- ELWA.CA: score=8.75 buy_ready=False sector_rank=10 price=1.65 support=1.43 resistance=1.84 source=Yahoo Finance as_of=2026-10-10T21:00:00+00:00 freshness=FRESH RSI=44.68 liquidity=361348.34 spike=0.48
- EMFD.CA: score=8.58 buy_ready=False sector_rank=14 price=12.22 support=11.7 resistance=15.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:14 PM market time freshness=DELAYED_CURRENT RSI=32.75 liquidity=46700868.0 spike=0.6
- ENGC.CA: score=6.04 buy_ready=False sector_rank=10 price=34.53 support=33.33 resistance=45.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:14 PM market time freshness=DELAYED_CURRENT RSI=23.98 liquidity=7646022.5 spike=0.43
- EOSB.CA: score=9.4 buy_ready=False sector_rank=10 price=1.57 support=1.6 resistance=1.64 source=Yahoo Finance as_of=2026-10-10T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=7162.34 spike=0.14
- EPCO.CA: score=2.27 buy_ready=False sector_rank=10 price=9.17 support=9.25 resistance=12.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:25 PM market time freshness=DELAYED_CURRENT RSI=22.78 liquidity=3877359.75 spike=0.4
- EPPK.CA: score=-5.19 buy_ready=False sector_rank=10 price=10.29 support=10.29 resistance=10.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=8 September 01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=419183.72 spike=0.28
- ETEL.CA: score=24.4 buy_ready=False sector_rank=1 price=143.48 support=124.01 resistance=156.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:27 PM market time freshness=DELAYED_CURRENT RSI=67.03 liquidity=124611328.0 spike=0.47
- ETRS.CA: score=9.13 buy_ready=False sector_rank=10 price=10.06 support=10.0 resistance=10.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:26 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=32074300.0 spike=3.37
- EXPA.CA: score=8.37 buy_ready=False sector_rank=12 price=14.8 support=15.22 resistance=22.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=15.93 liquidity=28536968.0 spike=0.74
- FAIT.CA: score=5.86 buy_ready=False sector_rank=12 price=44.04 support=38.48 resistance=48.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=33.4 liquidity=3289522.5 spike=1.1
- FAITA.CA: score=7.52 buy_ready=False sector_rank=12 price=0.98 support=0.98 resistance=1.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 12:59 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=54672.4 spike=2.05
- FERC.CA: score=8.48 buy_ready=False sector_rank=13 price=71.07 support=70.42 resistance=82.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:25 PM market time freshness=DELAYED_CURRENT RSI=26.08 liquidity=9449349.0 spike=1.59
- FWRY.CA: score=20.31 buy_ready=False sector_rank=2 price=18.55 support=17.5 resistance=19.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=43.34 liquidity=128712112.0 spike=1.16
- GBCO.CA: score=15.44 buy_ready=False sector_rank=16 price=29.81 support=27.0 resistance=32.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:28 PM market time freshness=DELAYED_CURRENT RSI=43.81 liquidity=31657036.0 spike=0.32
- GDWA.CA: score=8.39 buy_ready=False sector_rank=10 price=0.62 support=0.61 resistance=0.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:28 PM market time freshness=DELAYED_CURRENT RSI=18.72 liquidity=12387062.0 spike=0.54
- GGCC.CA: score=-1.21 buy_ready=False sector_rank=10 price=0.67 support=0.67 resistance=0.71 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=4398822.5 spike=0.3
- GIHD.CA: score=4.39 buy_ready=False sector_rank=10 price=54.16 support=53.3 resistance=60.06 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=12670202.0 spike=0.65
- GMCI.CA: score=6.19 buy_ready=False sector_rank=10 price=1.61 support=1.49 resistance=1.9 source=Yahoo Finance as_of=2026-10-10T21:00:00+00:00 freshness=FRESH RSI=36.84 liquidity=539179.34 spike=1.13
- GRCA.CA: score=4.6 buy_ready=False sector_rank=10 price=33.99 support=32.11 resistance=56.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:28 PM market time freshness=DELAYED_CURRENT RSI=31.66 liquidity=4208494.0 spike=0.23
- GSSC.CA: score=0.25 buy_ready=False sector_rank=10 price=265.61 support=246.0 resistance=333.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:14 PM market time freshness=DELAYED_CURRENT RSI=32.92 liquidity=861444.5 spike=0.24
- HDBK.CA: score=11.37 buy_ready=False sector_rank=12 price=104.11 support=102.03 resistance=121.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=27.03 liquidity=17334202.0 spike=0.63
- HELI.CA: score=8.58 buy_ready=False sector_rank=14 price=7.16 support=6.94 resistance=8.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=23.5 liquidity=57105676.0 spike=0.52
- HRHO.CA: score=17.59 buy_ready=False sector_rank=7 price=25.3 support=22.81 resistance=27.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:28 PM market time freshness=DELAYED_CURRENT RSI=53.97 liquidity=60471524.0 spike=0.45
- ICID.CA: score=15.48 buy_ready=False sector_rank=10 price=17.89 support=16.52 resistance=20.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=49.13 liquidity=8027173.5 spike=1.03
- IDRE.CA: score=1.41 buy_ready=False sector_rank=10 price=43.1 support=42.1 resistance=48.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=7020301.5 spike=0.48
- IFAP.CA: score=4.63 buy_ready=False sector_rank=18 price=18.51 support=17.17 resistance=21.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:28 PM market time freshness=DELAYED_CURRENT RSI=32.55 liquidity=7726907.5 spike=1.0
- INFI.CA: score=14.6 buy_ready=False sector_rank=10 price=118.72 support=104.0 resistance=147.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:27 PM market time freshness=DELAYED_CURRENT RSI=41.3 liquidity=8207913.0 spike=0.59
- IRON.CA: score=17.27 buy_ready=False sector_rank=13 price=27.92 support=25.01 resistance=32.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=51.18 liquidity=13752813.0 spike=1.21
- ISMA.CA: score=0.32 buy_ready=False sector_rank=10 price=23.53 support=23.07 resistance=25.92 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=5930755.5 spike=0.64
- ISMQ.CA: score=9.85 buy_ready=False sector_rank=13 price=7.8 support=7.6 resistance=9.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=32.03 liquidity=16780984.0 spike=0.84
- JUFO.CA: score=6.86 buy_ready=False sector_rank=19 price=24.68 support=24.4 resistance=27.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=32.7 liquidity=11914673.0 spike=0.72
- KABO.CA: score=5.27 buy_ready=False sector_rank=15 price=8.0 support=7.3 resistance=8.67 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=57142380.0 spike=1.88
- KWIN.CA: score=-1.6 buy_ready=False sector_rank=10 price=69.93 support=69.81 resistance=74.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:26 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=4011889.0 spike=0.37
- KZPC.CA: score=6.01 buy_ready=False sector_rank=10 price=12.69 support=12.15 resistance=14.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:11 PM market time freshness=DELAYED_CURRENT RSI=33.64 liquidity=3620007.25 spike=0.31
- LCSW.CA: score=4.44 buy_ready=False sector_rank=9 price=31.98 support=31.1 resistance=34.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=13611089.0 spike=0.72
- LUTS.CA: score=16.39 buy_ready=False sector_rank=10 price=0.82 support=0.72 resistance=1.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:28 PM market time freshness=DELAYED_CURRENT RSI=40.98 liquidity=60487536.0 spike=0.9
- MAAL.CA: score=4.39 buy_ready=False sector_rank=10 price=9.84 support=9.8 resistance=10.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=11409946.0 spike=0.49
- MASR.CA: score=16.39 buy_ready=False sector_rank=10 price=7.39 support=6.82 resistance=8.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=66759716.0 spike=0.93
- MBSC.CA: score=4.44 buy_ready=False sector_rank=9 price=348.48 support=348.01 resistance=376.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=61743444.0 spike=0.76
- MCQE.CA: score=4.76 buy_ready=False sector_rank=9 price=183.74 support=182.0 resistance=194.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=57108304.0 spike=1.16
- MCRO.CA: score=9.39 buy_ready=False sector_rank=10 price=1.43 support=1.41 resistance=1.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:28 PM market time freshness=DELAYED_CURRENT RSI=33.33 liquidity=29037426.0 spike=0.37
- MENA.CA: score=8.58 buy_ready=False sector_rank=14 price=6.11 support=6.01 resistance=6.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=10051239.0 spike=8.03
- MEPA.CA: score=8.39 buy_ready=False sector_rank=10 price=1.6 support=1.56 resistance=2.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:25 PM market time freshness=DELAYED_CURRENT RSI=28.38 liquidity=11996720.0 spike=0.96
- MFPC.CA: score=11.85 buy_ready=False sector_rank=13 price=43.69 support=43.0 resistance=51.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:26 PM market time freshness=DELAYED_CURRENT RSI=31.74 liquidity=28634832.0 spike=0.3
- MFSC.CA: score=-3.29 buy_ready=False sector_rank=10 price=39.79 support=39.0 resistance=42.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=2318123.5 spike=0.91
- MHOT.CA: score=13.39 buy_ready=False sector_rank=11 price=17.61 support=16.2 resistance=21.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=45.04 liquidity=18172006.0 spike=0.97
- MICH.CA: score=12.06 buy_ready=False sector_rank=10 price=44.6 support=42.01 resistance=50.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=42.23 liquidity=7672114.0 spike=0.8
- MILS.CA: score=0.15 buy_ready=False sector_rank=10 price=163.59 support=161.02 resistance=179.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=5753493.0 spike=0.59
- MIPH.CA: score=3.64 buy_ready=False sector_rank=17 price=788.67 support=739.69 resistance=1000.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:27 PM market time freshness=DELAYED_CURRENT RSI=40.02 liquidity=699737.13 spike=0.08
- MOED.CA: score=8.39 buy_ready=False sector_rank=10 price=0.64 support=0.59 resistance=0.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:28 PM market time freshness=DELAYED_CURRENT RSI=27.72 liquidity=14158783.0 spike=0.45
- MOIL.CA: score=-0.26 buy_ready=False sector_rank=8 price=0.67 support=0.67 resistance=0.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:27 PM market time freshness=DELAYED_CURRENT RSI=31.58 liquidity=220375.06 spike=0.83
- MOIN.CA: score=-0.44 buy_ready=False sector_rank=10 price=33.57 support=33.3 resistance=35.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:13 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=5163638.0 spike=0.37
- MOSC.CA: score=0.29 buy_ready=False sector_rank=10 price=267.9 support=257.0 resistance=329.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:08 PM market time freshness=DELAYED_CURRENT RSI=33.58 liquidity=899315.5 spike=0.27
- MPCI.CA: score=9.95 buy_ready=False sector_rank=10 price=320.37 support=305.45 resistance=455.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=28.7 liquidity=136039120.0 spike=1.28
- MPCO.CA: score=7.91 buy_ready=False sector_rank=18 price=2.2 support=2.25 resistance=3.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=15.79 liquidity=80478968.0 spike=0.5
- MPRC.CA: score=3.33 buy_ready=False sector_rank=10 price=36.89 support=36.53 resistance=39.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=8933972.0 spike=0.44
- MTIE.CA: score=9.44 buy_ready=False sector_rank=16 price=7.6 support=7.5 resistance=8.62 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=29.75 liquidity=12654505.0 spike=0.72
- NAHO.CA: score=4.39 buy_ready=False sector_rank=10 price=0.13 support=0.12 resistance=0.14 source=Yahoo Finance as_of=2026-10-10T21:00:00+00:00 freshness=FRESH RSI=48.15 liquidity=2061.5 spike=0.06
- NCCW.CA: score=4.39 buy_ready=False sector_rank=10 price=6.41 support=6.4 resistance=6.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=25236992.0 spike=0.44
- NEDA.CA: score=-0.27 buy_ready=False sector_rank=10 price=2.6 support=2.48 resistance=2.8 source=Yahoo Finance as_of=2026-10-10T21:00:00+00:00 freshness=FRESH RSI=25.0 liquidity=339450.79 spike=0.47
- NHPS.CA: score=0.14 buy_ready=False sector_rank=10 price=66.85 support=66.5 resistance=71.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=5748902.0 spike=0.39
- NINH.CA: score=4.39 buy_ready=False sector_rank=10 price=17.43 support=17.27 resistance=18.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=10852622.0 spike=0.76
- NIPH.CA: score=12.94 buy_ready=False sector_rank=17 price=293.43 support=290.0 resistance=368.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=46.96 liquidity=86862984.0 spike=0.71
- OBRI.CA: score=4.39 buy_ready=False sector_rank=10 price=26.28 support=25.85 resistance=28.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=11657666.0 spike=0.84
- OCDI.CA: score=8.58 buy_ready=False sector_rank=14 price=25.64 support=24.2 resistance=32.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:26 PM market time freshness=DELAYED_CURRENT RSI=29.79 liquidity=27414410.0 spike=0.54
- OCPH.CA: score=-1.72 buy_ready=False sector_rank=10 price=206.9 support=200.0 resistance=222.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=3807597.25 spike=1.04
- ODIN.CA: score=1.48 buy_ready=False sector_rank=10 price=2.3 support=2.29 resistance=2.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=7084756.5 spike=0.78
- OFH.CA: score=9.39 buy_ready=False sector_rank=10 price=0.81 support=0.83 resistance=1.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=31.2 liquidity=28994674.0 spike=0.29
- OIH.CA: score=6.52 buy_ready=False sector_rank=3 price=1.78 support=1.74 resistance=1.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=48124164.0 spike=0.53
- OLFI.CA: score=6.86 buy_ready=False sector_rank=19 price=20.81 support=20.82 resistance=23.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=21.29 liquidity=14489643.0 spike=0.83
- ORAS.CA: score=4.6 buy_ready=False sector_rank=6 price=849.39 support=840.01 resistance=859.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=129412992.0 spike=1.0
- ORHD.CA: score=3.58 buy_ready=False sector_rank=14 price=10.9 support=10.9 resistance=11.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=138439120.0 spike=0.9
- ORWE.CA: score=16.65 buy_ready=False sector_rank=15 price=26.64 support=26.01 resistance=28.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=36.06 liquidity=40466980.0 spike=1.07
- PHAR.CA: score=14.94 buy_ready=False sector_rank=17 price=107.97 support=102.0 resistance=127.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=42.96 liquidity=45425672.0 spike=0.61
- PHDC.CA: score=15.58 buy_ready=False sector_rank=14 price=12.61 support=12.36 resistance=14.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:25 PM market time freshness=DELAYED_CURRENT RSI=42.34 liquidity=43605636.0 spike=0.41
- PHTV.CA: score=6.99 buy_ready=False sector_rank=10 price=337.0 support=315.1 resistance=378.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:05 PM market time freshness=DELAYED_CURRENT RSI=41.35 liquidity=596135.81 spike=0.49
- POUL.CA: score=6.86 buy_ready=False sector_rank=19 price=9.59 support=9.12 resistance=41.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=1.89 liquidity=20238390.0 spike=0.61
- PRCL.CA: score=0.85 buy_ready=False sector_rank=9 price=22.97 support=22.66 resistance=25.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=6408010.5 spike=0.52
- PRDC.CA: score=15.58 buy_ready=False sector_rank=14 price=6.71 support=6.81 resistance=8.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=37.4 liquidity=30121872.0 spike=0.86
- PRMH.CA: score=0.8 buy_ready=False sector_rank=10 price=2.09 support=2.03 resistance=2.82 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=16.46 liquidity=2406118.75 spike=0.61
- RACC.CA: score=4.8 buy_ready=False sector_rank=10 price=9.01 support=8.51 resistance=10.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:25 PM market time freshness=DELAYED_CURRENT RSI=34.96 liquidity=4409234.0 spike=0.64
- RAKT.CA: score=13.78 buy_ready=False sector_rank=10 price=23.22 support=20.26 resistance=25.08 source=Yahoo Finance as_of=2026-10-10T21:00:00+00:00 freshness=FRESH RSI=64.25 liquidity=628797.58 spike=1.88
- RAYA.CA: score=6.58 buy_ready=False sector_rank=21 price=6.05 support=5.72 resistance=7.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:28 PM market time freshness=DELAYED_CURRENT RSI=33.74 liquidity=17179938.0 spike=0.48
- RMDA.CA: score=7.94 buy_ready=False sector_rank=17 price=5.09 support=4.83 resistance=6.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=22.08 liquidity=15352979.0 spike=0.47
- ROTO.CA: score=1.95 buy_ready=False sector_rank=10 price=38.03 support=37.38 resistance=41.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=7554528.5 spike=0.89
- RREI.CA: score=0.79 buy_ready=False sector_rank=10 price=3.47 support=3.46 resistance=3.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=6401799.5 spike=0.59
- RTVC.CA: score=4.76 buy_ready=False sector_rank=10 price=3.48 support=3.37 resistance=4.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:14 PM market time freshness=DELAYED_CURRENT RSI=34.88 liquidity=3631193.5 spike=1.37
- RUBX.CA: score=21.39 buy_ready=False sector_rank=10 price=17.01 support=12.65 resistance=19.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=53.77 liquidity=89123424.0 spike=0.95
- SAUD.CA: score=14.37 buy_ready=False sector_rank=12 price=21.8 support=21.6 resistance=26.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:26 PM market time freshness=DELAYED_CURRENT RSI=41.08 liquidity=11048836.0 spike=0.58
- SCEM.CA: score=16.44 buy_ready=False sector_rank=9 price=86.76 support=74.55 resistance=102.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:27 PM market time freshness=DELAYED_CURRENT RSI=42.88 liquidity=48537992.0 spike=0.71
- SCFM.CA: score=-0.95 buy_ready=False sector_rank=10 price=239.31 support=223.11 resistance=290.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:12 PM market time freshness=DELAYED_CURRENT RSI=31.78 liquidity=654073.5 spike=0.3
- SCTS.CA: score=0.92 buy_ready=False sector_rank=5 price=516.71 support=520.3 resistance=635.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:05 PM market time freshness=DELAYED_CURRENT RSI=26.52 liquidity=1065621.63 spike=0.67
- SDTI.CA: score=19.39 buy_ready=False sector_rank=10 price=85.25 support=71.0 resistance=94.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=70.0 liquidity=22943054.0 spike=0.69
- SEIG.CA: score=-4.91 buy_ready=False sector_rank=10 price=210.19 support=209.0 resistance=224.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=695586.0 spike=0.31
- SIPC.CA: score=4.99 buy_ready=False sector_rank=10 price=5.34 support=5.32 resistance=5.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=69945008.0 spike=1.3
- SKPC.CA: score=7.85 buy_ready=False sector_rank=13 price=15.5 support=15.4 resistance=18.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:28 PM market time freshness=DELAYED_CURRENT RSI=17.27 liquidity=51613608.0 spike=0.6
- SMFR.CA: score=8.92 buy_ready=False sector_rank=10 price=219.82 support=205.01 resistance=255.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:14 PM market time freshness=DELAYED_CURRENT RSI=44.24 liquidity=2528531.0 spike=0.7
- SNFC.CA: score=17.1 buy_ready=False sector_rank=10 price=11.3 support=10.58 resistance=11.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:14 PM market time freshness=DELAYED_CURRENT RSI=54.69 liquidity=7707843.0 spike=0.63
- SPIN.CA: score=0.67 buy_ready=False sector_rank=15 price=15.55 support=15.11 resistance=19.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=32.42 liquidity=2161187.0 spike=0.36
- SPMD.CA: score=3.13 buy_ready=False sector_rank=10 price=0.36 support=0.36 resistance=0.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=8741258.0 spike=0.12
- SUGR.CA: score=8.68 buy_ready=False sector_rank=19 price=53.54 support=50.5 resistance=64.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:28 PM market time freshness=DELAYED_CURRENT RSI=39.78 liquidity=5827869.5 spike=0.4
- SVCE.CA: score=4.39 buy_ready=False sector_rank=10 price=9.57 support=9.5 resistance=10.16 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=48871636.0 spike=0.52
- SWDY.CA: score=7.72 buy_ready=False sector_rank=20 price=112.03 support=102.31 resistance=129.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=33.52 liquidity=48138984.0 spike=0.81
- TALM.CA: score=21.85 buy_ready=False sector_rank=5 price=21.69 support=17.61 resistance=25.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:27 PM market time freshness=DELAYED_CURRENT RSI=53.58 liquidity=71019504.0 spike=0.98
- TMGH.CA: score=7.7 buy_ready=False sector_rank=14 price=84.39 support=84.4 resistance=99.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=17.64 liquidity=226872160.0 spike=1.06
- TRTO.CA: score=9.4 buy_ready=False sector_rank=10 price=0.07 support=0.05 resistance=0.07 source=Yahoo Finance as_of=2026-10-10T21:00:00+00:00 freshness=FRESH RSI=65.22 liquidity=4054.65 spike=0.37
- UEFM.CA: score=10.64 buy_ready=False sector_rank=10 price=503.68 support=407.57 resistance=550.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 12:55 PM market time freshness=DELAYED_CURRENT RSI=51.53 liquidity=2250248.0 spike=0.62
- UEGC.CA: score=10.39 buy_ready=False sector_rank=10 price=1.44 support=1.37 resistance=1.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:26 PM market time freshness=DELAYED_CURRENT RSI=28.79 liquidity=17077638.0 spike=0.51
- UNIP.CA: score=3.4 buy_ready=False sector_rank=10 price=0.33 support=0.33 resistance=0.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=9006476.0 spike=0.79
- UNIT.CA: score=5.16 buy_ready=False sector_rank=14 price=16.99 support=16.41 resistance=23.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:13 PM market time freshness=DELAYED_CURRENT RSI=37.1 liquidity=1579839.75 spike=0.1
- WKOL.CA: score=8.39 buy_ready=False sector_rank=10 price=279.22 support=266.18 resistance=379.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:26 PM market time freshness=DELAYED_CURRENT RSI=21.59 liquidity=10395365.0 spike=0.9
- ZEOT.CA: score=0.21 buy_ready=False sector_rank=10 price=11.05 support=11.0 resistance=12.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=5718380.5 spike=1.05
- ZMID.CA: score=8.58 buy_ready=False sector_rank=14 price=7.18 support=7.07 resistance=9.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=16.35 liquidity=41910672.0 spike=0.39

## Backtesting Lite
- EFIH.CA: 180d return=22.89%, max drawdown=-22.68%, MA20>MA50 days last20=9, as_of=2026-10-10T21:00:00+00:00
- ARAB.CA: 180d return=36.36%, max drawdown=-26.79%, MA20>MA50 days last20=13, as_of=2026-10-10T21:00:00+00:00
- ETEL.CA: 180d return=113.03%, max drawdown=-30.44%, MA20>MA50 days last20=20, as_of=2026-10-10T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- EFIH.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=E-Finance For Digital and Financial Investments summary=Evidence rejected for EFIH.CA: source text did not clearly match EFIH.CA / E-Finance For Digital and Financial Investments.
- ARAB.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Arab Developers Holding summary=Arab Developers Holding unveils EGP 1bn expansion plans to improve financial efficiency; FRA gives initial approval for Arab Developers’ rights issue; Arab Developers stock stabilizes after correction
  - Arab Developers Holding unveils EGP 1bn expansion plans to improve financial efficiency: https://english.mubasher.info/news/4601724/Arab-Developers-Holding-unveils-EGP-1bn-expansion-plans-to-improve-financial-efficiency/
  - FRA gives initial approval for Arab Developers’ rights issue: https://english.mubasher.info/news/4582627/FRA-gives-initial-approval-for-Arab-Developers-rights-issue/
  - Arab Developers stock stabilizes after correction: https://english.mubasher.info/news/4564643/Arab-Developers-stock-stabilizes-after-correction/
- ETEL.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Telecom Egypt summary=Evidence rejected for ETEL.CA: source text did not clearly match ETEL.CA / Telecom Egypt.
- BINV.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=B Investments Holding summary=Evidence rejected for BINV.CA: source text did not clearly match BINV.CA / B Investments Holding.
- TALM.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Talim Management Services summary=Evidence rejected for TALM.CA: source text did not clearly match TALM.CA / Talim Management Services.
- RUBX.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Rubex International for Plastic and Acrylic Manufacturing summary=Evidence rejected for RUBX.CA: source text did not clearly match RUBX.CA / Rubex International for Plastic and Acrylic Manufacturing.
- AMIA.CA: status=OLD_ACCEPTED latest=2023-01-01 age_days=1380 sources=3 expected=Arab Moltaqa Investments Company summary=Arab Moltaqa recrods EGP 221m consolidated profit in 2023; dividends proposed; Arab Moltaqa hikes stake in Expedition Investments for EGP 25m; Arab Moltaqa unveils sale, purchase deals
  - Arab Moltaqa recrods EGP 221m consolidated profit in 2023; dividends proposed: https://english.mubasher.info/news/4252672/Arab-Moltaqa-recrods-EGP-221m-consolidated-profit-in-2023-dividends-proposed/
  - Arab Moltaqa hikes stake in Expedition Investments for EGP 25m: https://english.mubasher.info/news/4235831/Arab-Moltaqa-hikes-stake-in-Expedition-Investments-for-EGP-25m/
  - Arab Moltaqa unveils sale, purchase deals: https://english.mubasher.info/news/4219733/Arab-Moltaqa-unveils-sale-purchase-deals/
- FWRY.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Fawry For Banking Technology and Electronic Payments summary=Evidence rejected for FWRY.CA: source text did not clearly match FWRY.CA / Fawry For Banking Technology and Electronic Payments.

## Warnings
- Evidence rejected for EFIH.CA: source text did not clearly match EFIH.CA / E-Finance For Digital and Financial Investments.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence for ARAB.CA matches the company but no source/report date was detected.
- Evidence rejected for ETEL.CA: source text did not clearly match ETEL.CA / Telecom Egypt.
- Evidence rejected for BINV.CA: source text did not clearly match BINV.CA / B Investments Holding.
- Evidence rejected for TALM.CA: source text did not clearly match TALM.CA / Talim Management Services.
- Evidence rejected for RUBX.CA: source text did not clearly match RUBX.CA / Rubex International for Plastic and Acrylic Manufacturing.
- Evidence for AMIA.CA matches the company but appears old; latest detected date is 2023-01-01.
- Evidence rejected for FWRY.CA: source text did not clearly match FWRY.CA / Fawry For Banking Technology and Electronic Payments.
