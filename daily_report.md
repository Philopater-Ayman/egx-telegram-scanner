# Telegram-First EGX Scanner Report

Scan phase: Pre-market risk check
Generated UTC: 2026-09-30T11:23:38.411482+00:00
Generated Cairo: 2026-09-30 14:23
Run timing: target 08:45 Cairo | generated Cairo 2026-09-30 14:23 | cron 45 5 * * 0-4
Trigger: scheduled cron=45 5 * * 0-4 mapped to pre_market; Cairo now 2026-09-30 14:20

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 3
- Tradeable price/liquidity tickers: 176/187
- Top sector: Investment Holding

## Market Context
- Market trend: Bearish
- Source: Mubasher EGX market page (delayed public data)
- As of: Wednesday, September 30
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 5.26% / above MA50 21.05%
- EGX70 regime: BEARISH / above MA20 5.13% / above MA50 17.95%
- Sector breadth: 0.0%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- CCAP.CA: liquidity=535988064.0 spike=0.66 score=22.26
- COMI.CA: liquidity=421971616.0 spike=0.77 score=7.9
- ETEL.CA: liquidity=366311616.0 spike=1.28 score=21.61
- GTWL.CA: liquidity=328793472.0 spike=2.39 score=5.18
- BIOC.CA: liquidity=245310656.0 spike=4.08 score=7.4

## AI Narrative
- Provider: OpenRouter OK
- Model: nvidia/nemotron-3-super-120b-a12b:free
- Summary: EGX30 and EGX70 are bearish with weak breadth, triggering a defensive risk mode that blocks new buys; the scanner flagged a few stocks with strong rank scores and bullish‑watch outlooks, but their near‑term support/resistance positioning and liquidity spikes are outweighed by the broader market downturn.
- BINV.CA, CCAP.CA, ETEL.CA show high rank scores, bullish‑watch outlooks and liquidity accumulation/spikes, yet sit 5‑25% below 20‑day resistance and above support, giving limited upside room in a bearish regime.
- ALCN.CA and AMOC.CA have moderate scores and tradeable liquidity, but AMOC’s RSI is low and both are below their 20‑day averages, indicating weak near‑term momentum.
- Sector breadth is 0.0% and leading sectors (Investment Holding, Telecommunications, Energy & Petrochemicals) still show mixed returns, so the defensive risk mode overrides individual bullish signals.
- Uncertainty remains: liquidity spikes may be short‑lived, and if the EGX30/EGX70 trend reverses, the watched stocks could break resistance; otherwise, downside pressure likely persists.

## Top Liquidity Spikes
- BIOC.CA: spike=4.08 liquidity=245310656.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- RAKT.CA: spike=3.01 liquidity=529908.59 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- GTWL.CA: spike=2.39 liquidity=328793472.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- SWDY.CA: spike=2.09 liquidity=136747632.0 outlook=WEAK_OR_RISKY score=22 buy_ready=False
- UEFM.CA: spike=2.06 liquidity=7368846.0 outlook=NEUTRAL score=37 buy_ready=False

## Sector Leaderboard
- #1 Investment Holding: score=5.65 5d=-5.69% 20d=14.67% aboveMA50=66.67%
- #2 Telecommunications: score=5.13 5d=-1.84% 20d=9.52% aboveMA50=50.0%
- #3 Energy & Petrochemicals: score=4.46 5d=0.0% 20d=1.89% aboveMA50=66.67%
- #4 Education: score=2.03 5d=-6.04% 20d=9.74% aboveMA50=66.67%
- #5 Industrial Goods & Construction: score=1.5 5d=0.0% 20d=0.0% aboveMA50=0.0%
- #6 Transportation & Logistics: score=1.41 5d=-4.29% 20d=-5.12% aboveMA50=50.0%
- #7 Fintech & Payments: score=-0.08 5d=-2.72% 20d=-2.81% aboveMA50=0.0%
- #8 Banking & Financials: score=-0.25 5d=-3.95% 20d=-4.91% aboveMA50=30.0%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- BINV.CA: BULLISH_WATCH score=94.65 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=momentum is extended
- CCAP.CA: BULLISH_WATCH score=77.65 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; momentum is extended
- ETEL.CA: BULLISH_WATCH score=76.13 liquidity=TRADEABLE sector=LEADING risk=momentum is extended
- ALCN.CA: BULLISH_WATCH score=71.41 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- CANA.CA: BULLISH_WATCH score=71 liquidity=TRADEABLE sector=LAGGING risk=liquidity is cooling; sector is not leading
- TALM.CA: CONSTRUCTIVE score=60.03 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; below MA20
- RUBX.CA: CONSTRUCTIVE score=59 liquidity=TRADEABLE sector=LAGGING risk=liquidity is cooling; sector is not leading; high short-term volatility
- ORWE.CA: CONSTRUCTIVE score=58 liquidity=TRADEABLE sector=LAGGING risk=below MA20; sector is not leading
- SNFC.CA: CONSTRUCTIVE score=57 liquidity=TRADEABLE sector=LAGGING risk=liquidity is cooling; momentum is extended; sector is not leading
- CPCI.CA: CONSTRUCTIVE score=56 liquidity=TRADEABLE sector=LAGGING risk=overheated RSI; sector is not leading

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- EKHO.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ARVA.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=3.86 buy_ready=False sector_rank=16 price=242.96 support=240.1 resistance=359.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=21.37 liquidity=6455732.5 spike=0.27
- ABUK.CA: score=15.9 buy_ready=False sector_rank=13 price=85.05 support=85.02 resistance=96.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=35.84 liquidity=103765528.0 spike=0.64
- ACAMD.CA: score=12.4 buy_ready=False sector_rank=16 price=2.02 support=1.87 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=42.0 liquidity=20811992.0 spike=0.4
- ACGC.CA: score=11.85 buy_ready=False sector_rank=9 price=14.05 support=13.11 resistance=16.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=34.72 liquidity=21739270.0 spike=0.88
- ADCI.CA: score=0.44 buy_ready=False sector_rank=16 price=258.05 support=256.0 resistance=311.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=32.21 liquidity=2960160.5 spike=1.04
- ADIB.CA: score=13.9 buy_ready=False sector_rank=8 price=49.23 support=49.0 resistance=54.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=42.01 liquidity=61081016.0 spike=0.75
- ADPC.CA: score=3.16 buy_ready=False sector_rank=16 price=3.46 support=3.4 resistance=4.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=24.1 liquidity=6755709.5 spike=0.37
- AFDI.CA: score=5.86 buy_ready=False sector_rank=16 price=50.5 support=48.03 resistance=56.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:00 PM market time freshness=DELAYED_CURRENT RSI=31.43 liquidity=8458527.0 spike=0.98
- AFMC.CA: score=7.4 buy_ready=False sector_rank=16 price=145.04 support=131.0 resistance=190.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=32.66 liquidity=13379093.0 spike=0.26
- AJWA.CA: score=16.4 buy_ready=False sector_rank=16 price=180.07 support=175.15 resistance=188.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=51.37 liquidity=10582802.0 spike=0.66
- ALCN.CA: score=21.56 buy_ready=False sector_rank=6 price=33.05 support=30.4 resistance=34.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=55.25 liquidity=21762414.0 spike=0.6
- ALUM.CA: score=0.44 buy_ready=False sector_rank=16 price=22.5 support=21.65 resistance=30.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=17.0 liquidity=4036486.75 spike=0.63
- AMER.CA: score=7.4 buy_ready=False sector_rank=15 price=4.18 support=4.21 resistance=5.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=26.15 liquidity=32489638.0 spike=0.83
- AMES.CA: score=8.4 buy_ready=False sector_rank=16 price=44.61 support=40.15 resistance=104.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=19.37 liquidity=80334152.0 spike=0.31
- AMIA.CA: score=9.25 buy_ready=False sector_rank=16 price=18.42 support=17.12 resistance=20.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:00 PM market time freshness=DELAYED_CURRENT RSI=45.39 liquidity=3851544.5 spike=0.15
- AMOC.CA: score=19.78 buy_ready=False sector_rank=3 price=13.24 support=12.18 resistance=14.63 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=39.17 liquidity=64327928.0 spike=0.44
- APSW.CA: score=-3.2 buy_ready=False sector_rank=16 price=7.92 support=7.81 resistance=8.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=28.46 liquidity=398953.22 spike=0.57
- ARAB.CA: score=7.4 buy_ready=False sector_rank=15 price=0.23 support=0.2 resistance=0.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=25.0 liquidity=39909968.0 spike=0.55
- ARCC.CA: score=7.4 buy_ready=False sector_rank=21 price=62.51 support=60.01 resistance=81.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=13.38 liquidity=18224348.0 spike=0.75
- AREH.CA: score=3.8 buy_ready=False sector_rank=16 price=1.19 support=1.2 resistance=1.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=10.53 liquidity=7399140.5 spike=0.54
- ASCM.CA: score=4.79 buy_ready=False sector_rank=16 price=55.44 support=56.1 resistance=66.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=17.41 liquidity=7393315.5 spike=0.45
- ASPI.CA: score=6.4 buy_ready=False sector_rank=16 price=0.34 support=0.33 resistance=0.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=24.06 liquidity=16107819.0 spike=0.31
- ATLC.CA: score=6.82 buy_ready=False sector_rank=18 price=5.43 support=5.41 resistance=8.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=24.54 liquidity=9420547.0 spike=0.39
- ATQA.CA: score=7.9 buy_ready=False sector_rank=13 price=11.18 support=11.05 resistance=13.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=29.87 liquidity=42570128.0 spike=0.48
- AXPH.CA: score=4.5 buy_ready=False sector_rank=16 price=1442.18 support=1363.0 resistance=1588.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=13044902.0 spike=2.05
- BINV.CA: score=23.98 buy_ready=False sector_rank=1 price=59.3 support=49.51 resistance=72.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=65.39 liquidity=41165656.0 spike=1.86
- BIOC.CA: score=7.4 buy_ready=False sector_rank=16 price=315.96 support=270.0 resistance=317.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=245310656.0 spike=4.08
- BTFH.CA: score=6.9 buy_ready=False sector_rank=18 price=2.76 support=2.65 resistance=3.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=28.12 liquidity=110005048.0 spike=1.25
- CAED.CA: score=9.49 buy_ready=False sector_rank=16 price=112.52 support=103.1 resistance=152.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=37.7 liquidity=7091381.0 spike=0.35
- CANA.CA: score=16.03 buy_ready=False sector_rank=8 price=45.66 support=41.35 resistance=52.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=56.75 liquidity=7125226.0 spike=0.29
- CCAP.CA: score=22.26 buy_ready=False sector_rank=1 price=6.62 support=5.85 resistance=7.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=65.77 liquidity=535988064.0 spike=0.66
- CCRS.CA: score=1.31 buy_ready=False sector_rank=16 price=2.3 support=2.23 resistance=2.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=33.96 liquidity=3910558.75 spike=0.22
- CEFM.CA: score=-0.63 buy_ready=False sector_rank=16 price=131.62 support=113.0 resistance=167.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=31.6 liquidity=1966703.38 spike=0.25
- CERA.CA: score=6.4 buy_ready=False sector_rank=16 price=1.23 support=1.18 resistance=2.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=17.07 liquidity=47355408.0 spike=0.32
- CFGH.CA: score=-3.59 buy_ready=False sector_rank=16 price=0.11 support=0.11 resistance=0.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=9.09 liquidity=8576.05 spike=0.63
- CICH.CA: score=-1.58 buy_ready=False sector_rank=18 price=11.47 support=10.75 resistance=13.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=29.97 liquidity=1020846.06 spike=0.16
- CIEB.CA: score=9.2 buy_ready=False sector_rank=8 price=23.5 support=23.56 resistance=26.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=29.7 liquidity=13640125.0 spike=1.15
- CIRA.CA: score=17.81 buy_ready=False sector_rank=4 price=38.12 support=33.2 resistance=41.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=49.37 liquidity=12814664.0 spike=0.33
- CLHO.CA: score=7.4 buy_ready=False sector_rank=17 price=15.15 support=13.9 resistance=18.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=24.54 liquidity=23388204.0 spike=0.42
- CNFN.CA: score=2.53 buy_ready=False sector_rank=18 price=3.97 support=3.84 resistance=4.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:00 PM market time freshness=DELAYED_CURRENT RSI=13.68 liquidity=6132315.5 spike=0.59
- COMI.CA: score=7.9 buy_ready=False sector_rank=8 price=126.34 support=126.81 resistance=142.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=15.78 liquidity=421971616.0 spike=0.77
- COPR.CA: score=12.4 buy_ready=False sector_rank=16 price=0.47 support=0.44 resistance=0.53 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=37.5 liquidity=22449980.0 spike=0.73
- COSG.CA: score=6.4 buy_ready=False sector_rank=16 price=1.5 support=1.51 resistance=2.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=16.67 liquidity=14045687.0 spike=0.55
- CPCI.CA: score=10.43 buy_ready=False sector_rank=16 price=576.16 support=530.0 resistance=594.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=79.5 liquidity=3748067.25 spike=1.14
- CSAG.CA: score=9.56 buy_ready=False sector_rank=6 price=36.35 support=35.01 resistance=44.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=20.67 liquidity=10154702.0 spike=0.93
- DAPH.CA: score=7.4 buy_ready=False sector_rank=16 price=91.27 support=91.65 resistance=143.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=11.45 liquidity=15740828.0 spike=0.55
- DEIN.CA: score=5.4 buy_ready=False sector_rank=16 price=10.35 support=10.35 resistance=12.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10 September 11:17 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=49.68 spike=0.01
- DOMT.CA: score=0.95 buy_ready=False sector_rank=14 price=24.02 support=24.01 resistance=29.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=24.72 liquidity=4534704.5 spike=1.01
- DSCW.CA: score=7.5 buy_ready=False sector_rank=16 price=1.63 support=1.67 resistance=1.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=15.15 liquidity=31999868.0 spike=1.55
- DTPP.CA: score=2.4 buy_ready=False sector_rank=16 price=275.0 support=250.01 resistance=292.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=61710476.0 spike=0.73
- EALR.CA: score=-1.36 buy_ready=False sector_rank=16 price=321.51 support=322.52 resistance=411.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=24.9 liquidity=2240820.25 spike=0.18
- EASB.CA: score=1.66 buy_ready=False sector_rank=16 price=7.06 support=6.04 resistance=9.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=27.75 liquidity=4260607.0 spike=0.29
- EAST.CA: score=7.6 buy_ready=False sector_rank=14 price=29.1 support=28.5 resistance=36.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=2.13 liquidity=71128288.0 spike=1.6
- EBSC.CA: score=-2.19 buy_ready=False sector_rank=16 price=1.66 support=1.65 resistance=2.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=14.47 liquidity=1411736.0 spike=0.25
- ECAP.CA: score=-1.56 buy_ready=False sector_rank=16 price=30.0 support=29.13 resistance=34.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=21.37 liquidity=2041695.13 spike=0.32
- EDFM.CA: score=-2.21 buy_ready=False sector_rank=16 price=386.4 support=354.0 resistance=465.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:00 PM market time freshness=DELAYED_CURRENT RSI=33.58 liquidity=394052.38 spike=0.23
- EEII.CA: score=6.98 buy_ready=False sector_rank=16 price=2.06 support=2.05 resistance=2.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=34.52 liquidity=8583259.0 spike=0.76
- EFIC.CA: score=6.9 buy_ready=False sector_rank=13 price=163.0 support=147.0 resistance=239.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=9.83 liquidity=20112174.0 spike=0.06
- EFID.CA: score=6.4 buy_ready=False sector_rank=14 price=18.3 support=18.53 resistance=32.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=7.78 liquidity=33557552.0 spike=0.5
- EFIH.CA: score=14.43 buy_ready=False sector_rank=7 price=22.26 support=20.2 resistance=24.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=38.24 liquidity=64481656.0 spike=1.23
- EGAL.CA: score=7.9 buy_ready=False sector_rank=13 price=336.04 support=340.0 resistance=395.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=28.79 liquidity=36612248.0 spike=0.67
- EGAS.CA: score=16.14 buy_ready=False sector_rank=3 price=54.71 support=53.62 resistance=61.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=39.9 liquidity=9357462.0 spike=0.72
- EGBE.CA: score=3.91 buy_ready=False sector_rank=8 price=0.51 support=0.49 resistance=0.53 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=49.02 liquidity=9013.57 spike=0.1
- EGCH.CA: score=12.9 buy_ready=False sector_rank=13 price=13.15 support=13.35 resistance=14.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=39.92 liquidity=66761716.0 spike=0.51
- EGSA.CA: score=3.05 buy_ready=False sector_rank=2 price=8.85 support=8.82 resistance=9.1 source=Yahoo Finance as_of=2026-09-28T21:00:00+00:00 freshness=FRESH RSI=17.24 liquidity=0.0 spike=0.0
- EGTS.CA: score=2.4 buy_ready=False sector_rank=15 price=15.9 support=15.65 resistance=17.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=20602560.0 spike=0.59
- EHDR.CA: score=3.83 buy_ready=False sector_rank=16 price=2.4 support=2.42 resistance=3.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=14.93 liquidity=7426511.5 spike=0.45
- ELEC.CA: score=6.4 buy_ready=False sector_rank=19 price=1.78 support=1.72 resistance=2.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=21.28 liquidity=23471542.0 spike=0.32
- ELKA.CA: score=5.74 buy_ready=False sector_rank=16 price=1.47 support=1.43 resistance=1.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=14.29 liquidity=9337468.0 spike=0.54
- ELNA.CA: score=-3.36 buy_ready=False sector_rank=16 price=35.22 support=33.46 resistance=38.99 source=Yahoo Finance as_of=2026-09-28T21:00:00+00:00 freshness=FRESH RSI=0.0 liquidity=236889.73 spike=0.68
- ELSH.CA: score=4.15 buy_ready=False sector_rank=16 price=11.11 support=10.8 resistance=14.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=16.91 liquidity=6751023.5 spike=0.24
- ELWA.CA: score=-3.08 buy_ready=False sector_rank=16 price=1.51 support=1.51 resistance=1.92 source=Yahoo Finance as_of=2026-09-28T21:00:00+00:00 freshness=FRESH RSI=6.06 liquidity=519399.23 spike=0.47
- EMFD.CA: score=7.4 buy_ready=False sector_rank=15 price=12.07 support=12.0 resistance=15.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=19.63 liquidity=64302640.0 spike=0.59
- ENGC.CA: score=7.0 buy_ready=False sector_rank=16 price=34.55 support=35.7 resistance=46.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=22.75 liquidity=23025994.0 spike=1.3
- EOSB.CA: score=7.42 buy_ready=False sector_rank=16 price=1.57 support=1.53 resistance=1.64 source=Yahoo Finance as_of=2026-09-28T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=17401.88 spike=0.32
- EPCO.CA: score=0.14 buy_ready=False sector_rank=16 price=9.42 support=9.25 resistance=12.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=33.92 liquidity=2737980.5 spike=0.19
- EPPK.CA: score=-7.18 buy_ready=False sector_rank=16 price=10.29 support=10.29 resistance=10.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=8 September 01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=419183.72 spike=0.28
- ETEL.CA: score=21.61 buy_ready=False sector_rank=2 price=134.03 support=113.5 resistance=140.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=65.7 liquidity=366311616.0 spike=1.28
- ETRS.CA: score=7.44 buy_ready=False sector_rank=16 price=10.13 support=9.92 resistance=11.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=22.33 liquidity=11177772.0 spike=1.02
- EXPA.CA: score=13.9 buy_ready=False sector_rank=8 price=20.72 support=20.6 resistance=22.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=48.73 liquidity=30099562.0 spike=0.87
- FAIT.CA: score=6.25 buy_ready=False sector_rank=8 price=42.99 support=38.48 resistance=48.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=25.27 liquidity=4353391.5 spike=0.86
- FAITA.CA: score=-2.07 buy_ready=False sector_rank=8 price=0.98 support=0.98 resistance=1.0 source=Yahoo Finance as_of=2026-09-28T21:00:00+00:00 freshness=FRESH RSI=31.82 liquidity=25134.29 spike=0.73
- FERC.CA: score=-1.18 buy_ready=False sector_rank=13 price=73.89 support=70.42 resistance=86.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=31.91 liquidity=1917934.63 spike=0.15
- FWRY.CA: score=7.97 buy_ready=False sector_rank=7 price=18.27 support=17.5 resistance=19.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=11.63 liquidity=87164296.0 spike=0.86
- GBCO.CA: score=14.6 buy_ready=False sector_rank=10 price=30.0 support=27.0 resistance=32.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=45.18 liquidity=105421008.0 spike=1.48
- GDWA.CA: score=6.4 buy_ready=False sector_rank=16 price=0.64 support=0.61 resistance=0.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=7.69 liquidity=14094406.0 spike=0.4
- GGCC.CA: score=6.58 buy_ready=False sector_rank=16 price=0.67 support=0.67 resistance=0.91 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=21.47 liquidity=9178188.0 spike=0.52
- GIHD.CA: score=2.4 buy_ready=False sector_rank=16 price=61.81 support=60.9 resistance=68.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=17244742.0 spike=0.6
- GMCI.CA: score=-0.97 buy_ready=False sector_rank=16 price=1.57 support=1.5 resistance=1.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:52 PM market time freshness=DELAYED_CURRENT RSI=6.67 liquidity=887180.44 spike=1.87
- GRCA.CA: score=0.26 buy_ready=False sector_rank=16 price=33.62 support=32.11 resistance=63.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=13.7 liquidity=3861500.25 spike=0.12
- GSSC.CA: score=-1.71 buy_ready=False sector_rank=16 price=256.42 support=246.0 resistance=333.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=31.61 liquidity=885411.56 spike=0.12
- GTWL.CA: score=5.18 buy_ready=False sector_rank=16 price=143.17 support=124.5 resistance=165.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=328793472.0 spike=2.39
- HDBK.CA: score=15.9 buy_ready=False sector_rank=8 price=104.37 support=105.5 resistance=124.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=41.33 liquidity=22316760.0 spike=0.48
- HELI.CA: score=12.4 buy_ready=False sector_rank=15 price=7.22 support=7.02 resistance=8.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=35.29 liquidity=61542976.0 spike=0.39
- HRHO.CA: score=6.62 buy_ready=False sector_rank=18 price=23.5 support=23.02 resistance=26.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=10.96 liquidity=81302112.0 spike=1.11
- ICID.CA: score=11.84 buy_ready=False sector_rank=16 price=17.98 support=16.52 resistance=19.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=40.99 liquidity=6441749.0 spike=0.78
- IDRE.CA: score=6.39 buy_ready=False sector_rank=16 price=46.03 support=45.0 resistance=59.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=34.37 liquidity=8989787.0 spike=0.56
- IFAP.CA: score=3.05 buy_ready=False sector_rank=11 price=18.94 support=17.17 resistance=23.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=26.61 liquidity=5563470.0 spike=0.34
- INFI.CA: score=3.18 buy_ready=False sector_rank=16 price=117.36 support=104.0 resistance=160.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=19.19 liquidity=5782034.5 spike=0.34
- IRON.CA: score=2.63 buy_ready=False sector_rank=13 price=25.35 support=25.82 resistance=30.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=29.03 liquidity=5724393.0 spike=0.44
- ISMA.CA: score=2.52 buy_ready=False sector_rank=16 price=22.99 support=23.6 resistance=34.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=21.2 liquidity=5124799.5 spike=0.33
- ISMQ.CA: score=6.9 buy_ready=False sector_rank=13 price=7.74 support=7.7 resistance=9.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=18.53 liquidity=12245855.0 spike=0.53
- ISPH.CA: score=6.4 buy_ready=False sector_rank=17 price=11.51 support=11.22 resistance=13.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=21.56 liquidity=49086932.0 spike=0.72
- JUFO.CA: score=6.4 buy_ready=False sector_rank=14 price=24.63 support=24.5 resistance=27.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=19.49 liquidity=15562148.0 spike=0.8
- KABO.CA: score=9.73 buy_ready=False sector_rank=9 price=8.18 support=7.97 resistance=10.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:00 PM market time freshness=DELAYED_CURRENT RSI=29.51 liquidity=47190396.0 spike=1.44
- KWIN.CA: score=4.83 buy_ready=False sector_rank=16 price=74.74 support=74.0 resistance=118.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=27.5 liquidity=7428618.5 spike=0.39
- KZPC.CA: score=5.61 buy_ready=False sector_rank=16 price=12.57 support=12.8 resistance=14.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=25.08 liquidity=5212934.5 spike=0.18
- LCSW.CA: score=6.23 buy_ready=False sector_rank=21 price=29.45 support=29.16 resistance=37.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=16.67 liquidity=8828976.0 spike=0.42
- LUTS.CA: score=12.4 buy_ready=False sector_rank=16 price=0.86 support=0.72 resistance=1.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=40.11 liquidity=63330756.0 spike=0.61
- MAAL.CA: score=-2.71 buy_ready=False sector_rank=16 price=10.14 support=9.77 resistance=10.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=4891904.0 spike=0.22
- MASR.CA: score=7.4 buy_ready=False sector_rank=16 price=7.31 support=6.82 resistance=8.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=27.0 liquidity=27584812.0 spike=0.29
- MBSC.CA: score=7.4 buy_ready=False sector_rank=21 price=290.0 support=295.22 resistance=464.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=0.89 liquidity=22867164.0 spike=0.62
- MCQE.CA: score=6.4 buy_ready=False sector_rank=21 price=178.54 support=180.04 resistance=254.23 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=13.46 liquidity=12831342.0 spike=0.6
- MCRO.CA: score=7.4 buy_ready=False sector_rank=16 price=1.49 support=1.41 resistance=1.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=27.45 liquidity=36854600.0 spike=0.3
- MENA.CA: score=-1.98 buy_ready=False sector_rank=15 price=6.2 support=5.8 resistance=7.07 source=Yahoo Finance as_of=2026-09-28T21:00:00+00:00 freshness=FRESH RSI=27.73 liquidity=624048.58 spike=0.46
- MEPA.CA: score=3.35 buy_ready=False sector_rank=16 price=1.62 support=1.6 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=12.7 liquidity=6949718.0 spike=0.19
- MFPC.CA: score=15.9 buy_ready=False sector_rank=13 price=44.64 support=42.81 resistance=51.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=42.8 liquidity=37332132.0 spike=0.24
- MFSC.CA: score=7.22 buy_ready=False sector_rank=16 price=47.94 support=45.22 resistance=58.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=38.29 liquidity=4736842.5 spike=1.04
- MHOT.CA: score=10.82 buy_ready=False sector_rank=12 price=16.87 support=16.61 resistance=21.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=43.27 liquidity=8689445.0 spike=0.49
- MICH.CA: score=7.54 buy_ready=False sector_rank=16 price=44.19 support=42.5 resistance=52.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=19.56 liquidity=13855396.0 spike=1.07
- MILS.CA: score=3.05 buy_ready=False sector_rank=16 price=175.09 support=165.5 resistance=232.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=28.6 liquidity=5654621.0 spike=0.31
- MIPH.CA: score=3.98 buy_ready=False sector_rank=17 price=778.4 support=739.69 resistance=1000.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:50 PM market time freshness=DELAYED_CURRENT RSI=46.59 liquidity=1577151.25 spike=0.17
- MOED.CA: score=4.65 buy_ready=False sector_rank=16 price=0.63 support=0.59 resistance=0.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=10.81 liquidity=8253681.5 spike=0.17
- MOIL.CA: score=10.98 buy_ready=False sector_rank=3 price=0.7 support=0.67 resistance=0.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=80.0 liquidity=195180.7 spike=0.79
- MOIN.CA: score=5.08 buy_ready=False sector_rank=16 price=33.34 support=32.5 resistance=45.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=31.23 liquidity=7677906.5 spike=0.26
- MOSC.CA: score=-1.73 buy_ready=False sector_rank=16 price=261.23 support=257.0 resistance=329.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=22.37 liquidity=867827.06 spike=0.23
- MPCI.CA: score=7.48 buy_ready=False sector_rank=16 price=326.57 support=335.01 resistance=467.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=12.36 liquidity=120272272.0 spike=1.04
- MPCO.CA: score=16.49 buy_ready=False sector_rank=11 price=2.34 support=2.08 resistance=3.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=52.75 liquidity=104066512.0 spike=0.55
- MPRC.CA: score=12.33 buy_ready=False sector_rank=16 price=37.86 support=37.65 resistance=44.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=37.77 liquidity=9934082.0 spike=0.32
- MTIE.CA: score=7.8 buy_ready=False sector_rank=10 price=7.81 support=7.5 resistance=8.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=21.43 liquidity=23196032.0 spike=1.08
- NAHO.CA: score=5.41 buy_ready=False sector_rank=16 price=0.13 support=0.12 resistance=0.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=40.0 liquidity=5756.3 spike=0.12
- NCCW.CA: score=15.4 buy_ready=False sector_rank=16 price=6.98 support=5.96 resistance=8.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=48.32 liquidity=25089210.0 spike=0.31
- NEDA.CA: score=-2.91 buy_ready=False sector_rank=16 price=2.54 support=2.48 resistance=2.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=34.09 liquidity=689498.56 spike=0.74
- NHPS.CA: score=6.4 buy_ready=False sector_rank=16 price=67.78 support=69.5 resistance=91.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=30.44 liquidity=13225131.0 spike=0.92
- NINH.CA: score=2.51 buy_ready=False sector_rank=16 price=19.21 support=18.53 resistance=24.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=22.59 liquidity=5111437.0 spike=0.31
- NIPH.CA: score=12.4 buy_ready=False sector_rank=17 price=309.87 support=290.0 resistance=368.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=37.74 liquidity=101679688.0 spike=0.81
- OBRI.CA: score=5.13 buy_ready=False sector_rank=16 price=23.45 support=23.67 resistance=34.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=11.9 liquidity=8725434.0 spike=0.79
- OCDI.CA: score=7.4 buy_ready=False sector_rank=15 price=24.93 support=24.5 resistance=34.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=5.43 liquidity=18129470.0 spike=0.28
- OCPH.CA: score=-1.56 buy_ready=False sector_rank=16 price=210.76 support=190.0 resistance=263.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=16.24 liquidity=2042569.0 spike=0.39
- ODIN.CA: score=2.17 buy_ready=False sector_rank=16 price=2.43 support=2.35 resistance=3.06 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=30.39 liquidity=4773636.5 spike=0.36
- OFH.CA: score=2.4 buy_ready=False sector_rank=16 price=0.94 support=0.86 resistance=0.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=117042416.0 spike=0.9
- OIH.CA: score=14.26 buy_ready=False sector_rank=1 price=1.84 support=1.7 resistance=2.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=17.65 liquidity=59732832.0 spike=0.53
- OLFI.CA: score=13.38 buy_ready=False sector_rank=14 price=21.61 support=21.2 resistance=23.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=38.71 liquidity=29678280.0 spike=1.99
- ORAS.CA: score=4.6 buy_ready=False sector_rank=5 price=790.17 support=763.0 resistance=797.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=139823680.0 spike=1.0
- ORHD.CA: score=7.4 buy_ready=False sector_rank=15 price=37.77 support=38.02 resistance=44.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=33.98 liquidity=110271536.0 spike=0.67
- ORWE.CA: score=16.85 buy_ready=False sector_rank=9 price=26.63 support=26.01 resistance=29.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=40.77 liquidity=49389124.0 spike=0.93
- PHAR.CA: score=8.24 buy_ready=False sector_rank=17 price=110.0 support=102.0 resistance=133.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=21.31 liquidity=117796264.0 spike=1.42
- PHDC.CA: score=7.4 buy_ready=False sector_rank=15 price=12.55 support=12.5 resistance=15.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=12.35 liquidity=100601176.0 spike=0.77
- PHTV.CA: score=3.12 buy_ready=False sector_rank=16 price=335.78 support=320.11 resistance=378.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:49 PM market time freshness=DELAYED_CURRENT RSI=40.66 liquidity=715588.31 spike=0.44
- POUL.CA: score=7.28 buy_ready=False sector_rank=14 price=9.87 support=9.12 resistance=41.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=5.77 liquidity=42275788.0 spike=1.44
- PRCL.CA: score=2.04 buy_ready=False sector_rank=21 price=23.0 support=22.8 resistance=25.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=9637757.0 spike=0.64
- PRDC.CA: score=5.85 buy_ready=False sector_rank=15 price=7.13 support=6.81 resistance=9.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=26.19 liquidity=8453287.0 spike=0.23
- PRMH.CA: score=0.1 buy_ready=False sector_rank=16 price=2.18 support=2.2 resistance=2.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=22.77 liquidity=3704060.0 spike=0.64
- RACC.CA: score=1.43 buy_ready=False sector_rank=16 price=8.95 support=8.51 resistance=10.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=27.09 liquidity=5028725.5 spike=0.39
- RAKT.CA: score=0.95 buy_ready=False sector_rank=16 price=21.32 support=21.02 resistance=23.0 source=Yahoo Finance as_of=2026-09-28T21:00:00+00:00 freshness=FRESH RSI=21.01 liquidity=529908.59 spike=3.01
- RAYA.CA: score=7.4 buy_ready=False sector_rank=20 price=6.24 support=5.72 resistance=7.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=19.62 liquidity=29841826.0 spike=0.56
- RMDA.CA: score=7.4 buy_ready=False sector_rank=17 price=5.3 support=4.83 resistance=6.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=13.67 liquidity=27857192.0 spike=0.52
- ROTO.CA: score=3.51 buy_ready=False sector_rank=16 price=37.05 support=35.02 resistance=44.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=21.7 liquidity=6105548.0 spike=0.79
- RREI.CA: score=4.59 buy_ready=False sector_rank=16 price=3.82 support=3.6 resistance=4.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=25.0 liquidity=7189332.0 spike=0.51
- RTVC.CA: score=-0.98 buy_ready=False sector_rank=16 price=3.5 support=3.39 resistance=4.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=18.18 liquidity=2603134.0 spike=1.01
- RUBX.CA: score=19.4 buy_ready=False sector_rank=16 price=14.33 support=12.55 resistance=18.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=53.43 liquidity=46388696.0 spike=0.69
- SAUD.CA: score=8.35 buy_ready=False sector_rank=8 price=22.11 support=21.6 resistance=26.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=40.76 liquidity=4446305.5 spike=0.23
- SCEM.CA: score=7.4 buy_ready=False sector_rank=21 price=75.55 support=76.0 resistance=105.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=3.88 liquidity=18737810.0 spike=0.26
- SCFM.CA: score=-0.59 buy_ready=False sector_rank=16 price=238.57 support=223.11 resistance=315.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:48 PM market time freshness=DELAYED_CURRENT RSI=29.59 liquidity=3007374.0 spike=0.49
- SCTS.CA: score=1.4 buy_ready=False sector_rank=4 price=527.58 support=520.3 resistance=639.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=16.31 liquidity=1590340.0 spike=0.74
- SDTI.CA: score=14.13 buy_ready=False sector_rank=16 price=83.57 support=69.15 resistance=94.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=76.49 liquidity=9726360.0 spike=0.28
- SEIG.CA: score=-2.14 buy_ready=False sector_rank=16 price=209.68 support=211.15 resistance=268.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:48 PM market time freshness=DELAYED_CURRENT RSI=32.01 liquidity=462900.88 spike=0.26
- SIPC.CA: score=7.4 buy_ready=False sector_rank=16 price=4.89 support=4.22 resistance=7.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=32.14 liquidity=19538912.0 spike=0.27
- SKPC.CA: score=6.9 buy_ready=False sector_rank=13 price=15.8 support=15.7 resistance=19.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=18.99 liquidity=71452504.0 spike=0.53
- SMFR.CA: score=-1.15 buy_ready=False sector_rank=16 price=208.48 support=205.01 resistance=274.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=14.71 liquidity=1450375.88 spike=0.22
- SNFC.CA: score=13.44 buy_ready=False sector_rank=16 price=11.16 support=10.26 resistance=11.71 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=66.88 liquidity=6043022.0 spike=0.43
- SPIN.CA: score=4.54 buy_ready=False sector_rank=9 price=16.34 support=15.11 resistance=20.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:00 PM market time freshness=DELAYED_CURRENT RSI=21.0 liquidity=5691151.5 spike=0.78
- SPMD.CA: score=9.06 buy_ready=False sector_rank=16 price=0.37 support=0.37 resistance=0.62 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=40.83 liquidity=7664510.5 spike=0.1
- SUGR.CA: score=6.36 buy_ready=False sector_rank=14 price=51.22 support=51.2 resistance=64.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=28.36 liquidity=8963169.0 spike=0.31
- SVCE.CA: score=7.4 buy_ready=False sector_rank=16 price=9.46 support=9.6 resistance=13.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=10.4 liquidity=38304340.0 spike=0.24
- SWDY.CA: score=9.58 buy_ready=False sector_rank=19 price=106.01 support=107.77 resistance=139.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=10.95 liquidity=136747632.0 spike=2.09
- TALM.CA: score=17.81 buy_ready=False sector_rank=4 price=18.99 support=17.61 resistance=25.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=58.43 liquidity=20474718.0 spike=0.31
- TMGH.CA: score=6.4 buy_ready=False sector_rank=15 price=86.62 support=86.1 resistance=100.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=8.44 liquidity=205463024.0 spike=0.76
- TRTO.CA: score=-2.6 buy_ready=False sector_rank=16 price=0.05 support=0.05 resistance=0.08 source=Yahoo Finance as_of=2026-09-28T21:00:00+00:00 freshness=FRESH RSI=0.0 liquidity=3186.0 spike=0.13
- UEFM.CA: score=10.89 buy_ready=False sector_rank=16 price=490.0 support=421.1 resistance=574.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=46.56 liquidity=7368846.0 spike=2.06
- UEGC.CA: score=6.4 buy_ready=False sector_rank=16 price=1.43 support=1.41 resistance=1.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=22.22 liquidity=23455368.0 spike=0.61
- UNIP.CA: score=4.76 buy_ready=False sector_rank=16 price=0.33 support=0.32 resistance=0.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=20.39 liquidity=7358913.5 spike=0.36
- UNIT.CA: score=4.12 buy_ready=False sector_rank=15 price=16.68 support=16.66 resistance=23.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:00 PM market time freshness=DELAYED_CURRENT RSI=40.08 liquidity=1721540.5 spike=0.11
- WCDF.CA: score=2.05 buy_ready=False sector_rank=16 price=628.2 support=575.5 resistance=796.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=33.39 liquidity=4649398.0 spike=0.83
- WKOL.CA: score=4.98 buy_ready=False sector_rank=16 price=276.87 support=291.0 resistance=379.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=19.86 liquidity=8581176.0 spike=0.63
- ZEOT.CA: score=0.39 buy_ready=False sector_rank=16 price=11.41 support=10.6 resistance=14.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=16.3 liquidity=2985454.0 spike=0.49
- ZMID.CA: score=7.4 buy_ready=False sector_rank=15 price=7.47 support=7.2 resistance=9.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=11.95 liquidity=68896896.0 spike=0.42

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
