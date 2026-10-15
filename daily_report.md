# Telegram-First EGX Scanner Report

Scan phase: Open liquidity confirmation
Generated UTC: 2026-10-15T11:24:10.040907+00:00
Generated Cairo: 2026-10-15 14:24
Run timing: target 09:15 Cairo | generated Cairo 2026-10-15 14:24 | cron 15 6 * * 0-4
Trigger: scheduled cron=15 6 * * 0-4 mapped to open_confirm; Cairo now 2026-10-15 14:20

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 4
- Tradeable price/liquidity tickers: 177/186
- Top sector: Telecommunications

## Market Context
- Market trend: Bullish
- Source: Mubasher EGX market page (delayed public data)
- As of: Thursday, October 15
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 15.79% / above MA50 21.05%
- EGX70 regime: BEARISH / above MA20 12.5% / above MA50 15.0%
- Sector breadth: 0.0%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- COMI.CA: liquidity=494126528.0 spike=0.92 score=7.72
- CCAP.CA: liquidity=306784032.0 spike=0.51 score=8.7
- ETEL.CA: liquidity=242842336.0 spike=0.91 score=23.96
- UEGC.CA: liquidity=213967040.0 spike=6.29 score=7.4
- EGAL.CA: liquidity=179948528.0 spike=3.28 score=12.06

## AI Narrative
- Provider: OpenRouter OK
- Model: nvidia/nemotron-3-super-120b-a12b:free
- Summary: EGX30 and EGX70 remain bearish with weak breadth, keeping the scanner in defensive mode; only a few trade‑able stocks show bullish‑watch outlooks but liquidity is cooling and prices sit near resistance, so the scanner advises HOLD.
- EFIH.CA (Fintech) – bullish watch, liquidity tradeable but cooling, far above support, resistance close; limited upside expected 1‑3d.

## Top Liquidity Spikes
- UEGC.CA: spike=6.29 liquidity=213967040.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- GGCC.CA: spike=6.28 liquidity=78068744.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- ZEOT.CA: spike=6.18 liquidity=38681396.0 outlook=WEAK_OR_RISKY score=20 buy_ready=False
- FAITA.CA: spike=5.41 liquidity=176361.05 outlook=NEUTRAL score=41 buy_ready=False
- INFI.CA: spike=4.18 liquidity=55665988.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False

## Sector Leaderboard
- #1 Telecommunications: score=4.9 5d=-1.18% 20d=4.64% aboveMA50=50.0%
- #2 Fintech & Payments: score=2.69 5d=-2.77% 20d=-0.64% aboveMA50=50.0%
- #3 Automotive & Distribution: score=1.95 5d=-3.83% 20d=-2.92% aboveMA50=50.0%
- #4 Industrial Goods & Construction: score=1.5 5d=0.0% 20d=0.0% aboveMA50=0.0%
- #5 Transportation & Logistics: score=1.24 5d=-3.55% 20d=1.78% aboveMA50=50.0%
- #6 Education: score=-0.08 5d=-3.29% 20d=-7.64% aboveMA50=33.33%
- #7 Energy & Petrochemicals: score=-0.39 5d=-5.24% 20d=1.34% aboveMA50=33.33%
- #8 Banking & Financials: score=-0.7 5d=-4.06% 20d=-6.24% aboveMA50=20.0%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- ETEL.CA: BULLISH_WATCH score=89.9 liquidity=TRADEABLE sector=LEADING risk=No major short-term scanner risk flags.
- GBCO.CA: BULLISH_WATCH score=86.95 liquidity=TRADEABLE sector=LEADING risk=No major short-term scanner risk flags.
- EFIH.CA: BULLISH_WATCH score=72.69 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; far above support
- AMIA.CA: BULLISH_WATCH score=71 liquidity=TRADEABLE sector=LAGGING risk=liquidity is cooling; sector is not leading
- KZPC.CA: BULLISH_WATCH score=71 liquidity=TRADEABLE sector=LAGGING risk=liquidity is cooling; sector is not leading
- ORWE.CA: BULLISH_WATCH score=70 liquidity=TRADEABLE sector=LAGGING risk=sector is not leading
- TALM.CA: BULLISH_WATCH score=70 liquidity=TRADEABLE sector=NEUTRAL risk=liquidity is cooling
- ALCN.CA: CONSTRUCTIVE score=59.24 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; below MA20
- ACAMD.CA: CONSTRUCTIVE score=58 liquidity=TRADEABLE sector=LAGGING risk=momentum is extended; close to resistance; sector is not leading
- AMOC.CA: CONSTRUCTIVE score=58 liquidity=TRADEABLE sector=NEUTRAL risk=liquidity is cooling; below MA20

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- EKHO.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ARVA.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- GTWL.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=0.37 buy_ready=False sector_rank=19 price=231.33 support=225.0 resistance=359.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=24.7 liquidity=2970629.25 spike=0.16
- ABUK.CA: score=10.5 buy_ready=False sector_rank=17 price=86.33 support=83.0 resistance=96.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=32.15 liquidity=25669180.0 spike=0.28
- ACAMD.CA: score=21.88 buy_ready=False sector_rank=19 price=2.13 support=1.87 resistance=2.16 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=62.07 liquidity=56484220.0 spike=1.24
- ACGC.CA: score=4.18 buy_ready=False sector_rank=14 price=13.04 support=12.81 resistance=14.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=39.75 liquidity=1495088.5 spike=0.12
- ADCI.CA: score=-1.28 buy_ready=False sector_rank=19 price=259.81 support=250.06 resistance=288.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=32.29 liquidity=1320486.13 spike=0.63
- ADIB.CA: score=8.72 buy_ready=False sector_rank=8 price=47.11 support=43.5 resistance=54.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=30.8 liquidity=49998724.0 spike=0.63
- ADPC.CA: score=2.73 buy_ready=False sector_rank=19 price=3.26 support=3.01 resistance=4.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=20.45 liquidity=6330648.0 spike=0.42
- AFDI.CA: score=3.47 buy_ready=False sector_rank=19 price=50.1 support=46.12 resistance=56.82 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=43.15 liquidity=1068805.25 spike=0.16
- AFMC.CA: score=6.02 buy_ready=False sector_rank=19 price=132.2 support=122.0 resistance=179.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=34.51 liquidity=8616473.0 spike=0.42
- AJWA.CA: score=16.58 buy_ready=False sector_rank=19 price=225.0 support=176.0 resistance=222.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=88.63 liquidity=30654518.0 spike=1.09
- ALCN.CA: score=13.85 buy_ready=False sector_rank=5 price=33.18 support=30.55 resistance=36.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=44.75 liquidity=6352630.0 spike=0.18
- ALUM.CA: score=-0.15 buy_ready=False sector_rank=19 price=21.1 support=20.52 resistance=27.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=26.87 liquidity=3451717.75 spike=0.75
- AMER.CA: score=14.53 buy_ready=False sector_rank=16 price=4.62 support=4.05 resistance=5.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=43.24 liquidity=28647942.0 spike=0.57
- AMES.CA: score=8.4 buy_ready=False sector_rank=19 price=39.13 support=38.02 resistance=59.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=31.25 liquidity=31281276.0 spike=0.34
- AMIA.CA: score=16.42 buy_ready=False sector_rank=19 price=19.0 support=17.12 resistance=19.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=51.65 liquidity=9015664.0 spike=0.5
- AMOC.CA: score=16.84 buy_ready=False sector_rank=7 price=13.41 support=12.18 resistance=14.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=52.03 liquidity=56926976.0 spike=0.45
- APSW.CA: score=1.58 buy_ready=False sector_rank=19 price=7.91 support=7.81 resistance=8.92 source=Yahoo Finance as_of=2026-10-13T21:00:00+00:00 freshness=FRESH RSI=39.15 liquidity=183875.86 spike=0.28
- ARAB.CA: score=19.53 buy_ready=False sector_rank=16 price=0.27 support=0.2 resistance=0.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=64.91 liquidity=49175356.0 spike=0.5
- ARCC.CA: score=12.88 buy_ready=False sector_rank=13 price=66.73 support=60.01 resistance=74.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=47.31 liquidity=10517985.0 spike=0.34
- AREH.CA: score=4.53 buy_ready=False sector_rank=19 price=1.2 support=1.11 resistance=1.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=29.63 liquidity=8125069.5 spike=0.97
- ASCM.CA: score=0.74 buy_ready=False sector_rank=19 price=50.51 support=48.0 resistance=61.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=30.22 liquidity=4337373.0 spike=0.51
- ASPI.CA: score=6.4 buy_ready=False sector_rank=19 price=0.34 support=0.31 resistance=0.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=27.32 liquidity=14290628.0 spike=0.44
- ATLC.CA: score=1.79 buy_ready=False sector_rank=11 price=5.49 support=5.2 resistance=7.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=33.96 liquidity=3680599.0 spike=0.38
- ATQA.CA: score=12.5 buy_ready=False sector_rank=17 price=11.56 support=10.61 resistance=13.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=37.75 liquidity=23681724.0 spike=0.32
- AXPH.CA: score=0.63 buy_ready=False sector_rank=19 price=1371.17 support=1300.0 resistance=1987.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=24.72 liquidity=3231832.75 spike=0.47
- BINV.CA: score=10.65 buy_ready=False sector_rank=9 price=59.29 support=50.0 resistance=72.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=64.99 liquidity=1944221.0 spike=0.07
- BIOC.CA: score=16.4 buy_ready=False sector_rank=19 price=298.27 support=225.21 resistance=380.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=59.39 liquidity=27703250.0 spike=0.26
- BTFH.CA: score=7.37 buy_ready=False sector_rank=11 price=2.76 support=2.55 resistance=3.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=34.85 liquidity=112885576.0 spike=1.13
- CAED.CA: score=5.51 buy_ready=False sector_rank=19 price=104.81 support=95.0 resistance=136.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=37.43 liquidity=3110781.0 spike=0.36
- CANA.CA: score=10.64 buy_ready=False sector_rank=8 price=44.0 support=41.7 resistance=52.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=41.51 liquidity=3924608.5 spike=0.16
- CCAP.CA: score=8.7 buy_ready=False sector_rank=9 price=6.07 support=6.07 resistance=7.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=24.86 liquidity=306784032.0 spike=0.51
- CCRS.CA: score=0.75 buy_ready=False sector_rank=19 price=2.05 support=1.87 resistance=2.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=18.42 liquidity=3354141.25 spike=0.28
- CEFM.CA: score=2.92 buy_ready=False sector_rank=19 price=126.22 support=113.0 resistance=152.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:00 PM market time freshness=DELAYED_CURRENT RSI=35.75 liquidity=515127.91 spike=0.19
- CERA.CA: score=12.86 buy_ready=False sector_rank=19 price=1.26 support=1.18 resistance=1.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=46.84 liquidity=149791904.0 spike=1.23
- CFGH.CA: score=-3.6 buy_ready=False sector_rank=19 price=0.1 support=0.1 resistance=0.12 source=Yahoo Finance as_of=2026-10-13T21:00:00+00:00 freshness=FRESH RSI=0.0 liquidity=2652.3 spike=0.46
- CICH.CA: score=-0.25 buy_ready=False sector_rank=11 price=11.0 support=10.6 resistance=13.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:00 PM market time freshness=DELAYED_CURRENT RSI=29.55 liquidity=1645524.63 spike=0.47
- CIEB.CA: score=6.77 buy_ready=False sector_rank=8 price=23.01 support=22.56 resistance=25.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=30.26 liquidity=8052694.5 spike=0.84
- CIRA.CA: score=13.97 buy_ready=False sector_rank=6 price=37.5 support=35.51 resistance=41.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=40.69 liquidity=12282683.0 spike=0.51
- CLHO.CA: score=11.32 buy_ready=False sector_rank=15 price=14.09 support=13.86 resistance=16.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=25.89 liquidity=130523384.0 spike=3.37
- CNFN.CA: score=12.32 buy_ready=False sector_rank=11 price=4.14 support=3.8 resistance=4.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=36.13 liquidity=9954384.0 spike=1.13
- COMI.CA: score=7.72 buy_ready=False sector_rank=8 price=125.26 support=120.0 resistance=134.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=24.92 liquidity=494126528.0 spike=0.92
- COPR.CA: score=9.58 buy_ready=False sector_rank=19 price=0.47 support=0.44 resistance=0.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=42.03 liquidity=7179421.5 spike=0.31
- COSG.CA: score=6.4 buy_ready=False sector_rank=19 price=1.46 support=1.34 resistance=1.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=30.16 liquidity=10002004.0 spike=0.66
- CPCI.CA: score=8.73 buy_ready=False sector_rank=19 price=607.02 support=531.02 resistance=619.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=75.91 liquidity=2326972.0 spike=0.56
- CSAG.CA: score=11.21 buy_ready=False sector_rank=5 price=36.09 support=34.06 resistance=39.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=40.41 liquidity=6709027.0 spike=0.89
- DAPH.CA: score=12.4 buy_ready=False sector_rank=19 price=94.4 support=89.1 resistance=129.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=37.77 liquidity=28701820.0 spike=0.71
- DEIN.CA: score=5.4 buy_ready=False sector_rank=19 price=10.35 support=10.35 resistance=12.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 09:54 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=37.26 spike=0.01
- DOMT.CA: score=-2.62 buy_ready=False sector_rank=12 price=23.52 support=22.85 resistance=27.23 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=27.6 liquidity=460877.13 spike=0.1
- DSCW.CA: score=3.94 buy_ready=False sector_rank=19 price=1.61 support=1.55 resistance=1.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=28.95 liquidity=7539336.0 spike=0.43
- DTPP.CA: score=2.4 buy_ready=False sector_rank=19 price=268.03 support=246.6 resistance=272.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=71034840.0 spike=0.96
- EALR.CA: score=-1.93 buy_ready=False sector_rank=19 price=305.27 support=290.17 resistance=411.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=25.33 liquidity=1667120.63 spike=0.18
- EASB.CA: score=4.45 buy_ready=False sector_rank=19 price=6.88 support=6.04 resistance=8.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=36.5 liquidity=2047459.5 spike=0.35
- EAST.CA: score=7.54 buy_ready=False sector_rank=12 price=29.01 support=27.01 resistance=33.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=20.59 liquidity=60347416.0 spike=1.31
- EBSC.CA: score=-1.65 buy_ready=False sector_rank=19 price=1.62 support=1.5 resistance=2.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=29.63 liquidity=1954781.75 spike=0.85
- ECAP.CA: score=-2.02 buy_ready=False sector_rank=19 price=28.39 support=27.5 resistance=32.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=23.9 liquidity=1578658.75 spike=0.37
- EDFM.CA: score=2.9 buy_ready=False sector_rank=19 price=385.55 support=335.2 resistance=425.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:00 PM market time freshness=DELAYED_CURRENT RSI=50.14 liquidity=504182.41 spike=0.44
- EEII.CA: score=-1.41 buy_ready=False sector_rank=19 price=1.95 support=1.83 resistance=2.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=25.0 liquidity=2190159.25 spike=0.24
- EFIC.CA: score=6.21 buy_ready=False sector_rank=17 price=155.03 support=147.0 resistance=199.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=26.89 liquidity=9707251.0 spike=0.27
- EFID.CA: score=8.92 buy_ready=False sector_rank=12 price=18.7 support=18.07 resistance=31.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=32.98 liquidity=36380488.0 spike=0.75
- EFIH.CA: score=24.08 buy_ready=False sector_rank=2 price=24.44 support=20.2 resistance=25.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=53.64 liquidity=36525768.0 spike=0.54
- EGAL.CA: score=12.06 buy_ready=False sector_rank=17 price=305.98 support=306.1 resistance=376.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=16.96 liquidity=179948528.0 spike=3.28
- EGAS.CA: score=7.11 buy_ready=False sector_rank=7 price=52.61 support=48.08 resistance=60.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=36.26 liquidity=3261473.5 spike=0.29
- EGBE.CA: score=3.96 buy_ready=False sector_rank=8 price=0.5 support=0.5 resistance=0.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=45.57 liquidity=136571.92 spike=1.05
- EGCH.CA: score=6.5 buy_ready=False sector_rank=17 price=12.14 support=11.86 resistance=14.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=24.18 liquidity=37454540.0 spike=0.47
- EGSA.CA: score=8.99 buy_ready=False sector_rank=1 price=8.81 support=8.82 resistance=9.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=40.0 liquidity=7506.72 spike=1.01
- EGTS.CA: score=5.08 buy_ready=False sector_rank=16 price=13.89 support=13.56 resistance=19.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=18.84 liquidity=7544819.5 spike=0.21
- EHDR.CA: score=4.08 buy_ready=False sector_rank=19 price=2.3 support=2.1 resistance=2.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=27.03 liquidity=7677249.5 spike=0.68
- ELEC.CA: score=6.45 buy_ready=False sector_rank=18 price=1.73 support=1.65 resistance=2.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=27.78 liquidity=31114438.0 spike=0.58
- ELKA.CA: score=16.5 buy_ready=False sector_rank=19 price=1.58 support=1.38 resistance=1.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=39.06 liquidity=35608200.0 spike=3.05
- ELNA.CA: score=4.61 buy_ready=False sector_rank=19 price=35.22 support=33.46 resistance=36.4 source=Yahoo Finance as_of=2026-10-13T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=229528.75 spike=1.49
- ELSH.CA: score=7.4 buy_ready=False sector_rank=19 price=11.21 support=10.76 resistance=13.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=30.9 liquidity=18294172.0 spike=0.88
- ELWA.CA: score=6.43 buy_ready=False sector_rank=19 price=1.65 support=1.43 resistance=1.75 source=Yahoo Finance as_of=2026-10-13T21:00:00+00:00 freshness=FRESH RSI=45.45 liquidity=30036.6 spike=0.06
- EMFD.CA: score=7.53 buy_ready=False sector_rank=16 price=12.08 support=11.7 resistance=14.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=33.33 liquidity=45548288.0 spike=0.68
- ENGC.CA: score=2.14 buy_ready=False sector_rank=19 price=33.83 support=32.37 resistance=45.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=25.39 liquidity=5738832.5 spike=0.31
- EOSB.CA: score=7.4 buy_ready=False sector_rank=19 price=1.57 support=1.64 resistance=1.64 source=Yahoo Finance as_of=2026-10-13T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=157.0 spike=0.0
- EPCO.CA: score=-2.67 buy_ready=False sector_rank=19 price=8.83 support=8.0 resistance=11.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=25.56 liquidity=933391.56 spike=0.17
- EPPK.CA: score=-7.18 buy_ready=False sector_rank=19 price=10.29 support=10.29 resistance=10.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=8 September 01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=419183.72 spike=0.28
- ETEL.CA: score=23.96 buy_ready=False sector_rank=1 price=144.99 support=128.52 resistance=156.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=58.33 liquidity=242842336.0 spike=0.91
- ETRS.CA: score=4.95 buy_ready=False sector_rank=19 price=10.49 support=9.82 resistance=11.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=47.76 liquidity=2553623.5 spike=0.24
- EXPA.CA: score=7.72 buy_ready=False sector_rank=8 price=14.52 support=14.02 resistance=22.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=9.23 liquidity=16059072.0 spike=0.43
- FAIT.CA: score=1.3 buy_ready=False sector_rank=8 price=43.54 support=38.48 resistance=47.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=32.45 liquidity=2577104.0 spike=0.86
- FAITA.CA: score=13.9 buy_ready=False sector_rank=8 price=1.0 support=0.98 resistance=1.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=45.9 liquidity=176361.05 spike=5.41
- FERC.CA: score=-2.18 buy_ready=False sector_rank=17 price=69.85 support=66.72 resistance=82.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=25.03 liquidity=1313175.5 spike=0.24
- FWRY.CA: score=17.08 buy_ready=False sector_rank=2 price=18.6 support=17.5 resistance=19.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=42.09 liquidity=77108856.0 spike=0.69
- GBCO.CA: score=20.78 buy_ready=False sector_rank=3 price=30.8 support=27.0 resistance=32.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=44.58 liquidity=95935624.0 spike=0.91
- GDWA.CA: score=6.4 buy_ready=False sector_rank=19 price=0.63 support=0.6 resistance=0.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=22.94 liquidity=10780494.0 spike=0.52
- GGCC.CA: score=7.4 buy_ready=False sector_rank=19 price=0.7 support=0.63 resistance=0.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=78068744.0 spike=6.28
- GIHD.CA: score=6.31 buy_ready=False sector_rank=19 price=53.67 support=53.3 resistance=78.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=22.82 liquidity=8909625.0 spike=0.46
- GMCI.CA: score=3.77 buy_ready=False sector_rank=19 price=1.54 support=1.49 resistance=1.82 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=40.38 liquidity=371923.31 spike=0.89
- GRCA.CA: score=2.13 buy_ready=False sector_rank=19 price=32.92 support=30.51 resistance=46.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=28.85 liquidity=3727992.5 spike=0.29
- GSSC.CA: score=-0.89 buy_ready=False sector_rank=19 price=269.26 support=246.0 resistance=333.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=34.66 liquidity=1708861.63 spike=0.56
- HDBK.CA: score=7.72 buy_ready=False sector_rank=8 price=101.82 support=98.01 resistance=121.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=31.61 liquidity=12785670.0 spike=0.48
- HELI.CA: score=7.53 buy_ready=False sector_rank=16 price=7.42 support=6.92 resistance=8.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=30.98 liquidity=65890376.0 spike=0.63
- HRHO.CA: score=16.11 buy_ready=False sector_rank=11 price=25.7 support=22.81 resistance=27.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=58.06 liquidity=77864928.0 spike=0.59
- ICID.CA: score=5.81 buy_ready=False sector_rank=19 price=17.52 support=16.52 resistance=20.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=59.11 liquidity=411517.59 spike=0.05
- IDRE.CA: score=0.24 buy_ready=False sector_rank=19 price=43.08 support=40.05 resistance=59.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=32.67 liquidity=2838341.75 spike=0.21
- IFAP.CA: score=3.52 buy_ready=False sector_rank=20 price=18.22 support=17.17 resistance=21.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=23.77 liquidity=7117335.0 spike=1.0
- INFI.CA: score=7.4 buy_ready=False sector_rank=19 price=129.75 support=111.25 resistance=131.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=55665988.0 spike=4.18
- IRON.CA: score=13.54 buy_ready=False sector_rank=17 price=26.78 support=25.01 resistance=32.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=44.3 liquidity=11052244.0 spike=1.02
- ISMA.CA: score=-0.04 buy_ready=False sector_rank=19 price=22.28 support=18.91 resistance=31.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=28.72 liquidity=2564760.0 spike=0.34
- ISMQ.CA: score=1.48 buy_ready=False sector_rank=17 price=7.61 support=7.14 resistance=9.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=32.26 liquidity=4975077.5 spike=0.26
- ISPH.CA: score=6.58 buy_ready=False sector_rank=15 price=11.25 support=10.03 resistance=12.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=34.03 liquidity=19625060.0 spike=0.33
- JUFO.CA: score=1.74 buy_ready=False sector_rank=12 price=24.35 support=23.5 resistance=27.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=28.95 liquidity=4824934.5 spike=0.28
- KABO.CA: score=1.7 buy_ready=False sector_rank=14 price=7.51 support=7.3 resistance=9.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=34.35 liquidity=4009281.0 spike=0.16
- KWIN.CA: score=-0.45 buy_ready=False sector_rank=19 price=66.69 support=60.0 resistance=93.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=19.32 liquidity=3154596.25 spike=0.33
- KZPC.CA: score=12.4 buy_ready=False sector_rank=19 price=13.4 support=12.15 resistance=14.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=41.76 liquidity=5003315.0 spike=0.54
- LCSW.CA: score=16.88 buy_ready=False sector_rank=13 price=33.51 support=28.86 resistance=35.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=56.59 liquidity=16061367.0 spike=0.81
- LUTS.CA: score=12.4 buy_ready=False sector_rank=19 price=0.74 support=0.65 resistance=1.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=40.26 liquidity=38166608.0 spike=0.63
- MAAL.CA: score=10.77 buy_ready=False sector_rank=19 price=8.72 support=8.45 resistance=12.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=38.04 liquidity=8372056.0 spike=0.34
- MASR.CA: score=12.4 buy_ready=False sector_rank=19 price=7.4 support=6.82 resistance=7.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=44.57 liquidity=39160764.0 spike=0.69
- MBSC.CA: score=14.88 buy_ready=False sector_rank=13 price=340.04 support=288.0 resistance=414.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=49.92 liquidity=33903672.0 spike=0.4
- MCQE.CA: score=11.88 buy_ready=False sector_rank=13 price=174.0 support=170.0 resistance=228.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=39.19 liquidity=41373196.0 spike=0.76
- MCRO.CA: score=7.4 buy_ready=False sector_rank=19 price=1.39 support=1.25 resistance=1.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=28.57 liquidity=38712412.0 spike=0.66
- MENA.CA: score=-0.34 buy_ready=False sector_rank=16 price=6.04 support=5.57 resistance=7.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:55 PM market time freshness=DELAYED_CURRENT RSI=34.83 liquidity=1866774.88 spike=1.13
- MEPA.CA: score=5.15 buy_ready=False sector_rank=19 price=1.63 support=1.53 resistance=2.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=36.36 liquidity=3749160.5 spike=0.38
- MFPC.CA: score=15.5 buy_ready=False sector_rank=17 price=43.77 support=42.0 resistance=51.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=36.16 liquidity=20408176.0 spike=0.23
- MFSC.CA: score=-3.29 buy_ready=False sector_rank=19 price=38.29 support=36.25 resistance=49.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=17.38 liquidity=306251.41 spike=0.13
- MHOT.CA: score=0.52 buy_ready=False sector_rank=10 price=15.76 support=15.08 resistance=19.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=33.08 liquidity=3091336.0 spike=0.18
- MICH.CA: score=4.51 buy_ready=False sector_rank=19 price=41.31 support=38.91 resistance=47.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=44.71 liquidity=2107393.0 spike=0.24
- MILS.CA: score=1.44 buy_ready=False sector_rank=19 price=154.15 support=147.06 resistance=207.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=26.66 liquidity=4036302.0 spike=0.5
- MIPH.CA: score=3.57 buy_ready=False sector_rank=15 price=793.49 support=666.66 resistance=1000.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:55 PM market time freshness=DELAYED_CURRENT RSI=40.54 liquidity=994122.13 spike=0.12
- MOED.CA: score=2.38 buy_ready=False sector_rank=19 price=0.61 support=0.57 resistance=0.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=31.09 liquidity=5984873.0 spike=0.33
- MOIL.CA: score=-1.15 buy_ready=False sector_rank=7 price=0.68 support=0.63 resistance=0.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:34 PM market time freshness=DELAYED_CURRENT RSI=34.67 liquidity=7283.11 spike=0.03
- MOIN.CA: score=3.31 buy_ready=False sector_rank=19 price=31.79 support=31.0 resistance=38.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:00 PM market time freshness=DELAYED_CURRENT RSI=34.61 liquidity=5908172.0 spike=0.56
- MOSC.CA: score=6.68 buy_ready=False sector_rank=19 price=265.01 support=231.0 resistance=329.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=38.82 liquidity=4100744.25 spike=1.09
- MPCI.CA: score=7.4 buy_ready=False sector_rank=19 price=317.2 support=294.2 resistance=455.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=27.56 liquidity=79646512.0 spike=0.78
- MPCO.CA: score=7.4 buy_ready=False sector_rank=20 price=2.08 support=2.0 resistance=3.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=20.24 liquidity=44828868.0 spike=0.34
- MPRC.CA: score=6.48 buy_ready=False sector_rank=19 price=35.97 support=34.53 resistance=41.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=39.67 liquidity=4075210.5 spike=0.25
- MTIE.CA: score=14.23 buy_ready=False sector_rank=3 price=7.68 support=7.27 resistance=8.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=40.7 liquidity=9446370.0 spike=0.51
- NAHO.CA: score=2.42 buy_ready=False sector_rank=19 price=0.13 support=0.12 resistance=0.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:34 PM market time freshness=DELAYED_CURRENT RSI=61.9 liquidity=17533.57 spike=0.6
- NCCW.CA: score=7.4 buy_ready=False sector_rank=19 price=5.86 support=5.3 resistance=8.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=27.82 liquidity=15637881.0 spike=0.37
- NEDA.CA: score=-2.55 buy_ready=False sector_rank=19 price=2.6 support=2.47 resistance=2.8 source=Yahoo Finance as_of=2026-10-13T21:00:00+00:00 freshness=FRESH RSI=27.27 liquidity=51441.0 spike=0.08
- NHPS.CA: score=3.91 buy_ready=False sector_rank=19 price=65.17 support=63.02 resistance=86.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=26.15 liquidity=7510847.5 spike=0.52
- NINH.CA: score=7.4 buy_ready=False sector_rank=19 price=16.55 support=16.02 resistance=23.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=21.33 liquidity=14406568.0 spike=1.0
- NIPH.CA: score=7.58 buy_ready=False sector_rank=15 price=273.4 support=241.0 resistance=368.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=28.57 liquidity=49336972.0 spike=0.39
- OBRI.CA: score=13.46 buy_ready=False sector_rank=19 price=27.18 support=22.8 resistance=33.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:08 PM market time freshness=DELAYED_CURRENT RSI=40.7 liquidity=14311080.0 spike=1.03
- OCDI.CA: score=7.53 buy_ready=False sector_rank=16 price=25.56 support=24.2 resistance=30.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=32.64 liquidity=33733940.0 spike=0.78
- OCPH.CA: score=-1.35 buy_ready=False sector_rank=19 price=199.78 support=190.0 resistance=251.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=34.19 liquidity=2253209.75 spike=0.63
- ODIN.CA: score=1.57 buy_ready=False sector_rank=19 price=2.26 support=2.11 resistance=3.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=27.93 liquidity=4173508.25 spike=0.49
- OFH.CA: score=7.4 buy_ready=False sector_rank=19 price=0.8 support=0.76 resistance=1.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:08 PM market time freshness=DELAYED_CURRENT RSI=25.96 liquidity=10349025.0 spike=0.11
- OIH.CA: score=7.85 buy_ready=False sector_rank=9 price=1.79 support=1.7 resistance=2.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=23.53 liquidity=9149217.0 spike=0.1
- OLFI.CA: score=-0.39 buy_ready=False sector_rank=12 price=20.75 support=19.8 resistance=23.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=24.12 liquidity=2694402.25 spike=0.15
- ORAS.CA: score=4.6 buy_ready=False sector_rank=4 price=895.22 support=886.0 resistance=914.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=146569168.0 spike=1.0
- ORHD.CA: score=6.53 buy_ready=False sector_rank=16 price=10.7 support=10.01 resistance=44.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=3.34 liquidity=75284128.0 spike=0.48
- ORWE.CA: score=18.61 buy_ready=False sector_rank=14 price=27.85 support=26.01 resistance=28.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=46.81 liquidity=57605232.0 spike=1.46
- PHAR.CA: score=12.58 buy_ready=False sector_rank=15 price=107.9 support=102.0 resistance=124.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=40.86 liquidity=18714392.0 spike=0.27
- PHDC.CA: score=9.53 buy_ready=False sector_rank=16 price=12.8 support=12.35 resistance=13.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=34.5 liquidity=79850968.0 spike=0.85
- PHTV.CA: score=2.79 buy_ready=False sector_rank=19 price=337.97 support=315.0 resistance=378.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:48 PM market time freshness=DELAYED_CURRENT RSI=48.45 liquidity=385905.38 spike=0.39
- POUL.CA: score=6.92 buy_ready=False sector_rank=12 price=9.94 support=9.12 resistance=40.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=2.43 liquidity=26018144.0 spike=0.77
- PRCL.CA: score=-0.76 buy_ready=False sector_rank=13 price=22.36 support=21.0 resistance=33.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=26.9 liquidity=2362219.5 spike=0.21
- PRDC.CA: score=12.53 buy_ready=False sector_rank=16 price=6.44 support=6.07 resistance=8.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=37.71 liquidity=20839048.0 spike=0.58
- PRMH.CA: score=-0.88 buy_ready=False sector_rank=19 price=2.02 support=1.8 resistance=2.82 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=25.22 liquidity=2721759.75 spike=0.68
- RACC.CA: score=9.05 buy_ready=False sector_rank=19 price=9.09 support=8.51 resistance=10.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=39.34 liquidity=7330843.0 spike=1.16
- RAKT.CA: score=3.52 buy_ready=False sector_rank=19 price=22.06 support=20.26 resistance=25.08 source=Yahoo Finance as_of=2026-10-13T21:00:00+00:00 freshness=FRESH RSI=49.81 liquidity=120822.62 spike=0.35
- RAYA.CA: score=6.4 buy_ready=False sector_rank=21 price=5.97 support=5.7 resistance=7.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=28.03 liquidity=14965214.0 spike=0.4
- RMDA.CA: score=7.58 buy_ready=False sector_rank=15 price=5.19 support=4.83 resistance=6.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=27.59 liquidity=12541464.0 spike=0.47
- ROTO.CA: score=4.71 buy_ready=False sector_rank=19 price=37.38 support=35.56 resistance=42.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:08 PM market time freshness=DELAYED_CURRENT RSI=37.96 liquidity=2308026.0 spike=0.27
- RREI.CA: score=2.04 buy_ready=False sector_rank=19 price=3.6 support=3.29 resistance=4.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:08 PM market time freshness=DELAYED_CURRENT RSI=34.76 liquidity=4640272.5 spike=0.5
- RTVC.CA: score=-2.65 buy_ready=False sector_rank=19 price=3.45 support=3.31 resistance=4.06 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:08 PM market time freshness=DELAYED_CURRENT RSI=31.07 liquidity=953032.25 spike=0.35
- RUBX.CA: score=17.4 buy_ready=False sector_rank=19 price=16.42 support=12.9 resistance=19.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:08 PM market time freshness=DELAYED_CURRENT RSI=48.47 liquidity=28842054.0 spike=0.28
- SAUD.CA: score=10.68 buy_ready=False sector_rank=8 price=22.18 support=20.2 resistance=26.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=32.01 liquidity=37355556.0 spike=1.98
- SCEM.CA: score=16.88 buy_ready=False sector_rank=13 price=88.76 support=74.55 resistance=96.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=53.53 liquidity=49803616.0 spike=0.79
- SCFM.CA: score=-2.96 buy_ready=False sector_rank=19 price=232.8 support=220.35 resistance=280.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=31.34 liquidity=637075.69 spike=0.35
- SCTS.CA: score=1.26 buy_ready=False sector_rank=6 price=485.26 support=463.13 resistance=616.97 source=Yahoo Finance as_of=2026-10-13T21:00:00+00:00 freshness=FRESH RSI=20.97 liquidity=1427634.95 spike=1.43
- SDTI.CA: score=15.4 buy_ready=False sector_rank=19 price=85.95 support=73.02 resistance=94.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:08 PM market time freshness=DELAYED_CURRENT RSI=66.01 liquidity=19045346.0 spike=0.57
- SEIG.CA: score=-2.76 buy_ready=False sector_rank=19 price=194.09 support=173.1 resistance=267.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=33.48 liquidity=837842.81 spike=0.38
- SIPC.CA: score=3.42 buy_ready=False sector_rank=19 price=5.74 support=5.61 resistance=6.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:08 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=78395232.0 spike=1.51
- SKPC.CA: score=6.5 buy_ready=False sector_rank=17 price=15.26 support=14.98 resistance=18.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=22.06 liquidity=36709752.0 spike=0.45
- SMFR.CA: score=3.51 buy_ready=False sector_rank=19 price=199.32 support=181.6 resistance=255.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:08 PM market time freshness=DELAYED_CURRENT RSI=35.69 liquidity=2109733.0 spike=0.58
- SNFC.CA: score=11.38 buy_ready=False sector_rank=19 price=11.1 support=10.81 resistance=11.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=40.51 liquidity=5976682.5 spike=0.53
- SPIN.CA: score=2.1 buy_ready=False sector_rank=14 price=15.0 support=14.94 resistance=18.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=28.13 liquidity=4415719.5 spike=0.8
- SPMD.CA: score=2.4 buy_ready=False sector_rank=19 price=0.38 support=0.34 resistance=0.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:08 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=30514110.0 spike=0.8
- SUGR.CA: score=3.94 buy_ready=False sector_rank=12 price=57.79 support=54.6 resistance=57.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=15538372.0 spike=1.51
- SVCE.CA: score=7.4 buy_ready=False sector_rank=19 price=9.37 support=8.81 resistance=12.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:08 PM market time freshness=DELAYED_CURRENT RSI=30.27 liquidity=33462576.0 spike=0.4
- SWDY.CA: score=12.45 buy_ready=False sector_rank=18 price=113.55 support=102.31 resistance=128.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=39.13 liquidity=24362650.0 spike=0.4
- TALM.CA: score=16.9 buy_ready=False sector_rank=6 price=21.07 support=18.71 resistance=23.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=52.86 liquidity=7930872.0 spike=0.19
- TMGH.CA: score=6.53 buy_ready=False sector_rank=16 price=84.53 support=81.22 resistance=96.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=15.12 liquidity=179762336.0 spike=0.8
- TRTO.CA: score=4.4 buy_ready=False sector_rank=19 price=0.07 support=0.05 resistance=0.07 source=Yahoo Finance as_of=2026-10-13T21:00:00+00:00 freshness=FRESH RSI=88.24 liquidity=4962.82 spike=0.51
- UEFM.CA: score=4.24 buy_ready=False sector_rank=19 price=479.54 support=407.57 resistance=550.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=49.89 liquidity=844462.44 spike=0.27
- UEGC.CA: score=7.4 buy_ready=False sector_rank=19 price=1.67 support=1.5 resistance=1.71 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=213967040.0 spike=6.29
- UNIP.CA: score=5.79 buy_ready=False sector_rank=19 price=0.33 support=0.31 resistance=0.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:08 PM market time freshness=DELAYED_CURRENT RSI=34.0 liquidity=8394220.0 spike=0.86
- UNIT.CA: score=5.54 buy_ready=False sector_rank=16 price=17.15 support=16.15 resistance=20.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=38.75 liquidity=3012392.5 spike=0.45
- WCDF.CA: score=-0.88 buy_ready=False sector_rank=19 price=538.77 support=515.0 resistance=720.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=21.47 liquidity=1724803.38 spike=0.52
- WKOL.CA: score=-1.29 buy_ready=False sector_rank=19 price=276.7 support=266.18 resistance=379.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=27.19 liquidity=2307011.75 spike=0.21
- ZEOT.CA: score=17.4 buy_ready=False sector_rank=19 price=11.26 support=9.75 resistance=14.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:08 PM market time freshness=DELAYED_CURRENT RSI=39.3 liquidity=38681396.0 spike=6.18
- ZMID.CA: score=7.53 buy_ready=False sector_rank=16 price=7.2 support=6.83 resistance=9.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=18.48 liquidity=78803784.0 spike=0.78

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
- ARAB.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Arab Developers Holding summary=Arab Developers Holding unveils EGP 1bn expansion plans to improve financial efficiency; FRA gives initial approval for Arab Developers’ rights issue; Arab Developers stock stabilizes after correction
  - Arab Developers Holding unveils EGP 1bn expansion plans to improve financial efficiency: https://english.mubasher.info/news/4601724/Arab-Developers-Holding-unveils-EGP-1bn-expansion-plans-to-improve-financial-efficiency/
  - FRA gives initial approval for Arab Developers’ rights issue: https://english.mubasher.info/news/4582627/FRA-gives-initial-approval-for-Arab-Developers-rights-issue/
  - Arab Developers stock stabilizes after correction: https://english.mubasher.info/news/4564643/Arab-Developers-stock-stabilizes-after-correction/
- ORWE.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=652 sources=3 expected=Oriental Weavers summary=Oriental Weavers to disburse EGP 1.5/shr dividends for 2025; Oriental Weavers’ consolidated profits cross EGP 2.2bn in 2025; Oriental Weavers generates EGP 12.5bn consolidated sales in H1-25
  - Oriental Weavers to disburse EGP 1.5/shr dividends for 2025: https://english.mubasher.info/news/4590236/Oriental-Weavers-to-disburse-EGP-1-5-shr-dividends-for-2025/
  - Oriental Weavers’ consolidated profits cross EGP 2.2bn in 2025: https://english.mubasher.info/news/4562972/Oriental-Weavers-consolidated-profits-cross-EGP-2-2bn-in-2025/
  - Oriental Weavers generates EGP 12.5bn consolidated sales in H1-25: https://english.mubasher.info/news/4487417/Oriental-Weavers-generates-EGP-12-5bn-consolidated-sales-in-H1-25/
- RUBX.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Rubex International for Plastic and Acrylic Manufacturing summary=Evidence rejected for RUBX.CA: source text did not clearly match RUBX.CA / Rubex International for Plastic and Acrylic Manufacturing.
- ZEOT.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Extracted Oil & Derivatives Co. summary=Extracted Oils stock nears record high on strong momentum; Extracted Oils stock witnesses increasing buying power amid current resistance – Analysis; Extracted Oils swings to nearly EGP 14.5m net profits in Q1-25/26
  - Extracted Oils stock nears record high on strong momentum: https://english.mubasher.info/news/4599376/Extracted-Oils-stock-nears-record-high-on-strong-momentum/
  - Extracted Oils stock witnesses increasing buying power amid current resistance – Analysis: https://english.mubasher.info/news/4555925/Extracted-Oils-stock-witnesses-increasing-buying-power-amid-current-resistance-Analysis/
  - Extracted Oils swings to nearly EGP 14.5m net profits in Q1-25/26: https://english.mubasher.info/news/4537956/Extracted-Oils-swings-to-nearly-EGP-14-5m-net-profits-in-Q1-25-26/

## Warnings
- Evidence rejected for EFIH.CA: source text did not clearly match EFIH.CA / E-Finance For Digital and Financial Investments.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence rejected for ETEL.CA: source text did not clearly match ETEL.CA / Telecom Egypt.
- Evidence for ACAMD.CA matches the company but appears old; latest detected date is 2020-01-01.
- Evidence rejected for GBCO.CA: source text did not clearly match GBCO.CA / GB Corp.
- Evidence for ARAB.CA matches the company but no source/report date was detected.
- Evidence for ORWE.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for RUBX.CA: source text did not clearly match RUBX.CA / Rubex International for Plastic and Acrylic Manufacturing.
- Evidence for ZEOT.CA matches the company but no source/report date was detected.
