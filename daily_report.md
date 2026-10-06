# Telegram-First EGX Scanner Report

Scan phase: Intraday liquidity update
Generated UTC: 2026-10-06T14:42:58.332701+00:00
Generated Cairo: 2026-10-06 17:42
Run timing: target 11:00 Cairo | generated Cairo 2026-10-06 17:42 | cron 0 8 * * 0-4
Trigger: scheduled cron=0 8 * * 0-4 mapped to intraday; Cairo now 2026-10-06 17:39

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 3
- Tradeable price/liquidity tickers: 175/187
- Top sector: Telecommunications

## Market Context
- Market trend: Bearish
- Source: Mubasher EGX market page (delayed public data)
- As of: Tuesday, October 06
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 15.79% / above MA50 31.58%
- EGX70 regime: BEARISH / above MA20 25.0% / above MA50 30.56%
- Sector breadth: 42.86%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- HRHO.CA: liquidity=432105632.0 spike=3.88 score=27.68
- CCAP.CA: liquidity=422883520.0 spike=0.51 score=19.4
- AMOC.CA: liquidity=323626272.0 spike=2.44 score=24.1
- COMI.CA: liquidity=295190016.0 spike=0.53 score=9.54
- RUBX.CA: liquidity=255272896.0 spike=3.3 score=9.33

## AI Narrative
- Provider: OpenRouter OK
- Model: nvidia/nemotron-3-super-120b-a12b:free
- Summary: EGX30 and EGX70 are bearish with weak breadth (42.86% above MA20); risk mode is DEFENSIVE_NO_NEW_BUY, so the scanner maintains HOLD despite spotting accumulation‑spike stocks.
- Top tickets (EFIH.CA, HRHO.CA, GBCO.CA) show accumulation‑spike liquidity and a BULLISH_WATCH outlook, but trade above 20‑day support with mixed resistance distances.
- Liquidity spikes range 2.4‑4.3× average, while RSI sits between 55‑61, indicating moderate momentum without overbought extremes.
- Sector leadership is confined to Telecommunications, Fintech & Payments, and Education; most flagged stocks lie outside these leading sectors, lowering conviction.
- EGX30/EGX70 bearish trend and defensive risk mode override individual bullish signals, keeping the scanner in HOLD with low confidence.
- Uncertainty persists due to sub‑50% MA20 breadth and proximity to resistance, so any near‑term move could reverse quickly.

## Top Liquidity Spikes
- DAPH.CA: spike=7.2 liquidity=198143456.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- SEIG.CA: spike=6.23 liquidity=11234654.0 outlook=CONSTRUCTIVE score=57.82 buy_ready=False
- LCSW.CA: spike=5.65 liquidity=86468392.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- RAKT.CA: spike=5.41 liquidity=1328407.13 outlook=BULLISH_WATCH score=85.82 buy_ready=False
- EXPA.CA: spike=4.25 liquidity=133471608.0 outlook=BULLISH_WATCH score=85.85 buy_ready=False

## Sector Leaderboard
- #1 Telecommunications: score=12.51 5d=5.63% 20d=11.67% aboveMA50=100.0%
- #2 Fintech & Payments: score=8.82 5d=6.55% 20d=-1.6% aboveMA50=50.0%
- #3 Education: score=7.98 5d=4.04% 20d=8.12% aboveMA50=66.67%
- #4 Automotive & Distribution: score=6.91 5d=5.28% 20d=-1.74% aboveMA50=50.0%
- #5 Investment Holding: score=6.86 5d=1.61% 20d=13.4% aboveMA50=66.67%
- #6 Transportation & Logistics: score=5.81 5d=6.75% 20d=-1.89% aboveMA50=50.0%
- #7 Energy & Petrochemicals: score=5.54 5d=1.86% 20d=2.59% aboveMA50=33.33%
- #8 Non-bank Financial Services: score=4.2 5d=5.81% 20d=-7.26% aboveMA50=40.0%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- EFIH.CA: BULLISH_WATCH score=100 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=far above support
- CIRA.CA: BULLISH_WATCH score=93.98 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- ICID.CA: BULLISH_WATCH score=89.82 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- GBCO.CA: BULLISH_WATCH score=87.91 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=No major short-term scanner risk flags.
- EXPA.CA: BULLISH_WATCH score=85.85 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- RAKT.CA: BULLISH_WATCH score=85.82 liquidity=TRADEABLE sector=IMPROVING risk=sector is not leading
- TALM.CA: BULLISH_WATCH score=83.98 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; far above support
- AMOC.CA: BULLISH_WATCH score=80.54 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=close to resistance
- HRHO.CA: BULLISH_WATCH score=80.2 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- SIPC.CA: BULLISH_WATCH score=79.82 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=far above support; sector is not leading

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- EKHO.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ARVA.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=9.75 buy_ready=False sector_rank=14 price=265.53 support=230.11 resistance=359.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=25.59 liquidity=20503122.0 spike=1.01
- ABUK.CA: score=17.63 buy_ready=False sector_rank=15 price=86.53 support=83.55 resistance=96.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=47.65 liquidity=26489044.0 spike=0.22
- ACAMD.CA: score=18.73 buy_ready=False sector_rank=14 price=2.05 support=1.87 resistance=2.16 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=51.02 liquidity=34152072.0 spike=0.78
- ACGC.CA: score=16.68 buy_ready=False sector_rank=9 price=14.39 support=13.11 resistance=16.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=57.59 liquidity=8066355.0 spike=0.38
- ADCI.CA: score=6.14 buy_ready=False sector_rank=14 price=270.94 support=256.0 resistance=298.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=47.3 liquidity=1411385.88 spike=0.59
- ADIB.CA: score=16.26 buy_ready=False sector_rank=10 price=48.18 support=48.2 resistance=54.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=36.98 liquidity=96988848.0 spike=1.36
- ADPC.CA: score=10.25 buy_ready=False sector_rank=14 price=3.56 support=3.4 resistance=4.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=38.61 liquidity=6524606.5 spike=0.4
- AFDI.CA: score=13.62 buy_ready=False sector_rank=14 price=53.55 support=47.7 resistance=56.82 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=51.74 liquidity=4893312.5 spike=0.67
- AFMC.CA: score=16.73 buy_ready=False sector_rank=14 price=156.22 support=131.0 resistance=184.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=48.59 liquidity=14460122.0 spike=0.44
- AJWA.CA: score=22.43 buy_ready=False sector_rank=14 price=197.44 support=176.0 resistance=193.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=76.88 liquidity=44293128.0 spike=2.85
- ALCN.CA: score=23.32 buy_ready=False sector_rank=6 price=34.7 support=30.4 resistance=36.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=65.61 liquidity=12262324.0 spike=0.36
- ALUM.CA: score=7.2 buy_ready=False sector_rank=14 price=23.69 support=21.65 resistance=28.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=39.84 liquidity=2476551.5 spike=0.46
- AMER.CA: score=8.66 buy_ready=False sector_rank=19 price=5.05 support=4.79 resistance=5.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=134808864.0 spike=3.33
- AMES.CA: score=15.73 buy_ready=False sector_rank=14 price=47.31 support=40.15 resistance=82.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=44.51 liquidity=43177528.0 spike=0.2
- AMIA.CA: score=20.37 buy_ready=False sector_rank=14 price=19.35 support=17.12 resistance=19.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=75.79 liquidity=45078112.0 spike=2.82
- AMOC.CA: score=24.1 buy_ready=False sector_rank=7 price=14.36 support=12.18 resistance=14.63 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=59.7 liquidity=323626272.0 spike=2.44
- APSW.CA: score=13.27 buy_ready=False sector_rank=14 price=8.6 support=7.81 resistance=8.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=54.36 liquidity=1102873.63 spike=1.72
- ARAB.CA: score=8.64 buy_ready=False sector_rank=19 price=0.28 support=0.26 resistance=0.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=228523888.0 spike=3.32
- ARCC.CA: score=22.3 buy_ready=False sector_rank=12 price=70.51 support=60.01 resistance=78.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=49.71 liquidity=30130612.0 spike=1.06
- AREH.CA: score=7.66 buy_ready=False sector_rank=14 price=1.3 support=1.14 resistance=1.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=37.78 liquidity=3932762.0 spike=0.33
- ASCM.CA: score=15.26 buy_ready=False sector_rank=14 price=57.38 support=53.8 resistance=66.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=46.98 liquidity=8533268.0 spike=0.7
- ASPI.CA: score=9.73 buy_ready=False sector_rank=14 price=0.36 support=0.33 resistance=0.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=32.54 liquidity=19336642.0 spike=0.39
- ATLC.CA: score=13.84 buy_ready=False sector_rank=8 price=6.17 support=5.2 resistance=7.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=40.11 liquidity=5159054.5 spike=0.39
- ATQA.CA: score=17.63 buy_ready=False sector_rank=15 price=12.16 support=10.91 resistance=13.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=44.34 liquidity=71462776.0 spike=0.84
- AXPH.CA: score=3.95 buy_ready=False sector_rank=14 price=1498.34 support=1334.35 resistance=1987.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:08 PM market time freshness=DELAYED_CURRENT RSI=33.15 liquidity=4220480.0 spike=0.64
- BINV.CA: score=20.83 buy_ready=False sector_rank=5 price=58.0 support=49.91 resistance=72.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=64.86 liquidity=7425051.0 spike=0.3
- BIOC.CA: score=18.49 buy_ready=False sector_rank=14 price=336.26 support=225.21 resistance=380.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=65.73 liquidity=167170048.0 spike=1.88
- BTFH.CA: score=14.98 buy_ready=False sector_rank=8 price=2.77 support=2.65 resistance=3.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=43.06 liquidity=104175496.0 spike=1.15
- CAED.CA: score=12.11 buy_ready=False sector_rank=14 price=121.24 support=103.1 resistance=150.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=42.84 liquidity=5384648.5 spike=0.27
- CANA.CA: score=12.19 buy_ready=False sector_rank=10 price=45.17 support=41.35 resistance=52.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=67.09 liquidity=3647450.75 spike=0.16
- CCAP.CA: score=19.4 buy_ready=False sector_rank=5 price=6.56 support=6.0 resistance=7.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=51.06 liquidity=422883520.0 spike=0.51
- CCRS.CA: score=9.57 buy_ready=False sector_rank=14 price=2.34 support=2.21 resistance=2.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=40.21 liquidity=4843641.0 spike=0.33
- CEFM.CA: score=5.97 buy_ready=False sector_rank=14 price=139.84 support=113.0 resistance=154.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=45.24 liquidity=1240701.38 spike=0.31
- CERA.CA: score=20.89 buy_ready=False sector_rank=14 price=1.41 support=1.18 resistance=1.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=54.29 liquidity=221149408.0 spike=1.58
- CFGH.CA: score=-1.22 buy_ready=False sector_rank=14 price=0.11 support=0.11 resistance=0.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:09 PM market time freshness=DELAYED_CURRENT RSI=0.0 liquidity=8846.85 spike=1.02
- CICH.CA: score=7.17 buy_ready=False sector_rank=8 price=12.01 support=10.75 resistance=13.0 source=Yahoo Finance as_of=2026-10-04T21:00:00+00:00 freshness=FRESH RSI=51.43 liquidity=1486573.81 spike=0.35
- CIEB.CA: score=9.58 buy_ready=False sector_rank=10 price=24.29 support=23.0 resistance=26.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=47.86 liquidity=4036066.5 spike=0.41
- CIRA.CA: score=22.4 buy_ready=False sector_rank=3 price=39.49 support=36.62 resistance=41.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=52.25 liquidity=15808757.0 spike=0.45
- CLHO.CA: score=16.5 buy_ready=False sector_rank=17 price=15.25 support=13.9 resistance=17.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=41.69 liquidity=51206864.0 spike=1.08
- CNFN.CA: score=12.87 buy_ready=False sector_rank=8 price=4.18 support=3.84 resistance=4.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=35.66 liquidity=8151211.5 spike=1.02
- COMI.CA: score=9.54 buy_ready=False sector_rank=10 price=125.24 support=124.5 resistance=141.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=27.59 liquidity=295190016.0 spike=0.53
- COPR.CA: score=21.73 buy_ready=False sector_rank=14 price=0.49 support=0.44 resistance=0.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=54.42 liquidity=14798260.0 spike=0.57
- COSG.CA: score=8.93 buy_ready=False sector_rank=14 price=1.62 support=1.46 resistance=1.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=35.09 liquidity=4200785.0 spike=0.24
- CPCI.CA: score=8.85 buy_ready=False sector_rank=14 price=599.44 support=530.0 resistance=613.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=89.97 liquidity=2118317.0 spike=0.57
- CSAG.CA: score=8.81 buy_ready=False sector_rank=6 price=36.9 support=34.52 resistance=42.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=49.79 liquidity=2490168.75 spike=0.29
- DAPH.CA: score=9.73 buy_ready=False sector_rank=14 price=106.0 support=94.21 resistance=114.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=198143456.0 spike=7.2
- DEIN.CA: score=7.73 buy_ready=False sector_rank=14 price=10.35 support=10.35 resistance=12.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10 September 11:17 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=49.68 spike=0.01
- DOMT.CA: score=5.53 buy_ready=False sector_rank=21 price=24.5 support=23.81 resistance=28.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=39.48 liquidity=2694269.75 spike=0.58
- DSCW.CA: score=13.73 buy_ready=False sector_rank=14 price=1.7 support=1.58 resistance=1.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=36.36 liquidity=11141674.0 spike=0.55
- DTPP.CA: score=6.55 buy_ready=False sector_rank=14 price=318.01 support=310.5 resistance=334.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=168991712.0 spike=1.91
- EALR.CA: score=5.35 buy_ready=False sector_rank=14 price=343.3 support=312.0 resistance=411.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=32.64 liquidity=6621978.0 spike=0.68
- EASB.CA: score=6.98 buy_ready=False sector_rank=14 price=7.53 support=6.04 resistance=9.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=37.29 liquidity=2248732.25 spike=0.15
- EAST.CA: score=8.33 buy_ready=False sector_rank=21 price=29.01 support=27.91 resistance=36.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=16.02 liquidity=63210792.0 spike=1.25
- EBSC.CA: score=4.44 buy_ready=False sector_rank=14 price=1.83 support=1.61 resistance=2.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=35.44 liquidity=707335.19 spike=0.16
- ECAP.CA: score=8.46 buy_ready=False sector_rank=14 price=30.24 support=29.13 resistance=34.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=32.09 liquidity=8116321.0 spike=1.81
- EDFM.CA: score=5.8 buy_ready=False sector_rank=14 price=399.94 support=354.0 resistance=431.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=40.95 liquidity=1076073.88 spike=0.84
- EEII.CA: score=12.84 buy_ready=False sector_rank=14 price=2.16 support=2.02 resistance=2.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=46.84 liquidity=7114373.0 spike=0.74
- EFIC.CA: score=8.63 buy_ready=False sector_rank=15 price=165.28 support=147.0 resistance=239.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=25.06 liquidity=37575176.0 spike=0.4
- EFID.CA: score=7.83 buy_ready=False sector_rank=21 price=19.05 support=18.1 resistance=32.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=12.33 liquidity=30690510.0 spike=0.5
- EFIH.CA: score=31.14 buy_ready=False sector_rank=2 price=24.8 support=20.2 resistance=24.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=55.18 liquidity=156655232.0 spike=2.87
- EGAL.CA: score=14.63 buy_ready=False sector_rank=15 price=343.41 support=331.5 resistance=380.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=35.32 liquidity=37357380.0 spike=0.69
- EGAS.CA: score=9.37 buy_ready=False sector_rank=7 price=56.33 support=53.62 resistance=60.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=53.64 liquidity=3151714.75 spike=0.27
- EGBE.CA: score=10.57 buy_ready=False sector_rank=10 price=0.53 support=0.49 resistance=0.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=65.06 liquidity=29810.14 spike=0.24
- EGCH.CA: score=14.63 buy_ready=False sector_rank=15 price=13.33 support=12.88 resistance=14.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=41.53 liquidity=40635008.0 spike=0.41
- EGSA.CA: score=12.43 buy_ready=False sector_rank=1 price=8.87 support=8.82 resistance=9.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=5 October 12:40 PM market time freshness=DELAYED_CURRENT RSI=11.76 liquidity=30250.42 spike=3.82
- EGTS.CA: score=13.56 buy_ready=False sector_rank=19 price=16.9 support=15.65 resistance=19.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=51.49 liquidity=9556439.0 spike=0.27
- EHDR.CA: score=8.5 buy_ready=False sector_rank=14 price=2.53 support=2.35 resistance=3.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=32.89 liquidity=8769269.0 spike=0.7
- ELEC.CA: score=13.27 buy_ready=False sector_rank=18 price=1.88 support=1.72 resistance=2.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=43.14 liquidity=22557666.0 spike=0.33
- ELKA.CA: score=12.09 buy_ready=False sector_rank=14 price=1.6 support=1.43 resistance=1.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=39.62 liquidity=7365554.5 spike=0.51
- ELNA.CA: score=1.16 buy_ready=False sector_rank=14 price=35.22 support=33.46 resistance=38.99 source=Yahoo Finance as_of=2026-10-04T21:00:00+00:00 freshness=FRESH RSI=0.0 liquidity=287148.67 spike=1.07
- ELSH.CA: score=14.73 buy_ready=False sector_rank=14 price=11.83 support=10.8 resistance=14.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=40.11 liquidity=11372618.0 spike=0.44
- ELWA.CA: score=0.58 buy_ready=False sector_rank=14 price=1.55 support=1.43 resistance=1.9 source=Yahoo Finance as_of=2026-10-04T21:00:00+00:00 freshness=FRESH RSI=28.95 liquidity=1192602.51 spike=1.33
- EMFD.CA: score=14.86 buy_ready=False sector_rank=19 price=12.77 support=11.7 resistance=15.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=38.74 liquidity=121219608.0 spike=1.43
- ENGC.CA: score=11.82 buy_ready=False sector_rank=14 price=36.85 support=33.33 resistance=46.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=38.67 liquidity=7095203.0 spike=0.41
- EOSB.CA: score=11.01 buy_ready=False sector_rank=14 price=1.57 support=1.58 resistance=1.64 source=Yahoo Finance as_of=2026-10-04T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=78889.36 spike=1.6
- EPCO.CA: score=2.03 buy_ready=False sector_rank=14 price=9.86 support=9.25 resistance=12.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=27.11 liquidity=2298112.0 spike=0.16
- EPPK.CA: score=-4.85 buy_ready=False sector_rank=14 price=10.29 support=10.29 resistance=10.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=8 September 01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=419183.72 spike=0.28
- ETEL.CA: score=23.4 buy_ready=False sector_rank=1 price=149.89 support=120.1 resistance=156.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=75.33 liquidity=229111008.0 spike=0.75
- ETRS.CA: score=22.37 buy_ready=False sector_rank=14 price=11.05 support=9.82 resistance=11.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=52.34 liquidity=12163137.0 spike=1.32
- EXPA.CA: score=25.54 buy_ready=False sector_rank=10 price=21.5 support=20.4 resistance=22.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=56.57 liquidity=133471608.0 spike=4.25
- FAIT.CA: score=10.4 buy_ready=False sector_rank=10 price=45.42 support=38.48 resistance=48.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=44.0 liquidity=1863376.5 spike=0.49
- FAITA.CA: score=4.56 buy_ready=False sector_rank=10 price=0.98 support=0.98 resistance=0.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:36 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=17353.11 spike=0.56
- FERC.CA: score=7.1 buy_ready=False sector_rank=15 price=75.93 support=70.42 resistance=82.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=46.16 liquidity=3466545.5 spike=0.48
- FWRY.CA: score=22.04 buy_ready=False sector_rank=2 price=18.81 support=17.5 resistance=19.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=48.83 liquidity=166252640.0 spike=1.82
- GBCO.CA: score=26.28 buy_ready=False sector_rank=4 price=31.8 support=27.0 resistance=32.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=61.11 liquidity=225791888.0 spike=2.44
- GDWA.CA: score=6.64 buy_ready=False sector_rank=14 price=0.67 support=0.61 resistance=0.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=24.87 liquidity=7914876.5 spike=0.31
- GGCC.CA: score=9.73 buy_ready=False sector_rank=14 price=0.73 support=0.65 resistance=0.91 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=23.69 liquidity=13466427.0 spike=0.89
- GIHD.CA: score=9.73 buy_ready=False sector_rank=14 price=63.8 support=60.9 resistance=79.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=31.9 liquidity=15937957.0 spike=0.57
- GMCI.CA: score=4.14 buy_ready=False sector_rank=14 price=1.71 support=1.49 resistance=1.91 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=43.14 liquidity=407795.19 spike=0.89
- GRCA.CA: score=9.21 buy_ready=False sector_rank=14 price=37.59 support=32.11 resistance=62.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=44.31 liquidity=3477743.25 spike=0.14
- GSSC.CA: score=5.72 buy_ready=False sector_rank=14 price=278.09 support=246.0 resistance=333.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:09 PM market time freshness=DELAYED_CURRENT RSI=49.85 liquidity=992711.75 spike=0.23
- GTWL.CA: score=9.73 buy_ready=False sector_rank=14 price=162.96 support=124.5 resistance=245.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=26.68 liquidity=138864224.0 spike=0.9
- HDBK.CA: score=17.54 buy_ready=False sector_rank=10 price=107.02 support=102.03 resistance=123.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=52.07 liquidity=33550840.0 spike=0.94
- HELI.CA: score=14.0 buy_ready=False sector_rank=19 price=7.41 support=6.94 resistance=8.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=39.24 liquidity=58058360.0 spike=0.49
- HRHO.CA: score=27.68 buy_ready=False sector_rank=8 price=26.8 support=22.81 resistance=26.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=58.57 liquidity=432105632.0 spike=3.88
- ICID.CA: score=20.77 buy_ready=False sector_rank=14 price=18.11 support=16.52 resistance=20.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=48.26 liquidity=11818232.0 spike=1.52
- IDRE.CA: score=14.73 buy_ready=False sector_rank=14 price=51.6 support=45.0 resistance=59.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=40.59 liquidity=10221499.0 spike=0.68
- IFAP.CA: score=8.69 buy_ready=False sector_rank=11 price=19.49 support=17.17 resistance=22.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=42.3 liquidity=4463709.0 spike=0.47
- INFI.CA: score=21.13 buy_ready=False sector_rank=14 price=131.14 support=104.0 resistance=150.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=37.36 liquidity=41067272.0 spike=3.2
- IRON.CA: score=14.88 buy_ready=False sector_rank=15 price=30.72 support=25.01 resistance=30.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=58.68 liquidity=4252692.5 spike=0.35
- ISMA.CA: score=7.0 buy_ready=False sector_rank=14 price=25.98 support=22.7 resistance=34.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=40.85 liquidity=2274708.75 spike=0.16
- ISMQ.CA: score=13.47 buy_ready=False sector_rank=15 price=8.23 support=7.6 resistance=9.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=41.85 liquidity=8833625.0 spike=0.41
- ISPH.CA: score=9.34 buy_ready=False sector_rank=17 price=11.69 support=11.22 resistance=13.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=34.51 liquidity=46866828.0 spike=0.71
- JUFO.CA: score=12.83 buy_ready=False sector_rank=21 price=25.2 support=24.4 resistance=27.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=38.07 liquidity=12396644.0 spike=0.74
- KABO.CA: score=15.61 buy_ready=False sector_rank=9 price=8.63 support=7.97 resistance=10.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=41.69 liquidity=14841571.0 spike=0.44
- KWIN.CA: score=10.96 buy_ready=False sector_rank=14 price=78.03 support=72.21 resistance=98.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=38.12 liquidity=6236099.5 spike=0.48
- KZPC.CA: score=12.73 buy_ready=False sector_rank=14 price=13.19 support=12.15 resistance=14.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=29.14 liquidity=11480226.0 spike=0.52
- LCSW.CA: score=10.18 buy_ready=False sector_rank=12 price=35.27 support=33.15 resistance=35.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=86468392.0 spike=5.65
- LUTS.CA: score=18.73 buy_ready=False sector_rank=14 price=0.92 support=0.72 resistance=1.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=48.95 liquidity=50455832.0 spike=0.56
- MAAL.CA: score=19.73 buy_ready=False sector_rank=14 price=10.66 support=8.18 resistance=12.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=70.26 liquidity=15962616.0 spike=0.7
- MASR.CA: score=16.73 buy_ready=False sector_rank=14 price=7.61 support=6.82 resistance=8.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=46.27 liquidity=46180988.0 spike=0.62
- MBSC.CA: score=8.48 buy_ready=False sector_rank=12 price=382.43 support=380.02 resistance=404.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=181064864.0 spike=2.65
- MCQE.CA: score=8.18 buy_ready=False sector_rank=12 price=194.99 support=193.65 resistance=209.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=97528320.0 spike=2.5
- MCRO.CA: score=9.73 buy_ready=False sector_rank=14 price=1.51 support=1.41 resistance=1.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=34.55 liquidity=59846260.0 spike=0.6
- MENA.CA: score=8.93 buy_ready=False sector_rank=19 price=6.75 support=5.8 resistance=7.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:51 PM market time freshness=DELAYED_CURRENT RSI=52.6 liquidity=928134.19 spike=0.74
- MEPA.CA: score=7.79 buy_ready=False sector_rank=14 price=1.73 support=1.56 resistance=2.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=38.03 liquidity=3064732.25 spike=0.18
- MFPC.CA: score=17.63 buy_ready=False sector_rank=15 price=45.43 support=43.0 resistance=51.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=49.65 liquidity=19149782.0 spike=0.18
- MFSC.CA: score=6.41 buy_ready=False sector_rank=14 price=45.28 support=42.5 resistance=49.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=50.18 liquidity=1679702.25 spike=0.61
- MHOT.CA: score=10.67 buy_ready=False sector_rank=20 price=17.45 support=16.2 resistance=21.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=45.45 liquidity=7685420.0 spike=0.42
- MICH.CA: score=12.05 buy_ready=False sector_rank=14 price=47.5 support=42.01 resistance=52.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=40.34 liquidity=7319373.0 spike=0.69
- MILS.CA: score=10.41 buy_ready=False sector_rank=14 price=183.85 support=165.5 resistance=213.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=36.61 liquidity=5683890.0 spike=0.5
- MIPH.CA: score=9.11 buy_ready=False sector_rank=17 price=820.83 support=739.69 resistance=1000.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=49.71 liquidity=1772564.0 spike=0.2
- MOED.CA: score=8.73 buy_ready=False sector_rank=14 price=0.69 support=0.59 resistance=0.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=30.24 liquidity=14763992.0 spike=0.39
- MOIL.CA: score=5.64 buy_ready=False sector_rank=7 price=0.68 support=0.67 resistance=0.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=70.97 liquidity=381320.53 spike=1.52
- MOIN.CA: score=13.07 buy_ready=False sector_rank=14 price=35.07 support=32.0 resistance=45.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=45.54 liquidity=5339842.5 spike=0.3
- MOSC.CA: score=5.3 buy_ready=False sector_rank=14 price=283.4 support=257.0 resistance=329.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=39.71 liquidity=573933.63 spike=0.15
- MPCI.CA: score=9.73 buy_ready=False sector_rank=14 price=350.36 support=305.45 resistance=455.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=33.71 liquidity=70678384.0 spike=0.66
- MPCO.CA: score=13.23 buy_ready=False sector_rank=11 price=2.4 support=2.18 resistance=3.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=33.94 liquidity=72194120.0 spike=0.38
- MPRC.CA: score=13.54 buy_ready=False sector_rank=14 price=40.0 support=37.65 resistance=42.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=61.7 liquidity=4813021.0 spike=0.22
- MTIE.CA: score=15.33 buy_ready=False sector_rank=4 price=8.05 support=7.5 resistance=8.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=42.0 liquidity=7931551.0 spike=0.42
- NAHO.CA: score=4.74 buy_ready=False sector_rank=14 price=0.13 support=0.12 resistance=0.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:55 AM market time freshness=DELAYED_CURRENT RSI=46.87 liquidity=9674.72 spike=0.25
- NCCW.CA: score=12.73 buy_ready=False sector_rank=14 price=7.03 support=6.27 resistance=8.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=34.04 liquidity=24325682.0 spike=0.31
- NEDA.CA: score=4.79 buy_ready=False sector_rank=14 price=2.61 support=2.48 resistance=2.89 source=Yahoo Finance as_of=2026-10-04T21:00:00+00:00 freshness=FRESH RSI=35.71 liquidity=62509.5 spike=0.07
- NHPS.CA: score=14.81 buy_ready=False sector_rank=14 price=74.62 support=66.0 resistance=87.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=47.08 liquidity=15563600.0 spike=1.04
- NINH.CA: score=11.21 buy_ready=False sector_rank=14 price=19.16 support=18.53 resistance=24.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=38.94 liquidity=6477319.0 spike=0.42
- NIPH.CA: score=16.34 buy_ready=False sector_rank=17 price=317.47 support=290.0 resistance=368.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=53.64 liquidity=109909024.0 spike=0.86
- OBRI.CA: score=15.73 buy_ready=False sector_rank=14 price=28.5 support=22.8 resistance=33.62 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=45.07 liquidity=11861350.0 spike=0.96
- OCDI.CA: score=9.42 buy_ready=False sector_rank=19 price=27.2 support=24.2 resistance=34.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=34.53 liquidity=60306036.0 spike=1.21
- OCPH.CA: score=6.96 buy_ready=False sector_rank=14 price=227.48 support=190.0 resistance=262.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=44.1 liquidity=1230724.63 spike=0.3
- ODIN.CA: score=8.4 buy_ready=False sector_rank=14 price=2.54 support=2.35 resistance=3.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=41.74 liquidity=3670739.0 spike=0.38
- OFH.CA: score=14.73 buy_ready=False sector_rank=14 price=0.88 support=0.83 resistance=1.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=38.26 liquidity=42103628.0 spike=0.39
- OIH.CA: score=11.4 buy_ready=False sector_rank=5 price=1.86 support=1.7 resistance=2.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=25.93 liquidity=39105936.0 spike=0.36
- OLFI.CA: score=12.83 buy_ready=False sector_rank=21 price=21.08 support=21.2 resistance=23.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=33.93 liquidity=58566552.0 spike=3.85
- ORAS.CA: score=4.6 buy_ready=False sector_rank=16 price=841.0 support=819.0 resistance=844.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=178414304.0 spike=1.0
- ORHD.CA: score=9.12 buy_ready=False sector_rank=19 price=38.81 support=37.41 resistance=44.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=30.6 liquidity=168138448.0 spike=1.06
- ORWE.CA: score=18.61 buy_ready=False sector_rank=9 price=27.08 support=26.01 resistance=28.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=57.72 liquidity=25510862.0 spike=0.63
- PHAR.CA: score=16.34 buy_ready=False sector_rank=17 price=113.86 support=102.0 resistance=132.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=44.83 liquidity=28986994.0 spike=0.36
- PHDC.CA: score=16.0 buy_ready=False sector_rank=19 price=12.93 support=12.36 resistance=15.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=39.23 liquidity=97609128.0 spike=0.84
- PHTV.CA: score=0.47 buy_ready=False sector_rank=14 price=343.57 support=315.1 resistance=378.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=25.66 liquidity=744505.13 spike=0.58
- POUL.CA: score=7.83 buy_ready=False sector_rank=21 price=9.96 support=9.12 resistance=41.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=5.03 liquidity=20927474.0 spike=0.63
- PRCL.CA: score=5.41 buy_ready=False sector_rank=12 price=25.53 support=22.8 resistance=34.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=27.98 liquidity=5231894.5 spike=0.41
- PRDC.CA: score=18.1 buy_ready=False sector_rank=19 price=7.12 support=6.81 resistance=8.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=43.77 liquidity=67322896.0 spike=2.05
- PRMH.CA: score=2.46 buy_ready=False sector_rank=14 price=2.26 support=2.03 resistance=2.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=32.97 liquidity=2733999.75 spike=0.65
- RACC.CA: score=18.75 buy_ready=False sector_rank=14 price=9.4 support=8.51 resistance=10.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=43.39 liquidity=22006796.0 spike=3.01
- RAKT.CA: score=20.06 buy_ready=False sector_rank=14 price=23.89 support=20.26 resistance=22.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=52.16 liquidity=1328407.13 spike=5.41
- RAYA.CA: score=14.79 buy_ready=False sector_rank=13 price=6.49 support=5.72 resistance=7.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=40.0 liquidity=20624944.0 spike=0.55
- RMDA.CA: score=9.34 buy_ready=False sector_rank=17 price=5.4 support=4.83 resistance=6.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=29.14 liquidity=35804596.0 spike=0.88
- ROTO.CA: score=11.1 buy_ready=False sector_rank=14 price=39.52 support=35.02 resistance=44.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=46.31 liquidity=4369769.5 spike=0.57
- RREI.CA: score=15.41 buy_ready=False sector_rank=14 price=3.92 support=3.53 resistance=4.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=40.0 liquidity=14672731.0 spike=1.34
- RTVC.CA: score=9.4 buy_ready=False sector_rank=14 price=3.64 support=3.37 resistance=4.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=35.58 liquidity=4355663.5 spike=1.66
- RUBX.CA: score=9.33 buy_ready=False sector_rank=14 price=17.85 support=16.4 resistance=19.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=255272896.0 spike=3.3
- SAUD.CA: score=10.72 buy_ready=False sector_rank=10 price=23.08 support=21.6 resistance=26.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=51.34 liquidity=5183457.0 spike=0.27
- SCEM.CA: score=15.18 buy_ready=False sector_rank=12 price=85.85 support=74.55 resistance=104.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=39.22 liquidity=24325754.0 spike=0.37
- SCFM.CA: score=5.15 buy_ready=False sector_rank=14 price=249.42 support=223.11 resistance=290.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=37.73 liquidity=1419094.88 spike=0.51
- SCTS.CA: score=3.3 buy_ready=False sector_rank=3 price=558.03 support=520.3 resistance=635.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=33.98 liquidity=898283.06 spike=0.5
- SDTI.CA: score=19.73 buy_ready=False sector_rank=14 price=85.0 support=71.0 resistance=94.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=74.63 liquidity=12425302.0 spike=0.37
- SEIG.CA: score=23.73 buy_ready=False sector_rank=14 price=242.56 support=200.0 resistance=267.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=55.41 liquidity=11234654.0 spike=6.23
- SIPC.CA: score=22.23 buy_ready=False sector_rank=14 price=5.79 support=4.22 resistance=6.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=44.44 liquidity=105836560.0 spike=2.25
- SKPC.CA: score=8.63 buy_ready=False sector_rank=15 price=16.03 support=15.4 resistance=19.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=27.39 liquidity=70052448.0 spike=0.69
- SMFR.CA: score=7.01 buy_ready=False sector_rank=14 price=237.22 support=220.0 resistance=245.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=12306974.0 spike=2.14
- SNFC.CA: score=15.3 buy_ready=False sector_rank=14 price=11.52 support=10.58 resistance=11.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=77.69 liquidity=6574261.5 spike=0.54
- SPIN.CA: score=10.45 buy_ready=False sector_rank=9 price=16.54 support=15.11 resistance=19.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=42.26 liquidity=4840529.5 spike=0.71
- SPMD.CA: score=8.73 buy_ready=False sector_rank=14 price=0.39 support=0.36 resistance=0.62 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=10.29 liquidity=11291584.0 spike=0.15
- SUGR.CA: score=10.01 buy_ready=False sector_rank=21 price=55.65 support=50.5 resistance=64.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=30.18 liquidity=8174654.5 spike=0.4
- SVCE.CA: score=14.73 buy_ready=False sector_rank=14 price=10.41 support=9.24 resistance=13.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=38.61 liquidity=88064896.0 spike=0.8
- SWDY.CA: score=14.27 buy_ready=False sector_rank=18 price=118.04 support=102.31 resistance=139.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=42.39 liquidity=52587804.0 spike=0.73
- TALM.CA: score=22.4 buy_ready=False sector_rank=3 price=21.83 support=17.61 resistance=25.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=43.34 liquidity=34931540.0 spike=0.49
- TMGH.CA: score=8.0 buy_ready=False sector_rank=19 price=87.98 support=84.4 resistance=99.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=23.37 liquidity=148670528.0 spike=0.63
- TRTO.CA: score=-4.03 buy_ready=False sector_rank=14 price=0.07 support=0.07 resistance=0.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=20634.12 spike=1.61
- UEFM.CA: score=11.94 buy_ready=False sector_rank=14 price=511.1 support=407.57 resistance=550.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=43.01 liquidity=3214338.25 spike=0.92
- UEGC.CA: score=15.73 buy_ready=False sector_rank=14 price=1.57 support=1.37 resistance=1.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=43.28 liquidity=25296758.0 spike=0.76
- UNIP.CA: score=13.71 buy_ready=False sector_rank=14 price=0.36 support=0.32 resistance=0.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=45.0 liquidity=8977513.0 spike=0.68
- UNIT.CA: score=-0.23 buy_ready=False sector_rank=19 price=17.53 support=16.41 resistance=23.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=30.17 liquidity=773385.75 spike=0.05
- WCDF.CA: score=4.08 buy_ready=False sector_rank=14 price=661.09 support=575.5 resistance=765.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:08 PM market time freshness=DELAYED_CURRENT RSI=30.23 liquidity=1355727.75 spike=0.34
- WKOL.CA: score=3.44 buy_ready=False sector_rank=14 price=296.29 support=266.18 resistance=379.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=24.64 liquidity=4709979.0 spike=0.39
- ZEOT.CA: score=10.11 buy_ready=False sector_rank=14 price=12.9 support=10.6 resistance=14.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=50.2 liquidity=1384880.13 spike=0.24
- ZMID.CA: score=9.0 buy_ready=False sector_rank=19 price=7.6 support=7.07 resistance=9.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=19.2 liquidity=95237464.0 spike=0.82

## Backtesting Lite
- EFIH.CA: 180d return=12.93%, max drawdown=-22.68%, MA20>MA50 days last20=11, as_of=2026-10-04T21:00:00+00:00
- HRHO.CA: 180d return=0.69%, max drawdown=-22.96%, MA20>MA50 days last20=0, as_of=2026-10-04T21:00:00+00:00
- GBCO.CA: 180d return=11.72%, max drawdown=-24.35%, MA20>MA50 days last20=4, as_of=2026-10-04T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- EFIH.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=E-Finance For Digital and Financial Investments summary=Evidence rejected for EFIH.CA: source text did not clearly match EFIH.CA / E-Finance For Digital and Financial Investments.
- HRHO.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=EFG Holding summary=Evidence rejected for HRHO.CA: source text did not clearly match HRHO.CA / EFG Holding.
- GBCO.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=GB Corp summary=Evidence rejected for GBCO.CA: source text did not clearly match GBCO.CA / GB Corp.
- EXPA.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Export Development Bank of Egypt summary=Evidence rejected for EXPA.CA: source text did not clearly match EXPA.CA / Export Development Bank of Egypt.
- AMOC.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Alexandria Mineral Oils summary=AMOC achieves EGP 10.5bn consolidated sales in Q1-26; AMOC studies potential project with Germany’s SULZER; AMOC to pay out EGP 0.4/shr dividends for H2-25
  - AMOC achieves EGP 10.5bn consolidated sales in Q1-26: https://english.mubasher.info/news/4604903/AMOC-achieves-EGP-10-5bn-consolidated-sales-in-Q1-26/
  - AMOC studies potential project with Germany’s SULZER: https://english.mubasher.info/news/4586853/AMOC-studies-potential-project-with-Germany-s-SULZER/
  - AMOC to pay out EGP 0.4/shr dividends for H2-25: https://english.mubasher.info/news/4586775/AMOC-to-pay-out-EGP-0-4-shr-dividends-for-H2-25/
- SEIG.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=643 sources=3 expected=Saudi Egyptian Investment & Finance Co. S.A.E summary=Saudi Egyptian Investment unveils EGP 2/shr dividends for 2025; Saudi Egyptian Investment and Finance sees 15% higher profit in 2020; Saudi Egyptian Investment records higher profit in 2019
  - Saudi Egyptian Investment unveils EGP 2/shr dividends for 2025: https://english.mubasher.info/news/4590273/Saudi-Egyptian-Investment-unveils-EGP-2-shr-dividends-for-2025/
  - Saudi Egyptian Investment and Finance sees 15% higher profit in 2020: https://english.mubasher.info/news/3766715/Saudi-Egyptian-Investment-and-Finance-sees-15-higher-profit-in-2020/
  - Saudi Egyptian Investment records higher profit in 2019: https://english.mubasher.info/news/3588475/Saudi-Egyptian-Investment-records-higher-profit-in-2019/
- ETEL.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Telecom Egypt summary=Evidence rejected for ETEL.CA: source text did not clearly match ETEL.CA / Telecom Egypt.
- ALCN.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Alexandria Containers and Cargo Handling summary=Evidence rejected for ALCN.CA: source text did not clearly match ALCN.CA / Alexandria Containers and Cargo Handling.

## Warnings
- Evidence rejected for EFIH.CA: source text did not clearly match EFIH.CA / E-Finance For Digital and Financial Investments.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence rejected for HRHO.CA: source text did not clearly match HRHO.CA / EFG Holding.
- Evidence rejected for GBCO.CA: source text did not clearly match GBCO.CA / GB Corp.
- Evidence rejected for EXPA.CA: source text did not clearly match EXPA.CA / Export Development Bank of Egypt.
- Evidence for AMOC.CA matches the company but no source/report date was detected.
- Evidence for SEIG.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for ETEL.CA: source text did not clearly match ETEL.CA / Telecom Egypt.
- Evidence rejected for ALCN.CA: source text did not clearly match ALCN.CA / Alexandria Containers and Cargo Handling.
