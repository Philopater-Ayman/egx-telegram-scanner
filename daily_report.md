# Telegram-First EGX Scanner Report

Scan phase: Pre-market risk check
Generated UTC: 2026-10-14T10:39:08.544560+00:00
Generated Cairo: 2026-10-14 13:39
Run timing: target 08:45 Cairo | generated Cairo 2026-10-14 13:39 | cron 45 5 * * 0-4
Trigger: scheduled cron=45 5 * * 0-4 mapped to pre_market; Cairo now 2026-10-14 13:34

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 4
- Tradeable price/liquidity tickers: 173/186
- Top sector: Telecommunications

## Market Context
- Market trend: Bullish
- Source: Mubasher EGX market page (delayed public data)
- As of: Wednesday, October 14
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 15.79% / above MA50 26.32%
- EGX70 regime: BEARISH / above MA20 10.81% / above MA50 13.51%
- Sector breadth: 0.0%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- COMI.CA: liquidity=508460416.0 spike=0.95 score=7.25
- ORAS.CA: liquidity=362999520.0 spike=1.0 score=5.6
- CCAP.CA: liquidity=247553088.0 spike=0.39 score=11.79
- ETEL.CA: liquidity=183686592.0 spike=0.68 score=24.4
- TMGH.CA: liquidity=110083480.0 spike=0.49 score=6.4

## AI Narrative
- Provider: OpenRouter OK
- Model: nvidia/nemotron-3-super-120b-a12b:free
- Summary: EGX30 and EGX70 remain bearish with weak breadth, putting the market in a defensive risk mode that blocks new buys; the scanner flags a handful of stocks with bullish‑watch or constructive outlooks and tradeable liquidity, but notes cooling liquidity and sector‑leadership gaps add uncertainty for the next 1‑3 days.
- ETEL.CA (Telecom) – bullish watch outlook 88.9, liquidity tradeable, 7.7% below 20‑day resistance, RSI 61.5; sector leading but liquidity is cooling, introducing uncertainty.
- EFIH.CA (Fintech & Payments) – bullish watch outlook 82.8, support 17.8% below, resistance 6.6% above, RSI 54.4; sector rank 2, liquidity cooling suggests caution.
- ARAB.CA (Real Estate) – constructive outlook 55, far above support (35%), tight resistance 3.7% away, RSI 61.7; sector not leading, liquidity cooling adds downside risk.
- ORWE.CA (Textiles) – neutral outlook 49, high liquidity spike 0.75, RSI 37.2 (oversold), sector not leading; liquidity cooling and weak sector bias create mixed signals.

## Top Liquidity Spikes
- MOSC.CA: spike=3.14 liquidity=10246499.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- ZEOT.CA: spike=2.45 liquidity=13793515.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- MTIE.CA: spike=2.37 liquidity=40275080.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- CFGH.CA: spike=2.1 liquidity=12242.47 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- EGSA.CA: spike=2.05 liquidity=14868.3 outlook=NEUTRAL score=38.93 buy_ready=False

## Sector Leaderboard
- #1 Telecommunications: score=8.93 5d=-1.39% 20d=7.18% aboveMA50=100.0%
- #2 Fintech & Payments: score=2.81 5d=-1.84% 20d=0.58% aboveMA50=50.0%
- #3 Industrial Goods & Construction: score=1.5 5d=0.0% 20d=0.0% aboveMA50=0.0%
- #4 Automotive & Distribution: score=1.1 5d=-3.26% 20d=1.34% aboveMA50=0.0%
- #5 Energy & Petrochemicals: score=-0.24 5d=-3.74% 20d=0.0% aboveMA50=33.33%
- #6 Transportation & Logistics: score=-0.24 5d=-5.39% 20d=-0.61% aboveMA50=50.0%
- #7 Education: score=-0.27 5d=-3.51% 20d=-6.79% aboveMA50=33.33%
- #8 Investment Holding: score=-0.52 5d=-5.29% 20d=-8.61% aboveMA50=66.67%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- ETEL.CA: BULLISH_WATCH score=88.93 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- EFIH.CA: BULLISH_WATCH score=82.81 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- TALM.CA: BULLISH_WATCH score=70 liquidity=TRADEABLE sector=NEUTRAL risk=liquidity is cooling
- SDTI.CA: CONSTRUCTIVE score=65 liquidity=TRADEABLE sector=LAGGING risk=liquidity is cooling; sector is not leading
- AMOC.CA: CONSTRUCTIVE score=58 liquidity=TRADEABLE sector=NEUTRAL risk=liquidity is cooling; below MA20
- ICID.CA: CONSTRUCTIVE score=58 liquidity=TRADEABLE sector=LAGGING risk=below MA20; sector is not leading
- ALCN.CA: CONSTRUCTIVE score=58 liquidity=TRADEABLE sector=NEUTRAL risk=liquidity is cooling; below MA20
- BINV.CA: CONSTRUCTIVE score=57 liquidity=TRADEABLE sector=LAGGING risk=liquidity is cooling; momentum is extended; sector is not leading
- ARAB.CA: CONSTRUCTIVE score=55 liquidity=TRADEABLE sector=LAGGING risk=liquidity is cooling; far above support; sector is not leading
- RUBX.CA: CONSTRUCTIVE score=55 liquidity=TRADEABLE sector=LAGGING risk=liquidity is cooling; far above support; sector is not leading; high short-term volatility

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- EKHO.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ARVA.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- MICH.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=-0.73 buy_ready=False sector_rank=19 price=234.81 support=225.0 resistance=359.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=23.05 liquidity=1865782.38 spike=0.09
- ABUK.CA: score=10.4 buy_ready=False sector_rank=13 price=85.24 support=83.0 resistance=96.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=31.06 liquidity=25803118.0 spike=0.28
- ACAMD.CA: score=14.72 buy_ready=False sector_rank=19 price=2.02 support=1.87 resistance=2.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=45.45 liquidity=49564812.0 spike=1.16
- ACGC.CA: score=5.37 buy_ready=False sector_rank=17 price=13.28 support=12.81 resistance=14.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:19 PM market time freshness=DELAYED_CURRENT RSI=37.41 liquidity=2974181.5 spike=0.17
- ADCI.CA: score=3.65 buy_ready=False sector_rank=19 price=260.97 support=250.06 resistance=288.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:18 PM market time freshness=DELAYED_CURRENT RSI=38.41 liquidity=1248982.0 spike=0.58
- ADIB.CA: score=8.29 buy_ready=False sector_rank=9 price=46.65 support=43.5 resistance=54.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=15.58 liquidity=78101952.0 spike=1.02
- ADPC.CA: score=-0.0 buy_ready=False sector_rank=19 price=3.16 support=3.01 resistance=4.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:18 PM market time freshness=DELAYED_CURRENT RSI=15.32 liquidity=3595541.0 spike=0.23
- AFDI.CA: score=0.74 buy_ready=False sector_rank=19 price=49.48 support=46.12 resistance=56.82 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:10 PM market time freshness=DELAYED_CURRENT RSI=34.49 liquidity=1343544.63 spike=0.2
- AFMC.CA: score=3.45 buy_ready=False sector_rank=19 price=134.93 support=122.0 resistance=179.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=34.45 liquidity=6045259.5 spike=0.29
- AJWA.CA: score=3.3 buy_ready=False sector_rank=19 price=220.17 support=210.01 resistance=222.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=37820380.0 spike=1.45
- ALCN.CA: score=11.98 buy_ready=False sector_rank=6 price=33.0 support=30.4 resistance=36.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:18 PM market time freshness=DELAYED_CURRENT RSI=45.53 liquidity=5075874.0 spike=0.15
- ALUM.CA: score=-1.75 buy_ready=False sector_rank=19 price=21.12 support=20.52 resistance=27.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=23.54 liquidity=1854048.75 spike=0.39
- AMER.CA: score=14.4 buy_ready=False sector_rank=16 price=4.8 support=4.05 resistance=5.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=38.92 liquidity=31837136.0 spike=0.57
- AMES.CA: score=8.4 buy_ready=False sector_rank=19 price=39.92 support=38.02 resistance=59.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=28.79 liquidity=34782152.0 spike=0.35
- AMIA.CA: score=8.16 buy_ready=False sector_rank=19 price=18.42 support=17.12 resistance=19.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:16 PM market time freshness=DELAYED_CURRENT RSI=47.66 liquidity=2760805.75 spike=0.15
- AMOC.CA: score=16.9 buy_ready=False sector_rank=5 price=13.57 support=12.18 resistance=14.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=41765776.0 spike=0.33
- APSW.CA: score=2.06 buy_ready=False sector_rank=19 price=7.91 support=7.81 resistance=8.92 source=Yahoo Finance as_of=2026-10-12T21:00:00+00:00 freshness=FRESH RSI=42.21 liquidity=659891.74 spike=0.96
- ARAB.CA: score=19.4 buy_ready=False sector_rank=16 price=0.27 support=0.2 resistance=0.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=61.67 liquidity=40299864.0 spike=0.41
- ARCC.CA: score=12.86 buy_ready=False sector_rank=12 price=67.47 support=60.01 resistance=74.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=42.62 liquidity=13841016.0 spike=0.44
- AREH.CA: score=-0.66 buy_ready=False sector_rank=19 price=1.18 support=1.11 resistance=1.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:18 PM market time freshness=DELAYED_CURRENT RSI=26.92 liquidity=2939697.25 spike=0.35
- ASCM.CA: score=-0.0 buy_ready=False sector_rank=19 price=50.18 support=48.0 resistance=61.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=24.83 liquidity=3598487.25 spike=0.4
- ASPI.CA: score=4.43 buy_ready=False sector_rank=19 price=0.33 support=0.31 resistance=0.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=22.8 liquidity=8027314.0 spike=0.23
- ATLC.CA: score=-2.89 buy_ready=False sector_rank=10 price=5.69 support=5.38 resistance=5.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:19 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=3916394.75 spike=0.38
- ATQA.CA: score=7.4 buy_ready=False sector_rank=13 price=11.68 support=10.61 resistance=13.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:19 PM market time freshness=DELAYED_CURRENT RSI=27.11 liquidity=37164648.0 spike=0.51
- AXPH.CA: score=0.14 buy_ready=False sector_rank=19 price=1382.47 support=1300.0 resistance=1987.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=18.49 liquidity=2741115.5 spike=0.39
- BINV.CA: score=10.38 buy_ready=False sector_rank=8 price=59.19 support=49.91 resistance=72.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:19 PM market time freshness=DELAYED_CURRENT RSI=62.17 liquidity=1591376.63 spike=0.06
- BIOC.CA: score=16.4 buy_ready=False sector_rank=19 price=302.66 support=225.21 resistance=380.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=56.45 liquidity=61991336.0 spike=0.61
- BTFH.CA: score=7.2 buy_ready=False sector_rank=10 price=2.7 support=2.55 resistance=3.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:19 PM market time freshness=DELAYED_CURRENT RSI=32.86 liquidity=59247140.0 spike=0.6
- CAED.CA: score=4.61 buy_ready=False sector_rank=19 price=107.65 support=95.0 resistance=145.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=33.02 liquidity=7207051.5 spike=0.73
- CANA.CA: score=16.25 buy_ready=False sector_rank=9 price=43.98 support=41.35 resistance=52.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:17 PM market time freshness=DELAYED_CURRENT RSI=42.05 liquidity=12862071.0 spike=0.54
- CCAP.CA: score=11.79 buy_ready=False sector_rank=8 price=6.25 support=6.07 resistance=7.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=24.04 liquidity=247553088.0 spike=0.39
- CCRS.CA: score=0.19 buy_ready=False sector_rank=19 price=2.1 support=1.87 resistance=2.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:18 PM market time freshness=DELAYED_CURRENT RSI=18.18 liquidity=2794288.25 spike=0.21
- CEFM.CA: score=-1.32 buy_ready=False sector_rank=19 price=126.05 support=113.0 resistance=152.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:19 PM market time freshness=DELAYED_CURRENT RSI=30.95 liquidity=1275182.63 spike=0.46
- CERA.CA: score=2.4 buy_ready=False sector_rank=19 price=1.3 support=1.23 resistance=1.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=99571320.0 spike=0.81
- CFGH.CA: score=-1.39 buy_ready=False sector_rank=19 price=0.1 support=0.1 resistance=0.12 source=Yahoo Finance as_of=2026-10-12T21:00:00+00:00 freshness=FRESH RSI=0.0 liquidity=12242.47 spike=2.1
- CICH.CA: score=0.76 buy_ready=False sector_rank=10 price=11.0 support=10.6 resistance=13.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:19 PM market time freshness=DELAYED_CURRENT RSI=25.38 liquidity=2568411.75 spike=0.77
- CIEB.CA: score=8.93 buy_ready=False sector_rank=9 price=23.08 support=22.56 resistance=25.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:18 PM market time freshness=DELAYED_CURRENT RSI=26.5 liquidity=12589555.0 spike=1.34
- CIRA.CA: score=7.42 buy_ready=False sector_rank=7 price=37.53 support=35.51 resistance=41.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=26.28 liquidity=8528199.0 spike=0.33
- CLHO.CA: score=6.66 buy_ready=False sector_rank=15 price=14.02 support=13.9 resistance=16.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:19 PM market time freshness=DELAYED_CURRENT RSI=27.06 liquidity=41933932.0 spike=1.13
- CNFN.CA: score=0.86 buy_ready=False sector_rank=10 price=4.01 support=3.8 resistance=4.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:11 PM market time freshness=DELAYED_CURRENT RSI=30.72 liquidity=3661354.75 spike=0.42
- COMI.CA: score=7.25 buy_ready=False sector_rank=9 price=122.45 support=120.0 resistance=134.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:19 PM market time freshness=DELAYED_CURRENT RSI=13.94 liquidity=508460416.0 spike=0.95
- COPR.CA: score=12.4 buy_ready=False sector_rank=19 price=0.47 support=0.44 resistance=0.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=40.43 liquidity=10708363.0 spike=0.44
- COSG.CA: score=6.4 buy_ready=False sector_rank=19 price=1.44 support=1.34 resistance=1.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=20.63 liquidity=12003327.0 spike=0.8
- CPCI.CA: score=10.73 buy_ready=False sector_rank=19 price=607.98 support=530.0 resistance=619.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=70.44 liquidity=3333280.25 spike=0.83
- CSAG.CA: score=3.41 buy_ready=False sector_rank=6 price=36.38 support=34.06 resistance=39.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:18 PM market time freshness=DELAYED_CURRENT RSI=32.98 liquidity=4505696.5 spike=0.57
- DAPH.CA: score=7.4 buy_ready=False sector_rank=19 price=97.46 support=89.1 resistance=129.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=33.81 liquidity=17811628.0 spike=0.44
- DEIN.CA: score=5.4 buy_ready=False sector_rank=19 price=10.35 support=10.35 resistance=12.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 09:54 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=37.26 spike=0.01
- DOMT.CA: score=-2.89 buy_ready=False sector_rank=14 price=23.24 support=22.85 resistance=28.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:16 PM market time freshness=DELAYED_CURRENT RSI=25.45 liquidity=710739.0 spike=0.14
- DSCW.CA: score=5.87 buy_ready=False sector_rank=19 price=1.61 support=1.55 resistance=1.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=20.0 liquidity=9466725.0 spike=0.53
- DTPP.CA: score=7.4 buy_ready=False sector_rank=19 price=262.7 support=250.0 resistance=379.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:19 PM market time freshness=DELAYED_CURRENT RSI=26.8 liquidity=12558567.0 spike=0.17
- EALR.CA: score=-1.64 buy_ready=False sector_rank=19 price=312.93 support=290.17 resistance=411.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:11 PM market time freshness=DELAYED_CURRENT RSI=23.48 liquidity=1957618.63 spike=0.21
- EASB.CA: score=4.09 buy_ready=False sector_rank=19 price=6.99 support=6.04 resistance=8.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=38.21 liquidity=1691954.63 spike=0.25
- EAST.CA: score=6.4 buy_ready=False sector_rank=14 price=27.59 support=27.01 resistance=34.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=18.31 liquidity=16048372.0 spike=0.34
- EBSC.CA: score=-2.65 buy_ready=False sector_rank=19 price=1.63 support=1.5 resistance=2.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=24.05 liquidity=948064.19 spike=0.4
- ECAP.CA: score=-2.65 buy_ready=False sector_rank=19 price=28.69 support=27.5 resistance=32.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:12 PM market time freshness=DELAYED_CURRENT RSI=18.18 liquidity=954707.63 spike=0.22
- EDFM.CA: score=2.92 buy_ready=False sector_rank=19 price=394.37 support=335.2 resistance=425.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:18 PM market time freshness=DELAYED_CURRENT RSI=44.63 liquidity=523154.84 spike=0.46
- EEII.CA: score=0.85 buy_ready=False sector_rank=19 price=1.94 support=1.83 resistance=2.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=28.17 liquidity=4446099.0 spike=0.49
- EFIC.CA: score=4.68 buy_ready=False sector_rank=13 price=154.24 support=147.0 resistance=203.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:19 PM market time freshness=DELAYED_CURRENT RSI=22.24 liquidity=8276479.0 spike=0.21
- EFID.CA: score=8.4 buy_ready=False sector_rank=14 price=18.51 support=18.07 resistance=31.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=26.74 liquidity=25875800.0 spike=0.51
- EFIH.CA: score=24.12 buy_ready=False sector_rank=2 price=23.79 support=20.2 resistance=25.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:19 PM market time freshness=DELAYED_CURRENT RSI=54.41 liquidity=17976078.0 spike=0.26
- EGAL.CA: score=7.4 buy_ready=False sector_rank=13 price=319.2 support=306.1 resistance=376.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=14.6 liquidity=25652010.0 spike=0.47
- EGAS.CA: score=0.8 buy_ready=False sector_rank=5 price=51.96 support=48.08 resistance=60.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=31.41 liquidity=1895046.5 spike=0.17
- EGBE.CA: score=3.8 buy_ready=False sector_rank=9 price=0.52 support=0.49 resistance=0.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:17 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=150153.44 spike=1.2
- EGCH.CA: score=6.4 buy_ready=False sector_rank=13 price=12.18 support=11.86 resistance=14.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=21.23 liquidity=44590824.0 spike=0.55
- EGSA.CA: score=11.51 buy_ready=False sector_rank=1 price=8.95 support=8.82 resistance=9.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:15 PM market time freshness=DELAYED_CURRENT RSI=11.76 liquidity=14868.3 spike=2.05
- EGTS.CA: score=7.4 buy_ready=False sector_rank=16 price=14.3 support=13.56 resistance=19.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=14.74 liquidity=20873694.0 spike=0.6
- EHDR.CA: score=3.56 buy_ready=False sector_rank=19 price=2.31 support=2.1 resistance=2.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=24.36 liquidity=7157119.5 spike=0.61
- ELEC.CA: score=6.4 buy_ready=False sector_rank=18 price=1.71 support=1.65 resistance=2.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=23.08 liquidity=12150104.0 spike=0.22
- ELKA.CA: score=2.59 buy_ready=False sector_rank=19 price=1.51 support=1.38 resistance=1.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=32.79 liquidity=6185384.0 spike=0.51
- ELNA.CA: score=3.55 buy_ready=False sector_rank=19 price=35.22 support=33.46 resistance=36.4 source=Yahoo Finance as_of=2026-10-12T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=145599.49 spike=0.93
- ELSH.CA: score=7.56 buy_ready=False sector_rank=19 price=11.09 support=10.76 resistance=13.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=28.97 liquidity=21536858.0 spike=1.08
- ELWA.CA: score=6.52 buy_ready=False sector_rank=19 price=1.65 support=1.43 resistance=1.78 source=Yahoo Finance as_of=2026-10-12T21:00:00+00:00 freshness=FRESH RSI=45.45 liquidity=118291.8 spike=0.2
- EMFD.CA: score=7.4 buy_ready=False sector_rank=16 price=11.98 support=11.7 resistance=14.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=32.87 liquidity=13856785.0 spike=0.21
- ENGC.CA: score=2.29 buy_ready=False sector_rank=19 price=34.0 support=32.37 resistance=45.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=24.35 liquidity=5886498.0 spike=0.32
- EOSB.CA: score=7.42 buy_ready=False sector_rank=19 price=1.57 support=1.64 resistance=1.64 source=Yahoo Finance as_of=2026-10-12T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=23903.25 spike=0.54
- EPCO.CA: score=-1.57 buy_ready=False sector_rank=19 price=8.97 support=8.0 resistance=11.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:19 PM market time freshness=DELAYED_CURRENT RSI=20.51 liquidity=2032531.0 spike=0.34
- EPPK.CA: score=-7.18 buy_ready=False sector_rank=19 price=10.29 support=10.29 resistance=10.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=8 September 01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=419183.72 spike=0.28
- ETEL.CA: score=24.4 buy_ready=False sector_rank=1 price=144.81 support=126.02 resistance=156.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=61.5 liquidity=183686592.0 spike=0.68
- ETRS.CA: score=6.42 buy_ready=False sector_rank=19 price=10.5 support=9.82 resistance=11.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=41.94 liquidity=4024939.0 spike=0.38
- EXPA.CA: score=7.25 buy_ready=False sector_rank=9 price=14.5 support=14.02 resistance=22.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=8.73 liquidity=20334614.0 spike=0.53
- FAIT.CA: score=-0.21 buy_ready=False sector_rank=9 price=42.99 support=38.48 resistance=47.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=28.64 liquidity=1538891.0 spike=0.52
- FAITA.CA: score=3.28 buy_ready=False sector_rank=9 price=0.99 support=0.98 resistance=1.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=44.44 liquidity=27589.12 spike=0.93
- FERC.CA: score=-0.36 buy_ready=False sector_rank=13 price=70.01 support=66.72 resistance=82.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:18 PM market time freshness=DELAYED_CURRENT RSI=23.08 liquidity=3243817.25 spike=0.57
- FWRY.CA: score=19.12 buy_ready=False sector_rank=2 price=18.57 support=17.5 resistance=19.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:19 PM market time freshness=DELAYED_CURRENT RSI=44.93 liquidity=36437032.0 spike=0.32
- GBCO.CA: score=14.44 buy_ready=False sector_rank=4 price=29.99 support=27.0 resistance=32.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=41.25 liquidity=49498516.0 spike=0.48
- GDWA.CA: score=2.35 buy_ready=False sector_rank=19 price=0.62 support=0.6 resistance=0.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:16 PM market time freshness=DELAYED_CURRENT RSI=17.27 liquidity=5954680.0 spike=0.28
- GGCC.CA: score=3.25 buy_ready=False sector_rank=19 price=0.64 support=0.61 resistance=0.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=21.97 liquidity=5853030.5 spike=0.46
- GIHD.CA: score=7.1 buy_ready=False sector_rank=19 price=56.57 support=53.3 resistance=78.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=26.04 liquidity=9702494.0 spike=0.5
- GMCI.CA: score=3.7 buy_ready=False sector_rank=19 price=1.61 support=1.49 resistance=1.82 source=Yahoo Finance as_of=2026-10-12T21:00:00+00:00 freshness=FRESH RSI=36.84 liquidity=298038.37 spike=0.7
- GRCA.CA: score=1.47 buy_ready=False sector_rank=19 price=32.57 support=30.51 resistance=46.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=28.64 liquidity=3069580.25 spike=0.22
- GSSC.CA: score=-2.18 buy_ready=False sector_rank=19 price=261.41 support=246.0 resistance=333.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:07 PM market time freshness=DELAYED_CURRENT RSI=28.63 liquidity=420936.31 spike=0.13
- GTWL.CA: score=7.4 buy_ready=False sector_rank=19 price=139.67 support=116.16 resistance=241.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=21.25 liquidity=103627576.0 spike=0.66
- HDBK.CA: score=7.01 buy_ready=False sector_rank=9 price=103.92 support=98.01 resistance=121.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:18 PM market time freshness=DELAYED_CURRENT RSI=26.44 liquidity=6760585.0 spike=0.25
- HELI.CA: score=7.4 buy_ready=False sector_rank=16 price=7.25 support=6.92 resistance=8.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=23.04 liquidity=28539370.0 spike=0.27
- HRHO.CA: score=16.2 buy_ready=False sector_rank=10 price=25.48 support=22.81 resistance=27.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:19 PM market time freshness=DELAYED_CURRENT RSI=55.07 liquidity=31328948.0 spike=0.23
- ICID.CA: score=15.75 buy_ready=False sector_rank=19 price=17.6 support=16.52 resistance=20.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=54.6 liquidity=9813939.0 spike=1.27
- IDRE.CA: score=-0.35 buy_ready=False sector_rank=19 price=43.87 support=40.05 resistance=59.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=27.17 liquidity=2250635.5 spike=0.15
- IFAP.CA: score=-2.65 buy_ready=False sector_rank=20 price=18.26 support=17.17 resistance=21.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:17 PM market time freshness=DELAYED_CURRENT RSI=20.51 liquidity=949233.88 spike=0.13
- INFI.CA: score=12.4 buy_ready=False sector_rank=19 price=118.33 support=104.0 resistance=142.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=39.12 liquidity=10762393.0 spike=0.8
- IRON.CA: score=8.54 buy_ready=False sector_rank=13 price=26.69 support=25.01 resistance=32.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:18 PM market time freshness=DELAYED_CURRENT RSI=49.06 liquidity=5138007.5 spike=0.46
- ISMA.CA: score=2.07 buy_ready=False sector_rank=19 price=22.42 support=18.91 resistance=31.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=23.65 liquidity=4669650.0 spike=0.59
- ISMQ.CA: score=4.26 buy_ready=False sector_rank=13 price=7.64 support=7.14 resistance=9.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=28.18 liquidity=7863527.0 spike=0.4
- ISPH.CA: score=6.4 buy_ready=False sector_rank=15 price=11.16 support=10.03 resistance=12.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:19 PM market time freshness=DELAYED_CURRENT RSI=27.95 liquidity=13560842.0 spike=0.22
- JUFO.CA: score=4.5 buy_ready=False sector_rank=14 price=24.05 support=23.5 resistance=27.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:19 PM market time freshness=DELAYED_CURRENT RSI=23.47 liquidity=8095657.0 spike=0.47
- KABO.CA: score=2.7 buy_ready=False sector_rank=17 price=7.69 support=7.3 resistance=10.03 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:18 PM market time freshness=DELAYED_CURRENT RSI=33.33 liquidity=5295766.5 spike=0.2
- KWIN.CA: score=0.79 buy_ready=False sector_rank=19 price=68.07 support=60.0 resistance=93.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:18 PM market time freshness=DELAYED_CURRENT RSI=22.64 liquidity=4393327.5 spike=0.45
- KZPC.CA: score=8.38 buy_ready=False sector_rank=19 price=13.05 support=12.15 resistance=14.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=35.33 liquidity=2977164.5 spike=0.3
- LCSW.CA: score=16.86 buy_ready=False sector_rank=12 price=33.0 support=28.86 resistance=35.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:18 PM market time freshness=DELAYED_CURRENT RSI=49.16 liquidity=11378521.0 spike=0.57
- LUTS.CA: score=12.4 buy_ready=False sector_rank=19 price=0.77 support=0.65 resistance=1.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=37.78 liquidity=29801400.0 spike=0.46
- MAAL.CA: score=12.4 buy_ready=False sector_rank=19 price=9.19 support=8.45 resistance=12.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=48.7 liquidity=21789790.0 spike=0.91
- MASR.CA: score=12.4 buy_ready=False sector_rank=19 price=7.25 support=6.82 resistance=8.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:19 PM market time freshness=DELAYED_CURRENT RSI=38.91 liquidity=25845342.0 spike=0.44
- MBSC.CA: score=14.86 buy_ready=False sector_rank=12 price=340.25 support=288.0 resistance=414.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=48.43 liquidity=26120572.0 spike=0.3
- MCQE.CA: score=11.86 buy_ready=False sector_rank=12 price=179.21 support=170.0 resistance=228.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=37.83 liquidity=36166764.0 spike=0.68
- MCRO.CA: score=7.4 buy_ready=False sector_rank=19 price=1.4 support=1.25 resistance=1.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=25.0 liquidity=25368638.0 spike=0.38
- MENA.CA: score=-2.02 buy_ready=False sector_rank=16 price=6.02 support=5.72 resistance=7.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=28.21 liquidity=583319.75 spike=0.35
- MEPA.CA: score=-2.27 buy_ready=False sector_rank=19 price=1.64 support=1.57 resistance=1.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=5326228.0 spike=0.52
- MFPC.CA: score=10.4 buy_ready=False sector_rank=13 price=44.15 support=42.0 resistance=51.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=32.36 liquidity=13315449.0 spike=0.14
- MFSC.CA: score=-2.38 buy_ready=False sector_rank=19 price=38.18 support=36.25 resistance=49.37 source=Yahoo Finance as_of=2026-10-12T21:00:00+00:00 freshness=FRESH RSI=22.89 liquidity=1217712.93 spike=0.49
- MHOT.CA: score=3.79 buy_ready=False sector_rank=11 price=15.97 support=15.08 resistance=19.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=39.11 liquidity=1878417.75 spike=0.11
- MILS.CA: score=1.66 buy_ready=False sector_rank=19 price=156.73 support=147.06 resistance=207.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:15 PM market time freshness=DELAYED_CURRENT RSI=25.25 liquidity=4263342.0 spike=0.53
- MIPH.CA: score=-2.18 buy_ready=False sector_rank=15 price=775.03 support=666.66 resistance=1000.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:17 PM market time freshness=DELAYED_CURRENT RSI=30.18 liquidity=415803.41 spike=0.05
- MOED.CA: score=0.38 buy_ready=False sector_rank=19 price=0.62 support=0.57 resistance=0.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=28.14 liquidity=3984718.75 spike=0.19
- MOIL.CA: score=-1.08 buy_ready=False sector_rank=5 price=0.67 support=0.63 resistance=0.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:16 PM market time freshness=DELAYED_CURRENT RSI=28.99 liquidity=18332.56 spike=0.06
- MOIN.CA: score=1.91 buy_ready=False sector_rank=19 price=32.5 support=31.0 resistance=39.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=32.49 liquidity=4506348.5 spike=0.36
- MOSC.CA: score=6.68 buy_ready=False sector_rank=19 price=272.83 support=243.15 resistance=286.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:18 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=10246499.0 spike=3.14
- MPCI.CA: score=7.4 buy_ready=False sector_rank=19 price=315.23 support=294.2 resistance=455.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=23.99 liquidity=36433276.0 spike=0.34
- MPCO.CA: score=7.4 buy_ready=False sector_rank=20 price=2.15 support=2.0 resistance=3.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=15.96 liquidity=52123632.0 spike=0.37
- MPRC.CA: score=7.89 buy_ready=False sector_rank=19 price=36.74 support=34.53 resistance=41.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:18 PM market time freshness=DELAYED_CURRENT RSI=40.83 liquidity=5487805.5 spike=0.33
- MTIE.CA: score=7.18 buy_ready=False sector_rank=4 price=7.94 support=7.44 resistance=8.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:19 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=40275080.0 spike=2.37
- NAHO.CA: score=2.41 buy_ready=False sector_rank=19 price=0.13 support=0.12 resistance=0.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=46.15 liquidity=6695.53 spike=0.19
- NCCW.CA: score=7.4 buy_ready=False sector_rank=19 price=6.08 support=5.3 resistance=8.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=34.37 liquidity=14767297.0 spike=0.31
- NEDA.CA: score=-2.41 buy_ready=False sector_rank=19 price=2.6 support=2.47 resistance=2.8 source=Yahoo Finance as_of=2026-10-12T21:00:00+00:00 freshness=FRESH RSI=27.27 liquidity=192412.99 spike=0.28
- NHPS.CA: score=7.5 buy_ready=False sector_rank=19 price=66.33 support=63.02 resistance=86.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=40.24 liquidity=6101695.0 spike=0.43
- NINH.CA: score=3.09 buy_ready=False sector_rank=19 price=16.77 support=16.27 resistance=23.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=18.5 liquidity=5693527.0 spike=0.39
- NIPH.CA: score=7.4 buy_ready=False sector_rank=15 price=275.36 support=241.0 resistance=368.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=24.74 liquidity=87464256.0 spike=0.7
- OBRI.CA: score=9.7 buy_ready=False sector_rank=19 price=26.08 support=22.8 resistance=33.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:18 PM market time freshness=DELAYED_CURRENT RSI=36.97 liquidity=6297151.5 spike=0.45
- OCDI.CA: score=7.4 buy_ready=False sector_rank=16 price=25.69 support=24.2 resistance=30.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:19 PM market time freshness=DELAYED_CURRENT RSI=28.11 liquidity=15172810.0 spike=0.33
- OCPH.CA: score=-2.41 buy_ready=False sector_rank=19 price=203.36 support=190.0 resistance=251.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=30.14 liquidity=1185552.5 spike=0.32
- ODIN.CA: score=0.01 buy_ready=False sector_rank=19 price=2.27 support=2.11 resistance=3.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=22.12 liquidity=2614754.25 spike=0.3
- OFH.CA: score=7.4 buy_ready=False sector_rank=19 price=0.82 support=0.76 resistance=1.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=24.05 liquidity=19148708.0 spike=0.2
- OIH.CA: score=8.79 buy_ready=False sector_rank=8 price=1.81 support=1.7 resistance=2.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:18 PM market time freshness=DELAYED_CURRENT RSI=24.64 liquidity=19133824.0 spike=0.21
- OLFI.CA: score=2.72 buy_ready=False sector_rank=14 price=20.7 support=19.8 resistance=23.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:19 PM market time freshness=DELAYED_CURRENT RSI=7.03 liquidity=6324567.0 spike=0.35
- ORAS.CA: score=5.6 buy_ready=False sector_rank=3 price=921.8 support=882.75 resistance=925.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=362999520.0 spike=1.0
- ORHD.CA: score=6.4 buy_ready=False sector_rank=16 price=11.2 support=10.01 resistance=44.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=2.52 liquidity=68771920.0 spike=0.45
- ORWE.CA: score=17.4 buy_ready=False sector_rank=17 price=27.21 support=26.01 resistance=28.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=37.2 liquidity=29039034.0 spike=0.75
- PHAR.CA: score=12.4 buy_ready=False sector_rank=15 price=107.87 support=102.0 resistance=124.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=35.51 liquidity=24166822.0 spike=0.34
- PHDC.CA: score=14.4 buy_ready=False sector_rank=16 price=12.65 support=12.35 resistance=13.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:19 PM market time freshness=DELAYED_CURRENT RSI=35.68 liquidity=56647552.0 spike=0.6
- PHTV.CA: score=2.93 buy_ready=False sector_rank=19 price=325.6 support=315.1 resistance=378.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:17 PM market time freshness=DELAYED_CURRENT RSI=51.46 liquidity=530834.63 spike=0.48
- POUL.CA: score=1.96 buy_ready=False sector_rank=14 price=9.81 support=9.12 resistance=40.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:19 PM market time freshness=DELAYED_CURRENT RSI=1.91 liquidity=5556203.5 spike=0.17
- PRCL.CA: score=-1.34 buy_ready=False sector_rank=12 price=22.68 support=21.63 resistance=22.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=5804513.5 spike=0.51
- PRDC.CA: score=7.4 buy_ready=False sector_rank=16 price=6.32 support=6.07 resistance=8.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=33.41 liquidity=13148778.0 spike=0.37
- PRMH.CA: score=-4.08 buy_ready=False sector_rank=19 price=2.03 support=1.97 resistance=2.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=3521256.25 spike=0.9
- RACC.CA: score=-2.64 buy_ready=False sector_rank=19 price=8.97 support=8.51 resistance=10.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=31.76 liquidity=959622.63 spike=0.15
- RAKT.CA: score=4.62 buy_ready=False sector_rank=19 price=22.06 support=20.26 resistance=25.08 source=Yahoo Finance as_of=2026-10-12T21:00:00+00:00 freshness=FRESH RSI=49.81 liquidity=480885.93 spike=1.37
- RAYA.CA: score=6.4 buy_ready=False sector_rank=21 price=5.94 support=5.7 resistance=7.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=29.37 liquidity=26690526.0 spike=0.74
- RMDA.CA: score=7.4 buy_ready=False sector_rank=15 price=5.3 support=4.83 resistance=6.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:19 PM market time freshness=DELAYED_CURRENT RSI=24.39 liquidity=13996755.0 spike=0.5
- ROTO.CA: score=9.48 buy_ready=False sector_rank=19 price=37.85 support=35.56 resistance=42.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:11 PM market time freshness=DELAYED_CURRENT RSI=36.98 liquidity=5079585.0 spike=0.59
- RREI.CA: score=-0.21 buy_ready=False sector_rank=19 price=3.47 support=3.29 resistance=4.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:23 PM market time freshness=DELAYED_CURRENT RSI=25.79 liquidity=2385604.75 spike=0.25
- RTVC.CA: score=-2.88 buy_ready=False sector_rank=19 price=3.37 support=3.31 resistance=4.06 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=27.62 liquidity=724132.31 spike=0.26
- RUBX.CA: score=19.4 buy_ready=False sector_rank=19 price=16.49 support=12.72 resistance=19.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=56.24 liquidity=61702348.0 spike=0.61
- SAUD.CA: score=0.04 buy_ready=False sector_rank=9 price=21.76 support=20.2 resistance=26.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:17 PM market time freshness=DELAYED_CURRENT RSI=24.94 liquidity=1795022.5 spike=0.09
- SCEM.CA: score=16.86 buy_ready=False sector_rank=12 price=87.5 support=74.55 resistance=97.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:18 PM market time freshness=DELAYED_CURRENT RSI=47.17 liquidity=34180160.0 spike=0.54
- SCFM.CA: score=-3.01 buy_ready=False sector_rank=19 price=234.06 support=220.35 resistance=280.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:58 AM market time freshness=DELAYED_CURRENT RSI=27.94 liquidity=592392.5 spike=0.32
- SCTS.CA: score=-4.28 buy_ready=False sector_rank=7 price=484.22 support=463.13 resistance=509.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=1285105.88 spike=1.27
- SDTI.CA: score=17.18 buy_ready=False sector_rank=19 price=85.59 support=73.0 resistance=94.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=61.52 liquidity=9784818.0 spike=0.3
- SEIG.CA: score=-0.96 buy_ready=False sector_rank=19 price=197.67 support=173.1 resistance=267.0 source=Yahoo Finance as_of=2026-10-12T21:00:00+00:00 freshness=FRESH RSI=30.73 liquidity=1636707.58 spike=0.71
- SIPC.CA: score=3.0 buy_ready=False sector_rank=19 price=5.7 support=5.32 resistance=5.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:23 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=63019080.0 spike=1.3
- SKPC.CA: score=6.4 buy_ready=False sector_rank=13 price=15.39 support=14.98 resistance=18.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=16.48 liquidity=44194240.0 spike=0.53
- SMFR.CA: score=4.17 buy_ready=False sector_rank=19 price=199.75 support=181.6 resistance=255.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=37.32 liquidity=2768586.5 spike=0.78
- SNFC.CA: score=3.41 buy_ready=False sector_rank=19 price=11.16 support=10.8 resistance=11.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:17 PM market time freshness=DELAYED_CURRENT RSI=32.86 liquidity=3014271.0 spike=0.26
- SPIN.CA: score=-1.14 buy_ready=False sector_rank=17 price=15.16 support=14.94 resistance=18.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=25.53 liquidity=1464201.75 spike=0.25
- SPMD.CA: score=1.66 buy_ready=False sector_rank=19 price=0.35 support=0.34 resistance=0.62 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=23.14 liquidity=5256763.5 spike=0.08
- SUGR.CA: score=1.69 buy_ready=False sector_rank=14 price=54.0 support=50.5 resistance=62.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:18 PM market time freshness=DELAYED_CURRENT RSI=29.69 liquidity=4292272.0 spike=0.38
- SVCE.CA: score=7.4 buy_ready=False sector_rank=19 price=9.3 support=8.81 resistance=12.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=29.54 liquidity=29222862.0 spike=0.34
- SWDY.CA: score=7.4 buy_ready=False sector_rank=18 price=113.63 support=102.31 resistance=128.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=33.64 liquidity=37314132.0 spike=0.61
- TALM.CA: score=19.29 buy_ready=False sector_rank=7 price=21.31 support=18.71 resistance=25.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:19 PM market time freshness=DELAYED_CURRENT RSI=52.14 liquidity=8398604.0 spike=0.15
- TMGH.CA: score=6.4 buy_ready=False sector_rank=16 price=84.49 support=81.22 resistance=96.91 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=13.61 liquidity=110083480.0 spike=0.49
- TRTO.CA: score=4.4 buy_ready=False sector_rank=19 price=0.07 support=0.05 resistance=0.07 source=Yahoo Finance as_of=2026-10-12T21:00:00+00:00 freshness=FRESH RSI=78.95 liquidity=3294.61 spike=0.33
- UEFM.CA: score=3.95 buy_ready=False sector_rank=19 price=478.77 support=407.57 resistance=550.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:23 PM market time freshness=DELAYED_CURRENT RSI=52.92 liquidity=551703.0 spike=0.18
- UEGC.CA: score=8.4 buy_ready=False sector_rank=19 price=1.45 support=1.34 resistance=1.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:23 PM market time freshness=DELAYED_CURRENT RSI=28.36 liquidity=13846802.0 spike=0.41
- UNIP.CA: score=0.13 buy_ready=False sector_rank=19 price=0.32 support=0.31 resistance=0.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=30.67 liquidity=3725115.75 spike=0.36
- UNIT.CA: score=-2.26 buy_ready=False sector_rank=16 price=16.76 support=16.15 resistance=23.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT RSI=34.17 liquidity=342781.44 spike=0.04
- WCDF.CA: score=-1.75 buy_ready=False sector_rank=19 price=544.57 support=515.0 resistance=721.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=25.45 liquidity=853637.0 spike=0.23
- WKOL.CA: score=-0.32 buy_ready=False sector_rank=19 price=278.73 support=266.18 resistance=379.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=22.4 liquidity=3281549.25 spike=0.29
- ZEOT.CA: score=5.3 buy_ready=False sector_rank=19 price=11.17 support=10.31 resistance=11.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=13793515.0 spike=2.45
- ZMID.CA: score=7.4 buy_ready=False sector_rank=16 price=7.28 support=6.83 resistance=9.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=19.44 liquidity=31354170.0 spike=0.3

## Backtesting Lite
- ETEL.CA: 180d return=117.72%, max drawdown=-30.44%, MA20>MA50 days last20=20, as_of=2026-10-12T21:00:00+00:00
- EFIH.CA: 180d return=20.23%, max drawdown=-22.68%, MA20>MA50 days last20=7, as_of=2026-10-12T21:00:00+00:00
- ARAB.CA: 180d return=37.06%, max drawdown=-26.79%, MA20>MA50 days last20=11, as_of=2026-10-12T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- ETEL.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Telecom Egypt summary=Evidence rejected for ETEL.CA: source text did not clearly match ETEL.CA / Telecom Egypt.
- EFIH.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=E-Finance For Digital and Financial Investments summary=Evidence rejected for EFIH.CA: source text did not clearly match EFIH.CA / E-Finance For Digital and Financial Investments.
- ARAB.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Arab Developers Holding summary=Arab Developers Holding unveils EGP 1bn expansion plans to improve financial efficiency; FRA gives initial approval for Arab Developers’ rights issue; Arab Developers stock stabilizes after correction
  - Arab Developers Holding unveils EGP 1bn expansion plans to improve financial efficiency: https://english.mubasher.info/news/4601724/Arab-Developers-Holding-unveils-EGP-1bn-expansion-plans-to-improve-financial-efficiency/
  - FRA gives initial approval for Arab Developers’ rights issue: https://english.mubasher.info/news/4582627/FRA-gives-initial-approval-for-Arab-Developers-rights-issue/
  - Arab Developers stock stabilizes after correction: https://english.mubasher.info/news/4564643/Arab-Developers-stock-stabilizes-after-correction/
- RUBX.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Rubex International for Plastic and Acrylic Manufacturing summary=Evidence rejected for RUBX.CA: source text did not clearly match RUBX.CA / Rubex International for Plastic and Acrylic Manufacturing.
- TALM.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Talim Management Services summary=Evidence rejected for TALM.CA: source text did not clearly match TALM.CA / Talim Management Services.
- FWRY.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Fawry For Banking Technology and Electronic Payments summary=Evidence rejected for FWRY.CA: source text did not clearly match FWRY.CA / Fawry For Banking Technology and Electronic Payments.
- ORWE.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=651 sources=3 expected=Oriental Weavers summary=Oriental Weavers to disburse EGP 1.5/shr dividends for 2025; Oriental Weavers’ consolidated profits cross EGP 2.2bn in 2025; Oriental Weavers generates EGP 12.5bn consolidated sales in H1-25
  - Oriental Weavers to disburse EGP 1.5/shr dividends for 2025: https://english.mubasher.info/news/4590236/Oriental-Weavers-to-disburse-EGP-1-5-shr-dividends-for-2025/
  - Oriental Weavers’ consolidated profits cross EGP 2.2bn in 2025: https://english.mubasher.info/news/4562972/Oriental-Weavers-consolidated-profits-cross-EGP-2-2bn-in-2025/
  - Oriental Weavers generates EGP 12.5bn consolidated sales in H1-25: https://english.mubasher.info/news/4487417/Oriental-Weavers-generates-EGP-12-5bn-consolidated-sales-in-H1-25/
- SDTI.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=SHARM DREAMS Co. for Touristic Investment S.A.E summary=Sharm Dreams stock maintains strong uptrend - Analysis; Sharm Dreams stock is experiencing sideways movement amid anticipation of next trend – Analysis; Sharm Dreams stock hits historic level halting driving buying force
  - Sharm Dreams stock maintains strong uptrend - Analysis: https://english.mubasher.info/news/4577977/Sharm-Dreams-stock-maintains-strong-uptrend-Analysis/
  - Sharm Dreams stock is experiencing sideways movement amid anticipation of next trend – Analysis: https://english.mubasher.info/news/4547831/Sharm-Dreams-stock-is-experiencing-sideways-movement-amid-anticipation-of-next-trend-Analysis/
  - Sharm Dreams stock hits historic level halting driving buying force: https://english.mubasher.info/news/4529096/Sharm-Dreams-stock-hits-historic-level-halting-driving-buying-force/

## Warnings
- Evidence rejected for ETEL.CA: source text did not clearly match ETEL.CA / Telecom Egypt.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence rejected for EFIH.CA: source text did not clearly match EFIH.CA / E-Finance For Digital and Financial Investments.
- Evidence for ARAB.CA matches the company but no source/report date was detected.
- Evidence rejected for RUBX.CA: source text did not clearly match RUBX.CA / Rubex International for Plastic and Acrylic Manufacturing.
- Evidence rejected for TALM.CA: source text did not clearly match TALM.CA / Talim Management Services.
- Evidence rejected for FWRY.CA: source text did not clearly match FWRY.CA / Fawry For Banking Technology and Electronic Payments.
- Evidence for ORWE.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for SDTI.CA matches the company but no source/report date was detected.
