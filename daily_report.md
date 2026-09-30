# Telegram-First EGX Scanner Report

Scan phase: Intraday liquidity update
Generated UTC: 2026-09-30T14:33:37.656618+00:00
Generated Cairo: 2026-09-30 17:33
Run timing: target 11:00 Cairo | generated Cairo 2026-09-30 17:33 | cron 0 8 * * 0-4
Trigger: scheduled cron=0 8 * * 0-4 mapped to intraday; Cairo now 2026-09-30 17:30

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 3
- Tradeable price/liquidity tickers: 168/187
- Top sector: Investment Holding

## Market Context
- Market trend: Bearish
- Source: Mubasher EGX market page (delayed public data)
- As of: Wednesday, September 30
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 5.56% / above MA50 22.22%
- EGX70 regime: BEARISH / above MA20 5.71% / above MA50 17.14%
- Sector breadth: 0.0%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- CCAP.CA: liquidity=596172032.0 spike=0.73 score=22.3
- COMI.CA: liquidity=554237248.0 spike=1.02 score=8.22
- ETEL.CA: liquidity=394168288.0 spike=1.38 score=21.84
- GTWL.CA: liquidity=340087712.0 spike=2.47 score=10.34
- TMGH.CA: liquidity=294948288.0 spike=1.09 score=6.58

## AI Narrative
- Provider: OpenRouter OK
- Model: nvidia/nemotron-3-super-120b-a12b:free
- Summary: Scanner flagged HOLD across all tickets because EGX30 and EGX70 are bearish with weak breadth, shifting risk mode to defensive, so no new buys are allowed despite some bullish‑watch outliers.
- Top‑ranked tickets (BINV.CA, CCAP.CA, ETEL.CA) show bullish watch outlooks but sit in leading sectors (Investment Holding, Telecommunications) with mixed liquidity signals—accumulation spike for BINV.CA, cooling spikes f
- Liquidity, support and resistance levels suggest limited near‑term upside: BINV.CA’s support ~21% below and resistance ~22% above, CCAP.CA’s support 13.5% below/resistance 10% above, ETEL.CA’s tight resistance just 3.2% 
- EGX30 and EGX70 both bearish (<10% above MA20, negative median 5‑day returns) and sector breadth at 0% trigger DEFENSIVE_NO_NEW_BUY risk mode, overriding individual bullish watches and adding uncertainty to the 1‑3‑day o
- Extended momentum, cooling liquidity in many names, and weak market breadth raise the risk of reversal, so the short‑term outlook remains mixed with potential for pull‑backs despite the bullish watch scores.

## Top Liquidity Spikes
- BIOC.CA: spike=4.58 liquidity=275407136.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- RAKT.CA: spike=3.01 liquidity=529908.59 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- GTWL.CA: spike=2.47 liquidity=340087712.0 outlook=WEAK_OR_RISKY score=22 buy_ready=False
- SWDY.CA: spike=2.37 liquidity=154808208.0 outlook=WEAK_OR_RISKY score=22 buy_ready=False
- AXPH.CA: spike=2.19 liquidity=13937233.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False

## Sector Leaderboard
- #1 Investment Holding: score=5.75 5d=-5.69% 20d=14.67% aboveMA50=66.67%
- #2 Telecommunications: score=5.2 5d=-1.84% 20d=9.52% aboveMA50=50.0%
- #3 Energy & Petrochemicals: score=4.56 5d=0.0% 20d=1.89% aboveMA50=66.67%
- #4 Education: score=2.09 5d=-6.04% 20d=9.74% aboveMA50=66.67%
- #5 Textiles: score=2.03 5d=-1.75% 20d=-0.17% aboveMA50=25.0%
- #6 Industrial Goods & Construction: score=1.5 5d=0.0% 20d=0.0% aboveMA50=0.0%
- #7 Transportation & Logistics: score=1.46 5d=-4.29% 20d=-5.12% aboveMA50=50.0%
- #8 Banking & Financials: score=0.44 5d=-3.95% 20d=-4.91% aboveMA50=40.0%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- BINV.CA: BULLISH_WATCH score=90.75 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=momentum is extended; far above support
- CCAP.CA: BULLISH_WATCH score=77.75 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; momentum is extended
- ALCN.CA: BULLISH_WATCH score=77.46 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- ETEL.CA: BULLISH_WATCH score=76.2 liquidity=TRADEABLE sector=LEADING risk=momentum is extended
- CANA.CA: BULLISH_WATCH score=71.44 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; sector is not leading
- ORWE.CA: CONSTRUCTIVE score=65.03 liquidity=TRADEABLE sector=IMPROVING risk=below MA20
- TALM.CA: CONSTRUCTIVE score=60.09 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; below MA20
- RUBX.CA: CONSTRUCTIVE score=59 liquidity=TRADEABLE sector=LAGGING risk=liquidity is cooling; sector is not leading; high short-term volatility
- SNFC.CA: CONSTRUCTIVE score=57 liquidity=TRADEABLE sector=LAGGING risk=liquidity is cooling; momentum is extended; sector is not leading
- CPCI.CA: CONSTRUCTIVE score=56 liquidity=TRADEABLE sector=LAGGING risk=overheated RSI; sector is not leading

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- EKHO.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ARVA.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=5.1 buy_ready=False sector_rank=16 price=243.9 support=240.1 resistance=359.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=21.37 liquidity=7699704.5 spike=0.32
- ABUK.CA: score=15.96 buy_ready=False sector_rank=13 price=85.48 support=85.02 resistance=96.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=35.84 liquidity=111565256.0 spike=0.68
- ACAMD.CA: score=12.4 buy_ready=False sector_rank=16 price=2.02 support=1.87 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=42.0 liquidity=27397066.0 spike=0.53
- ACGC.CA: score=6.21 buy_ready=False sector_rank=5 price=14.65 support=13.8 resistance=14.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=42129212.0 spike=1.7
- ADCI.CA: score=1.08 buy_ready=False sector_rank=16 price=262.55 support=256.0 resistance=311.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=32.21 liquidity=3339518.25 spike=1.17
- ADIB.CA: score=14.18 buy_ready=False sector_rank=8 price=49.3 support=49.0 resistance=54.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=42.01 liquidity=70855640.0 spike=0.87
- ADPC.CA: score=3.92 buy_ready=False sector_rank=16 price=3.48 support=3.4 resistance=4.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=24.1 liquidity=7518196.5 spike=0.41
- AFDI.CA: score=6.23 buy_ready=False sector_rank=16 price=50.5 support=48.03 resistance=56.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=31.43 liquidity=8793905.0 spike=1.02
- AFMC.CA: score=7.4 buy_ready=False sector_rank=16 price=147.48 support=131.0 resistance=190.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=32.66 liquidity=15101536.0 spike=0.3
- AJWA.CA: score=16.4 buy_ready=False sector_rank=16 price=180.07 support=175.15 resistance=188.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=51.37 liquidity=10590182.0 spike=0.66
- ALCN.CA: score=21.58 buy_ready=False sector_rank=7 price=33.01 support=30.4 resistance=34.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=55.25 liquidity=23307642.0 spike=0.64
- ALUM.CA: score=2.07 buy_ready=False sector_rank=16 price=22.83 support=21.65 resistance=30.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=17.0 liquidity=4672282.0 spike=0.73
- AMER.CA: score=7.4 buy_ready=False sector_rank=17 price=4.21 support=4.21 resistance=5.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=26.15 liquidity=38108308.0 spike=0.97
- AMES.CA: score=8.4 buy_ready=False sector_rank=16 price=45.0 support=40.15 resistance=104.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=19.37 liquidity=93878896.0 spike=0.36
- AMIA.CA: score=10.34 buy_ready=False sector_rank=16 price=18.29 support=17.12 resistance=20.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=45.39 liquidity=4936922.5 spike=0.19
- AMOC.CA: score=19.82 buy_ready=False sector_rank=3 price=13.3 support=12.18 resistance=14.63 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=39.17 liquidity=75743312.0 spike=0.51
- APSW.CA: score=-3.19 buy_ready=False sector_rank=16 price=7.93 support=7.81 resistance=8.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=28.46 liquidity=406406.31 spike=0.58
- ARAB.CA: score=7.4 buy_ready=False sector_rank=17 price=0.23 support=0.2 resistance=0.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=25.0 liquidity=47255696.0 spike=0.65
- ARCC.CA: score=7.4 buy_ready=False sector_rank=21 price=62.63 support=60.01 resistance=81.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=13.38 liquidity=20644582.0 spike=0.85
- AREH.CA: score=4.76 buy_ready=False sector_rank=16 price=1.2 support=1.2 resistance=1.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=10.53 liquidity=8357688.0 spike=0.61
- ASCM.CA: score=5.53 buy_ready=False sector_rank=16 price=55.87 support=56.1 resistance=66.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=17.41 liquidity=8131910.0 spike=0.5
- ASPI.CA: score=6.4 buy_ready=False sector_rank=16 price=0.34 support=0.33 resistance=0.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=24.06 liquidity=17916470.0 spike=0.35
- ATLC.CA: score=7.4 buy_ready=False sector_rank=18 price=5.56 support=5.41 resistance=8.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=24.54 liquidity=10269668.0 spike=0.42
- ATQA.CA: score=7.96 buy_ready=False sector_rank=13 price=11.11 support=11.05 resistance=13.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=29.87 liquidity=52431060.0 spike=0.6
- AXPH.CA: score=4.78 buy_ready=False sector_rank=16 price=1442.15 support=1363.0 resistance=1588.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=13937233.0 spike=2.19
- BINV.CA: score=24.22 buy_ready=False sector_rank=1 price=59.92 support=49.51 resistance=72.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=65.39 liquidity=43199696.0 spike=1.96
- BIOC.CA: score=7.4 buy_ready=False sector_rank=16 price=321.63 support=270.0 resistance=321.63 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=275407136.0 spike=4.58
- BTFH.CA: score=7.34 buy_ready=False sector_rank=18 price=2.78 support=2.65 resistance=3.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=28.12 liquidity=129592856.0 spike=1.47
- CAED.CA: score=9.87 buy_ready=False sector_rank=16 price=113.25 support=103.1 resistance=152.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=37.7 liquidity=7469991.5 spike=0.37
- CANA.CA: score=16.79 buy_ready=False sector_rank=8 price=45.91 support=41.35 resistance=52.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=56.75 liquidity=7618218.0 spike=0.31
- CCAP.CA: score=22.3 buy_ready=False sector_rank=1 price=6.64 support=5.85 resistance=7.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=65.77 liquidity=596172032.0 spike=0.73
- CCRS.CA: score=4.03 buy_ready=False sector_rank=16 price=2.22 support=2.23 resistance=2.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=33.96 liquidity=6625658.0 spike=0.37
- CEFM.CA: score=-0.31 buy_ready=False sector_rank=16 price=132.84 support=113.0 resistance=167.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=31.6 liquidity=2292019.75 spike=0.29
- CERA.CA: score=2.4 buy_ready=False sector_rank=16 price=1.26 support=1.18 resistance=1.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=55272584.0 spike=0.37
- CFGH.CA: score=-3.59 buy_ready=False sector_rank=16 price=0.11 support=0.11 resistance=0.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=9.09 liquidity=8576.05 spike=0.63
- CICH.CA: score=-1.42 buy_ready=False sector_rank=18 price=11.51 support=10.75 resistance=13.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=29.97 liquidity=1177849.25 spike=0.19
- CIEB.CA: score=9.86 buy_ready=False sector_rank=8 price=23.49 support=23.56 resistance=26.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=29.7 liquidity=15832981.0 spike=1.34
- CIRA.CA: score=17.84 buy_ready=False sector_rank=4 price=38.08 support=33.2 resistance=41.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=49.37 liquidity=13435599.0 spike=0.35
- CLHO.CA: score=7.45 buy_ready=False sector_rank=14 price=15.19 support=13.9 resistance=18.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=24.54 liquidity=27065196.0 spike=0.49
- CNFN.CA: score=3.24 buy_ready=False sector_rank=18 price=4.01 support=3.84 resistance=4.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=13.68 liquidity=6838914.5 spike=0.66
- COMI.CA: score=8.22 buy_ready=False sector_rank=8 price=126.51 support=126.81 resistance=142.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=15.78 liquidity=554237248.0 spike=1.02
- COPR.CA: score=12.4 buy_ready=False sector_rank=16 price=0.46 support=0.44 resistance=0.53 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=37.5 liquidity=23069368.0 spike=0.75
- COSG.CA: score=6.4 buy_ready=False sector_rank=16 price=1.51 support=1.51 resistance=2.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=16.67 liquidity=16277571.0 spike=0.64
- CPCI.CA: score=10.81 buy_ready=False sector_rank=16 price=576.31 support=530.0 resistance=594.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=79.5 liquidity=3988271.5 spike=1.21
- CSAG.CA: score=9.58 buy_ready=False sector_rank=7 price=35.78 support=35.01 resistance=44.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=20.67 liquidity=10568168.0 spike=0.96
- DAPH.CA: score=7.4 buy_ready=False sector_rank=16 price=92.54 support=91.65 resistance=143.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=11.45 liquidity=17764722.0 spike=0.62
- DEIN.CA: score=5.4 buy_ready=False sector_rank=16 price=10.35 support=10.35 resistance=12.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10 September 11:17 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=49.68 spike=0.01
- DOMT.CA: score=1.03 buy_ready=False sector_rank=15 price=24.05 support=24.01 resistance=29.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=24.72 liquidity=4593120.5 spike=1.02
- DSCW.CA: score=7.86 buy_ready=False sector_rank=16 price=1.62 support=1.67 resistance=1.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=15.15 liquidity=35775576.0 spike=1.73
- DTPP.CA: score=12.4 buy_ready=False sector_rank=16 price=276.65 support=290.0 resistance=380.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=47.09 liquidity=64052268.0 spike=0.76
- EALR.CA: score=-1.22 buy_ready=False sector_rank=16 price=321.91 support=322.52 resistance=411.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=24.9 liquidity=2380997.0 spike=0.19
- EASB.CA: score=2.08 buy_ready=False sector_rank=16 price=7.01 support=6.04 resistance=9.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=27.75 liquidity=4680846.0 spike=0.32
- EAST.CA: score=8.1 buy_ready=False sector_rank=15 price=29.29 support=28.5 resistance=36.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=2.13 liquidity=82572472.0 spike=1.85
- EBSC.CA: score=-1.99 buy_ready=False sector_rank=16 price=1.67 support=1.65 resistance=2.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=14.47 liquidity=1610468.12 spike=0.28
- ECAP.CA: score=-1.41 buy_ready=False sector_rank=16 price=29.98 support=29.13 resistance=34.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=21.37 liquidity=2188775.25 spike=0.34
- EDFM.CA: score=-2.14 buy_ready=False sector_rank=16 price=387.63 support=354.0 resistance=465.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=33.58 liquidity=455047.38 spike=0.26
- EEII.CA: score=8.28 buy_ready=False sector_rank=16 price=2.07 support=2.05 resistance=2.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=34.52 liquidity=9884920.0 spike=0.87
- EFIC.CA: score=6.96 buy_ready=False sector_rank=13 price=162.92 support=147.0 resistance=239.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=9.83 liquidity=23309532.0 spike=0.07
- EFID.CA: score=6.4 buy_ready=False sector_rank=15 price=18.26 support=18.53 resistance=32.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=7.78 liquidity=38892564.0 spike=0.58
- EFIH.CA: score=14.68 buy_ready=False sector_rank=9 price=22.34 support=20.2 resistance=24.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=38.24 liquidity=68460248.0 spike=1.31
- EGAL.CA: score=7.96 buy_ready=False sector_rank=13 price=335.15 support=340.0 resistance=395.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=28.79 liquidity=42123148.0 spike=0.77
- EGAS.CA: score=16.82 buy_ready=False sector_rank=3 price=55.05 support=53.62 resistance=61.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=39.9 liquidity=10282622.0 spike=0.79
- EGBE.CA: score=6.2 buy_ready=False sector_rank=8 price=0.52 support=0.49 resistance=0.53 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=49.02 liquidity=21980.88 spike=0.24
- EGCH.CA: score=12.96 buy_ready=False sector_rank=13 price=13.21 support=13.35 resistance=14.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=39.92 liquidity=78435952.0 spike=0.59
- EGSA.CA: score=3.08 buy_ready=False sector_rank=2 price=8.85 support=8.82 resistance=9.1 source=Yahoo Finance as_of=2026-09-28T21:00:00+00:00 freshness=FRESH RSI=17.24 liquidity=0.0 spike=0.0
- EGTS.CA: score=2.4 buy_ready=False sector_rank=17 price=16.0 support=15.65 resistance=17.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=25894452.0 spike=0.74
- EHDR.CA: score=5.23 buy_ready=False sector_rank=16 price=2.41 support=2.42 resistance=3.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=14.93 liquidity=8833187.0 spike=0.53
- ELEC.CA: score=6.4 buy_ready=False sector_rank=19 price=1.8 support=1.72 resistance=2.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=21.28 liquidity=26501656.0 spike=0.36
- ELKA.CA: score=6.4 buy_ready=False sector_rank=16 price=1.49 support=1.43 resistance=1.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=14.29 liquidity=10148253.0 spike=0.59
- ELNA.CA: score=-3.36 buy_ready=False sector_rank=16 price=35.22 support=33.46 resistance=38.99 source=Yahoo Finance as_of=2026-09-28T21:00:00+00:00 freshness=FRESH RSI=0.0 liquidity=236889.73 spike=0.68
- ELSH.CA: score=5.34 buy_ready=False sector_rank=16 price=11.12 support=10.8 resistance=14.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=16.91 liquidity=7943787.5 spike=0.29
- ELWA.CA: score=-3.26 buy_ready=False sector_rank=16 price=1.48 support=1.51 resistance=1.92 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=6.06 liquidity=335039.88 spike=0.3
- EMFD.CA: score=2.4 buy_ready=False sector_rank=17 price=13.56 support=11.7 resistance=13.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=78561720.0 spike=0.73
- ENGC.CA: score=7.26 buy_ready=False sector_rank=16 price=34.57 support=35.7 resistance=46.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=22.75 liquidity=25292774.0 spike=1.43
- EOSB.CA: score=7.42 buy_ready=False sector_rank=16 price=1.57 support=1.53 resistance=1.64 source=Yahoo Finance as_of=2026-09-28T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=17401.88 spike=0.32
- EPCO.CA: score=0.8 buy_ready=False sector_rank=16 price=9.5 support=9.25 resistance=12.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=33.92 liquidity=3402881.75 spike=0.23
- EPPK.CA: score=-7.18 buy_ready=False sector_rank=16 price=10.29 support=10.29 resistance=10.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=8 September 01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=419183.72 spike=0.28
- ETEL.CA: score=21.84 buy_ready=False sector_rank=2 price=135.67 support=113.5 resistance=140.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=65.7 liquidity=394168288.0 spike=1.38
- ETRS.CA: score=7.56 buy_ready=False sector_rank=16 price=10.13 support=9.92 resistance=11.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=22.33 liquidity=11825734.0 spike=1.08
- EXPA.CA: score=17.18 buy_ready=False sector_rank=8 price=20.91 support=20.6 resistance=22.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=48.73 liquidity=34479148.0 spike=1.0
- FAIT.CA: score=8.34 buy_ready=False sector_rank=8 price=43.53 support=38.48 resistance=48.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=25.27 liquidity=5861063.5 spike=1.15
- FAITA.CA: score=-1.8 buy_ready=False sector_rank=8 price=0.98 support=0.98 resistance=1.0 source=Yahoo Finance as_of=2026-09-28T21:00:00+00:00 freshness=FRESH RSI=31.82 liquidity=25134.29 spike=0.73
- FERC.CA: score=-0.95 buy_ready=False sector_rank=13 price=74.22 support=70.42 resistance=86.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=31.91 liquidity=2089312.75 spike=0.17
- FWRY.CA: score=8.22 buy_ready=False sector_rank=9 price=18.24 support=17.5 resistance=19.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=11.63 liquidity=109417744.0 spike=1.08
- GBCO.CA: score=14.68 buy_ready=False sector_rank=10 price=29.89 support=27.0 resistance=32.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=45.18 liquidity=107033504.0 spike=1.51
- GDWA.CA: score=6.4 buy_ready=False sector_rank=16 price=0.65 support=0.61 resistance=0.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=7.69 liquidity=16581422.0 spike=0.47
- GGCC.CA: score=7.4 buy_ready=False sector_rank=16 price=0.67 support=0.67 resistance=0.91 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=21.47 liquidity=12187484.0 spike=0.69
- GIHD.CA: score=2.4 buy_ready=False sector_rank=16 price=62.25 support=60.9 resistance=68.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=17927806.0 spike=0.63
- GMCI.CA: score=-0.97 buy_ready=False sector_rank=16 price=1.57 support=1.5 resistance=1.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:52 PM market time freshness=DELAYED_CURRENT RSI=6.67 liquidity=887180.44 spike=1.87
- GRCA.CA: score=0.49 buy_ready=False sector_rank=16 price=33.94 support=32.11 resistance=63.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=13.7 liquidity=4092791.25 spike=0.13
- GSSC.CA: score=-1.68 buy_ready=False sector_rank=16 price=257.26 support=246.0 resistance=333.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=31.61 liquidity=922485.88 spike=0.12
- GTWL.CA: score=10.34 buy_ready=False sector_rank=16 price=145.03 support=151.96 resistance=248.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=14.1 liquidity=340087712.0 spike=2.47
- HDBK.CA: score=16.18 buy_ready=False sector_rank=8 price=104.35 support=105.5 resistance=124.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=41.33 liquidity=24461472.0 spike=0.53
- HELI.CA: score=12.4 buy_ready=False sector_rank=17 price=7.25 support=7.02 resistance=8.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=35.29 liquidity=78266080.0 spike=0.5
- HRHO.CA: score=7.06 buy_ready=False sector_rank=18 price=23.67 support=23.02 resistance=26.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=10.96 liquidity=97087872.0 spike=1.33
- ICID.CA: score=3.14 buy_ready=False sector_rank=16 price=18.76 support=17.06 resistance=18.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=11352350.0 spike=1.37
- IDRE.CA: score=7.16 buy_ready=False sector_rank=16 price=45.86 support=45.0 resistance=59.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=34.37 liquidity=9757540.0 spike=0.6
- IFAP.CA: score=3.95 buy_ready=False sector_rank=11 price=19.43 support=17.17 resistance=23.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=26.61 liquidity=6428887.5 spike=0.39
- INFI.CA: score=4.32 buy_ready=False sector_rank=16 price=117.2 support=104.0 resistance=160.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=19.19 liquidity=6920150.0 spike=0.41
- IRON.CA: score=4.07 buy_ready=False sector_rank=13 price=25.29 support=25.82 resistance=30.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=29.03 liquidity=7109732.5 spike=0.55
- ISMA.CA: score=3.75 buy_ready=False sector_rank=16 price=23.01 support=23.6 resistance=34.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=21.2 liquidity=6353790.5 spike=0.41
- ISMQ.CA: score=6.96 buy_ready=False sector_rank=13 price=7.81 support=7.7 resistance=9.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=18.53 liquidity=14450850.0 spike=0.62
- ISPH.CA: score=6.45 buy_ready=False sector_rank=14 price=11.49 support=11.22 resistance=13.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=21.56 liquidity=58237772.0 spike=0.85
- JUFO.CA: score=6.4 buy_ready=False sector_rank=15 price=24.67 support=24.5 resistance=27.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=19.49 liquidity=16627731.0 spike=0.85
- KABO.CA: score=6.31 buy_ready=False sector_rank=5 price=9.16 support=8.0 resistance=9.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=57301544.0 spike=1.75
- KWIN.CA: score=5.57 buy_ready=False sector_rank=16 price=76.52 support=74.0 resistance=118.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=27.5 liquidity=8172214.5 spike=0.43
- KZPC.CA: score=6.66 buy_ready=False sector_rank=16 price=12.59 support=12.8 resistance=14.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=25.08 liquidity=6263170.0 spike=0.22
- LCSW.CA: score=2.4 buy_ready=False sector_rank=21 price=33.3 support=28.86 resistance=33.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=13275335.0 spike=0.63
- LUTS.CA: score=2.4 buy_ready=False sector_rank=16 price=0.88 support=0.8 resistance=0.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=72891928.0 spike=0.7
- MAAL.CA: score=-2.24 buy_ready=False sector_rank=16 price=10.24 support=9.77 resistance=10.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=5360645.0 spike=0.24
- MASR.CA: score=7.4 buy_ready=False sector_rank=16 price=7.5 support=6.82 resistance=8.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=27.0 liquidity=40533656.0 spike=0.42
- MBSC.CA: score=7.4 buy_ready=False sector_rank=21 price=290.13 support=295.22 resistance=464.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=0.89 liquidity=27154464.0 spike=0.73
- MCQE.CA: score=6.4 buy_ready=False sector_rank=21 price=179.16 support=180.04 resistance=254.23 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=13.46 liquidity=14832554.0 spike=0.69
- MCRO.CA: score=7.4 buy_ready=False sector_rank=16 price=1.5 support=1.41 resistance=1.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=27.45 liquidity=43753132.0 spike=0.35
- MENA.CA: score=-1.98 buy_ready=False sector_rank=17 price=6.2 support=5.8 resistance=7.07 source=Yahoo Finance as_of=2026-09-28T21:00:00+00:00 freshness=FRESH RSI=27.73 liquidity=624048.58 spike=0.46
- MEPA.CA: score=4.21 buy_ready=False sector_rank=16 price=1.63 support=1.6 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=12.7 liquidity=7814909.5 spike=0.21
- MFPC.CA: score=15.96 buy_ready=False sector_rank=13 price=44.83 support=42.81 resistance=51.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=42.8 liquidity=47786596.0 spike=0.3
- MFSC.CA: score=7.59 buy_ready=False sector_rank=16 price=48.2 support=45.22 resistance=58.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=38.29 liquidity=4990828.5 spike=1.1
- MHOT.CA: score=11.27 buy_ready=False sector_rank=12 price=16.84 support=16.61 resistance=21.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=43.27 liquidity=9118383.0 spike=0.52
- MICH.CA: score=7.78 buy_ready=False sector_rank=16 price=44.99 support=42.5 resistance=52.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=19.56 liquidity=15410833.0 spike=1.19
- MILS.CA: score=3.29 buy_ready=False sector_rank=16 price=176.16 support=165.5 resistance=232.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=28.6 liquidity=5888311.5 spike=0.32
- MIPH.CA: score=4.22 buy_ready=False sector_rank=14 price=779.68 support=739.69 resistance=1000.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=46.59 liquidity=1766763.13 spike=0.19
- MOED.CA: score=5.69 buy_ready=False sector_rank=16 price=0.63 support=0.59 resistance=0.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=10.81 liquidity=9288520.0 spike=0.19
- MOIL.CA: score=11.03 buy_ready=False sector_rank=3 price=0.7 support=0.67 resistance=0.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=80.0 liquidity=210818.84 spike=0.86
- MOIN.CA: score=5.58 buy_ready=False sector_rank=16 price=33.68 support=32.5 resistance=45.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=31.23 liquidity=8184249.5 spike=0.27
- MOSC.CA: score=-1.61 buy_ready=False sector_rank=16 price=261.78 support=257.0 resistance=329.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=22.37 liquidity=986611.13 spike=0.26
- MPCI.CA: score=7.58 buy_ready=False sector_rank=16 price=328.83 support=335.01 resistance=467.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=12.36 liquidity=125930472.0 spike=1.09
- MPCO.CA: score=16.52 buy_ready=False sector_rank=11 price=2.35 support=2.08 resistance=3.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=52.75 liquidity=117033424.0 spike=0.62
- MPRC.CA: score=12.4 buy_ready=False sector_rank=16 price=37.77 support=37.65 resistance=44.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=37.77 liquidity=11328003.0 spike=0.37
- MTIE.CA: score=7.94 buy_ready=False sector_rank=10 price=7.83 support=7.5 resistance=8.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=21.43 liquidity=24627242.0 spike=1.14
- NAHO.CA: score=5.41 buy_ready=False sector_rank=16 price=0.13 support=0.12 resistance=0.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=40.0 liquidity=7634.54 spike=0.17
- NCCW.CA: score=15.4 buy_ready=False sector_rank=16 price=7.01 support=5.96 resistance=8.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=48.32 liquidity=27361704.0 spike=0.34
- NEDA.CA: score=-1.71 buy_ready=False sector_rank=16 price=2.61 support=2.48 resistance=2.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=34.09 liquidity=893392.81 spike=0.96
- NHPS.CA: score=6.4 buy_ready=False sector_rank=16 price=68.59 support=69.5 resistance=91.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=30.44 liquidity=13960007.0 spike=0.97
- NINH.CA: score=3.92 buy_ready=False sector_rank=16 price=19.0 support=18.53 resistance=24.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=22.59 liquidity=6518855.0 spike=0.39
- NIPH.CA: score=12.45 buy_ready=False sector_rank=14 price=315.11 support=290.0 resistance=368.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=37.74 liquidity=125318792.0 spike=1.0
- OBRI.CA: score=6.04 buy_ready=False sector_rank=16 price=23.91 support=23.67 resistance=34.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=11.9 liquidity=9644193.0 spike=0.87
- OCDI.CA: score=7.4 buy_ready=False sector_rank=17 price=25.39 support=24.5 resistance=34.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=5.43 liquidity=25586392.0 spike=0.39
- OCPH.CA: score=-1.23 buy_ready=False sector_rank=16 price=213.43 support=190.0 resistance=263.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=16.24 liquidity=2370981.0 spike=0.46
- ODIN.CA: score=2.83 buy_ready=False sector_rank=16 price=2.44 support=2.35 resistance=3.06 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=30.39 liquidity=5429136.0 spike=0.41
- OFH.CA: score=2.52 buy_ready=False sector_rank=16 price=0.97 support=0.86 resistance=0.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=137826448.0 spike=1.06
- OIH.CA: score=14.3 buy_ready=False sector_rank=1 price=1.84 support=1.7 resistance=2.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=17.65 liquidity=78359544.0 spike=0.7
- OLFI.CA: score=13.64 buy_ready=False sector_rank=15 price=21.61 support=21.2 resistance=23.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=38.71 liquidity=31643564.0 spike=2.12
- ORAS.CA: score=4.6 buy_ready=False sector_rank=6 price=790.21 support=763.0 resistance=797.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=157466320.0 spike=1.0
- ORHD.CA: score=7.4 buy_ready=False sector_rank=17 price=37.62 support=38.02 resistance=44.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=33.98 liquidity=130895784.0 spike=0.79
- ORWE.CA: score=17.81 buy_ready=False sector_rank=5 price=26.77 support=26.01 resistance=29.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=40.77 liquidity=51708064.0 spike=0.98
- PHAR.CA: score=4.01 buy_ready=False sector_rank=14 price=113.83 support=105.52 resistance=113.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=148109392.0 spike=1.78
- PHDC.CA: score=7.66 buy_ready=False sector_rank=17 price=12.7 support=12.5 resistance=15.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=12.35 liquidity=148640992.0 spike=1.13
- PHTV.CA: score=3.14 buy_ready=False sector_rank=16 price=335.92 support=320.11 resistance=378.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=40.66 liquidity=744604.0 spike=0.46
- POUL.CA: score=7.6 buy_ready=False sector_rank=15 price=9.87 support=9.12 resistance=41.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=5.77 liquidity=46862412.0 spike=1.6
- PRCL.CA: score=2.4 buy_ready=False sector_rank=21 price=23.41 support=22.8 resistance=25.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=10399997.0 spike=0.7
- PRDC.CA: score=7.4 buy_ready=False sector_rank=17 price=7.22 support=6.81 resistance=9.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=26.19 liquidity=10818956.0 spike=0.29
- PRMH.CA: score=0.58 buy_ready=False sector_rank=16 price=2.19 support=2.2 resistance=2.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=22.77 liquidity=4175232.5 spike=0.73
- RACC.CA: score=2.38 buy_ready=False sector_rank=16 price=8.85 support=8.51 resistance=10.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=27.09 liquidity=5984843.5 spike=0.47
- RAKT.CA: score=0.95 buy_ready=False sector_rank=16 price=21.32 support=21.02 resistance=23.0 source=Yahoo Finance as_of=2026-09-28T21:00:00+00:00 freshness=FRESH RSI=21.01 liquidity=529908.59 spike=3.01
- RAYA.CA: score=7.4 buy_ready=False sector_rank=20 price=6.2 support=5.72 resistance=7.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=19.62 liquidity=31688446.0 spike=0.59
- RMDA.CA: score=7.45 buy_ready=False sector_rank=14 price=5.28 support=4.83 resistance=6.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=13.67 liquidity=30877150.0 spike=0.58
- ROTO.CA: score=3.75 buy_ready=False sector_rank=16 price=37.06 support=35.02 resistance=44.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=21.7 liquidity=6348817.0 spike=0.82
- RREI.CA: score=2.4 buy_ready=False sector_rank=16 price=3.91 support=3.53 resistance=3.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=10311700.0 spike=0.73
- RTVC.CA: score=0.12 buy_ready=False sector_rank=16 price=3.48 support=3.39 resistance=4.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=18.18 liquidity=3221825.75 spike=1.25
- RUBX.CA: score=19.4 buy_ready=False sector_rank=16 price=14.31 support=12.55 resistance=18.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=53.43 liquidity=47938864.0 spike=0.71
- SAUD.CA: score=9.32 buy_ready=False sector_rank=8 price=22.16 support=21.6 resistance=26.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=40.76 liquidity=5148153.5 spike=0.26
- SCEM.CA: score=7.4 buy_ready=False sector_rank=21 price=75.91 support=76.0 resistance=105.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=3.88 liquidity=20139336.0 spike=0.28
- SCFM.CA: score=-0.58 buy_ready=False sector_rank=16 price=238.84 support=223.11 resistance=315.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=29.59 liquidity=3020874.5 spike=0.49
- SCTS.CA: score=1.44 buy_ready=False sector_rank=4 price=527.44 support=520.3 resistance=639.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=16.31 liquidity=1599735.38 spike=0.75
- SDTI.CA: score=14.4 buy_ready=False sector_rank=16 price=83.75 support=69.15 resistance=94.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=76.49 liquidity=11262444.0 spike=0.32
- SEIG.CA: score=-2.06 buy_ready=False sector_rank=16 price=212.28 support=211.15 resistance=268.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:10 PM market time freshness=DELAYED_CURRENT RSI=32.01 liquidity=537446.31 spike=0.3
- SIPC.CA: score=10.4 buy_ready=False sector_rank=16 price=5.1 support=4.22 resistance=7.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=32.14 liquidity=23021730.0 spike=0.32
- SKPC.CA: score=6.96 buy_ready=False sector_rank=13 price=15.83 support=15.7 resistance=19.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=18.99 liquidity=77729472.0 spike=0.58
- SMFR.CA: score=-1.12 buy_ready=False sector_rank=16 price=208.93 support=205.01 resistance=274.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=14.71 liquidity=1477217.13 spike=0.22
- SNFC.CA: score=16.23 buy_ready=False sector_rank=16 price=11.36 support=10.26 resistance=11.71 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=66.88 liquidity=8828868.0 spike=0.63
- SPIN.CA: score=5.67 buy_ready=False sector_rank=5 price=16.38 support=15.11 resistance=20.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=21.0 liquidity=5859497.0 spike=0.8
- SPMD.CA: score=9.62 buy_ready=False sector_rank=16 price=0.38 support=0.37 resistance=0.62 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=40.83 liquidity=8223340.0 spike=0.11
- SUGR.CA: score=7.4 buy_ready=False sector_rank=15 price=51.58 support=51.2 resistance=64.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=28.36 liquidity=11092725.0 spike=0.38
- SVCE.CA: score=7.4 buy_ready=False sector_rank=16 price=9.54 support=9.6 resistance=13.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=10.4 liquidity=42435544.0 spike=0.27
- SWDY.CA: score=10.14 buy_ready=False sector_rank=19 price=104.84 support=107.77 resistance=139.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=10.95 liquidity=154808208.0 spike=2.37
- TALM.CA: score=17.84 buy_ready=False sector_rank=4 price=18.99 support=17.61 resistance=25.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=58.43 liquidity=24312682.0 spike=0.37
- TMGH.CA: score=6.58 buy_ready=False sector_rank=17 price=86.82 support=86.1 resistance=100.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=8.44 liquidity=294948288.0 spike=1.09
- TRTO.CA: score=-2.6 buy_ready=False sector_rank=16 price=0.05 support=0.05 resistance=0.08 source=Yahoo Finance as_of=2026-09-28T21:00:00+00:00 freshness=FRESH RSI=0.0 liquidity=3186.0 spike=0.13
- UEFM.CA: score=11.24 buy_ready=False sector_rank=16 price=490.0 support=421.1 resistance=574.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=46.56 liquidity=7596696.0 spike=2.12
- UEGC.CA: score=6.4 buy_ready=False sector_rank=16 price=1.47 support=1.41 resistance=1.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=22.22 liquidity=29134212.0 spike=0.75
- UNIP.CA: score=1.09 buy_ready=False sector_rank=16 price=0.34 support=0.32 resistance=0.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=8690775.0 spike=0.43
- UNIT.CA: score=4.13 buy_ready=False sector_rank=17 price=16.68 support=16.66 resistance=23.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=40.08 liquidity=1731236.5 spike=0.12
- WCDF.CA: score=2.36 buy_ready=False sector_rank=16 price=630.26 support=575.5 resistance=796.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=33.39 liquidity=4961371.5 spike=0.88
- WKOL.CA: score=5.13 buy_ready=False sector_rank=16 price=277.26 support=291.0 resistance=379.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=19.86 liquidity=8732442.0 spike=0.65
- ZEOT.CA: score=1.21 buy_ready=False sector_rank=16 price=11.65 support=10.6 resistance=14.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=16.3 liquidity=3811007.0 spike=0.63
- ZMID.CA: score=7.4 buy_ready=False sector_rank=17 price=7.44 support=7.2 resistance=9.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=11.95 liquidity=79061424.0 spike=0.48

## Backtesting Lite
- BINV.CA: 180d return=56.72%, max drawdown=-17.77%, MA20>MA50 days last20=20, as_of=2026-09-28T21:00:00+00:00
- CCAP.CA: 180d return=103.59%, max drawdown=-17.02%, MA20>MA50 days last20=20, as_of=2026-09-28T21:00:00+00:00
- ETEL.CA: 180d return=100.57%, max drawdown=-30.44%, MA20>MA50 days last20=20, as_of=2026-09-28T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- BINV.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=B Investments Holding summary=Evidence rejected for BINV.CA: source text did not clearly match BINV.CA / B Investments Holding.
- CCAP.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Qalaa Holdings summary=Evidence rejected for CCAP.CA: source text did not clearly match CCAP.CA / Qalaa Holdings.
- ETEL.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Telecom Egypt summary=Evidence rejected for ETEL.CA: source text did not clearly match ETEL.CA / Telecom Egypt.
- ALCN.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Alexandria Containers and Cargo Handling summary=Evidence rejected for ALCN.CA: source text did not clearly match ALCN.CA / Alexandria Containers and Cargo Handling.
- AMOC.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Alexandria Mineral Oils summary=AMOC achieves EGP 10.5bn consolidated sales in Q1-26; AMOC studies potential project with Germany’s SULZER; AMOC to pay out EGP 0.4/shr dividends for H2-25
  - AMOC achieves EGP 10.5bn consolidated sales in Q1-26: https://english.mubasher.info/news/4604903/AMOC-achieves-EGP-10-5bn-consolidated-sales-in-Q1-26/
  - AMOC studies potential project with Germany’s SULZER: https://english.mubasher.info/news/4586853/AMOC-studies-potential-project-with-Germany-s-SULZER/
  - AMOC to pay out EGP 0.4/shr dividends for H2-25: https://english.mubasher.info/news/4586775/AMOC-to-pay-out-EGP-0-4-shr-dividends-for-H2-25/
- RUBX.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Rubex International for Plastic and Acrylic Manufacturing summary=Evidence rejected for RUBX.CA: source text did not clearly match RUBX.CA / Rubex International for Plastic and Acrylic Manufacturing.
- TALM.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Talim Management Services summary=Evidence rejected for TALM.CA: source text did not clearly match TALM.CA / Talim Management Services.
- CIRA.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Cairo Investment and Real Estate Development summary=CIRA Education take over 51% of L’École Française Hurghada; CIRA’s majority shareholder acquires 37.5% additional equity, backs regional expansion; CIRA Education launches Middle East’s 1st initiative for care economy
  - CIRA Education take over 51% of L’École Française Hurghada: https://english.mubasher.info/news/4488666/CIRA-Education-take-over-51-of-L-%C3%89cole-Fran%C3%A7aise-Hurghada/
  - CIRA’s majority shareholder acquires 37.5% additional equity, backs regional expansion: https://english.mubasher.info/news/4393636/CIRA-s-majority-shareholder-acquires-37-5-additional-equity-backs-regional-expansion/
  - CIRA Education launches Middle East’s 1st initiative for care economy: https://english.mubasher.info/news/4391766/CIRA-Education-launches-Middle-East-s-1st-initiative-for-care-economy/

## Warnings
- Evidence rejected for BINV.CA: source text did not clearly match BINV.CA / B Investments Holding.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence rejected for CCAP.CA: source text did not clearly match CCAP.CA / Qalaa Holdings.
- Evidence rejected for ETEL.CA: source text did not clearly match ETEL.CA / Telecom Egypt.
- Evidence rejected for ALCN.CA: source text did not clearly match ALCN.CA / Alexandria Containers and Cargo Handling.
- Evidence for AMOC.CA matches the company but no source/report date was detected.
- Evidence rejected for RUBX.CA: source text did not clearly match RUBX.CA / Rubex International for Plastic and Acrylic Manufacturing.
- Evidence rejected for TALM.CA: source text did not clearly match TALM.CA / Talim Management Services.
- Evidence for CIRA.CA matches the company but no source/report date was detected.
