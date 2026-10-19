# Telegram-First EGX Scanner Report

Scan phase: Pre-market risk check
Generated UTC: 2026-10-19T11:17:33.923624+00:00
Generated Cairo: 2026-10-19 14:17
Run timing: target 08:45 Cairo | generated Cairo 2026-10-19 14:17 | cron 45 5 * * 0-4
Trigger: scheduled cron=45 5 * * 0-4 mapped to pre_market; Cairo now 2026-10-19 14:13

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 3
- Tradeable price/liquidity tickers: 176/187
- Top sector: Telecommunications

## Market Context
- Market trend: Bullish
- Source: Mubasher EGX market page (delayed public data)
- As of: Monday, October 19
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 0.0% / above MA50 10.53%
- EGX70 regime: BEARISH / above MA20 2.5% / above MA50 10.0%
- Sector breadth: 0.0%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- CCAP.CA: liquidity=577976640.0 spike=0.99 score=7.84
- COMI.CA: liquidity=392324480.0 spike=0.81 score=13.75
- NIPH.CA: liquidity=332608000.0 spike=2.77 score=6.12
- ARCC.CA: liquidity=261255184.0 spike=8.33 score=17.4
- POUL.CA: liquidity=239605968.0 spike=8.5 score=12.0

## AI Narrative
- Provider: OpenRouter OK
- Model: nvidia/nemotron-3-super-120b-a12b:free
- Summary: EGX30 and EGX70 are bearish with negligible sector breadth, forcing a defensive risk mode that blocks new buys; the scanner highlighted the top‑ranked tickets based on rank_score despite their BUY‑ready flags being false.
- Liquidity: all selected stocks show tradeable liquidity but liquidity spikes are cooling (spike < 1× for most), limiting near‑term inflow.
- Sector: tickets arise from leading sectors (Telecom, Industrial Goods & Construction, Fintech & Payments) yet overall sector breadth is 0 %, indicating weak sector‑wide support.
- Support/Resistance: prices sit close to 20‑day support (single‑digit % distance) while resistance lies 8‑13 % above, suggesting limited upside over the next 1‑3 days.
- Outlook: most tickets carry CONSTRUCTIVE or BULLISH_WATCH outlook scores (50‑70), but the bearish regime and low confidence temper any bullish expectation.
- Uncertainty: a rapid shift in EGX30/EGX70 trend (e.g., MA20/MA50 cross or liquidity spike) could alter risk mode; monitor these cues for any change in scanner bias.

## Top Liquidity Spikes
- POUL.CA: spike=8.5 liquidity=239605968.0 outlook=WEAK_OR_RISKY score=22 buy_ready=False
- ARCC.CA: spike=8.33 liquidity=261255184.0 outlook=NEUTRAL score=48 buy_ready=False
- CPCI.CA: spike=3.73 liquidity=15394772.0 outlook=CONSTRUCTIVE score=62 buy_ready=False
- NIPH.CA: spike=2.77 liquidity=332608000.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- MOIL.CA: spike=2.69 liquidity=777249.5 outlook=WEAK_OR_RISKY score=0 buy_ready=False

## Sector Leaderboard
- #1 Telecommunications: score=2.38 5d=-2.54% 20d=1.09% aboveMA50=50.0%
- #2 Industrial Goods & Construction: score=1.5 5d=0.0% 20d=0.0% aboveMA50=0.0%
- #3 Fintech & Payments: score=-0.25 5d=-2.15% 20d=-2.04% aboveMA50=0.0%
- #4 Energy & Petrochemicals: score=-0.64 5d=-4.88% 20d=-5.29% aboveMA50=33.33%
- #5 Transportation & Logistics: score=-1.17 5d=-3.85% 20d=-6.69% aboveMA50=0.0%
- #6 Tourism & Leisure: score=-2.44 5d=-3.41% 20d=-6.57% aboveMA50=0.0%
- #7 Food, Beverages & Tobacco: score=-2.51 5d=-1.88% 20d=-13.16% aboveMA50=0.0%
- #8 Investment Holding: score=-2.89 5d=-5.32% 20d=-14.68% aboveMA50=33.33%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- SDTI.CA: BULLISH_WATCH score=71 liquidity=TRADEABLE sector=LAGGING risk=liquidity is cooling; sector is not leading
- ETEL.CA: BULLISH_WATCH score=70.38 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; below MA20
- AMOC.CA: CONSTRUCTIVE score=63 liquidity=TRADEABLE sector=NEUTRAL risk=below MA20
- CPCI.CA: CONSTRUCTIVE score=62 liquidity=ACCUMULATION_SPIKE sector=LAGGING risk=below MA20; momentum is extended; sector is not leading
- ABUK.CA: CONSTRUCTIVE score=58 liquidity=TRADEABLE sector=LAGGING risk=below MA20; sector is not leading
- INFI.CA: CONSTRUCTIVE score=56 liquidity=ACCUMULATION_SPIKE sector=LAGGING risk=below MA50; far above support; sector is not leading
- RUBX.CA: CONSTRUCTIVE score=55 liquidity=TRADEABLE sector=LAGGING risk=liquidity is cooling; far above support; sector is not leading; high short-term volatility
- ARAB.CA: CONSTRUCTIVE score=53 liquidity=TRADEABLE sector=LAGGING risk=liquidity is cooling; momentum is extended; far above support; sector is not leading
- BINV.CA: CONSTRUCTIVE score=53 liquidity=TRADEABLE sector=LAGGING risk=liquidity is cooling; below MA20; sector is not leading
- TALM.CA: CONSTRUCTIVE score=53 liquidity=TRADEABLE sector=LAGGING risk=liquidity is cooling; below MA20; sector is not leading

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- EKHO.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ARVA.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=2.95 buy_ready=False sector_rank=18 price=218.43 support=214.0 resistance=316.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=25.72 liquidity=5546685.0 spike=0.47
- ABUK.CA: score=15.64 buy_ready=False sector_rank=19 price=87.01 support=81.75 resistance=96.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=41.64 liquidity=92833808.0 spike=1.12
- ACAMD.CA: score=14.48 buy_ready=False sector_rank=18 price=2.03 support=1.87 resistance=2.16 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=67.86 liquidity=48486608.0 spike=1.04
- ACGC.CA: score=6.42 buy_ready=False sector_rank=16 price=12.86 support=12.6 resistance=14.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=39.02 liquidity=4018186.0 spike=0.35
- ADCI.CA: score=5.51 buy_ready=False sector_rank=18 price=256.27 support=250.06 resistance=288.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=35.29 liquidity=2552253.75 spike=1.28
- ADIB.CA: score=7.75 buy_ready=False sector_rank=9 price=44.97 support=43.5 resistance=54.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=24.12 liquidity=62133904.0 spike=0.84
- ADPC.CA: score=5.75 buy_ready=False sector_rank=18 price=3.12 support=3.01 resistance=4.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=29.09 liquidity=9347163.0 spike=0.64
- AFDI.CA: score=5.3 buy_ready=False sector_rank=18 price=47.14 support=45.6 resistance=56.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=35.4 liquidity=2904975.0 spike=0.54
- AFMC.CA: score=12.4 buy_ready=False sector_rank=18 price=126.01 support=120.1 resistance=179.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=36.91 liquidity=17634906.0 spike=0.91
- AJWA.CA: score=14.4 buy_ready=False sector_rank=18 price=214.03 support=176.0 resistance=229.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=79.43 liquidity=15813385.0 spike=0.51
- ALCN.CA: score=13.53 buy_ready=False sector_rank=5 price=31.95 support=31.25 resistance=36.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=51.24 liquidity=11603958.0 spike=0.4
- ALUM.CA: score=0.35 buy_ready=False sector_rank=18 price=19.53 support=19.26 resistance=27.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=27.49 liquidity=3948310.75 spike=0.94
- AMER.CA: score=7.4 buy_ready=False sector_rank=17 price=4.16 support=4.05 resistance=5.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=34.25 liquidity=48554524.0 spike=1.0
- AMES.CA: score=8.4 buy_ready=False sector_rank=18 price=36.0 support=35.1 resistance=54.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:00 PM market time freshness=DELAYED_CURRENT RSI=31.56 liquidity=46588864.0 spike=0.59
- AMIA.CA: score=12.54 buy_ready=False sector_rank=18 price=17.69 support=17.3 resistance=19.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=36.48 liquidity=19037814.0 spike=1.07
- AMOC.CA: score=16.74 buy_ready=False sector_rank=4 price=12.97 support=12.18 resistance=14.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=52.16 liquidity=108676520.0 spike=0.91
- APSW.CA: score=1.86 buy_ready=False sector_rank=18 price=7.88 support=7.81 resistance=8.92 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:56 PM market time freshness=DELAYED_CURRENT RSI=44.09 liquidity=456216.97 spike=0.73
- ARAB.CA: score=17.4 buy_ready=False sector_rank=17 price=0.26 support=0.2 resistance=0.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=66.07 liquidity=82235144.0 spike=0.78
- ARCC.CA: score=17.4 buy_ready=False sector_rank=13 price=65.64 support=60.01 resistance=74.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=54.01 liquidity=261255184.0 spike=8.33
- AREH.CA: score=3.57 buy_ready=False sector_rank=18 price=1.13 support=1.1 resistance=1.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=34.69 liquidity=7166928.0 spike=0.85
- ASCM.CA: score=7.0 buy_ready=False sector_rank=18 price=45.42 support=45.5 resistance=61.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=23.71 liquidity=11220135.0 spike=1.3
- ASPI.CA: score=11.4 buy_ready=False sector_rank=18 price=0.32 support=0.31 resistance=0.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=35.43 liquidity=22266148.0 spike=0.8
- ATLC.CA: score=9.51 buy_ready=False sector_rank=14 price=5.06 support=4.84 resistance=7.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=38.1 liquidity=7111255.5 spike=0.94
- ATQA.CA: score=7.4 buy_ready=False sector_rank=19 price=10.64 support=10.61 resistance=13.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=33.87 liquidity=23901070.0 spike=0.33
- AXPH.CA: score=4.11 buy_ready=False sector_rank=18 price=1296.47 support=1300.0 resistance=1987.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=24.16 liquidity=6626117.5 spike=1.04
- BINV.CA: score=15.84 buy_ready=False sector_rank=8 price=58.0 support=52.11 resistance=67.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=58.12 liquidity=12190384.0 spike=0.78
- BIOC.CA: score=3.28 buy_ready=False sector_rank=18 price=291.27 support=257.0 resistance=297.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:00 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=148213536.0 spike=1.44
- BTFH.CA: score=11.4 buy_ready=False sector_rank=14 price=2.68 support=2.55 resistance=3.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=42.25 liquidity=74216632.0 spike=0.7
- CAED.CA: score=13.58 buy_ready=False sector_rank=18 price=94.17 support=95.0 resistance=136.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=36.17 liquidity=12825503.0 spike=1.59
- CANA.CA: score=7.75 buy_ready=False sector_rank=9 price=40.88 support=42.03 resistance=52.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=30.04 liquidity=17878406.0 spike=0.78
- CCAP.CA: score=7.84 buy_ready=False sector_rank=8 price=6.18 support=5.92 resistance=7.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=24.86 liquidity=577976640.0 spike=0.99
- CCRS.CA: score=1.69 buy_ready=False sector_rank=18 price=1.86 support=1.83 resistance=2.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=16.09 liquidity=5287450.0 spike=0.59
- CEFM.CA: score=3.59 buy_ready=False sector_rank=18 price=126.94 support=113.0 resistance=152.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:51 PM market time freshness=DELAYED_CURRENT RSI=41.65 liquidity=1189034.88 spike=0.45
- CERA.CA: score=11.4 buy_ready=False sector_rank=18 price=1.23 support=1.18 resistance=1.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:00 PM market time freshness=DELAYED_CURRENT RSI=48.68 liquidity=101032384.0 spike=0.85
- CFGH.CA: score=-3.51 buy_ready=False sector_rank=18 price=0.11 support=0.1 resistance=0.12 source=Yahoo Finance as_of=2026-10-17T21:00:00+00:00 freshness=FRESH RSI=9.09 liquidity=6587.26 spike=1.04
- CICH.CA: score=-1.3 buy_ready=False sector_rank=14 price=10.89 support=9.63 resistance=13.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:41 PM market time freshness=DELAYED_CURRENT RSI=28.8 liquidity=1303333.25 spike=0.37
- CIEB.CA: score=7.27 buy_ready=False sector_rank=9 price=22.15 support=21.97 resistance=25.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=28.84 liquidity=11889978.0 spike=1.26
- CIRA.CA: score=7.67 buy_ready=False sector_rank=10 price=35.14 support=35.01 resistance=41.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=33.6 liquidity=9956623.0 spike=0.46
- CLHO.CA: score=6.58 buy_ready=False sector_rank=12 price=13.74 support=13.0 resistance=16.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=33.05 liquidity=31244648.0 spike=0.76
- CNFN.CA: score=11.64 buy_ready=False sector_rank=14 price=3.99 support=3.8 resistance=4.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=43.64 liquidity=10267184.0 spike=1.12
- COMI.CA: score=13.75 buy_ready=False sector_rank=9 price=124.91 support=120.0 resistance=134.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=37.04 liquidity=392324480.0 spike=0.81
- COPR.CA: score=12.4 buy_ready=False sector_rank=18 price=0.43 support=0.41 resistance=0.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=39.87 liquidity=10014578.0 spike=0.49
- COSG.CA: score=6.42 buy_ready=False sector_rank=18 price=1.38 support=1.34 resistance=1.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:00 PM market time freshness=DELAYED_CURRENT RSI=31.82 liquidity=15192333.0 spike=1.01
- CPCI.CA: score=20.4 buy_ready=False sector_rank=18 price=564.64 support=546.54 resistance=619.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:56 PM market time freshness=DELAYED_CURRENT RSI=63.76 liquidity=15394772.0 spike=3.73
- CSAG.CA: score=15.29 buy_ready=False sector_rank=5 price=33.95 support=34.06 resistance=39.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=42.24 liquidity=11862572.0 spike=1.88
- DAPH.CA: score=11.6 buy_ready=False sector_rank=18 price=84.02 support=85.3 resistance=126.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:00 PM market time freshness=DELAYED_CURRENT RSI=36.3 liquidity=45163656.0 spike=1.1
- DEIN.CA: score=5.4 buy_ready=False sector_rank=18 price=10.35 support=10.35 resistance=12.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 09:54 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=37.26 spike=0.01
- DOMT.CA: score=3.06 buy_ready=False sector_rank=7 price=23.07 support=22.85 resistance=27.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=36.53 liquidity=1062705.88 spike=0.24
- DSCW.CA: score=6.4 buy_ready=False sector_rank=18 price=1.52 support=1.45 resistance=1.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:00 PM market time freshness=DELAYED_CURRENT RSI=22.92 liquidity=13422312.0 spike=0.75
- DTPP.CA: score=7.4 buy_ready=False sector_rank=18 price=242.35 support=225.0 resistance=358.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=34.72 liquidity=20525926.0 spike=0.37
- EALR.CA: score=-1.46 buy_ready=False sector_rank=18 price=290.06 support=290.17 resistance=387.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=25.16 liquidity=2140443.25 spike=0.52
- EASB.CA: score=4.92 buy_ready=False sector_rank=18 price=6.16 support=6.04 resistance=8.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT RSI=34.49 liquidity=6842436.5 spike=1.34
- EAST.CA: score=14.0 buy_ready=False sector_rank=7 price=28.66 support=27.01 resistance=32.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=36.82 liquidity=12813411.0 spike=0.3
- EBSC.CA: score=4.27 buy_ready=False sector_rank=18 price=1.53 support=1.45 resistance=2.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=28.09 liquidity=5154384.0 spike=2.36
- ECAP.CA: score=-2.64 buy_ready=False sector_rank=18 price=27.43 support=27.0 resistance=32.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=27.54 liquidity=960281.38 spike=0.23
- EDFM.CA: score=2.89 buy_ready=False sector_rank=18 price=381.69 support=335.2 resistance=425.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:51 PM market time freshness=DELAYED_CURRENT RSI=52.41 liquidity=493543.19 spike=0.42
- EEII.CA: score=0.63 buy_ready=False sector_rank=18 price=1.82 support=1.78 resistance=2.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=20.97 liquidity=4233875.5 spike=0.46
- EFIC.CA: score=11.4 buy_ready=False sector_rank=19 price=148.16 support=147.0 resistance=199.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=37.45 liquidity=17561516.0 spike=0.55
- EFID.CA: score=14.0 buy_ready=False sector_rank=7 price=18.12 support=18.07 resistance=21.23 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=38.62 liquidity=30961692.0 spike=0.66
- EFIH.CA: score=16.9 buy_ready=False sector_rank=3 price=23.52 support=20.2 resistance=25.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=55.02 liquidity=40256216.0 spike=0.61
- EGAL.CA: score=9.24 buy_ready=False sector_rank=19 price=295.0 support=280.0 resistance=376.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=12.62 liquidity=169443264.0 spike=2.42
- EGAS.CA: score=3.48 buy_ready=False sector_rank=4 price=50.51 support=48.08 resistance=60.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=26.37 liquidity=4731748.5 spike=0.58
- EGBE.CA: score=2.76 buy_ready=False sector_rank=9 price=0.5 support=0.5 resistance=0.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=39.29 liquidity=6253.51 spike=0.05
- EGCH.CA: score=6.4 buy_ready=False sector_rank=19 price=11.27 support=10.85 resistance=14.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=12.78 liquidity=59832276.0 spike=0.73
- EGSA.CA: score=4.18 buy_ready=False sector_rank=1 price=8.76 support=8.75 resistance=9.09 source=Yahoo Finance as_of=2026-10-17T21:00:00+00:00 freshness=FRESH RSI=22.73 liquidity=8541.0 spike=1.61
- EGTS.CA: score=2.4 buy_ready=False sector_rank=17 price=13.52 support=12.06 resistance=13.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=25424474.0 spike=0.7
- EHDR.CA: score=2.64 buy_ready=False sector_rank=18 price=2.21 support=2.08 resistance=2.23 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=11896607.0 spike=1.12
- ELEC.CA: score=6.4 buy_ready=False sector_rank=15 price=1.64 support=1.6 resistance=2.06 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=28.07 liquidity=30774570.0 spike=0.81
- ELKA.CA: score=11.07 buy_ready=False sector_rank=18 price=1.47 support=1.38 resistance=1.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:00 PM market time freshness=DELAYED_CURRENT RSI=46.38 liquidity=9673745.0 spike=0.72
- ELNA.CA: score=3.5 buy_ready=False sector_rank=18 price=35.22 support=33.46 resistance=36.4 source=Yahoo Finance as_of=2026-10-17T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=99743.04 spike=0.6
- ELSH.CA: score=12.4 buy_ready=False sector_rank=18 price=10.47 support=10.35 resistance=13.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=35.73 liquidity=13874172.0 spike=0.67
- ELWA.CA: score=6.46 buy_ready=False sector_rank=18 price=1.65 support=1.43 resistance=1.74 source=Yahoo Finance as_of=2026-10-17T21:00:00+00:00 freshness=FRESH RSI=52.78 liquidity=57608.1 spike=0.13
- EMFD.CA: score=12.4 buy_ready=False sector_rank=17 price=11.79 support=11.2 resistance=14.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=37.32 liquidity=23266154.0 spike=0.39
- ENGC.CA: score=4.88 buy_ready=False sector_rank=18 price=31.45 support=31.2 resistance=45.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=25.09 liquidity=8477257.0 spike=0.47
- EOSB.CA: score=4.4 buy_ready=False sector_rank=18 price=1.57 support=1.57 resistance=1.64 source=Yahoo Finance as_of=2026-10-17T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- EPCO.CA: score=0.6 buy_ready=False sector_rank=18 price=8.27 support=8.0 resistance=11.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=26.15 liquidity=4195855.5 spike=0.85
- EPPK.CA: score=-7.18 buy_ready=False sector_rank=18 price=10.29 support=10.29 resistance=10.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=8 September 01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=419183.72 spike=0.28
- ETEL.CA: score=20.95 buy_ready=False sector_rank=1 price=140.69 support=129.0 resistance=156.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=57.51 liquidity=148836592.0 spike=0.62
- ETRS.CA: score=13.4 buy_ready=False sector_rank=18 price=10.15 support=9.82 resistance=11.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:00 PM market time freshness=DELAYED_CURRENT RSI=46.4 liquidity=15046099.0 spike=1.5
- EXPA.CA: score=6.75 buy_ready=False sector_rank=9 price=14.13 support=14.0 resistance=22.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=8.13 liquidity=18242866.0 spike=0.47
- FAIT.CA: score=5.64 buy_ready=False sector_rank=9 price=42.63 support=38.48 resistance=47.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=42.93 liquidity=2868464.0 spike=1.01
- FAITA.CA: score=4.83 buy_ready=False sector_rank=9 price=0.99 support=0.98 resistance=1.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:51 PM market time freshness=DELAYED_CURRENT RSI=57.32 liquidity=40900.1 spike=1.02
- FERC.CA: score=-0.94 buy_ready=False sector_rank=19 price=64.2 support=64.01 resistance=82.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=23.46 liquidity=2663025.5 spike=0.6
- FWRY.CA: score=13.9 buy_ready=False sector_rank=3 price=18.2 support=17.5 resistance=19.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=45.74 liquidity=81444200.0 spike=0.75
- GBCO.CA: score=12.7 buy_ready=False sector_rank=11 price=29.33 support=27.0 resistance=32.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=44.46 liquidity=24234288.0 spike=0.22
- GDWA.CA: score=6.4 buy_ready=False sector_rank=18 price=0.6 support=0.58 resistance=0.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:00 PM market time freshness=DELAYED_CURRENT RSI=31.34 liquidity=12663362.0 spike=0.67
- GGCC.CA: score=12.4 buy_ready=False sector_rank=18 price=0.64 support=0.61 resistance=0.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:00 PM market time freshness=DELAYED_CURRENT RSI=38.58 liquidity=15395993.0 spike=0.96
- GIHD.CA: score=5.42 buy_ready=False sector_rank=18 price=48.53 support=48.48 resistance=78.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=15.21 liquidity=8017567.5 spike=0.42
- GMCI.CA: score=1.59 buy_ready=False sector_rank=18 price=1.54 support=1.47 resistance=1.78 source=Yahoo Finance as_of=2026-10-17T21:00:00+00:00 freshness=FRESH RSI=40.38 liquidity=187829.18 spike=0.49
- GRCA.CA: score=5.19 buy_ready=False sector_rank=18 price=29.03 support=29.0 resistance=44.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:00 PM market time freshness=DELAYED_CURRENT RSI=30.07 liquidity=6792416.5 spike=0.93
- GSSC.CA: score=2.97 buy_ready=False sector_rank=18 price=262.93 support=246.0 resistance=333.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:32 PM market time freshness=DELAYED_CURRENT RSI=41.05 liquidity=573691.13 spike=0.25
- GTWL.CA: score=7.6 buy_ready=False sector_rank=18 price=121.22 support=116.16 resistance=238.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:00 PM market time freshness=DELAYED_CURRENT RSI=21.22 liquidity=179054288.0 spike=1.1
- HDBK.CA: score=7.51 buy_ready=False sector_rank=9 price=93.71 support=96.1 resistance=121.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=29.19 liquidity=27825226.0 spike=1.38
- HELI.CA: score=7.4 buy_ready=False sector_rank=17 price=6.84 support=6.8 resistance=8.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=30.91 liquidity=63282372.0 spike=0.79
- HRHO.CA: score=13.4 buy_ready=False sector_rank=14 price=24.7 support=22.81 resistance=27.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=52.6 liquidity=54353064.0 spike=0.4
- ICID.CA: score=8.19 buy_ready=False sector_rank=18 price=16.84 support=16.3 resistance=20.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:37 PM market time freshness=DELAYED_CURRENT RSI=42.54 liquidity=2789562.25 spike=0.34
- IDRE.CA: score=5.6 buy_ready=False sector_rank=18 price=40.11 support=40.05 resistance=59.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=36.34 liquidity=4195873.5 spike=0.42
- IFAP.CA: score=1.91 buy_ready=False sector_rank=21 price=18.01 support=17.17 resistance=21.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:51 PM market time freshness=DELAYED_CURRENT RSI=26.04 liquidity=5511478.5 spike=0.83
- INFI.CA: score=17.44 buy_ready=False sector_rank=18 price=127.48 support=104.0 resistance=138.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=52.9 liquidity=28014176.0 spike=1.52
- IRON.CA: score=11.58 buy_ready=False sector_rank=19 price=26.35 support=25.01 resistance=32.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=42.15 liquidity=11274399.0 spike=1.09
- ISMA.CA: score=5.33 buy_ready=False sector_rank=18 price=20.74 support=18.91 resistance=31.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=30.17 liquidity=8566478.0 spike=1.18
- ISMQ.CA: score=6.4 buy_ready=False sector_rank=19 price=7.1 support=7.07 resistance=9.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=31.38 liquidity=15579017.0 spike=0.82
- ISPH.CA: score=6.58 buy_ready=False sector_rank=12 price=10.64 support=10.03 resistance=12.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=33.75 liquidity=33801620.0 spike=0.71
- JUFO.CA: score=7.24 buy_ready=False sector_rank=7 price=23.0 support=23.1 resistance=27.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=31.74 liquidity=18918860.0 spike=1.12
- KABO.CA: score=6.02 buy_ready=False sector_rank=16 price=6.7 support=6.91 resistance=9.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=33.19 liquidity=9622974.0 spike=0.42
- KWIN.CA: score=-0.96 buy_ready=False sector_rank=18 price=63.09 support=60.0 resistance=93.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=19.53 liquidity=2640791.5 spike=0.32
- KZPC.CA: score=7.87 buy_ready=False sector_rank=18 price=12.91 support=12.15 resistance=14.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=41.67 liquidity=2471830.75 spike=0.3
- LCSW.CA: score=13.82 buy_ready=False sector_rank=13 price=32.6 support=28.86 resistance=35.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=55.88 liquidity=9418423.0 spike=0.47
- LUTS.CA: score=2.78 buy_ready=False sector_rank=18 price=0.7 support=0.63 resistance=0.71 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=64831932.0 spike=1.19
- MAAL.CA: score=7.24 buy_ready=False sector_rank=18 price=7.85 support=7.38 resistance=12.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=15.62 liquidity=9841534.0 spike=0.39
- MASR.CA: score=12.54 buy_ready=False sector_rank=18 price=7.02 support=6.82 resistance=7.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=48.04 liquidity=58443012.0 spike=1.07
- MBSC.CA: score=12.4 buy_ready=False sector_rank=13 price=334.61 support=288.0 resistance=414.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=51.98 liquidity=48027812.0 spike=0.54
- MCQE.CA: score=11.4 buy_ready=False sector_rank=13 price=161.72 support=160.0 resistance=224.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=36.18 liquidity=46334016.0 spike=0.8
- MCRO.CA: score=6.4 buy_ready=False sector_rank=18 price=1.31 support=1.25 resistance=1.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=30.91 liquidity=31241720.0 spike=0.57
- MENA.CA: score=-1.11 buy_ready=False sector_rank=17 price=5.93 support=5.57 resistance=7.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:38 PM market time freshness=DELAYED_CURRENT RSI=32.71 liquidity=1487640.25 spike=0.92
- MEPA.CA: score=8.54 buy_ready=False sector_rank=18 price=1.52 support=1.49 resistance=2.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=37.66 liquidity=7136292.5 spike=0.76
- MFPC.CA: score=12.4 buy_ready=False sector_rank=19 price=43.5 support=42.0 resistance=51.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=38.26 liquidity=51473128.0 spike=0.77
- MFSC.CA: score=-2.21 buy_ready=False sector_rank=18 price=37.07 support=36.25 resistance=49.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT RSI=20.12 liquidity=1385071.38 spike=0.63
- MHOT.CA: score=-0.14 buy_ready=False sector_rank=6 price=15.56 support=15.08 resistance=19.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:56 PM market time freshness=DELAYED_CURRENT RSI=30.23 liquidity=2837900.5 spike=0.16
- MICH.CA: score=10.83 buy_ready=False sector_rank=18 price=39.34 support=38.0 resistance=47.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:00 PM market time freshness=DELAYED_CURRENT RSI=39.02 liquidity=8426578.0 spike=0.97
- MILS.CA: score=2.92 buy_ready=False sector_rank=18 price=146.08 support=141.0 resistance=207.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=24.99 liquidity=5523168.0 spike=0.71
- MIPH.CA: score=4.46 buy_ready=False sector_rank=12 price=751.21 support=666.66 resistance=1000.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=46.49 liquidity=1888803.88 spike=0.2
- MOED.CA: score=6.4 buy_ready=False sector_rank=18 price=0.56 support=0.57 resistance=0.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:00 PM market time freshness=DELAYED_CURRENT RSI=32.17 liquidity=13144255.0 spike=0.82
- MOIL.CA: score=2.9 buy_ready=False sector_rank=4 price=0.67 support=0.63 resistance=0.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:52 PM market time freshness=DELAYED_CURRENT RSI=22.83 liquidity=777249.5 spike=2.69
- MOIN.CA: score=2.55 buy_ready=False sector_rank=18 price=29.8 support=28.8 resistance=38.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=29.88 liquidity=5146084.0 spike=0.52
- MOSC.CA: score=4.52 buy_ready=False sector_rank=18 price=249.91 support=231.0 resistance=329.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=37.42 liquidity=2120389.0 spike=0.61
- MPCI.CA: score=8.42 buy_ready=False sector_rank=18 price=303.85 support=294.2 resistance=455.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=27.71 liquidity=156338528.0 spike=1.51
- MPCO.CA: score=7.4 buy_ready=False sector_rank=21 price=1.92 support=1.84 resistance=3.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=18.68 liquidity=103013952.0 spike=0.82
- MPRC.CA: score=7.56 buy_ready=False sector_rank=18 price=34.58 support=32.15 resistance=41.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=33.86 liquidity=18005100.0 spike=1.08
- MTIE.CA: score=6.7 buy_ready=False sector_rank=11 price=7.28 support=7.27 resistance=8.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=34.91 liquidity=14914197.0 spike=0.8
- NAHO.CA: score=3.73 buy_ready=False sector_rank=18 price=0.13 support=0.12 resistance=0.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:39 PM market time freshness=DELAYED_CURRENT RSI=47.06 liquidity=50753.7 spike=1.64
- NCCW.CA: score=6.4 buy_ready=False sector_rank=18 price=5.52 support=5.3 resistance=8.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=31.55 liquidity=17764688.0 spike=0.47
- NEDA.CA: score=4.55 buy_ready=False sector_rank=18 price=2.6 support=2.47 resistance=2.8 source=Yahoo Finance as_of=2026-10-17T21:00:00+00:00 freshness=FRESH RSI=60.0 liquidity=154640.19 spike=0.24
- NHPS.CA: score=1.56 buy_ready=False sector_rank=18 price=61.24 support=61.18 resistance=86.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:52 PM market time freshness=DELAYED_CURRENT RSI=30.23 liquidity=5156096.5 spike=0.35
- NINH.CA: score=6.4 buy_ready=False sector_rank=18 price=15.14 support=15.19 resistance=23.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=19.22 liquidity=12679049.0 spike=0.94
- NIPH.CA: score=6.12 buy_ready=False sector_rank=12 price=295.65 support=230.01 resistance=302.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=332608000.0 spike=2.77
- OBRI.CA: score=13.4 buy_ready=False sector_rank=18 price=25.12 support=22.8 resistance=33.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=46.7 liquidity=11541825.0 spike=0.79
- OCDI.CA: score=7.4 buy_ready=False sector_rank=17 price=24.48 support=24.0 resistance=30.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=33.09 liquidity=19899474.0 spike=0.48
- OCPH.CA: score=6.66 buy_ready=False sector_rank=18 price=193.06 support=190.0 resistance=247.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:00 PM market time freshness=DELAYED_CURRENT RSI=38.51 liquidity=4544491.5 spike=1.36
- ODIN.CA: score=2.4 buy_ready=False sector_rank=18 price=2.22 support=1.91 resistance=2.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=9739369.0 spike=1.13
- OFH.CA: score=7.4 buy_ready=False sector_rank=18 price=0.72 support=0.73 resistance=1.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=31.84 liquidity=25693530.0 spike=0.28
- OIH.CA: score=7.84 buy_ready=False sector_rank=8 price=1.77 support=1.7 resistance=2.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=25.0 liquidity=29977386.0 spike=0.38
- OLFI.CA: score=4.52 buy_ready=False sector_rank=7 price=20.06 support=19.8 resistance=23.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=22.65 liquidity=7524023.5 spike=0.46
- ORAS.CA: score=6.6 buy_ready=False sector_rank=2 price=852.23 support=830.0 resistance=875.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=128722848.0 spike=1.0
- ORHD.CA: score=6.4 buy_ready=False sector_rank=17 price=10.0 support=10.01 resistance=44.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=2.84 liquidity=94072616.0 spike=0.64
- ORWE.CA: score=12.4 buy_ready=False sector_rank=16 price=26.08 support=26.01 resistance=28.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=41.75 liquidity=21144618.0 spike=0.47
- PHAR.CA: score=13.06 buy_ready=False sector_rank=12 price=103.94 support=101.5 resistance=122.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=41.96 liquidity=79674888.0 spike=1.24
- PHDC.CA: score=14.4 buy_ready=False sector_rank=17 price=12.5 support=12.2 resistance=13.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=39.52 liquidity=49269256.0 spike=0.52
- PHTV.CA: score=4.77 buy_ready=False sector_rank=18 price=330.0 support=315.0 resistance=377.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:56 PM market time freshness=DELAYED_CURRENT RSI=42.94 liquidity=1311287.38 spike=1.53
- POUL.CA: score=12.0 buy_ready=False sector_rank=7 price=10.2 support=9.12 resistance=40.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=3.26 liquidity=239605968.0 spike=8.5
- PRCL.CA: score=6.86 buy_ready=False sector_rank=13 price=20.25 support=20.01 resistance=32.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=27.37 liquidity=13212958.0 spike=1.23
- PRDC.CA: score=11.4 buy_ready=False sector_rank=17 price=5.94 support=5.91 resistance=8.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=38.46 liquidity=15783782.0 spike=0.45
- PRMH.CA: score=-4.85 buy_ready=False sector_rank=18 price=2.06 support=1.81 resistance=2.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=2754441.0 spike=0.76
- RACC.CA: score=6.69 buy_ready=False sector_rank=18 price=8.08 support=8.14 resistance=10.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=33.9 liquidity=9254588.0 spike=1.52
- RAKT.CA: score=1.68 buy_ready=False sector_rank=18 price=22.06 support=20.26 resistance=25.08 source=Yahoo Finance as_of=2026-10-17T21:00:00+00:00 freshness=FRESH RSI=49.81 liquidity=282787.13 spike=0.78
- RAYA.CA: score=11.4 buy_ready=False sector_rank=20 price=5.77 support=5.61 resistance=7.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=35.04 liquidity=18068124.0 spike=0.51
- RMDA.CA: score=7.64 buy_ready=False sector_rank=12 price=5.03 support=4.83 resistance=6.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=30.77 liquidity=27752128.0 spike=1.03
- ROTO.CA: score=5.63 buy_ready=False sector_rank=18 price=34.91 support=35.56 resistance=42.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=36.12 liquidity=4234292.0 spike=0.5
- RREI.CA: score=2.48 buy_ready=False sector_rank=18 price=3.31 support=3.29 resistance=4.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:56 PM market time freshness=DELAYED_CURRENT RSI=32.76 liquidity=6078458.0 spike=0.75
- RTVC.CA: score=-1.46 buy_ready=False sector_rank=18 price=3.26 support=3.26 resistance=4.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=32.67 liquidity=2136564.25 spike=0.83
- RUBX.CA: score=17.4 buy_ready=False sector_rank=18 price=16.32 support=12.9 resistance=19.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:00 PM market time freshness=DELAYED_CURRENT RSI=48.7 liquidity=50943328.0 spike=0.48
- SAUD.CA: score=12.75 buy_ready=False sector_rank=9 price=20.58 support=20.2 resistance=26.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=39.56 liquidity=13211814.0 spike=0.61
- SCEM.CA: score=16.4 buy_ready=False sector_rank=13 price=85.52 support=74.55 resistance=95.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=55.79 liquidity=18974696.0 spike=0.28
- SCFM.CA: score=9.16 buy_ready=False sector_rank=18 price=217.48 support=220.35 resistance=280.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=35.17 liquidity=4500545.0 spike=2.63
- SCTS.CA: score=-0.5 buy_ready=False sector_rank=10 price=476.42 support=460.0 resistance=611.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=22.15 liquidity=1209444.75 spike=1.29
- SDTI.CA: score=14.98 buy_ready=False sector_rank=18 price=83.3 support=76.1 resistance=94.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=42.97 liquidity=7576176.0 spike=0.23
- SEIG.CA: score=4.88 buy_ready=False sector_rank=18 price=202.43 support=173.1 resistance=259.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=37.34 liquidity=2241504.25 spike=1.12
- SIPC.CA: score=2.72 buy_ready=False sector_rank=18 price=5.57 support=5.17 resistance=5.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=62661736.0 spike=1.16
- SKPC.CA: score=6.4 buy_ready=False sector_rank=19 price=14.93 support=14.6 resistance=18.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:56 PM market time freshness=DELAYED_CURRENT RSI=27.3 liquidity=35442144.0 spike=0.48
- SMFR.CA: score=3.59 buy_ready=False sector_rank=18 price=190.8 support=181.6 resistance=245.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:55 PM market time freshness=DELAYED_CURRENT RSI=40.16 liquidity=2192958.75 spike=0.69
- SNFC.CA: score=5.83 buy_ready=False sector_rank=18 price=10.97 support=10.81 resistance=11.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=43.42 liquidity=3425611.0 spike=0.32
- SPIN.CA: score=0.9 buy_ready=False sector_rank=16 price=14.0 support=14.06 resistance=17.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=30.14 liquidity=4498897.0 spike=0.85
- SPMD.CA: score=2.78 buy_ready=False sector_rank=18 price=0.37 support=0.34 resistance=0.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=18570220.0 spike=1.19
- SUGR.CA: score=10.78 buy_ready=False sector_rank=7 price=54.7 support=50.5 resistance=60.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=51.16 liquidity=5786456.5 spike=0.58
- SVCE.CA: score=6.4 buy_ready=False sector_rank=18 price=8.9 support=8.81 resistance=12.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=33.33 liquidity=44650460.0 spike=0.56
- SWDY.CA: score=12.62 buy_ready=False sector_rank=15 price=108.04 support=102.31 resistance=128.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=41.0 liquidity=68051520.0 spike=1.11
- TALM.CA: score=15.71 buy_ready=False sector_rank=10 price=20.01 support=18.71 resistance=23.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=50.15 liquidity=26513336.0 spike=0.76
- TMGH.CA: score=6.4 buy_ready=False sector_rank=17 price=81.53 support=81.22 resistance=96.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=20.13 liquidity=129237440.0 spike=0.59
- TRTO.CA: score=0.13 buy_ready=False sector_rank=18 price=0.06 support=0.05 resistance=0.07 source=Yahoo Finance as_of=2026-10-17T21:00:00+00:00 freshness=FRESH RSI=78.95 liquidity=13117.0 spike=1.36
- UEFM.CA: score=2.55 buy_ready=False sector_rank=18 price=478.05 support=407.57 resistance=550.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:49 PM market time freshness=DELAYED_CURRENT RSI=55.2 liquidity=1145956.25 spike=0.37
- UEGC.CA: score=15.9 buy_ready=False sector_rank=18 price=1.57 support=1.34 resistance=1.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=54.12 liquidity=61599572.0 spike=1.25
- UNIP.CA: score=8.38 buy_ready=False sector_rank=18 price=0.3 support=0.3 resistance=0.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=39.38 liquidity=6975177.0 spike=0.79
- UNIT.CA: score=3.46 buy_ready=False sector_rank=17 price=16.29 support=16.0 resistance=19.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=39.88 liquidity=1060986.25 spike=0.24
- WCDF.CA: score=-1.24 buy_ready=False sector_rank=18 price=499.72 support=506.1 resistance=719.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:53 PM market time freshness=DELAYED_CURRENT RSI=21.92 liquidity=2361220.25 spike=0.81
- WKOL.CA: score=8.38 buy_ready=False sector_rank=18 price=257.45 support=266.01 resistance=352.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:00 PM market time freshness=DELAYED_CURRENT RSI=29.25 liquidity=11915257.0 spike=1.99
- ZEOT.CA: score=12.68 buy_ready=False sector_rank=18 price=10.61 support=9.75 resistance=14.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=39.77 liquidity=9862568.0 spike=1.21
- ZMID.CA: score=7.4 buy_ready=False sector_rank=17 price=6.83 support=6.5 resistance=9.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=18.84 liquidity=52412648.0 spike=0.55

## Backtesting Lite
- ETEL.CA: 180d return=91.76%, max drawdown=-30.44%, MA20>MA50 days last20=20, as_of=2026-10-17T21:00:00+00:00
- CPCI.CA: 180d return=121.04%, max drawdown=-7.27%, MA20>MA50 days last20=20, as_of=2026-10-17T21:00:00+00:00
- INFI.CA: 180d return=8.57%, max drawdown=-37.66%, MA20>MA50 days last20=7, as_of=2026-10-17T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- ETEL.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Telecom Egypt summary=Evidence rejected for ETEL.CA: source text did not clearly match ETEL.CA / Telecom Egypt.
- CPCI.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Kahira Pharmaceuticals & Chemical Industries Company summary=Kahira Pharmaceuticals&#39; net profits up 22.5% in H1-21/22; Kahira Pharmaceuticals sees EGP 9m block trading deal; Adel Taha Abdel Wahab named Chairman of Kahira Pharmaceuticals
  - Kahira Pharmaceuticals&#39; net profits up 22.5% in H1-21/22: https://english.mubasher.info/news/3910780/Kahira-Pharmaceuticals-net-profits-up-22-5-in-H1-21-22/
  - Kahira Pharmaceuticals sees EGP 9m block trading deal: https://english.mubasher.info/news/3903033/Kahira-Pharmaceuticals-sees-EGP-9m-block-trading-deal/
  - Adel Taha Abdel Wahab named Chairman of Kahira Pharmaceuticals: https://english.mubasher.info/news/3816375/Adel-Taha-Abdel-Wahab-named-Chairman-of-Kahira-Pharmaceuticals/
- INFI.CA: status=RECENT_ACCEPTED latest=2026-01-01 age_days=291 sources=3 expected=Ismailia National Co. for Food Industries summary=Foodico stock targets higher levels; Foodico plans to log nearly EGP 70.5m profits in 2026; Foodico to secure EGP 12m loan from national bank
  - Foodico stock targets higher levels: https://english.mubasher.info/news/4564894/Foodico-stock-targets-higher-levels/
  - Foodico plans to log nearly EGP 70.5m profits in 2026: https://english.mubasher.info/news/4541309/Foodico-plans-to-log-nearly-EGP-70-5m-profits-in-2026/
  - Foodico to secure EGP 12m loan from national bank: https://english.mubasher.info/news/3888447/Foodico-to-secure-EGP-12m-loan-from-national-bank/
- ARCC.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=656 sources=3 expected=Arabian Cement Company summary=Arabian Cement to pay out EGP 2bn dividends for 2025; Arabian Cement’s EGM approves nearly EGP 8m capital cut; Arabian Cement’s consolidated profits near EGP 3.6bn in 2025
  - Arabian Cement to pay out EGP 2bn dividends for 2025: https://english.mubasher.info/news/4587912/Arabian-Cement-to-pay-out-EGP-2bn-dividends-for-2025/
  - Arabian Cement’s EGM approves nearly EGP 8m capital cut: https://english.mubasher.info/news/4583762/Arabian-Cement-s-EGM-approves-nearly-EGP-8m-capital-cut/
  - Arabian Cement’s consolidated profits near EGP 3.6bn in 2025: https://english.mubasher.info/news/4562679/Arabian-Cement-s-consolidated-profits-near-EGP-3-6bn-in-2025/
- ARAB.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Arab Developers Holding summary=Arab Developers Holding unveils EGP 1bn expansion plans to improve financial efficiency; FRA gives initial approval for Arab Developers’ rights issue; Arab Developers stock stabilizes after correction
  - Arab Developers Holding unveils EGP 1bn expansion plans to improve financial efficiency: https://english.mubasher.info/news/4601724/Arab-Developers-Holding-unveils-EGP-1bn-expansion-plans-to-improve-financial-efficiency/
  - FRA gives initial approval for Arab Developers’ rights issue: https://english.mubasher.info/news/4582627/FRA-gives-initial-approval-for-Arab-Developers-rights-issue/
  - Arab Developers stock stabilizes after correction: https://english.mubasher.info/news/4564643/Arab-Developers-stock-stabilizes-after-correction/
- RUBX.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Rubex International for Plastic and Acrylic Manufacturing summary=Evidence rejected for RUBX.CA: source text did not clearly match RUBX.CA / Rubex International for Plastic and Acrylic Manufacturing.
- EFIH.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=E-Finance For Digital and Financial Investments summary=Evidence rejected for EFIH.CA: source text did not clearly match EFIH.CA / E-Finance For Digital and Financial Investments.
- AMOC.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Alexandria Mineral Oils summary=AMOC achieves EGP 10.5bn consolidated sales in Q1-26; AMOC studies potential project with Germany’s SULZER; AMOC to pay out EGP 0.4/shr dividends for H2-25
  - AMOC achieves EGP 10.5bn consolidated sales in Q1-26: https://english.mubasher.info/news/4604903/AMOC-achieves-EGP-10-5bn-consolidated-sales-in-Q1-26/
  - AMOC studies potential project with Germany’s SULZER: https://english.mubasher.info/news/4586853/AMOC-studies-potential-project-with-Germany-s-SULZER/
  - AMOC to pay out EGP 0.4/shr dividends for H2-25: https://english.mubasher.info/news/4586775/AMOC-to-pay-out-EGP-0-4-shr-dividends-for-H2-25/

## Warnings
- Evidence rejected for ETEL.CA: source text did not clearly match ETEL.CA / Telecom Egypt.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence for CPCI.CA matches the company but no source/report date was detected.
- Evidence for ARCC.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for ARAB.CA matches the company but no source/report date was detected.
- Evidence rejected for RUBX.CA: source text did not clearly match RUBX.CA / Rubex International for Plastic and Acrylic Manufacturing.
- Evidence rejected for EFIH.CA: source text did not clearly match EFIH.CA / E-Finance For Digital and Financial Investments.
- Evidence for AMOC.CA matches the company but no source/report date was detected.
