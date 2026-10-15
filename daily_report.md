# Telegram-First EGX Scanner Report

Scan phase: Intraday liquidity update
Generated UTC: 2026-10-15T13:05:24.928302+00:00
Generated Cairo: 2026-10-15 16:05
Run timing: target 11:00 Cairo | generated Cairo 2026-10-15 16:05 | cron 0 8 * * 0-4
Trigger: scheduled cron=0 8 * * 0-4 mapped to intraday; Cairo now 2026-10-15 16:00

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 3
- Tradeable price/liquidity tickers: 175/187
- Top sector: Telecommunications

## Market Context
- Market trend: Bullish
- Source: Mubasher EGX market page (delayed public data)
- As of: Thursday, October 15
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 16.67% / above MA50 22.22%
- EGX70 regime: BEARISH / above MA20 15.0% / above MA50 20.0%
- Sector breadth: 0.0%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- COMI.CA: liquidity=690684544.0 spike=1.29 score=8.36
- CCAP.CA: liquidity=356367104.0 spike=0.59 score=8.72
- ETEL.CA: liquidity=253711360.0 spike=0.95 score=23.97
- UEGC.CA: liquidity=224034928.0 spike=6.59 score=7.4
- TMGH.CA: liquidity=209270656.0 spike=0.93 score=6.65

## AI Narrative
- Provider: OpenRouter OK
- Model: nvidia/nemotron-3-super-120b-a12b:free
- Summary: EGX30 and EGX70 are both in a bearish trend with virtually no sector breadth, forcing the scanner into a defensive risk mode that blocks new buys; therefore all top‑ranked tickets remain on HOLD despite some bullish watch signals.
- Top tickets such as EFIH.CA, ETEL.CA and ACAMD.CA show tradeable liquidity and bullish‑watch outlooks, but the defensive EGX regime overrides these signals, keeping actions at HOLD with low confidence.
- Liquidity is moderate to high yet shows cooling spikes; prices sit a modest distance above 20‑day support and a few percent below 20‑day resistance, limiting near‑term upside over the next 1‑3 days.
- Leading sectors (Telecom, Fintech & Payments, Auto) display mixed breadth; many stocks are not in leading sectors, adding uncertainty to any short‑term move despite individual bullish watch scores.
- The bearish EGX30/EGX70 market regime shifts the risk mode to DEFENSIVE_NO_NEW_BUY, reducing confidence across the board and prompting the scanner to hold all positions rather than initiate new buys.

## Top Liquidity Spikes
- UEGC.CA: spike=6.59 liquidity=224034928.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- GGCC.CA: spike=6.55 liquidity=81387704.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- ZEOT.CA: spike=6.34 liquidity=39677248.0 outlook=WEAK_OR_RISKY score=20 buy_ready=False
- FAITA.CA: spike=5.47 liquidity=178495.05 outlook=NEUTRAL score=41 buy_ready=False
- INFI.CA: spike=4.39 liquidity=58489532.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False

## Sector Leaderboard
- #1 Telecommunications: score=4.93 5d=-1.18% 20d=4.64% aboveMA50=50.0%
- #2 Fintech & Payments: score=2.85 5d=-2.77% 20d=-0.64% aboveMA50=50.0%
- #3 Automotive & Distribution: score=2.16 5d=-3.83% 20d=-2.92% aboveMA50=50.0%
- #4 Industrial Goods & Construction: score=1.5 5d=0.0% 20d=0.0% aboveMA50=0.0%
- #5 Transportation & Logistics: score=1.3 5d=-3.55% 20d=1.78% aboveMA50=50.0%
- #6 Education: score=0.62 5d=-3.29% 20d=-7.64% aboveMA50=66.67%
- #7 Energy & Petrochemicals: score=-0.3 5d=-5.24% 20d=1.34% aboveMA50=33.33%
- #8 Banking & Financials: score=-0.56 5d=-4.06% 20d=-6.24% aboveMA50=20.0%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- ETEL.CA: BULLISH_WATCH score=89.93 liquidity=TRADEABLE sector=LEADING risk=No major short-term scanner risk flags.
- GBCO.CA: BULLISH_WATCH score=87.16 liquidity=TRADEABLE sector=LEADING risk=No major short-term scanner risk flags.
- ORWE.CA: BULLISH_WATCH score=82 liquidity=ACCUMULATION_SPIKE sector=LAGGING risk=sector is not leading
- EFIH.CA: BULLISH_WATCH score=72.85 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; far above support
- AMIA.CA: BULLISH_WATCH score=71 liquidity=TRADEABLE sector=LAGGING risk=liquidity is cooling; sector is not leading
- KZPC.CA: BULLISH_WATCH score=71 liquidity=TRADEABLE sector=LAGGING risk=liquidity is cooling; sector is not leading
- ICID.CA: BULLISH_WATCH score=71 liquidity=TRADEABLE sector=LAGGING risk=liquidity is cooling; sector is not leading
- TALM.CA: BULLISH_WATCH score=70.62 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- LCSW.CA: CONSTRUCTIVE score=64 liquidity=TRADEABLE sector=LAGGING risk=sector is not leading
- ALCN.CA: CONSTRUCTIVE score=59.3 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; below MA20

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- EKHO.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ARVA.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=0.53 buy_ready=False sector_rank=19 price=232.2 support=225.0 resistance=359.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=24.7 liquidity=3125486.5 spike=0.16
- ABUK.CA: score=10.59 buy_ready=False sector_rank=17 price=86.37 support=83.0 resistance=96.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=32.15 liquidity=70225456.0 spike=0.76
- ACAMD.CA: score=22.18 buy_ready=False sector_rank=19 price=2.14 support=1.87 resistance=2.16 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=62.07 liquidity=62882716.0 spike=1.39
- ACGC.CA: score=12.9 buy_ready=False sector_rank=14 price=13.5 support=12.81 resistance=14.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=39.75 liquidity=10563980.0 spike=0.82
- ADCI.CA: score=-0.98 buy_ready=False sector_rank=19 price=260.19 support=250.06 resistance=288.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=32.29 liquidity=1617976.63 spike=0.77
- ADIB.CA: score=8.78 buy_ready=False sector_rank=8 price=47.02 support=43.5 resistance=54.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=30.8 liquidity=54567808.0 spike=0.69
- ADPC.CA: score=3.15 buy_ready=False sector_rank=19 price=3.24 support=3.01 resistance=4.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=20.45 liquidity=6751096.0 spike=0.45
- AFDI.CA: score=3.93 buy_ready=False sector_rank=19 price=50.01 support=46.12 resistance=56.82 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=43.15 liquidity=1532817.38 spike=0.24
- AFMC.CA: score=6.43 buy_ready=False sector_rank=19 price=132.75 support=122.0 resistance=179.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=34.51 liquidity=9033261.0 spike=0.44
- AJWA.CA: score=16.98 buy_ready=False sector_rank=19 price=227.0 support=176.0 resistance=222.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=88.63 liquidity=36270556.0 spike=1.29
- ALCN.CA: score=15.85 buy_ready=False sector_rank=5 price=33.45 support=30.55 resistance=36.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=44.75 liquidity=8329712.5 spike=0.24
- ALUM.CA: score=-0.07 buy_ready=False sector_rank=19 price=21.13 support=20.52 resistance=27.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=26.87 liquidity=3531052.0 spike=0.77
- AMER.CA: score=14.65 buy_ready=False sector_rank=15 price=4.6 support=4.05 resistance=5.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=43.24 liquidity=34385600.0 spike=0.69
- AMES.CA: score=8.4 buy_ready=False sector_rank=19 price=39.11 support=38.02 resistance=59.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=31.25 liquidity=34364172.0 spike=0.37
- AMIA.CA: score=17.4 buy_ready=False sector_rank=19 price=19.0 support=17.12 resistance=19.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=51.65 liquidity=12434580.0 spike=0.69
- AMOC.CA: score=16.88 buy_ready=False sector_rank=7 price=13.42 support=12.18 resistance=14.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=52.03 liquidity=67823712.0 spike=0.53
- APSW.CA: score=1.71 buy_ready=False sector_rank=19 price=7.99 support=7.81 resistance=8.92 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=39.15 liquidity=307479.75 spike=0.47
- ARAB.CA: score=19.65 buy_ready=False sector_rank=15 price=0.27 support=0.2 resistance=0.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=64.91 liquidity=66120340.0 spike=0.67
- ARCC.CA: score=13.35 buy_ready=False sector_rank=12 price=66.92 support=60.01 resistance=74.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=47.31 liquidity=11688965.0 spike=0.37
- AREH.CA: score=5.13 buy_ready=False sector_rank=19 price=1.2 support=1.11 resistance=1.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=29.63 liquidity=8654350.0 spike=1.04
- ASCM.CA: score=2.1 buy_ready=False sector_rank=19 price=50.59 support=48.0 resistance=61.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=30.22 liquidity=5695445.0 spike=0.67
- ASPI.CA: score=6.4 buy_ready=False sector_rank=19 price=0.34 support=0.31 resistance=0.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=27.32 liquidity=15525600.0 spike=0.48
- ATLC.CA: score=2.75 buy_ready=False sector_rank=13 price=5.48 support=5.2 resistance=7.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=33.96 liquidity=4580230.5 spike=0.47
- ATQA.CA: score=12.59 buy_ready=False sector_rank=17 price=11.62 support=10.61 resistance=13.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=37.75 liquidity=29137638.0 spike=0.4
- AXPH.CA: score=0.65 buy_ready=False sector_rank=19 price=1371.51 support=1300.0 resistance=1987.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=24.72 liquidity=3249671.25 spike=0.48
- BINV.CA: score=11.05 buy_ready=False sector_rank=9 price=58.89 support=50.0 resistance=72.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=64.99 liquidity=2338475.25 spike=0.09
- BIOC.CA: score=16.4 buy_ready=False sector_rank=19 price=297.72 support=225.21 resistance=380.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=59.39 liquidity=31925714.0 spike=0.3
- BTFH.CA: score=7.83 buy_ready=False sector_rank=13 price=2.75 support=2.55 resistance=3.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=34.85 liquidity=133274232.0 spike=1.33
- CAED.CA: score=5.92 buy_ready=False sector_rank=19 price=104.41 support=95.0 resistance=136.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=37.43 liquidity=3524572.75 spike=0.41
- CANA.CA: score=11.5 buy_ready=False sector_rank=8 price=43.95 support=41.7 resistance=52.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=41.51 liquidity=4724065.0 spike=0.19
- CCAP.CA: score=8.72 buy_ready=False sector_rank=9 price=6.07 support=6.07 resistance=7.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=24.86 liquidity=356367104.0 spike=0.59
- CCRS.CA: score=1.0 buy_ready=False sector_rank=19 price=2.05 support=1.87 resistance=2.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=18.42 liquidity=3596357.25 spike=0.3
- CEFM.CA: score=2.94 buy_ready=False sector_rank=19 price=126.08 support=113.0 resistance=152.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=35.75 liquidity=543743.94 spike=0.2
- CERA.CA: score=13.12 buy_ready=False sector_rank=19 price=1.26 support=1.18 resistance=1.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=46.84 liquidity=166125584.0 spike=1.36
- CFGH.CA: score=-7.59 buy_ready=False sector_rank=19 price=0.11 support=0.1 resistance=0.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=6292.34 spike=0.98
- CICH.CA: score=-0.1 buy_ready=False sector_rank=13 price=10.99 support=10.6 resistance=13.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=29.55 liquidity=1724060.63 spike=0.49
- CIEB.CA: score=8.04 buy_ready=False sector_rank=8 price=22.99 support=22.56 resistance=25.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=30.26 liquidity=9260564.0 spike=0.96
- CIRA.CA: score=17.25 buy_ready=False sector_rank=6 price=37.77 support=35.51 resistance=41.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=40.69 liquidity=13807906.0 spike=0.58
- CLHO.CA: score=11.44 buy_ready=False sector_rank=16 price=14.05 support=13.86 resistance=16.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=25.89 liquidity=132545928.0 spike=3.42
- CNFN.CA: score=12.75 buy_ready=False sector_rank=13 price=4.16 support=3.8 resistance=4.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=36.13 liquidity=11299910.0 spike=1.29
- COMI.CA: score=8.36 buy_ready=False sector_rank=8 price=125.08 support=120.0 resistance=134.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=24.92 liquidity=690684544.0 spike=1.29
- COPR.CA: score=9.84 buy_ready=False sector_rank=19 price=0.47 support=0.44 resistance=0.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=42.03 liquidity=7443447.5 spike=0.32
- COSG.CA: score=6.4 buy_ready=False sector_rank=19 price=1.47 support=1.34 resistance=1.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=30.16 liquidity=11645836.0 spike=0.77
- CPCI.CA: score=8.79 buy_ready=False sector_rank=19 price=606.99 support=531.02 resistance=619.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=75.91 liquidity=2394917.75 spike=0.58
- CSAG.CA: score=11.39 buy_ready=False sector_rank=5 price=36.17 support=34.06 resistance=39.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=40.41 liquidity=6869389.0 spike=0.91
- DAPH.CA: score=12.4 buy_ready=False sector_rank=19 price=94.39 support=89.1 resistance=129.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=37.77 liquidity=31236638.0 spike=0.77
- DEIN.CA: score=5.4 buy_ready=False sector_rank=19 price=10.35 support=10.35 resistance=12.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 09:54 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=37.26 spike=0.01
- DOMT.CA: score=-2.09 buy_ready=False sector_rank=11 price=23.47 support=22.85 resistance=27.23 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=27.6 liquidity=556872.75 spike=0.13
- DSCW.CA: score=6.4 buy_ready=False sector_rank=19 price=1.62 support=1.55 resistance=1.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=28.95 liquidity=10243031.0 spike=0.58
- DTPP.CA: score=2.48 buy_ready=False sector_rank=19 price=264.49 support=246.6 resistance=272.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=76610640.0 spike=1.04
- EALR.CA: score=-1.9 buy_ready=False sector_rank=19 price=304.72 support=290.17 resistance=411.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:09 PM market time freshness=DELAYED_CURRENT RSI=25.33 liquidity=1697631.63 spike=0.19
- EASB.CA: score=4.89 buy_ready=False sector_rank=19 price=6.87 support=6.04 resistance=8.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=36.5 liquidity=2492960.75 spike=0.42
- EAST.CA: score=4.37 buy_ready=False sector_rank=11 price=29.29 support=27.76 resistance=29.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=69397896.0 spike=1.51
- EBSC.CA: score=-1.21 buy_ready=False sector_rank=19 price=1.65 support=1.5 resistance=2.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=29.63 liquidity=2346419.0 spike=1.02
- ECAP.CA: score=-1.54 buy_ready=False sector_rank=19 price=28.42 support=27.5 resistance=32.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=23.9 liquidity=2058956.88 spike=0.48
- EDFM.CA: score=3.01 buy_ready=False sector_rank=19 price=385.56 support=335.2 resistance=425.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=50.14 liquidity=614457.0 spike=0.53
- EEII.CA: score=-1.02 buy_ready=False sector_rank=19 price=1.95 support=1.83 resistance=2.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=25.0 liquidity=2575266.5 spike=0.28
- EFIC.CA: score=6.59 buy_ready=False sector_rank=17 price=155.09 support=147.0 resistance=199.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=26.89 liquidity=11139200.0 spike=0.31
- EFID.CA: score=9.35 buy_ready=False sector_rank=11 price=18.68 support=18.07 resistance=31.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=32.98 liquidity=44762852.0 spike=0.93
- EFIH.CA: score=24.14 buy_ready=False sector_rank=2 price=24.34 support=20.2 resistance=25.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=53.64 liquidity=37320380.0 spike=0.55
- EGAL.CA: score=12.53 buy_ready=False sector_rank=17 price=305.4 support=306.1 resistance=376.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=16.96 liquidity=190884784.0 spike=3.47
- EGAS.CA: score=7.84 buy_ready=False sector_rank=7 price=52.94 support=48.08 resistance=60.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=36.26 liquidity=3964640.5 spike=0.35
- EGBE.CA: score=4.52 buy_ready=False sector_rank=8 price=0.5 support=0.5 resistance=0.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=45.57 liquidity=168157.52 spike=1.29
- EGCH.CA: score=6.59 buy_ready=False sector_rank=17 price=12.08 support=11.86 resistance=14.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=24.18 liquidity=42353416.0 spike=0.53
- EGSA.CA: score=9.0 buy_ready=False sector_rank=1 price=8.81 support=8.82 resistance=9.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=40.0 liquidity=7506.72 spike=1.01
- EGTS.CA: score=6.2 buy_ready=False sector_rank=15 price=14.02 support=13.56 resistance=19.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=18.84 liquidity=8549872.0 spike=0.24
- EHDR.CA: score=5.45 buy_ready=False sector_rank=19 price=2.3 support=2.1 resistance=2.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=27.03 liquidity=9052617.0 spike=0.8
- ELEC.CA: score=6.48 buy_ready=False sector_rank=18 price=1.73 support=1.65 resistance=2.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=27.78 liquidity=31961176.0 spike=0.6
- ELKA.CA: score=17.06 buy_ready=False sector_rank=19 price=1.58 support=1.38 resistance=1.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=39.06 liquidity=38896596.0 spike=3.33
- ELNA.CA: score=4.61 buy_ready=False sector_rank=19 price=35.22 support=33.46 resistance=36.4 source=Yahoo Finance as_of=2026-10-13T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=229528.75 spike=1.49
- ELSH.CA: score=7.4 buy_ready=False sector_rank=19 price=11.2 support=10.76 resistance=13.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=30.9 liquidity=19732216.0 spike=0.95
- ELWA.CA: score=6.43 buy_ready=False sector_rank=19 price=1.65 support=1.43 resistance=1.75 source=Yahoo Finance as_of=2026-10-13T21:00:00+00:00 freshness=FRESH RSI=45.45 liquidity=30036.6 spike=0.06
- EMFD.CA: score=7.65 buy_ready=False sector_rank=15 price=12.06 support=11.7 resistance=14.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=33.33 liquidity=56230072.0 spike=0.84
- ENGC.CA: score=2.34 buy_ready=False sector_rank=19 price=33.89 support=32.37 resistance=45.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=25.39 liquidity=5942263.5 spike=0.33
- EOSB.CA: score=7.4 buy_ready=False sector_rank=19 price=1.57 support=1.64 resistance=1.64 source=Yahoo Finance as_of=2026-10-13T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=157.0 spike=0.0
- EPCO.CA: score=-2.23 buy_ready=False sector_rank=19 price=8.88 support=8.0 resistance=11.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=25.56 liquidity=1367112.75 spike=0.25
- EPPK.CA: score=-7.18 buy_ready=False sector_rank=19 price=10.29 support=10.29 resistance=10.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=8 September 01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=419183.72 spike=0.28
- ETEL.CA: score=23.97 buy_ready=False sector_rank=1 price=144.77 support=128.52 resistance=156.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=58.33 liquidity=253711360.0 spike=0.95
- ETRS.CA: score=6.65 buy_ready=False sector_rank=19 price=10.5 support=9.82 resistance=11.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=47.76 liquidity=4253306.0 spike=0.4
- EXPA.CA: score=7.78 buy_ready=False sector_rank=8 price=14.53 support=14.02 resistance=22.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=9.23 liquidity=16352489.0 spike=0.43
- FAIT.CA: score=1.54 buy_ready=False sector_rank=8 price=43.53 support=38.48 resistance=47.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=32.45 liquidity=2768405.5 spike=0.93
- FAITA.CA: score=13.95 buy_ready=False sector_rank=8 price=1.0 support=0.98 resistance=1.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:08 PM market time freshness=DELAYED_CURRENT RSI=45.9 liquidity=178495.05 spike=5.47
- FERC.CA: score=-2.09 buy_ready=False sector_rank=17 price=69.85 support=66.72 resistance=82.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:10 PM market time freshness=DELAYED_CURRENT RSI=25.03 liquidity=1320708.63 spike=0.24
- FWRY.CA: score=17.14 buy_ready=False sector_rank=2 price=18.69 support=17.5 resistance=19.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=42.09 liquidity=100443576.0 spike=0.9
- GBCO.CA: score=20.98 buy_ready=False sector_rank=3 price=30.81 support=27.0 resistance=32.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=44.58 liquidity=111612360.0 spike=1.06
- GDWA.CA: score=6.4 buy_ready=False sector_rank=19 price=0.63 support=0.6 resistance=0.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=22.94 liquidity=11473337.0 spike=0.56
- GGCC.CA: score=7.4 buy_ready=False sector_rank=19 price=0.7 support=0.63 resistance=0.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=81387704.0 spike=6.55
- GIHD.CA: score=7.01 buy_ready=False sector_rank=19 price=53.36 support=53.3 resistance=78.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=22.82 liquidity=9612328.0 spike=0.5
- GMCI.CA: score=3.77 buy_ready=False sector_rank=19 price=1.54 support=1.49 resistance=1.82 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=40.38 liquidity=371923.31 spike=0.89
- GRCA.CA: score=2.35 buy_ready=False sector_rank=19 price=32.86 support=30.51 resistance=46.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=28.85 liquidity=3946251.0 spike=0.31
- GSSC.CA: score=-0.89 buy_ready=False sector_rank=19 price=269.25 support=246.0 resistance=333.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=34.66 liquidity=1712879.5 spike=0.56
- GTWL.CA: score=2.4 buy_ready=False sector_rank=19 price=130.18 support=128.0 resistance=141.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=116937664.0 spike=0.73
- HDBK.CA: score=7.78 buy_ready=False sector_rank=8 price=101.91 support=98.01 resistance=121.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=31.61 liquidity=13804522.0 spike=0.52
- HELI.CA: score=7.65 buy_ready=False sector_rank=15 price=7.32 support=6.92 resistance=8.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=30.98 liquidity=86773416.0 spike=0.83
- HRHO.CA: score=16.17 buy_ready=False sector_rank=13 price=25.7 support=22.81 resistance=27.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=58.06 liquidity=92307200.0 spike=0.7
- ICID.CA: score=12.39 buy_ready=False sector_rank=19 price=18.21 support=16.52 resistance=20.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=59.11 liquidity=4992018.0 spike=0.61
- IDRE.CA: score=0.71 buy_ready=False sector_rank=19 price=43.9 support=40.05 resistance=59.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=32.67 liquidity=3305338.25 spike=0.25
- IFAP.CA: score=3.98 buy_ready=False sector_rank=20 price=18.45 support=17.17 resistance=21.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=23.77 liquidity=7476663.5 spike=1.05
- INFI.CA: score=7.4 buy_ready=False sector_rank=19 price=127.82 support=111.25 resistance=131.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=58489532.0 spike=4.39
- IRON.CA: score=13.91 buy_ready=False sector_rank=17 price=26.42 support=25.01 resistance=32.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=44.3 liquidity=12526620.0 spike=1.16
- ISMA.CA: score=0.39 buy_ready=False sector_rank=19 price=22.19 support=18.91 resistance=31.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=28.72 liquidity=2986980.5 spike=0.39
- ISMQ.CA: score=2.06 buy_ready=False sector_rank=17 price=7.6 support=7.14 resistance=9.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=32.26 liquidity=5476057.5 spike=0.29
- ISPH.CA: score=6.6 buy_ready=False sector_rank=16 price=11.27 support=10.03 resistance=12.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=34.03 liquidity=21386430.0 spike=0.36
- JUFO.CA: score=3.07 buy_ready=False sector_rank=11 price=24.43 support=23.5 resistance=27.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=28.95 liquidity=5721522.0 spike=0.33
- KABO.CA: score=3.13 buy_ready=False sector_rank=14 price=7.55 support=7.3 resistance=9.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=34.35 liquidity=5235788.0 spike=0.21
- KWIN.CA: score=-0.23 buy_ready=False sector_rank=19 price=66.71 support=60.0 resistance=93.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=19.32 liquidity=3368653.0 spike=0.35
- KZPC.CA: score=13.45 buy_ready=False sector_rank=19 price=13.5 support=12.15 resistance=14.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=41.76 liquidity=6051946.0 spike=0.65
- LCSW.CA: score=20.49 buy_ready=False sector_rank=12 price=34.0 support=28.86 resistance=35.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=56.59 liquidity=21199210.0 spike=1.07
- LUTS.CA: score=12.4 buy_ready=False sector_rank=19 price=0.74 support=0.65 resistance=1.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=40.26 liquidity=44025628.0 spike=0.73
- MAAL.CA: score=12.4 buy_ready=False sector_rank=19 price=8.61 support=8.45 resistance=12.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=38.04 liquidity=10120768.0 spike=0.41
- MASR.CA: score=12.4 buy_ready=False sector_rank=19 price=7.47 support=6.82 resistance=7.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=44.57 liquidity=43497460.0 spike=0.76
- MBSC.CA: score=17.35 buy_ready=False sector_rank=12 price=348.0 support=288.0 resistance=414.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=49.92 liquidity=44550904.0 spike=0.52
- MCQE.CA: score=12.35 buy_ready=False sector_rank=12 price=173.88 support=170.0 resistance=228.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=39.19 liquidity=47026564.0 spike=0.86
- MCRO.CA: score=7.4 buy_ready=False sector_rank=19 price=1.39 support=1.25 resistance=1.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=28.57 liquidity=42338176.0 spike=0.72
- MENA.CA: score=0.51 buy_ready=False sector_rank=15 price=5.88 support=5.57 resistance=7.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=34.83 liquidity=2198289.25 spike=1.33
- MEPA.CA: score=5.65 buy_ready=False sector_rank=19 price=1.63 support=1.53 resistance=2.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=36.36 liquidity=4253281.0 spike=0.43
- MFPC.CA: score=15.59 buy_ready=False sector_rank=17 price=43.86 support=42.0 resistance=51.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=36.16 liquidity=23258544.0 spike=0.26
- MFSC.CA: score=-3.29 buy_ready=False sector_rank=19 price=38.29 support=36.25 resistance=49.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=17.38 liquidity=314043.44 spike=0.13
- MHOT.CA: score=0.57 buy_ready=False sector_rank=10 price=15.74 support=15.08 resistance=19.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=33.08 liquidity=3142329.75 spike=0.18
- MICH.CA: score=4.72 buy_ready=False sector_rank=19 price=41.34 support=38.91 resistance=47.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=44.71 liquidity=2322667.0 spike=0.26
- MILS.CA: score=1.46 buy_ready=False sector_rank=19 price=154.16 support=147.06 resistance=207.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=26.66 liquidity=4062032.0 spike=0.51
- MIPH.CA: score=3.59 buy_ready=False sector_rank=16 price=793.49 support=666.66 resistance=1000.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:55 PM market time freshness=DELAYED_CURRENT RSI=40.54 liquidity=994122.13 spike=0.12
- MOED.CA: score=2.57 buy_ready=False sector_rank=19 price=0.61 support=0.57 resistance=0.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=31.09 liquidity=6174463.0 spike=0.34
- MOIL.CA: score=-1.11 buy_ready=False sector_rank=7 price=0.68 support=0.63 resistance=0.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=34.67 liquidity=11351.9 spike=0.04
- MOIN.CA: score=4.0 buy_ready=False sector_rank=19 price=31.96 support=31.0 resistance=38.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=34.61 liquidity=6597182.0 spike=0.63
- MOSC.CA: score=6.74 buy_ready=False sector_rank=19 price=265.41 support=231.0 resistance=329.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=38.82 liquidity=4135558.75 spike=1.1
- MPCI.CA: score=7.4 buy_ready=False sector_rank=19 price=317.03 support=294.2 resistance=455.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=27.56 liquidity=80594432.0 spike=0.78
- MPCO.CA: score=7.4 buy_ready=False sector_rank=20 price=2.07 support=2.0 resistance=3.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=20.24 liquidity=51872728.0 spike=0.39
- MPRC.CA: score=8.2 buy_ready=False sector_rank=19 price=35.97 support=34.53 resistance=41.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=39.67 liquidity=5795858.0 spike=0.36
- MTIE.CA: score=14.86 buy_ready=False sector_rank=3 price=7.66 support=7.27 resistance=8.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=40.7 liquidity=11831645.0 spike=0.64
- NAHO.CA: score=2.42 buy_ready=False sector_rank=19 price=0.13 support=0.12 resistance=0.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=61.9 liquidity=20303.49 spike=0.69
- NCCW.CA: score=7.4 buy_ready=False sector_rank=19 price=5.86 support=5.3 resistance=8.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=27.82 liquidity=19721786.0 spike=0.46
- NEDA.CA: score=-2.55 buy_ready=False sector_rank=19 price=2.6 support=2.47 resistance=2.8 source=Yahoo Finance as_of=2026-10-13T21:00:00+00:00 freshness=FRESH RSI=27.27 liquidity=51441.0 spike=0.08
- NHPS.CA: score=4.48 buy_ready=False sector_rank=19 price=65.45 support=63.02 resistance=86.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=26.15 liquidity=8084944.0 spike=0.56
- NINH.CA: score=7.46 buy_ready=False sector_rank=19 price=16.56 support=16.02 resistance=23.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=21.33 liquidity=14817810.0 spike=1.03
- NIPH.CA: score=7.6 buy_ready=False sector_rank=16 price=274.25 support=241.0 resistance=368.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=28.57 liquidity=51737920.0 spike=0.41
- OBRI.CA: score=13.56 buy_ready=False sector_rank=19 price=27.05 support=22.8 resistance=33.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=40.7 liquidity=15008598.0 spike=1.08
- OCDI.CA: score=7.65 buy_ready=False sector_rank=15 price=25.9 support=24.2 resistance=30.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=32.64 liquidity=37135788.0 spike=0.86
- OCPH.CA: score=-0.47 buy_ready=False sector_rank=19 price=197.38 support=190.0 resistance=251.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=34.19 liquidity=3126042.25 spike=0.88
- ODIN.CA: score=1.82 buy_ready=False sector_rank=19 price=2.25 support=2.11 resistance=3.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=27.93 liquidity=4418597.0 spike=0.51
- OFH.CA: score=7.4 buy_ready=False sector_rank=19 price=0.8 support=0.76 resistance=1.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=25.96 liquidity=10930923.0 spike=0.11
- OIH.CA: score=8.72 buy_ready=False sector_rank=9 price=1.79 support=1.7 resistance=2.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=23.53 liquidity=10729586.0 spike=0.12
- OLFI.CA: score=0.12 buy_ready=False sector_rank=11 price=20.77 support=19.8 resistance=23.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=24.12 liquidity=2763773.0 spike=0.15
- ORAS.CA: score=4.6 buy_ready=False sector_rank=4 price=897.37 support=886.0 resistance=914.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=171445216.0 spike=1.0
- ORHD.CA: score=6.65 buy_ready=False sector_rank=15 price=10.72 support=10.01 resistance=44.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=3.34 liquidity=80497784.0 spike=0.52
- ORWE.CA: score=19.0 buy_ready=False sector_rank=14 price=27.77 support=26.01 resistance=28.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=46.81 liquidity=61073612.0 spike=1.55
- PHAR.CA: score=12.6 buy_ready=False sector_rank=16 price=108.41 support=102.0 resistance=124.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=40.86 liquidity=21218842.0 spike=0.3
- PHDC.CA: score=9.83 buy_ready=False sector_rank=15 price=12.79 support=12.35 resistance=13.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=34.5 liquidity=102636120.0 spike=1.09
- PHTV.CA: score=2.87 buy_ready=False sector_rank=19 price=338.3 support=315.0 resistance=378.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=48.45 liquidity=474194.09 spike=0.48
- POUL.CA: score=7.35 buy_ready=False sector_rank=11 price=9.94 support=9.12 resistance=40.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=2.43 liquidity=28093590.0 spike=0.83
- PRCL.CA: score=-0.17 buy_ready=False sector_rank=12 price=22.43 support=21.0 resistance=33.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=26.9 liquidity=2477580.0 spike=0.22
- PRDC.CA: score=12.65 buy_ready=False sector_rank=15 price=6.48 support=6.07 resistance=8.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=37.71 liquidity=24112362.0 spike=0.67
- PRMH.CA: score=-0.78 buy_ready=False sector_rank=19 price=2.03 support=1.8 resistance=2.82 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=25.22 liquidity=2817062.0 spike=0.71
- RACC.CA: score=9.29 buy_ready=False sector_rank=19 price=9.09 support=8.51 resistance=10.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=39.34 liquidity=7512921.5 spike=1.19
- RAKT.CA: score=3.52 buy_ready=False sector_rank=19 price=22.06 support=20.26 resistance=25.08 source=Yahoo Finance as_of=2026-10-13T21:00:00+00:00 freshness=FRESH RSI=49.81 liquidity=120822.62 spike=0.35
- RAYA.CA: score=6.4 buy_ready=False sector_rank=21 price=5.97 support=5.7 resistance=7.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=28.03 liquidity=15923180.0 spike=0.43
- RMDA.CA: score=7.6 buy_ready=False sector_rank=16 price=5.14 support=4.83 resistance=6.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=27.59 liquidity=15250746.0 spike=0.57
- ROTO.CA: score=5.46 buy_ready=False sector_rank=19 price=37.63 support=35.56 resistance=42.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=37.96 liquidity=3056780.25 spike=0.35
- RREI.CA: score=2.35 buy_ready=False sector_rank=19 price=3.6 support=3.29 resistance=4.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=34.76 liquidity=4950947.0 spike=0.53
- RTVC.CA: score=-2.51 buy_ready=False sector_rank=19 price=3.43 support=3.31 resistance=4.06 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=31.07 liquidity=1087485.0 spike=0.4
- RUBX.CA: score=17.4 buy_ready=False sector_rank=19 price=16.49 support=12.9 resistance=19.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=48.47 liquidity=32096746.0 spike=0.31
- SAUD.CA: score=11.68 buy_ready=False sector_rank=8 price=22.0 support=20.2 resistance=26.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=32.01 liquidity=46421036.0 spike=2.45
- SCEM.CA: score=17.35 buy_ready=False sector_rank=12 price=89.99 support=74.55 resistance=96.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=53.53 liquidity=60807552.0 spike=0.96
- SCFM.CA: score=-2.96 buy_ready=False sector_rank=19 price=232.8 support=220.35 resistance=280.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=31.34 liquidity=637075.69 spike=0.35
- SCTS.CA: score=-0.44 buy_ready=False sector_rank=6 price=489.21 support=463.13 resistance=616.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:10 PM market time freshness=DELAYED_CURRENT RSI=20.97 liquidity=310174.38 spike=0.31
- SDTI.CA: score=15.4 buy_ready=False sector_rank=19 price=86.0 support=73.02 resistance=94.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=66.01 liquidity=19952600.0 spike=0.6
- SEIG.CA: score=-2.7 buy_ready=False sector_rank=19 price=192.4 support=173.1 resistance=267.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=33.48 liquidity=896071.81 spike=0.4
- SIPC.CA: score=3.7 buy_ready=False sector_rank=19 price=5.65 support=5.61 resistance=6.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=85325864.0 spike=1.65
- SKPC.CA: score=6.59 buy_ready=False sector_rank=17 price=15.28 support=14.98 resistance=18.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=22.06 liquidity=38644068.0 spike=0.47
- SMFR.CA: score=3.59 buy_ready=False sector_rank=19 price=199.05 support=181.6 resistance=255.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:09 PM market time freshness=DELAYED_CURRENT RSI=35.69 liquidity=2191264.0 spike=0.61
- SNFC.CA: score=14.07 buy_ready=False sector_rank=19 price=11.26 support=10.81 resistance=11.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=40.51 liquidity=8672306.0 spike=0.77
- SPIN.CA: score=2.45 buy_ready=False sector_rank=14 price=14.98 support=14.94 resistance=18.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=28.13 liquidity=4553044.0 spike=0.83
- SPMD.CA: score=2.4 buy_ready=False sector_rank=19 price=0.37 support=0.34 resistance=0.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=38412176.0 spike=1.0
- SUGR.CA: score=5.15 buy_ready=False sector_rank=11 price=58.12 support=54.6 resistance=58.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=19556738.0 spike=1.9
- SVCE.CA: score=7.4 buy_ready=False sector_rank=19 price=9.38 support=8.81 resistance=12.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=30.27 liquidity=38381860.0 spike=0.46
- SWDY.CA: score=12.48 buy_ready=False sector_rank=18 price=113.2 support=102.31 resistance=128.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=39.13 liquidity=27870438.0 spike=0.46
- TALM.CA: score=17.88 buy_ready=False sector_rank=6 price=21.05 support=18.71 resistance=23.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=52.86 liquidity=8633895.0 spike=0.2
- TMGH.CA: score=6.65 buy_ready=False sector_rank=15 price=84.49 support=81.22 resistance=96.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=15.12 liquidity=209270656.0 spike=0.93
- TRTO.CA: score=4.4 buy_ready=False sector_rank=19 price=0.07 support=0.05 resistance=0.07 source=Yahoo Finance as_of=2026-10-13T21:00:00+00:00 freshness=FRESH RSI=88.24 liquidity=4962.82 spike=0.51
- UEFM.CA: score=4.25 buy_ready=False sector_rank=19 price=479.55 support=407.57 resistance=550.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=49.89 liquidity=845432.44 spike=0.27
- UEGC.CA: score=7.4 buy_ready=False sector_rank=19 price=1.67 support=1.5 resistance=1.71 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=224034928.0 spike=6.59
- UNIP.CA: score=7.66 buy_ready=False sector_rank=19 price=0.33 support=0.31 resistance=0.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=34.0 liquidity=11019505.0 spike=1.13
- UNIT.CA: score=6.2 buy_ready=False sector_rank=15 price=16.98 support=16.15 resistance=20.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=38.75 liquidity=3544556.75 spike=0.53
- WCDF.CA: score=-0.84 buy_ready=False sector_rank=19 price=539.15 support=515.0 resistance=720.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=21.47 liquidity=1755129.38 spike=0.53
- WKOL.CA: score=-1.29 buy_ready=False sector_rank=19 price=276.7 support=266.18 resistance=379.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=27.19 liquidity=2311162.25 spike=0.21
- ZEOT.CA: score=17.4 buy_ready=False sector_rank=19 price=11.34 support=9.75 resistance=14.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=39.3 liquidity=39677248.0 spike=6.34
- ZMID.CA: score=7.65 buy_ready=False sector_rank=15 price=7.19 support=6.83 resistance=9.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=18.48 liquidity=92290968.0 spike=0.91

## Backtesting Lite
- EFIH.CA: 180d return=22.52%, max drawdown=-22.68%, MA20>MA50 days last20=6, as_of=2026-10-13T21:00:00+00:00
- ETEL.CA: 180d return=115.84%, max drawdown=-30.44%, MA20>MA50 days last20=20, as_of=2026-10-13T21:00:00+00:00
- ACAMD.CA: 180d return=27.97%, max drawdown=-26.43%, MA20>MA50 days last20=0, as_of=2026-10-13T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- EFIH.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=E-Finance For Digital and Financial Investments summary=Evidence rejected for EFIH.CA: source text did not clearly match EFIH.CA / E-Finance For Digital and Financial Investments.
- ETEL.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Telecom Egypt summary=Evidence rejected for ETEL.CA: source text did not clearly match ETEL.CA / Telecom Egypt.
- ACAMD.CA: status=OLD_ACCEPTED latest=2020-01-01 age_days=2479 sources=3 expected=Arab Co.,for asset management and development summary=Arab Company for Asset Management shifts to EGP 7m net profits in 9M-25; Arab Co. for Asset Management approves offer to sell land in El-Minya; Arab Co. Asset Management swings to loss in 2020
  - Arab Company for Asset Management shifts to EGP 7m net profits in 9M-25: https://english.mubasher.info/news/4543171/Arab-Company-for-Asset-Management-shifts-to-EGP-7m-net-profits-in-9M-25/
  - Arab Co. for Asset Management approves offer to sell land in El-Minya: https://english.mubasher.info/news/3777445/Arab-Co-for-Asset-Management-approves-offer-to-sell-land-in-El-Minya/
  - Arab Co. Asset Management swings to loss in 2020: https://english.mubasher.info/news/3767136/Arab-Co-Asset-Management-swings-to-loss-in-2020/
- GBCO.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=GB Corp summary=Evidence rejected for GBCO.CA: source text did not clearly match GBCO.CA / GB Corp.
- LCSW.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Lecico Egypt summary=Evidence rejected for LCSW.CA: source text did not clearly match LCSW.CA / Lecico Egypt.
- ARAB.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Arab Developers Holding summary=Arab Developers Holding unveils EGP 1bn expansion plans to improve financial efficiency; FRA gives initial approval for Arab Developers’ rights issue; Arab Developers stock stabilizes after correction
  - Arab Developers Holding unveils EGP 1bn expansion plans to improve financial efficiency: https://english.mubasher.info/news/4601724/Arab-Developers-Holding-unveils-EGP-1bn-expansion-plans-to-improve-financial-efficiency/
  - FRA gives initial approval for Arab Developers’ rights issue: https://english.mubasher.info/news/4582627/FRA-gives-initial-approval-for-Arab-Developers-rights-issue/
  - Arab Developers stock stabilizes after correction: https://english.mubasher.info/news/4564643/Arab-Developers-stock-stabilizes-after-correction/
- ORWE.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=652 sources=3 expected=Oriental Weavers summary=Oriental Weavers to disburse EGP 1.5/shr dividends for 2025; Oriental Weavers’ consolidated profits cross EGP 2.2bn in 2025; Oriental Weavers generates EGP 12.5bn consolidated sales in H1-25
  - Oriental Weavers to disburse EGP 1.5/shr dividends for 2025: https://english.mubasher.info/news/4590236/Oriental-Weavers-to-disburse-EGP-1-5-shr-dividends-for-2025/
  - Oriental Weavers’ consolidated profits cross EGP 2.2bn in 2025: https://english.mubasher.info/news/4562972/Oriental-Weavers-consolidated-profits-cross-EGP-2-2bn-in-2025/
  - Oriental Weavers generates EGP 12.5bn consolidated sales in H1-25: https://english.mubasher.info/news/4487417/Oriental-Weavers-generates-EGP-12-5bn-consolidated-sales-in-H1-25/
- TALM.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Talim Management Services summary=Evidence rejected for TALM.CA: source text did not clearly match TALM.CA / Talim Management Services.

## Warnings
- Evidence rejected for EFIH.CA: source text did not clearly match EFIH.CA / E-Finance For Digital and Financial Investments.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence rejected for ETEL.CA: source text did not clearly match ETEL.CA / Telecom Egypt.
- Evidence for ACAMD.CA matches the company but appears old; latest detected date is 2020-01-01.
- Evidence rejected for GBCO.CA: source text did not clearly match GBCO.CA / GB Corp.
- Evidence rejected for LCSW.CA: source text did not clearly match LCSW.CA / Lecico Egypt.
- Evidence for ARAB.CA matches the company but no source/report date was detected.
- Evidence for ORWE.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for TALM.CA: source text did not clearly match TALM.CA / Talim Management Services.
