# Telegram-First EGX Scanner Report

Scan phase: Open liquidity confirmation
Generated UTC: 2026-09-15T11:42:24.225729+00:00
Generated Cairo: 2026-09-15 14:42
Run timing: target 09:15 Cairo | generated Cairo 2026-09-15 14:42 | cron 15 6 * * 0-4
Trigger: scheduled cron=15 6 * * 0-4 mapped to open_confirm; Cairo now 2026-09-15 14:38

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 1
- Tradeable price/liquidity tickers: 173/189
- Top sector: Investment Holding

## Market Context
- Market trend: Bullish
- Source: Mubasher EGX market page (delayed public data)
- As of: Tuesday, September 15
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 31.58% / above MA50 57.89%
- EGX70 regime: BEARISH / above MA20 27.78% / above MA50 55.56%
- Sector breadth: 9.52%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- CCAP.CA: liquidity=743481792.0 spike=0.87 score=23.4
- COMI.CA: liquidity=650413696.0 spike=1.25 score=14.94
- SPMD.CA: liquidity=598085696.0 spike=33.0 score=9.47
- ETEL.CA: liquidity=325435648.0 spike=1.68 score=8.54
- TALM.CA: liquidity=313828704.0 spike=7.45 score=30.4

## AI Narrative
- Provider: OpenRouter OK
- Model: nvidia/nemotron-3-super-120b-a12b:free
- Summary: EGX30 and EGX70 are bearish with weak sector breadth (≈9.5%), putting the market in DEFENSIVE_NO_NEW_BUY mode; the scanner still highlights tickets with strong relative momentum, liquidity spikes and bullish‑watch outlooks, but they remain HOLD until the regime improves.
- TALM.CA: liquidity accumulation spike (7.45×), RSI 68, price just above 20‑day resistance, bullish watch but extended momentum and support ~34% away.
- CIRA.CA: tradeable liquidity (1.23× spike), RSI 64, bullish watch in leading Education sector, yet price sits far above support with limited near‑term upside.
- CCAP.CA: very high liquidity, RSI 83 (overheated), bullish watch in top‑ranked Investment Holding sector, resistance close; momentum may stall without regime shift.
- Overall: most flagged tickets show liquidity spikes and bullish‑watch scores, but bearish EGX30/EGX70 breadth and defensive risk mode keep confidence low and outlook uncertain for the next 1‑3 days.

## Top Liquidity Spikes
- SPMD.CA: spike=33.0 liquidity=598085696.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- TALM.CA: spike=7.45 liquidity=313828704.0 outlook=BULLISH_WATCH score=94.91 buy_ready=False
- UNIT.CA: spike=3.81 liquidity=42386100.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- IDRE.CA: spike=3.54 liquidity=33018958.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- EOSB.CA: spike=2.76 liquidity=187291.59 outlook=NEUTRAL score=38.17 buy_ready=False

## Sector Leaderboard
- #1 Investment Holding: score=12.77 5d=5.42% 20d=16.94% aboveMA50=100.0%
- #2 Education: score=7.91 5d=3.72% 20d=2.9% aboveMA50=66.67%
- #3 Telecommunications: score=5.46 5d=-0.22% 20d=1.85% aboveMA50=50.0%
- #4 Textiles: score=4.46 5d=-5.29% 20d=5.67% aboveMA50=100.0%
- #5 Basic Resources & Chemicals: score=3.25 5d=-3.13% 20d=1.58% aboveMA50=60.0%
- #6 Energy & Petrochemicals: score=2.03 5d=-2.0% 20d=-0.29% aboveMA50=50.0%
- #7 Tourism & Leisure: score=1.61 5d=-2.88% 20d=-4.33% aboveMA50=100.0%
- #8 Industrial Goods & Construction: score=1.5 5d=0.0% 20d=0.0% aboveMA50=0.0%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- TALM.CA: BULLISH_WATCH score=94.91 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=momentum is extended; far above support
- CIRA.CA: BULLISH_WATCH score=82.91 liquidity=TRADEABLE sector=LEADING risk=momentum is extended; far above support
- BINV.CA: BULLISH_WATCH score=82 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; momentum is extended
- ORWE.CA: BULLISH_WATCH score=80.46 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- SKPC.CA: BULLISH_WATCH score=79.25 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- KABO.CA: BULLISH_WATCH score=77.46 liquidity=TRADEABLE sector=IMPROVING risk=momentum is extended
- ACGC.CA: BULLISH_WATCH score=73.46 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=below MA20
- EGAL.CA: BULLISH_WATCH score=73.25 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- MEPA.CA: BULLISH_WATCH score=72.17 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; sector is not leading
- WKOL.CA: BULLISH_WATCH score=72.17 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; sector is not leading

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=12.47 buy_ready=False sector_rank=9 price=312.98 support=295.0 resistance=375.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=32.56 liquidity=14927505.0 spike=0.45
- ABUK.CA: score=20.3 buy_ready=False sector_rank=5 price=88.34 support=75.01 resistance=94.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=65.89 liquidity=40414164.0 spike=0.24
- ACAMD.CA: score=16.47 buy_ready=False sector_rank=9 price=2.07 support=1.95 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=54.39 liquidity=40891252.0 spike=0.72
- ACGC.CA: score=21.64 buy_ready=False sector_rank=4 price=14.19 support=11.85 resistance=16.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=54.19 liquidity=100393808.0 spike=2.43
- ADCI.CA: score=5.68 buy_ready=False sector_rank=9 price=276.52 support=267.66 resistance=319.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=28.35 liquidity=3213124.5 spike=0.43
- ADIB.CA: score=12.44 buy_ready=False sector_rank=10 price=52.09 support=50.51 resistance=55.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=33.33 liquidity=46178440.0 spike=0.67
- ADPC.CA: score=13.66 buy_ready=False sector_rank=9 price=3.82 support=3.82 resistance=4.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=38.71 liquidity=9189403.0 spike=0.35
- AFDI.CA: score=6.1 buy_ready=False sector_rank=9 price=53.06 support=51.6 resistance=68.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=19.16 liquidity=6631383.0 spike=0.25
- AFMC.CA: score=9.47 buy_ready=False sector_rank=9 price=159.17 support=157.0 resistance=267.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=19.7 liquidity=17945252.0 spike=0.29
- AJWA.CA: score=13.52 buy_ready=False sector_rank=9 price=180.0 support=175.15 resistance=202.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=44.32 liquidity=9051040.0 spike=0.17
- ALCN.CA: score=16.91 buy_ready=False sector_rank=16 price=30.93 support=30.03 resistance=34.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=48.33 liquidity=10799304.0 spike=0.36
- ALUM.CA: score=7.09 buy_ready=False sector_rank=9 price=25.87 support=25.34 resistance=30.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=23.58 liquidity=4622149.0 spike=0.28
- AMER.CA: score=7.35 buy_ready=False sector_rank=11 price=5.49 support=4.91 resistance=5.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=157579056.0 spike=2.5
- AMES.CA: score=8.47 buy_ready=False sector_rank=9 price=51.6 support=53.4 resistance=173.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=0.56 liquidity=175859888.0 spike=0.73
- AMIA.CA: score=10.5 buy_ready=False sector_rank=9 price=17.51 support=12.71 resistance=22.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=29.09 liquidity=8027989.0 spike=0.11
- AMOC.CA: score=19.81 buy_ready=False sector_rank=6 price=13.15 support=10.65 resistance=14.63 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=70.36 liquidity=54300616.0 spike=0.27
- APSW.CA: score=4.21 buy_ready=False sector_rank=9 price=8.39 support=8.41 resistance=9.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:10 PM market time freshness=DELAYED_CURRENT RSI=39.78 liquidity=739917.63 spike=0.61
- ARAB.CA: score=14.35 buy_ready=False sector_rank=11 price=0.25 support=0.23 resistance=0.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=47.17 liquidity=52151548.0 spike=0.53
- ARCC.CA: score=17.32 buy_ready=False sector_rank=12 price=72.38 support=71.51 resistance=81.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=41.74 liquidity=23247680.0 spike=0.42
- AREH.CA: score=8.67 buy_ready=False sector_rank=9 price=1.43 support=1.39 resistance=1.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=40.62 liquidity=4197163.5 spike=0.24
- ARVA.CA: score=4.47 buy_ready=False sector_rank=9 price=14.99 support=14.45 resistance=14.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=16 August 01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=30473338.0 spike=0.56
- ASCM.CA: score=14.47 buy_ready=False sector_rank=9 price=60.39 support=60.92 resistance=66.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=36.67 liquidity=12684428.0 spike=0.55
- ASPI.CA: score=12.47 buy_ready=False sector_rank=9 price=0.44 support=0.41 resistance=0.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=28.49 liquidity=46730192.0 spike=0.87
- ATLC.CA: score=3.41 buy_ready=False sector_rank=20 price=7.19 support=6.61 resistance=7.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=17056192.0 spike=0.6
- ATQA.CA: score=20.3 buy_ready=False sector_rank=5 price=12.47 support=10.8 resistance=13.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=70.72 liquidity=63115588.0 spike=0.58
- AXPH.CA: score=11.87 buy_ready=False sector_rank=9 price=1683.95 support=1340.0 resistance=1768.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=79.71 liquidity=7400499.5 spike=0.62
- BINV.CA: score=18.78 buy_ready=False sector_rank=1 price=51.98 support=46.25 resistance=55.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=64.94 liquidity=2377902.75 spike=0.21
- BIOC.CA: score=9.47 buy_ready=False sector_rank=9 price=273.78 support=281.06 resistance=555.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=9.58 liquidity=23229120.0 spike=0.17
- BTFH.CA: score=7.41 buy_ready=False sector_rank=20 price=2.91 support=2.88 resistance=3.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=34.48 liquidity=50924872.0 spike=0.5
- CAED.CA: score=12.47 buy_ready=False sector_rank=9 price=130.12 support=123.56 resistance=185.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=32.85 liquidity=35641692.0 spike=0.86
- CANA.CA: score=10.1 buy_ready=False sector_rank=10 price=41.71 support=41.0 resistance=44.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=51.64 liquidity=2655913.75 spike=0.15
- CCAP.CA: score=23.4 buy_ready=False sector_rank=1 price=6.75 support=5.32 resistance=6.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=82.76 liquidity=743481792.0 spike=0.87
- CCRS.CA: score=4.47 buy_ready=False sector_rank=9 price=2.59 support=2.45 resistance=2.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=26124392.0 spike=0.51
- CEFM.CA: score=9.16 buy_ready=False sector_rank=9 price=145.19 support=135.0 resistance=168.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=39.85 liquidity=1695867.13 spike=0.12
- CERA.CA: score=20.45 buy_ready=False sector_rank=9 price=1.4 support=1.22 resistance=1.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=54.05 liquidity=127681896.0 spike=1.49
- CFGH.CA: score=7.48 buy_ready=False sector_rank=9 price=0.12 support=0.11 resistance=0.12 source=Yahoo Finance as_of=2026-09-13T21:00:00+00:00 freshness=FRESH RSI=58.82 liquidity=8794.1 spike=0.35
- CICH.CA: score=10.61 buy_ready=False sector_rank=20 price=12.47 support=12.0 resistance=13.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=51.96 liquidity=2201144.25 spike=0.45
- CIEB.CA: score=16.88 buy_ready=False sector_rank=10 price=24.68 support=24.01 resistance=26.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=45.35 liquidity=9442301.0 spike=0.65
- CIRA.CA: score=27.86 buy_ready=False sector_rank=2 price=39.81 support=32.1 resistance=41.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=63.68 liquidity=48589036.0 spike=1.23
- CLHO.CA: score=8.85 buy_ready=False sector_rank=18 price=16.15 support=15.81 resistance=18.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=27.13 liquidity=31616108.0 spike=0.39
- CNFN.CA: score=0.99 buy_ready=False sector_rank=20 price=4.57 support=4.53 resistance=4.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=27.54 liquidity=3579207.75 spike=0.27
- COMI.CA: score=14.94 buy_ready=False sector_rank=10 price=133.0 support=132.9 resistance=142.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=35.91 liquidity=650413696.0 spike=1.25
- COPR.CA: score=12.47 buy_ready=False sector_rank=9 price=0.48 support=0.44 resistance=0.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=30.07 liquidity=38343468.0 spike=0.41
- COSG.CA: score=17.47 buy_ready=False sector_rank=9 price=1.81 support=1.74 resistance=2.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=46.51 liquidity=12123213.0 spike=0.21
- CPCI.CA: score=3.69 buy_ready=False sector_rank=9 price=532.43 support=525.01 resistance=569.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:08 PM market time freshness=DELAYED_CURRENT RSI=28.12 liquidity=1220116.75 spike=0.26
- CSAG.CA: score=16.91 buy_ready=False sector_rank=16 price=37.77 support=38.13 resistance=44.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=37.58 liquidity=11934945.0 spike=0.67
- DAPH.CA: score=17.47 buy_ready=False sector_rank=9 price=121.52 support=108.11 resistance=157.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=53.01 liquidity=22141574.0 spike=0.36
- DEIN.CA: score=7.47 buy_ready=False sector_rank=9 price=10.35 support=10.35 resistance=12.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10 September 11:17 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=49.68 spike=0.01
- DOMT.CA: score=14.93 buy_ready=False sector_rank=15 price=26.53 support=27.02 resistance=29.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=40.05 liquidity=10091527.0 spike=1.41
- DSCW.CA: score=13.47 buy_ready=False sector_rank=9 price=1.8 support=1.8 resistance=2.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=35.29 liquidity=14126296.0 spike=0.32
- DTPP.CA: score=19.75 buy_ready=False sector_rank=9 price=328.01 support=290.1 resistance=380.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=65.01 liquidity=58524064.0 spike=1.14
- EALR.CA: score=6.7 buy_ready=False sector_rank=9 price=380.36 support=340.0 resistance=471.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=19.39 liquidity=7233017.0 spike=0.26
- EASB.CA: score=4.97 buy_ready=False sector_rank=9 price=8.27 support=8.2 resistance=8.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=20432350.0 spike=1.25
- EAST.CA: score=8.11 buy_ready=False sector_rank=15 price=33.38 support=33.04 resistance=37.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=26.72 liquidity=53379376.0 spike=0.8
- EBSC.CA: score=11.93 buy_ready=False sector_rank=9 price=2.09 support=1.88 resistance=2.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=57.26 liquidity=2462147.0 spike=0.17
- ECAP.CA: score=1.49 buy_ready=False sector_rank=9 price=32.3 support=31.16 resistance=40.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=30.27 liquidity=2026656.25 spike=0.16
- EDFM.CA: score=10.01 buy_ready=False sector_rank=9 price=413.37 support=394.0 resistance=432.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:37 PM market time freshness=DELAYED_CURRENT RSI=54.82 liquidity=543144.38 spike=0.32
- EEII.CA: score=4.31 buy_ready=False sector_rank=9 price=2.2 support=2.15 resistance=3.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=29.67 liquidity=5837612.5 spike=0.23
- EFIC.CA: score=14.3 buy_ready=False sector_rank=5 price=195.0 support=192.75 resistance=260.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=44.04 liquidity=76580768.0 spike=0.77
- EFID.CA: score=18.31 buy_ready=False sector_rank=15 price=30.33 support=29.71 resistance=34.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=36.72 liquidity=91526464.0 spike=1.6
- EFIH.CA: score=17.26 buy_ready=False sector_rank=14 price=23.52 support=22.16 resistance=25.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=37.24 liquidity=36495696.0 spike=0.5
- EGAL.CA: score=20.3 buy_ready=False sector_rank=5 price=362.57 support=321.01 resistance=395.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=59.48 liquidity=48702632.0 spike=0.41
- EGAS.CA: score=10.4 buy_ready=False sector_rank=6 price=56.0 support=55.21 resistance=61.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=38.73 liquidity=5592669.5 spike=0.58
- EGBE.CA: score=2.52 buy_ready=False sector_rank=10 price=0.51 support=0.49 resistance=0.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=12.7 liquidity=82155.15 spike=0.58
- EGCH.CA: score=18.3 buy_ready=False sector_rank=5 price=13.83 support=13.3 resistance=14.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=47.29 liquidity=79543568.0 spike=0.65
- EGSA.CA: score=9.63 buy_ready=False sector_rank=3 price=9.0 support=8.67 resistance=9.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:38 PM market time freshness=DELAYED_CURRENT RSI=77.36 liquidity=9952.94 spike=1.22
- EGTS.CA: score=13.23 buy_ready=False sector_rank=11 price=16.83 support=16.17 resistance=19.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=43.73 liquidity=6874101.5 spike=0.26
- EHDR.CA: score=14.47 buy_ready=False sector_rank=9 price=2.8 support=2.81 resistance=3.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=41.51 liquidity=12625404.0 spike=0.56
- EKHO.CA: score=5.81 buy_ready=False sector_rank=6 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-09-13T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=13.3 buy_ready=False sector_rank=13 price=1.98 support=1.98 resistance=2.21 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=37.14 liquidity=59434892.0 spike=0.86
- ELKA.CA: score=14.47 buy_ready=False sector_rank=9 price=1.73 support=1.7 resistance=1.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=48.21 liquidity=15943821.0 spike=0.35
- ELNA.CA: score=-1.38 buy_ready=False sector_rank=9 price=35.74 support=35.17 resistance=38.99 source=Yahoo Finance as_of=2026-09-13T21:00:00+00:00 freshness=FRESH RSI=22.51 liquidity=147999.35 spike=0.32
- ELSH.CA: score=14.47 buy_ready=False sector_rank=9 price=12.83 support=12.76 resistance=14.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=43.55 liquidity=12069699.0 spike=0.3
- ELWA.CA: score=0.4 buy_ready=False sector_rank=9 price=1.71 support=1.62 resistance=1.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=34.92 liquidity=927827.94 spike=0.38
- EMFD.CA: score=16.35 buy_ready=False sector_rank=11 price=14.03 support=11.51 resistance=15.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=76.8 liquidity=29909252.0 spike=0.18
- ENGC.CA: score=9.32 buy_ready=False sector_rank=9 price=41.71 support=41.0 resistance=54.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=29.38 liquidity=9848191.0 spike=0.6
- EOSB.CA: score=13.18 buy_ready=False sector_rank=9 price=1.57 support=1.5 resistance=1.64 source=Yahoo Finance as_of=2026-09-13T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=187291.59 spike=2.76
- EPCO.CA: score=19.12 buy_ready=False sector_rank=9 price=11.42 support=10.8 resistance=12.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=9649569.0 spike=0.45
- EPPK.CA: score=-5.11 buy_ready=False sector_rank=9 price=10.29 support=10.29 resistance=10.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=8 September 01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=419183.72 spike=0.28
- ETEL.CA: score=8.54 buy_ready=False sector_rank=3 price=133.4 support=126.02 resistance=135.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=325435648.0 spike=1.68
- ETRS.CA: score=17.17 buy_ready=False sector_rank=9 price=10.87 support=10.7 resistance=11.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=44.68 liquidity=9702303.0 spike=0.42
- EXPA.CA: score=17.44 buy_ready=False sector_rank=10 price=20.82 support=19.8 resistance=22.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=59.51 liquidity=35959168.0 spike=0.99
- FAIT.CA: score=10.9 buy_ready=False sector_rank=10 price=45.97 support=39.58 resistance=48.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=69.14 liquidity=1455390.88 spike=0.17
- FAITA.CA: score=4.45 buy_ready=False sector_rank=10 price=0.99 support=0.98 resistance=1.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:48 PM market time freshness=DELAYED_CURRENT RSI=41.03 liquidity=6077.37 spike=0.11
- FERC.CA: score=9.91 buy_ready=False sector_rank=5 price=77.79 support=76.7 resistance=86.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=50.3 liquidity=5608377.5 spike=0.29
- FWRY.CA: score=16.26 buy_ready=False sector_rank=14 price=18.92 support=18.66 resistance=19.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=45.68 liquidity=78580304.0 spike=0.58
- GBCO.CA: score=17.68 buy_ready=False sector_rank=19 price=30.16 support=27.51 resistance=31.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=44.6 liquidity=52277816.0 spike=1.04
- GDWA.CA: score=13.47 buy_ready=False sector_rank=9 price=0.77 support=0.77 resistance=0.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=46.71 liquidity=14759127.0 spike=0.35
- GGCC.CA: score=17.47 buy_ready=False sector_rank=9 price=0.87 support=0.83 resistance=1.06 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=42.15 liquidity=14875339.0 spike=0.33
- GIHD.CA: score=19.47 buy_ready=False sector_rank=9 price=74.57 support=58.01 resistance=79.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=67.75 liquidity=15402197.0 spike=0.52
- GMCI.CA: score=-1.16 buy_ready=False sector_rank=9 price=1.76 support=1.77 resistance=1.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=28.0 liquidity=372814.06 spike=0.73
- GRCA.CA: score=8.47 buy_ready=False sector_rank=9 price=40.13 support=41.41 resistance=86.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=22.51 liquidity=33091754.0 spike=0.42
- GSSC.CA: score=12.07 buy_ready=False sector_rank=9 price=284.85 support=278.0 resistance=325.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:10 PM market time freshness=DELAYED_CURRENT RSI=46.79 liquidity=4600611.5 spike=0.36
- GTWL.CA: score=17.47 buy_ready=False sector_rank=9 price=237.96 support=161.03 resistance=248.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=66.07 liquidity=95053400.0 spike=0.31
- HDBK.CA: score=18.44 buy_ready=False sector_rank=10 price=109.02 support=88.85 resistance=124.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=69.38 liquidity=30039854.0 spike=0.52
- HELI.CA: score=21.35 buy_ready=False sector_rank=11 price=8.01 support=7.34 resistance=8.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=63.58 liquidity=108897416.0 spike=0.68
- HRHO.CA: score=12.41 buy_ready=False sector_rank=20 price=25.32 support=25.21 resistance=26.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=38.14 liquidity=48544296.0 spike=0.49
- ICID.CA: score=11.06 buy_ready=False sector_rank=9 price=18.28 support=13.4 resistance=19.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:10 PM market time freshness=DELAYED_CURRENT RSI=60.95 liquidity=1594666.13 spike=0.06
- IDRE.CA: score=9.47 buy_ready=False sector_rank=9 price=55.04 support=51.0 resistance=57.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=33018958.0 spike=3.54
- IFAP.CA: score=13.9 buy_ready=False sector_rank=17 price=20.38 support=20.2 resistance=22.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=47.55 liquidity=10920539.0 spike=0.45
- INFI.CA: score=12.47 buy_ready=False sector_rank=9 price=136.0 support=131.01 resistance=174.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=8.85 liquidity=14264661.0 spike=0.36
- IRON.CA: score=9.3 buy_ready=False sector_rank=5 price=27.42 support=27.83 resistance=33.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=7.1 liquidity=12841282.0 spike=0.91
- ISMA.CA: score=9.47 buy_ready=False sector_rank=9 price=29.86 support=29.0 resistance=40.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=34.04 liquidity=10155974.0 spike=0.38
- ISMQ.CA: score=15.3 buy_ready=False sector_rank=5 price=8.71 support=8.85 resistance=9.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=37.5 liquidity=19468840.0 spike=0.64
- ISPH.CA: score=11.85 buy_ready=False sector_rank=18 price=12.58 support=12.21 resistance=13.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=24.48 liquidity=45526504.0 spike=0.66
- JUFO.CA: score=15.11 buy_ready=False sector_rank=15 price=27.0 support=26.45 resistance=27.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=45.94 liquidity=13528655.0 spike=0.55
- KABO.CA: score=22.78 buy_ready=False sector_rank=4 price=9.65 support=8.82 resistance=10.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=63.2 liquidity=47059124.0 spike=0.88
- KWIN.CA: score=14.43 buy_ready=False sector_rank=9 price=86.68 support=84.5 resistance=137.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=38.98 liquidity=9958938.0 spike=0.15
- KZPC.CA: score=19.47 buy_ready=False sector_rank=9 price=14.2 support=11.5 resistance=16.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=59.71 liquidity=20442916.0 spike=0.31
- LCSW.CA: score=14.32 buy_ready=False sector_rank=12 price=33.06 support=32.61 resistance=37.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=42.77 liquidity=13512162.0 spike=0.46
- LUTS.CA: score=17.47 buy_ready=False sector_rank=9 price=0.94 support=0.79 resistance=1.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=52.97 liquidity=115214832.0 spike=0.42
- MAAL.CA: score=8.08 buy_ready=False sector_rank=9 price=8.7 support=8.18 resistance=10.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=47.28 liquidity=3613425.0 spike=0.34
- MASR.CA: score=18.47 buy_ready=False sector_rank=9 price=7.88 support=7.49 resistance=8.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=56.07 liquidity=79359256.0 spike=0.87
- MBSC.CA: score=17.32 buy_ready=False sector_rank=12 price=378.66 support=355.04 resistance=470.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=52.74 liquidity=31755468.0 spike=0.45
- MCQE.CA: score=17.32 buy_ready=False sector_rank=12 price=215.78 support=212.01 resistance=255.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=38.59 liquidity=21571924.0 spike=0.49
- MCRO.CA: score=20.05 buy_ready=False sector_rank=9 price=1.73 support=1.44 resistance=1.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=77.5 liquidity=196641312.0 spike=1.79
- MENA.CA: score=0.1 buy_ready=False sector_rank=11 price=6.6 support=6.58 resistance=7.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:09 PM market time freshness=DELAYED_CURRENT RSI=29.55 liquidity=746262.13 spike=0.23
- MEPA.CA: score=21.47 buy_ready=False sector_rank=9 price=1.95 support=1.8 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=57.5 liquidity=12345858.0 spike=0.35
- MFPC.CA: score=17.3 buy_ready=False sector_rank=5 price=47.0 support=38.93 resistance=48.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=79.61 liquidity=71111248.0 spike=0.53
- MFSC.CA: score=7.64 buy_ready=False sector_rank=9 price=49.04 support=48.88 resistance=58.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=50.82 liquidity=3175215.25 spike=0.63
- MHOT.CA: score=11.46 buy_ready=False sector_rank=7 price=17.92 support=17.72 resistance=19.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=47.83 liquidity=4815865.0 spike=0.42
- MICH.CA: score=14.25 buy_ready=False sector_rank=9 price=49.03 support=47.11 resistance=53.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=44.67 liquidity=6777502.5 spike=0.26
- MILS.CA: score=8.59 buy_ready=False sector_rank=9 price=199.21 support=191.0 resistance=248.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=19.84 liquidity=6123818.0 spike=0.11
- MIPH.CA: score=9.05 buy_ready=False sector_rank=18 price=813.48 support=700.2 resistance=820.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=67.27 liquidity=2198003.75 spike=0.54
- MOED.CA: score=16.47 buy_ready=False sector_rank=9 price=0.8 support=0.69 resistance=0.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=53.58 liquidity=57044652.0 spike=0.47
- MOIL.CA: score=8.0 buy_ready=False sector_rank=6 price=0.67 support=0.65 resistance=0.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=45.21 liquidity=185709.75 spike=0.86
- MOIN.CA: score=6.21 buy_ready=False sector_rank=9 price=36.86 support=35.5 resistance=39.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=53570216.0 spike=1.87
- MOSC.CA: score=3.24 buy_ready=False sector_rank=9 price=307.13 support=300.0 resistance=380.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=22.1 liquidity=769834.56 spike=0.07
- MPCI.CA: score=17.47 buy_ready=False sector_rank=9 price=406.32 support=345.0 resistance=490.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=51.77 liquidity=105022520.0 spike=0.64
- MPCO.CA: score=4.26 buy_ready=False sector_rank=17 price=2.86 support=2.52 resistance=2.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=175728320.0 spike=1.18
- MPRC.CA: score=14.47 buy_ready=False sector_rank=9 price=38.69 support=38.31 resistance=46.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=35.11 liquidity=21454514.0 spike=0.53
- MTIE.CA: score=13.6 buy_ready=False sector_rank=19 price=8.4 support=8.1 resistance=9.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=35.17 liquidity=14901062.0 spike=0.33
- NAHO.CA: score=3.21 buy_ready=False sector_rank=9 price=0.13 support=0.13 resistance=0.16 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=31.82 liquidity=141704.73 spike=1.3
- NCCW.CA: score=6.95 buy_ready=False sector_rank=9 price=8.55 support=7.61 resistance=8.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=119792672.0 spike=2.24
- NEDA.CA: score=4.74 buy_ready=False sector_rank=9 price=2.73 support=2.7 resistance=2.97 source=Yahoo Finance as_of=2026-09-13T21:00:00+00:00 freshness=FRESH RSI=45.24 liquidity=272033.58 spike=0.29
- NHPS.CA: score=4.9 buy_ready=False sector_rank=9 price=76.08 support=75.82 resistance=98.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=14.58 liquidity=5431014.5 spike=0.22
- NINH.CA: score=14.47 buy_ready=False sector_rank=9 price=20.68 support=21.4 resistance=26.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=46.49 liquidity=15484329.0 spike=0.51
- NIPH.CA: score=11.85 buy_ready=False sector_rank=18 price=314.12 support=301.0 resistance=414.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=16.45 liquidity=97918392.0 spike=0.41
- OBRI.CA: score=13.47 buy_ready=False sector_rank=9 price=30.53 support=30.1 resistance=34.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=37.48 liquidity=11455823.0 spike=0.53
- OCDI.CA: score=9.35 buy_ready=False sector_rank=11 price=30.0 support=30.0 resistance=34.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=34.84 liquidity=70383536.0 spike=0.8
- OCPH.CA: score=4.93 buy_ready=False sector_rank=9 price=239.33 support=241.05 resistance=295.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=28.04 liquidity=4462874.0 spike=0.39
- ODIN.CA: score=7.06 buy_ready=False sector_rank=9 price=2.75 support=2.55 resistance=3.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=25.88 liquidity=7595196.0 spike=0.24
- OFH.CA: score=19.47 buy_ready=False sector_rank=9 price=1.05 support=0.86 resistance=1.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=63.59 liquidity=73309032.0 spike=0.67
- OIH.CA: score=22.4 buy_ready=False sector_rank=1 price=2.15 support=1.75 resistance=2.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=70.18 liquidity=103272016.0 spike=0.81
- OLFI.CA: score=11.48 buy_ready=False sector_rank=15 price=22.32 support=22.07 resistance=25.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=36.76 liquidity=7367542.0 spike=0.17
- ORAS.CA: score=4.6 buy_ready=False sector_rank=8 price=845.97 support=834.5 resistance=855.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=71857832.0 spike=1.0
- ORHD.CA: score=19.35 buy_ready=False sector_rank=11 price=42.27 support=40.28 resistance=43.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=50.7 liquidity=63609456.0 spike=0.47
- ORWE.CA: score=20.78 buy_ready=False sector_rank=4 price=26.79 support=24.5 resistance=29.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=50.4 liquidity=20589784.0 spike=0.38
- PHAR.CA: score=11.85 buy_ready=False sector_rank=18 price=118.03 support=118.16 resistance=147.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=18.06 liquidity=64883416.0 spike=0.32
- PHDC.CA: score=14.35 buy_ready=False sector_rank=11 price=13.73 support=13.65 resistance=16.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=35.18 liquidity=92121832.0 spike=0.44
- PHTV.CA: score=-0.76 buy_ready=False sector_rank=9 price=368.82 support=345.0 resistance=369.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=3449860.25 spike=1.66
- POUL.CA: score=16.11 buy_ready=False sector_rank=15 price=37.97 support=36.97 resistance=41.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=57.38 liquidity=21872834.0 spike=0.93
- PRCL.CA: score=10.63 buy_ready=False sector_rank=12 price=32.63 support=30.9 resistance=36.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=41.06 liquidity=6308349.0 spike=0.29
- PRDC.CA: score=9.35 buy_ready=False sector_rank=11 price=7.88 support=7.77 resistance=10.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=25.16 liquidity=10792988.0 spike=0.16
- PRMH.CA: score=10.03 buy_ready=False sector_rank=9 price=2.6 support=2.28 resistance=2.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=65.48 liquidity=3557979.0 spike=0.3
- RACC.CA: score=8.92 buy_ready=False sector_rank=9 price=9.64 support=9.4 resistance=10.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=43.06 liquidity=4451378.5 spike=0.19
- RAKT.CA: score=11.08 buy_ready=False sector_rank=9 price=22.65 support=21.4 resistance=23.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=47.52 liquidity=315195.94 spike=1.15
- RAYA.CA: score=13.3 buy_ready=False sector_rank=21 price=7.05 support=6.95 resistance=7.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=52.45 liquidity=12609017.0 spike=0.2
- RMDA.CA: score=16.85 buy_ready=False sector_rank=18 price=6.15 support=5.77 resistance=6.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=51.3 liquidity=45541316.0 spike=0.76
- ROTO.CA: score=5.9 buy_ready=False sector_rank=9 price=40.29 support=35.02 resistance=52.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=12.86 liquidity=6427464.0 spike=0.49
- RREI.CA: score=17.47 buy_ready=False sector_rank=9 price=4.34 support=4.24 resistance=5.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=41.46 liquidity=11329327.0 spike=0.38
- RTVC.CA: score=3.36 buy_ready=False sector_rank=9 price=3.96 support=3.78 resistance=4.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=32.73 liquidity=895928.19 spike=0.12
- RUBX.CA: score=19.47 buy_ready=False sector_rank=9 price=13.0 support=12.36 resistance=13.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=36.32 liquidity=15390420.0 spike=0.77
- SAUD.CA: score=17.44 buy_ready=False sector_rank=10 price=23.05 support=22.83 resistance=24.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=39.95 liquidity=13973337.0 spike=0.89
- SCEM.CA: score=17.32 buy_ready=False sector_rank=12 price=94.85 support=94.0 resistance=112.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=48.59 liquidity=27019656.0 spike=0.17
- SCFM.CA: score=0.68 buy_ready=False sector_rank=9 price=271.96 support=270.0 resistance=305.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=33.35 liquidity=1216441.88 spike=0.12
- SCTS.CA: score=4.87 buy_ready=False sector_rank=2 price=605.87 support=566.66 resistance=660.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=19.76 liquidity=1472952.63 spike=0.29
- SDTI.CA: score=19.47 buy_ready=False sector_rank=9 price=73.99 support=67.0 resistance=76.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=58.42 liquidity=10584459.0 spike=0.52
- SEIG.CA: score=-4.03 buy_ready=False sector_rank=9 price=230.62 support=228.13 resistance=248.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=1497038.63 spike=0.91
- SIPC.CA: score=21.47 buy_ready=False sector_rank=9 price=5.95 support=4.1 resistance=6.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=64.01 liquidity=40925872.0 spike=0.67
- SKPC.CA: score=20.3 buy_ready=False sector_rank=5 price=17.99 support=16.8 resistance=19.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=54.32 liquidity=84223216.0 spike=0.6
- SMFR.CA: score=3.12 buy_ready=False sector_rank=9 price=239.07 support=240.0 resistance=276.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:09 PM market time freshness=DELAYED_CURRENT RSI=28.92 liquidity=3652488.0 spike=0.32
- SNFC.CA: score=18.89 buy_ready=False sector_rank=9 price=10.94 support=10.26 resistance=11.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=62.73 liquidity=8425542.0 spike=0.6
- SPIN.CA: score=18.78 buy_ready=False sector_rank=4 price=17.56 support=18.12 resistance=21.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=39.96 liquidity=11668763.0 spike=0.33
- SPMD.CA: score=9.47 buy_ready=False sector_rank=9 price=0.6 support=0.58 resistance=0.62 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=598085696.0 spike=33.0
- SUGR.CA: score=21.11 buy_ready=False sector_rank=15 price=61.54 support=50.0 resistance=64.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=49.23 liquidity=25552246.0 spike=0.36
- SVCE.CA: score=19.47 buy_ready=False sector_rank=9 price=11.73 support=10.28 resistance=13.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=60.29 liquidity=90135160.0 spike=0.54
- SWDY.CA: score=17.3 buy_ready=False sector_rank=13 price=125.8 support=115.0 resistance=139.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=49.59 liquidity=55907632.0 spike=0.59
- TALM.CA: score=30.4 buy_ready=False sector_rank=2 price=22.92 support=17.11 resistance=22.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=68.14 liquidity=313828704.0 spike=7.45
- TMGH.CA: score=16.35 buy_ready=False sector_rank=11 price=95.61 support=94.9 resistance=100.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=45.3 liquidity=146869456.0 spike=0.53
- TRTO.CA: score=9.48 buy_ready=False sector_rank=9 price=0.07 support=0.04 resistance=0.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=67.92 liquidity=10109.81 spike=0.31
- UEFM.CA: score=11.48 buy_ready=False sector_rank=9 price=534.5 support=440.66 resistance=570.0 source=Yahoo Finance as_of=2026-09-13T21:00:00+00:00 freshness=FRESH RSI=45.76 liquidity=5750685.5 spike=1.63
- UEGC.CA: score=9.47 buy_ready=False sector_rank=9 price=1.71 support=1.66 resistance=2.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=20.59 liquidity=12699329.0 spike=0.28
- UNIP.CA: score=14.47 buy_ready=False sector_rank=9 price=0.38 support=0.35 resistance=0.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=49.44 liquidity=14548965.0 spike=0.4
- UNIT.CA: score=9.35 buy_ready=False sector_rank=11 price=19.72 support=19.65 resistance=23.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=42386100.0 spike=3.81
- WCDF.CA: score=20.3 buy_ready=False sector_rank=9 price=731.54 support=630.0 resistance=729.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=86.64 liquidity=8328184.0 spike=2.75
- WKOL.CA: score=19.47 buy_ready=False sector_rank=9 price=348.75 support=326.5 resistance=390.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=48.27 liquidity=10983891.0 spike=0.55
- ZEOT.CA: score=13.08 buy_ready=False sector_rank=9 price=13.08 support=13.1 resistance=14.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=40.36 liquidity=5612362.5 spike=0.44
- ZMID.CA: score=19.35 buy_ready=False sector_rank=11 price=9.04 support=7.39 resistance=9.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=71.16 liquidity=121232952.0 spike=0.49

## Backtesting Lite
- TALM.CA: 180d return=45.38%, max drawdown=-12.27%, MA20>MA50 days last20=20, as_of=2026-09-13T21:00:00+00:00
- CIRA.CA: 180d return=124.03%, max drawdown=-16.44%, MA20>MA50 days last20=20, as_of=2026-09-13T21:00:00+00:00
- CCAP.CA: 180d return=83.16%, max drawdown=-18.62%, MA20>MA50 days last20=20, as_of=2026-09-13T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- TALM.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Talim Management Services summary=Evidence rejected for TALM.CA: source text did not clearly match TALM.CA / Talim Management Services.
- CIRA.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Cairo Investment and Real Estate Development summary=CIRA Education take over 51% of L’École Française Hurghada; CIRA’s majority shareholder acquires 37.5% additional equity, backs regional expansion; CIRA Education launches Middle East’s 1st initiative for care economy
  - CIRA Education take over 51% of L’École Française Hurghada: https://english.mubasher.info/news/4488666/CIRA-Education-take-over-51-of-L-%C3%89cole-Fran%C3%A7aise-Hurghada/
  - CIRA’s majority shareholder acquires 37.5% additional equity, backs regional expansion: https://english.mubasher.info/news/4393636/CIRA-s-majority-shareholder-acquires-37-5-additional-equity-backs-regional-expansion/
  - CIRA Education launches Middle East’s 1st initiative for care economy: https://english.mubasher.info/news/4391766/CIRA-Education-launches-Middle-East-s-1st-initiative-for-care-economy/
- CCAP.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Qalaa Holdings summary=Evidence rejected for CCAP.CA: source text did not clearly match CCAP.CA / Qalaa Holdings.
- KABO.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=El Nasr Clothing and Textiles summary=KABO posts EGP 17m in Q1-25/26 unaudited consolidated net profits; KABO sells over 1.9m shares in Spinalex for EGP 20m; KABO unveils international agreements, expansion plan including export lines
  - KABO posts EGP 17m in Q1-25/26 unaudited consolidated net profits: https://english.mubasher.info/news/4600162/KABO-posts-EGP-17m-in-Q1-25-26-unaudited-consolidated-net-profits/
  - KABO sells over 1.9m shares in Spinalex for EGP 20m: https://english.mubasher.info/news/4543747/KABO-sells-over-1-9m-shares-in-Spinalex-for-EGP-20m/
  - KABO unveils international agreements, expansion plan including export lines: https://english.mubasher.info/news/4533185/KABO-unveils-international-agreements-expansion-plan-including-export-lines/
- OIH.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Orascom Investment Holding summary=Evidence rejected for OIH.CA: source text did not clearly match OIH.CA / Orascom Investment Holding.
- ACGC.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Arab Cotton Ginning summary=Arab Cotton Ginning’s stock nears significant resistance level; Arab Cotton Ginning’s standalone profit grows 142% YoY in 9M-23/24; Arab Cotton Ginning’s consolidated profit leaps 371% YoY in H1-23/24
  - Arab Cotton Ginning’s stock nears significant resistance level: https://english.mubasher.info/news/4549011/Arab-Cotton-Ginning-s-stock-nears-significant-resistance-level/
  - Arab Cotton Ginning’s standalone profit grows 142% YoY in 9M-23/24: https://english.mubasher.info/news/4302757/Arab-Cotton-Ginning-s-standalone-profit-grows-142-YoY-in-9M-23-24/
  - Arab Cotton Ginning’s consolidated profit leaps 371% YoY in H1-23/24: https://english.mubasher.info/news/4279332/Arab-Cotton-Ginning-s-consolidated-profit-leaps-371-YoY-in-H1-23-24/
- MEPA.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Medical Packaging Company summary=Medical Packaging stock close to break above EGP 1.7; Medical Packaging announces EGP 62m capital hike; Medical Packaging&#39;s profit jumps 54% in Q1-21
  - Medical Packaging stock close to break above EGP 1.7: https://english.mubasher.info/news/4598700/Medical-Packaging-stock-close-to-break-above-EGP-1-7/
  - Medical Packaging announces EGP 62m capital hike: https://english.mubasher.info/news/3936298/Medical-Packaging-announces-EGP-62m-capital-hike/
  - Medical Packaging&#39;s profit jumps 54% in Q1-21: https://english.mubasher.info/news/3815448/Medical-Packaging-s-profit-jumps-54-in-Q1-21/
- SIPC.CA: status=OLD_ACCEPTED latest=2020-01-01 age_days=2449 sources=3 expected=Sabaa International Company for Pharmaceutical and Chemical Industry summary=Sabaa Pharmaceutical&#39;s shareholders approve capital raise via bonus issue; FRA approves Sabaa Pharmaceutical&#39;s capital raise; Sabaa Pharmaceutical&#39;s profit leaps 76% in 2020 initial results
  - Sabaa Pharmaceutical&#39;s shareholders approve capital raise via bonus issue: https://english.mubasher.info/news/3809286/Sabaa-Pharmaceutical-s-shareholders-approve-capital-raise-via-bonus-issue/
  - FRA approves Sabaa Pharmaceutical&#39;s capital raise: https://english.mubasher.info/news/3789753/FRA-approves-Sabaa-Pharmaceutical-s-capital-raise/
  - Sabaa Pharmaceutical&#39;s profit leaps 76% in 2020 initial results: https://english.mubasher.info/news/3779465/Sabaa-Pharmaceutical-s-profit-leaps-76-in-2020-initial-results/

## Warnings
- Evidence rejected for TALM.CA: source text did not clearly match TALM.CA / Talim Management Services.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence for CIRA.CA matches the company but no source/report date was detected.
- Evidence rejected for CCAP.CA: source text did not clearly match CCAP.CA / Qalaa Holdings.
- Evidence for KABO.CA matches the company but no source/report date was detected.
- Evidence rejected for OIH.CA: source text did not clearly match OIH.CA / Orascom Investment Holding.
- Evidence for ACGC.CA matches the company but no source/report date was detected.
- Evidence for MEPA.CA matches the company but no source/report date was detected.
- Evidence for SIPC.CA matches the company but appears old; latest detected date is 2020-01-01.
