# Telegram-First EGX Scanner Report

Scan phase: Pre-market risk check
Generated UTC: 2026-07-30T08:04:19.058060+00:00
Generated Cairo: 2026-07-30 11:04
Run timing: target 08:45 Cairo | generated Cairo 2026-07-30 11:04 | cron 45 5 * * 0-4
Trigger: scheduled cron=45 5 * * 0-4 mapped to pre_market; Cairo now 2026-07-30 10:56

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 33
- Data quality issues: 1
- Tradeable price/liquidity tickers: 159/189
- Top sector: Textiles

## Market Context
- Market trend: Bearish
- Source: Mubasher EGX market page (delayed public data)
- As of: Thursday, July 30
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 45.0% / above MA50 35.0%
- EGX70 regime: MIXED / above MA20 47.22% / above MA50 69.44%
- Sector breadth: 42.86%
- Risk mode: SELECTIVE_SWING_TRADES_ONLY

## Top Liquidity
- CCAP.CA: liquidity=176715360.0 spike=0.25 score=21.41
- AMOC.CA: liquidity=156676848.0 spike=2.63 score=11.12
- BIOC.CA: liquidity=130622816.0 spike=2.56 score=12.43
- AFMC.CA: liquidity=124133368.0 spike=2.59 score=12.49
- HELI.CA: liquidity=120836096.0 spike=0.63 score=23.4

## AI Narrative
- Provider: OpenRouter OK
- Model: nvidia/nemotron-3-super-120b-a12b:free
- Summary: Scanner found no strong HOLD candidates; top rows show mixed bullish‑watch/constructive outlook with cooling liquidity and modest support‑resistance gaps, set against a bearish EGX30 and mixed EGX70 regime that forces a selective swing‑trade risk mode.
- Prioritized tickets (COMI, GSSC, ATQA, MPCO, ADIB, OCDI) ranked highest on score and outlook, but liquidity spikes are low or cooling, limiting near‑term momentum.
- Most stocks sit 4‑17% below 20‑day support and only 2‑5% below resistance, indicating potential to test support before any bounce in the next 1‑3 days.

## Top Liquidity Spikes
- ELWA.CA: spike=3.74 liquidity=5051843.22 outlook=WEAK_OR_RISKY score=30.77 buy_ready=False
- AMOC.CA: spike=2.63 liquidity=156676848.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- AFMC.CA: spike=2.59 liquidity=124133368.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- BIOC.CA: spike=2.56 liquidity=130622816.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- PHAR.CA: spike=2.12 liquidity=105038160.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False

## Sector Leaderboard
- #1 Textiles: score=9.01 5d=3.67% 20d=13.7% aboveMA50=75.0%
- #2 Real Estate: score=7.09 5d=0.49% 20d=16.03% aboveMA50=69.23%
- #3 Education: score=6.45 5d=0.01% 20d=12.8% aboveMA50=66.67%
- #4 Agriculture & Food Production: score=6.26 5d=3.72% 20d=5.58% aboveMA50=50.0%
- #5 Banking & Financials: score=6.22 5d=1.31% 20d=7.08% aboveMA50=60.0%
- #6 Telecommunications: score=6.12 5d=1.55% 20d=8.63% aboveMA50=50.0%
- #7 General / Verified EGX Expansion: score=5.77 5d=0.0% 20d=9.94% aboveMA50=62.14%
- #8 Industrial Goods & Cables: score=5.72 5d=1.41% 20d=8.41% aboveMA50=50.0%

## Today's Prioritized Action Tickets
- HOLD: Local fallback HOLD: no candidate passed evidence, liquidity, freshness, and technical gates.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- ROTO.CA: BULLISH_WATCH score=89.77 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- MPCO.CA: BULLISH_WATCH score=84.26 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- COMI.CA: BULLISH_WATCH score=84.22 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- PRDC.CA: BULLISH_WATCH score=83.09 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; far above support
- EALR.CA: BULLISH_WATCH score=81.77 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- OCDI.CA: BULLISH_WATCH score=81.09 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- ACGC.CA: BULLISH_WATCH score=81.01 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; momentum is extended
- KABO.CA: BULLISH_WATCH score=77.01 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; momentum is extended; far above support
- SAUD.CA: BULLISH_WATCH score=76.22 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- CLHO.CA: BULLISH_WATCH score=76.19 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; sector is not leading

## BUY-Ready Candidates
- COMI.CA: rank=28.4 outlook=BULLISH_WATCH outlook_score=84.22 sector_rank=5 price=139.01 support=126.21 resistance=142.55 liquidity=57817560.0
- GSSC.CA: rank=27.09 outlook=CONSTRUCTIVE outlook_score=66.77 sector_rank=7 price=278.36 support=240.52 resistance=288.95 liquidity=13760382.0
- ATQA.CA: rank=26.9 outlook=CONSTRUCTIVE outlook_score=67.26 sector_rank=16 price=9.81 support=9.35 resistance=10.16 liquidity=12155030.0
- MPCO.CA: rank=26.4 outlook=BULLISH_WATCH outlook_score=84.26 sector_rank=4 price=1.9 support=1.7 resistance=1.95 liquidity=34354844.0
- ADIB.CA: rank=26.4 outlook=BULLISH_WATCH outlook_score=70.22 sector_rank=5 price=51.12 support=44.31 resistance=52.88 liquidity=37602748.0
- OCDI.CA: rank=26.4 outlook=BULLISH_WATCH outlook_score=81.09 sector_rank=2 price=28.0 support=23.91 resistance=28.7 liquidity=24152596.0
- PRDC.CA: rank=26.4 outlook=BULLISH_WATCH outlook_score=83.09 sector_rank=2 price=9.2 support=7.0 resistance=10.4 liquidity=11871684.0
- EFIH.CA: rank=25.97 outlook=BULLISH_WATCH outlook_score=75.92 sector_rank=11 price=22.34 support=20.1 resistance=24.0 liquidity=19054500.0
- EALR.CA: rank=25.58 outlook=BULLISH_WATCH outlook_score=81.77 sector_rank=7 price=374.0 support=335.0 resistance=425.0 liquidity=9275656.0
- BTFH.CA: rank=24.61 outlook=CONSTRUCTIVE outlook_score=64.02 sector_rank=12 price=3.08 support=2.91 resistance=3.2 liquidity=68594560.0

## Data Quality Issues
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=21.94 buy_ready=True sector_rank=7 price=243.8 support=197.0 resistance=255.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:42 AM market time freshness=DELAYED_CURRENT RSI=59.21 liquidity=5633956.0 spike=0.27
- ABUK.CA: score=21.9 buy_ready=False sector_rank=16 price=71.21 support=66.66 resistance=75.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:41 AM market time freshness=DELAYED_CURRENT RSI=55.49 liquidity=27174212.0 spike=0.18
- ACAMD.CA: score=24.31 buy_ready=False sector_rank=7 price=2.32 support=2.15 resistance=2.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:42 AM market time freshness=DELAYED_CURRENT RSI=51.43 liquidity=15327349.0 spike=0.21
- ACGC.CA: score=22.21 buy_ready=True sector_rank=1 price=10.25 support=8.92 resistance=11.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:41 AM market time freshness=DELAYED_CURRENT RSI=68.85 liquidity=4810281.0 spike=0.16
- ADCI.CA: score=12.43 buy_ready=False sector_rank=7 price=257.93 support=230.0 resistance=269.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:40 AM market time freshness=DELAYED_CURRENT RSI=76.53 liquidity=1124356.88 spike=0.1
- ADIB.CA: score=26.4 buy_ready=True sector_rank=5 price=51.12 support=44.31 resistance=52.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:41 AM market time freshness=DELAYED_CURRENT RSI=69.6 liquidity=37602748.0 spike=0.29
- ADPC.CA: score=4.52 buy_ready=False sector_rank=7 price=3.83 support=3.82 resistance=3.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:42 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=5210837.5 spike=0.16
- AFDI.CA: score=20.09 buy_ready=True sector_rank=7 price=51.64 support=41.84 resistance=52.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:42 AM market time freshness=DELAYED_CURRENT RSI=67.14 liquidity=5785605.5 spike=0.35
- AFMC.CA: score=12.49 buy_ready=False sector_rank=7 price=174.0 support=148.0 resistance=177.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:42 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=124133368.0 spike=2.59
- AJWA.CA: score=24.31 buy_ready=True sector_rank=7 price=191.0 support=161.0 resistance=210.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:41 AM market time freshness=DELAYED_CURRENT RSI=60.64 liquidity=17742390.0 spike=0.71
- ALCN.CA: score=15.06 buy_ready=False sector_rank=19 price=29.16 support=27.7 resistance=30.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:40 AM market time freshness=DELAYED_CURRENT RSI=53.97 liquidity=2428800.25 spike=0.11
- ALUM.CA: score=19.51 buy_ready=True sector_rank=7 price=23.7 support=20.55 resistance=24.09 source=Yahoo Finance as_of=2026-07-27T21:00:00+00:00 freshness=FRESH RSI=53.41 liquidity=3199642.3 spike=0.51
- AMER.CA: score=25.4 buy_ready=False sector_rank=2 price=4.64 support=2.28 resistance=4.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:42 AM market time freshness=DELAYED_CURRENT RSI=89.78 liquidity=16458364.0 spike=0.15
- AMES.CA: score=24.31 buy_ready=False sector_rank=7 price=121.88 support=45.15 resistance=144.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:42 AM market time freshness=DELAYED_CURRENT RSI=72.06 liquidity=10167858.0 spike=0.09
- AMIA.CA: score=21.09 buy_ready=False sector_rank=7 price=10.9 support=8.42 resistance=11.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:42 AM market time freshness=DELAYED_CURRENT RSI=71.3 liquidity=4778980.5 spike=0.34
- AMOC.CA: score=11.12 buy_ready=False sector_rank=17 price=8.78 support=8.55 resistance=8.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:41 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=156676848.0 spike=2.63
- APSW.CA: score=17.15 buy_ready=False sector_rank=7 price=8.98 support=8.0 resistance=9.34 source=Yahoo Finance as_of=2026-07-27T21:00:00+00:00 freshness=FRESH RSI=61.29 liquidity=839468.32 spike=0.5
- ARAB.CA: score=24.4 buy_ready=False sector_rank=2 price=0.24 support=0.2 resistance=0.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:41 AM market time freshness=DELAYED_CURRENT RSI=62.5 liquidity=20224862.0 spike=0.15
- ARCC.CA: score=23.02 buy_ready=False sector_rank=10 price=55.5 support=53.5 resistance=58.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:41 AM market time freshness=DELAYED_CURRENT RSI=59.77 liquidity=10709525.0 spike=0.41
- AREH.CA: score=12.54 buy_ready=False sector_rank=7 price=1.41 support=1.44 resistance=1.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:42 AM market time freshness=DELAYED_CURRENT RSI=38.18 liquidity=3230280.0 spike=0.11
- ARVA.CA: score=14.31 buy_ready=False sector_rank=7 price=12.35 support=10.5 resistance=12.6 source=Yahoo Finance as_of=2026-07-27T21:00:00+00:00 freshness=FRESH RSI=70.61 liquidity=0.0 spike=0.0
- ASCM.CA: score=22.31 buy_ready=False sector_rank=7 price=61.21 support=57.1 resistance=66.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:42 AM market time freshness=DELAYED_CURRENT RSI=71.17 liquidity=16277898.0 spike=0.3
- ASPI.CA: score=7.37 buy_ready=False sector_rank=7 price=0.42 support=0.42 resistance=0.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:42 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=8058207.5 spike=0.21
- ATLC.CA: score=11.96 buy_ready=False sector_rank=12 price=5.15 support=4.92 resistance=5.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:41 AM market time freshness=DELAYED_CURRENT RSI=46.03 liquidity=348537.66 spike=0.05
- ATQA.CA: score=26.9 buy_ready=True sector_rank=16 price=9.81 support=9.35 resistance=10.16 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:41 AM market time freshness=DELAYED_CURRENT RSI=64.46 liquidity=12155030.0 spike=0.36
- AXPH.CA: score=9.86 buy_ready=False sector_rank=7 price=1213.11 support=1075.0 resistance=1342.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:40 AM market time freshness=DELAYED_CURRENT RSI=79.08 liquidity=554605.19 spike=0.14
- BINV.CA: score=9.36 buy_ready=False sector_rank=14 price=46.41 support=44.98 resistance=51.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:41 AM market time freshness=DELAYED_CURRENT RSI=42.4 liquidity=955661.5 spike=0.13
- BIOC.CA: score=12.43 buy_ready=False sector_rank=7 price=239.75 support=212.22 resistance=239.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:42 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=130622816.0 spike=2.56
- BTFH.CA: score=24.61 buy_ready=True sector_rank=12 price=3.08 support=2.91 resistance=3.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:41 AM market time freshness=DELAYED_CURRENT RSI=52.5 liquidity=68594560.0 spike=0.31
- CAED.CA: score=19.7 buy_ready=False sector_rank=7 price=127.52 support=69.02 resistance=143.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:42 AM market time freshness=DELAYED_CURRENT RSI=77.42 liquidity=8389649.0 spike=0.13
- CANA.CA: score=18.13 buy_ready=True sector_rank=5 price=37.35 support=34.7 resistance=39.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:41 AM market time freshness=DELAYED_CURRENT RSI=67.38 liquidity=2731178.0 spike=0.16
- CCAP.CA: score=21.41 buy_ready=False sector_rank=14 price=5.25 support=4.65 resistance=5.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:42 AM market time freshness=DELAYED_CURRENT RSI=57.29 liquidity=176715360.0 spike=0.25
- CCRS.CA: score=21.33 buy_ready=True sector_rank=7 price=2.51 support=2.18 resistance=2.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:41 AM market time freshness=DELAYED_CURRENT RSI=64.47 liquidity=5022222.0 spike=0.28
- CEFM.CA: score=10.83 buy_ready=False sector_rank=7 price=140.98 support=132.06 resistance=144.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:42 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=32321638.0 spike=1.76
- CERA.CA: score=15.72 buy_ready=False sector_rank=7 price=1.28 support=1.19 resistance=1.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:41 AM market time freshness=DELAYED_CURRENT RSI=62.86 liquidity=3408768.25 spike=0.14
- CFGH.CA: score=-0.68 buy_ready=False sector_rank=7 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:42 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=9185.42 spike=0.58
- CICH.CA: score=12.92 buy_ready=False sector_rank=12 price=12.07 support=11.6 resistance=12.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:41 AM market time freshness=DELAYED_CURRENT RSI=51.3 liquidity=309404.63 spike=0.06
- CIEB.CA: score=12.06 buy_ready=False sector_rank=5 price=23.85 support=23.3 resistance=24.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:41 AM market time freshness=DELAYED_CURRENT RSI=38.46 liquidity=2655892.75 spike=0.3
- CIRA.CA: score=24.4 buy_ready=False sector_rank=3 price=34.41 support=27.45 resistance=36.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:41 AM market time freshness=DELAYED_CURRENT RSI=81.31 liquidity=29386316.0 spike=0.59
- CLHO.CA: score=18.81 buy_ready=True sector_rank=9 price=16.6 support=15.9 resistance=17.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:41 AM market time freshness=DELAYED_CURRENT RSI=56.17 liquidity=4737238.0 spike=0.11
- CNFN.CA: score=13.19 buy_ready=False sector_rank=12 price=4.79 support=4.61 resistance=5.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:41 AM market time freshness=DELAYED_CURRENT RSI=64.1 liquidity=1581304.63 spike=0.08
- COMI.CA: score=28.4 buy_ready=True sector_rank=5 price=139.01 support=126.21 resistance=142.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:41 AM market time freshness=DELAYED_CURRENT RSI=58.92 liquidity=57817560.0 spike=0.13
- COPR.CA: score=7.88 buy_ready=False sector_rank=7 price=0.39 support=0.39 resistance=0.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:42 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=8573952.0 spike=0.29
- COSG.CA: score=22.31 buy_ready=False sector_rank=7 price=1.62 support=1.47 resistance=1.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:42 AM market time freshness=DELAYED_CURRENT RSI=65.22 liquidity=10410401.0 spike=0.24
- CPCI.CA: score=15.02 buy_ready=False sector_rank=7 price=463.91 support=370.1 resistance=512.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:42 AM market time freshness=DELAYED_CURRENT RSI=73.91 liquidity=716240.31 spike=0.06
- CSAG.CA: score=11.47 buy_ready=False sector_rank=19 price=31.82 support=31.57 resistance=34.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:40 AM market time freshness=DELAYED_CURRENT RSI=50.22 liquidity=3834894.25 spike=0.25
- DAPH.CA: score=20.19 buy_ready=False sector_rank=7 price=95.02 support=78.8 resistance=98.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:42 AM market time freshness=DELAYED_CURRENT RSI=72.96 liquidity=5883255.0 spike=0.36
- DEIN.CA: score=-0.69 buy_ready=False sector_rank=7 price=11.38 support=13.65 resistance=13.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 June 12:11 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=40.95 spike=0.01
- DOMT.CA: score=11.01 buy_ready=False sector_rank=18 price=26.53 support=26.06 resistance=27.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:37 AM market time freshness=DELAYED_CURRENT RSI=44.07 liquidity=365622.16 spike=0.11
- DSCW.CA: score=21.31 buy_ready=False sector_rank=7 price=1.9 support=1.71 resistance=2.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:43 AM market time freshness=DELAYED_CURRENT RSI=82.76 liquidity=12814704.0 spike=0.24
- DTPP.CA: score=24.23 buy_ready=False sector_rank=7 price=238.68 support=120.0 resistance=273.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:41 AM market time freshness=DELAYED_CURRENT RSI=71.42 liquidity=9924275.0 spike=0.13
- EALR.CA: score=25.58 buy_ready=True sector_rank=7 price=374.0 support=335.0 resistance=425.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:42 AM market time freshness=DELAYED_CURRENT RSI=40.28 liquidity=9275656.0 spike=0.5
- EASB.CA: score=15.27 buy_ready=False sector_rank=7 price=7.45 support=6.88 resistance=8.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:42 AM market time freshness=DELAYED_CURRENT RSI=62.87 liquidity=960145.69 spike=0.07
- EAST.CA: score=4.74 buy_ready=False sector_rank=18 price=36.2 support=36.01 resistance=38.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:41 AM market time freshness=DELAYED_CURRENT RSI=31.93 liquidity=3087006.75 spike=0.05
- EBSC.CA: score=7.88 buy_ready=False sector_rank=7 price=1.87 support=1.71 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:41 AM market time freshness=DELAYED_CURRENT RSI=29.63 liquidity=575151.94 spike=0.07
- ECAP.CA: score=16.17 buy_ready=False sector_rank=7 price=32.33 support=31.52 resistance=34.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:42 AM market time freshness=DELAYED_CURRENT RSI=62.89 liquidity=1861214.88 spike=0.31
- EDFM.CA: score=15.77 buy_ready=False sector_rank=7 price=390.84 support=310.2 resistance=430.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:40 AM market time freshness=DELAYED_CURRENT RSI=73.24 liquidity=1464890.63 spike=0.34
- EEII.CA: score=2.83 buy_ready=False sector_rank=7 price=2.58 support=2.55 resistance=2.71 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:42 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=3517697.75 spike=0.16
- EFIC.CA: score=5.68 buy_ready=False sector_rank=16 price=197.28 support=196.0 resistance=207.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:42 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=7776981.5 spike=0.69
- EFID.CA: score=12.65 buy_ready=False sector_rank=18 price=26.81 support=25.85 resistance=28.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:41 AM market time freshness=DELAYED_CURRENT RSI=29.81 liquidity=12235070.0 spike=0.28
- EFIH.CA: score=25.97 buy_ready=True sector_rank=11 price=22.34 support=20.1 resistance=24.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:41 AM market time freshness=DELAYED_CURRENT RSI=42.67 liquidity=19054500.0 spike=0.31
- EGAL.CA: score=16.79 buy_ready=False sector_rank=16 price=295.05 support=272.28 resistance=312.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:41 AM market time freshness=DELAYED_CURRENT RSI=48.3 liquidity=6885510.5 spike=0.16
- EGAS.CA: score=16.54 buy_ready=True sector_rank=17 price=51.5 support=48.1 resistance=54.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:42 AM market time freshness=DELAYED_CURRENT RSI=61.84 liquidity=1684864.88 spike=0.13
- EGBE.CA: score=12.19 buy_ready=False sector_rank=5 price=0.47 support=-0.34 resistance=0.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:33 AM market time freshness=DELAYED_CURRENT RSI=96.42 liquidity=66631.8 spike=1.36
- EGCH.CA: score=19.9 buy_ready=False sector_rank=16 price=12.73 support=12.13 resistance=13.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:41 AM market time freshness=DELAYED_CURRENT RSI=56.22 liquidity=13600836.0 spike=0.22
- EGSA.CA: score=9.41 buy_ready=False sector_rank=6 price=8.87 support=8.67 resistance=9.21 source=Yahoo Finance history + Mubasher delayed current trading data as_of=29 July 01:02 PM market time freshness=DELAYED_CURRENT RSI=51.52 liquidity=10940.27 spike=0.61
- EGTS.CA: score=9.3 buy_ready=False sector_rank=2 price=17.61 support=15.1 resistance=19.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:41 AM market time freshness=DELAYED_CURRENT RSI=33.42 liquidity=2895406.0 spike=0.06
- EHDR.CA: score=7.85 buy_ready=False sector_rank=7 price=2.75 support=2.75 resistance=2.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:42 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=8540571.0 spike=0.21
- EKHO.CA: score=6.86 buy_ready=False sector_rank=17 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-07-27T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=20.29 buy_ready=False sector_rank=8 price=2.14 support=2.04 resistance=2.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:41 AM market time freshness=DELAYED_CURRENT RSI=62.16 liquidity=22198846.0 spike=0.32
- ELKA.CA: score=9.31 buy_ready=False sector_rank=7 price=1.82 support=1.81 resistance=1.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:42 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=10304525.0 spike=0.14
- ELNA.CA: score=16.47 buy_ready=False sector_rank=7 price=38.99 support=36.01 resistance=40.5 source=Yahoo Finance as_of=2026-07-27T21:00:00+00:00 freshness=FRESH RSI=50.7 liquidity=162939.22 spike=0.27
- ELSH.CA: score=9.31 buy_ready=False sector_rank=7 price=14.0 support=13.96 resistance=14.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:42 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=49229924.0 spike=0.35
- ELWA.CA: score=19.36 buy_ready=False sector_rank=7 price=1.83 support=1.82 resistance=2.14 source=Yahoo Finance as_of=2026-07-27T21:00:00+00:00 freshness=FRESH RSI=37.84 liquidity=5051843.22 spike=3.74
- EMFD.CA: score=21.4 buy_ready=False sector_rank=2 price=11.2 support=11.25 resistance=12.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:41 AM market time freshness=DELAYED_CURRENT RSI=40.35 liquidity=13027300.0 spike=0.22
- ENGC.CA: score=1.68 buy_ready=False sector_rank=7 price=41.0 support=41.0 resistance=42.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:42 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=2367443.0 spike=0.09
- EOSB.CA: score=14.31 buy_ready=False sector_rank=7 price=1.48 support=1.5 resistance=1.55 source=Yahoo Finance as_of=2026-07-27T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=3806.56 spike=0.1
- EPCO.CA: score=14.0 buy_ready=False sector_rank=7 price=10.56 support=8.5 resistance=11.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:43 AM market time freshness=DELAYED_CURRENT RSI=77.19 liquidity=2692914.5 spike=0.09
- EPPK.CA: score=17.26 buy_ready=False sector_rank=7 price=15.09 support=12.81 resistance=15.93 source=Yahoo Finance as_of=2026-07-27T21:00:00+00:00 freshness=FRESH RSI=50.29 liquidity=956374.03 spike=0.78
- ETEL.CA: score=26.4 buy_ready=False sector_rank=6 price=103.0 support=89.01 resistance=107.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:41 AM market time freshness=DELAYED_CURRENT RSI=72.61 liquidity=34983476.0 spike=0.42
- ETRS.CA: score=12.26 buy_ready=False sector_rank=7 price=10.4 support=10.65 resistance=10.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:43 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=3951193.25 spike=1.0
- EXPA.CA: score=18.1 buy_ready=False sector_rank=5 price=19.79 support=18.05 resistance=20.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:42 AM market time freshness=DELAYED_CURRENT RSI=78.76 liquidity=6704212.0 spike=0.22
- FAIT.CA: score=9.8 buy_ready=False sector_rank=5 price=36.32 support=35.06 resistance=38.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:41 AM market time freshness=DELAYED_CURRENT RSI=61.71 liquidity=403600.72 spike=0.14
- FAITA.CA: score=9.43 buy_ready=False sector_rank=5 price=0.97 support=0.96 resistance=0.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=29 July 01:04 PM market time freshness=DELAYED_CURRENT RSI=41.79 liquidity=32193.22 spike=0.76
- FERC.CA: score=11.71 buy_ready=False sector_rank=16 price=76.41 support=72.75 resistance=85.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:42 AM market time freshness=DELAYED_CURRENT RSI=58.06 liquidity=802232.44 spike=0.07
- FWRY.CA: score=20.97 buy_ready=False sector_rank=11 price=18.89 support=18.15 resistance=19.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:41 AM market time freshness=DELAYED_CURRENT RSI=40.59 liquidity=17517968.0 spike=0.13
- GBCO.CA: score=16.89 buy_ready=False sector_rank=13 price=29.7 support=30.12 resistance=34.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:42 AM market time freshness=DELAYED_CURRENT RSI=45.23 liquidity=5481352.0 spike=0.07
- GDWA.CA: score=21.31 buy_ready=False sector_rank=7 price=0.81 support=0.76 resistance=0.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:42 AM market time freshness=DELAYED_CURRENT RSI=72.67 liquidity=23766758.0 spike=0.26
- GGCC.CA: score=16.16 buy_ready=False sector_rank=7 price=0.82 support=0.45 resistance=0.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:42 AM market time freshness=DELAYED_CURRENT RSI=82.85 liquidity=4851941.0 spike=0.13
- GIHD.CA: score=3.91 buy_ready=False sector_rank=7 price=57.75 support=57.6 resistance=59.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:43 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=4602268.5 spike=0.09
- GMCI.CA: score=15.13 buy_ready=False sector_rank=7 price=2.07 support=1.71 resistance=2.26 source=Yahoo Finance as_of=2026-07-27T21:00:00+00:00 freshness=FRESH RSI=49.28 liquidity=820034.61 spike=0.62
- GRCA.CA: score=15.13 buy_ready=False sector_rank=7 price=59.7 support=48.0 resistance=68.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:42 AM market time freshness=DELAYED_CURRENT RSI=74.0 liquidity=820965.13 spike=0.05
- GSSC.CA: score=27.09 buy_ready=True sector_rank=7 price=278.36 support=240.52 resistance=288.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:43 AM market time freshness=DELAYED_CURRENT RSI=64.56 liquidity=13760382.0 spike=1.39
- GTWL.CA: score=24.31 buy_ready=True sector_rank=7 price=100.3 support=60.3 resistance=118.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:43 AM market time freshness=DELAYED_CURRENT RSI=51.57 liquidity=11633223.0 spike=0.08
- HDBK.CA: score=15.03 buy_ready=False sector_rank=5 price=81.59 support=76.9 resistance=86.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:41 AM market time freshness=DELAYED_CURRENT RSI=48.3 liquidity=2626308.5 spike=0.09
- HELI.CA: score=23.4 buy_ready=False sector_rank=2 price=8.31 support=6.36 resistance=8.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:41 AM market time freshness=DELAYED_CURRENT RSI=85.71 liquidity=120836096.0 spike=0.63
- HRHO.CA: score=12.61 buy_ready=False sector_rank=12 price=26.16 support=26.09 resistance=27.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:41 AM market time freshness=DELAYED_CURRENT RSI=33.73 liquidity=16181073.0 spike=0.19
- ICID.CA: score=15.74 buy_ready=False sector_rank=7 price=8.0 support=6.55 resistance=8.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:43 AM market time freshness=DELAYED_CURRENT RSI=54.66 liquidity=3432309.25 spike=0.49
- IDRE.CA: score=17.24 buy_ready=True sector_rank=7 price=46.93 support=41.1 resistance=52.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:43 AM market time freshness=DELAYED_CURRENT RSI=66.32 liquidity=2929008.0 spike=0.11
- IFAP.CA: score=13.28 buy_ready=False sector_rank=4 price=19.09 support=18.47 resistance=20.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:42 AM market time freshness=DELAYED_CURRENT RSI=54.42 liquidity=2875035.75 spike=0.31
- INFI.CA: score=16.9 buy_ready=False sector_rank=7 price=104.53 support=88.51 resistance=111.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:42 AM market time freshness=DELAYED_CURRENT RSI=75.05 liquidity=3592244.5 spike=0.22
- IRON.CA: score=3.26 buy_ready=False sector_rank=16 price=30.51 support=30.45 resistance=33.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:41 AM market time freshness=DELAYED_CURRENT RSI=27.59 liquidity=1358390.5 spike=0.2
- ISMA.CA: score=3.33 buy_ready=False sector_rank=7 price=30.13 support=30.0 resistance=31.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:43 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=4023463.5 spike=0.16
- ISMQ.CA: score=20.9 buy_ready=False sector_rank=16 price=9.06 support=9.05 resistance=10.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:42 AM market time freshness=DELAYED_CURRENT RSI=43.75 liquidity=29440452.0 spike=0.31
- ISPH.CA: score=21.08 buy_ready=False sector_rank=9 price=11.35 support=11.2 resistance=11.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:41 AM market time freshness=DELAYED_CURRENT RSI=43.51 liquidity=11725318.0 spike=0.24
- JUFO.CA: score=8.06 buy_ready=False sector_rank=18 price=28.55 support=28.5 resistance=31.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:41 AM market time freshness=DELAYED_CURRENT RSI=16.41 liquidity=5407717.0 spike=0.21
- KABO.CA: score=23.49 buy_ready=True sector_rank=1 price=7.91 support=6.04 resistance=8.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:41 AM market time freshness=DELAYED_CURRENT RSI=68.56 liquidity=6090648.0 spike=0.13
- KWIN.CA: score=23.31 buy_ready=False sector_rank=7 price=98.98 support=65.0 resistance=111.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:43 AM market time freshness=DELAYED_CURRENT RSI=89.58 liquidity=14540557.0 spike=0.29
- KZPC.CA: score=11.33 buy_ready=False sector_rank=7 price=8.51 support=8.26 resistance=8.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:43 AM market time freshness=DELAYED_CURRENT RSI=55.36 liquidity=1017416.69 spike=0.2
- LCSW.CA: score=4.53 buy_ready=False sector_rank=10 price=32.59 support=32.55 resistance=34.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:41 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=5503371.5 spike=0.07
- LUTS.CA: score=2.34 buy_ready=False sector_rank=7 price=0.55 support=0.55 resistance=0.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:43 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=3034647.5 spike=0.09
- MAAL.CA: score=14.38 buy_ready=False sector_rank=7 price=8.66 support=6.92 resistance=8.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:43 AM market time freshness=DELAYED_CURRENT RSI=78.06 liquidity=5076634.5 spike=0.31
- MASR.CA: score=22.31 buy_ready=False sector_rank=7 price=7.81 support=6.82 resistance=8.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:43 AM market time freshness=DELAYED_CURRENT RSI=58.55 liquidity=23460096.0 spike=0.26
- MBSC.CA: score=14.78 buy_ready=False sector_rank=10 price=243.33 support=222.66 resistance=249.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:41 AM market time freshness=DELAYED_CURRENT RSI=49.26 liquidity=1755019.0 spike=0.09
- MCQE.CA: score=14.76 buy_ready=False sector_rank=10 price=182.12 support=167.02 resistance=195.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:41 AM market time freshness=DELAYED_CURRENT RSI=58.38 liquidity=1740023.0 spike=0.1
- MCRO.CA: score=22.31 buy_ready=False sector_rank=7 price=1.47 support=1.17 resistance=1.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:43 AM market time freshness=DELAYED_CURRENT RSI=80.0 liquidity=43050184.0 spike=0.36
- MENA.CA: score=14.79 buy_ready=False sector_rank=2 price=6.97 support=6.61 resistance=7.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:37 AM market time freshness=DELAYED_CURRENT RSI=53.23 liquidity=394086.84 spike=0.05
- MEPA.CA: score=9.31 buy_ready=False sector_rank=7 price=1.78 support=1.78 resistance=1.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:43 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=11905693.0 spike=0.25
- MFPC.CA: score=19.9 buy_ready=False sector_rank=16 price=36.0 support=34.3 resistance=38.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:41 AM market time freshness=DELAYED_CURRENT RSI=55.66 liquidity=30927292.0 spike=0.34
- MFSC.CA: score=10.1 buy_ready=False sector_rank=7 price=46.75 support=45.05 resistance=53.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:41 AM market time freshness=DELAYED_CURRENT RSI=35.76 liquidity=789942.75 spike=0.14
- MHOT.CA: score=9.98 buy_ready=False sector_rank=15 price=16.67 support=16.2 resistance=18.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:40 AM market time freshness=DELAYED_CURRENT RSI=43.38 liquidity=948568.94 spike=0.08
- MICH.CA: score=17.25 buy_ready=True sector_rank=7 price=40.28 support=34.0 resistance=43.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:43 AM market time freshness=DELAYED_CURRENT RSI=68.11 liquidity=2944186.75 spike=0.18
- MILS.CA: score=10.29 buy_ready=False sector_rank=7 price=201.2 support=188.0 resistance=211.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:43 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=57764120.0 spike=1.49
- MIPH.CA: score=14.63 buy_ready=False sector_rank=9 price=743.05 support=630.5 resistance=780.0 source=Yahoo Finance as_of=2026-07-27T21:00:00+00:00 freshness=FRESH RSI=71.65 liquidity=550600.04 spike=0.16
- MOED.CA: score=15.65 buy_ready=False sector_rank=7 price=0.69 support=0.65 resistance=0.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:43 AM market time freshness=DELAYED_CURRENT RSI=46.9 liquidity=7346703.5 spike=0.33
- MOIL.CA: score=-1.67 buy_ready=False sector_rank=17 price=0.69 support=0.68 resistance=0.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:41 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=466878.16 spike=0.74
- MOIN.CA: score=8.49 buy_ready=False sector_rank=7 price=23.6 support=22.66 resistance=24.76 source=Yahoo Finance as_of=2026-07-27T21:00:00+00:00 freshness=FRESH RSI=41.28 liquidity=185661.2 spike=0.24
- MOSC.CA: score=19.66 buy_ready=True sector_rank=7 price=284.36 support=250.55 resistance=329.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:43 AM market time freshness=DELAYED_CURRENT RSI=61.26 liquidity=3347448.25 spike=0.26
- MPCI.CA: score=23.31 buy_ready=False sector_rank=7 price=291.48 support=223.51 resistance=298.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:43 AM market time freshness=DELAYED_CURRENT RSI=88.57 liquidity=17940746.0 spike=0.18
- MPCO.CA: score=26.4 buy_ready=True sector_rank=4 price=1.9 support=1.7 resistance=1.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:41 AM market time freshness=DELAYED_CURRENT RSI=61.7 liquidity=34354844.0 spike=0.57
- MPRC.CA: score=17.46 buy_ready=False sector_rank=7 price=45.66 support=37.15 resistance=45.82 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:43 AM market time freshness=DELAYED_CURRENT RSI=73.54 liquidity=3154725.75 spike=0.1
- MTIE.CA: score=21.41 buy_ready=False sector_rank=13 price=9.44 support=8.92 resistance=9.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:41 AM market time freshness=DELAYED_CURRENT RSI=57.84 liquidity=11957336.0 spike=0.51
- NAHO.CA: score=3.31 buy_ready=False sector_rank=7 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance as_of=2026-07-27T21:00:00+00:00 freshness=FRESH RSI=0.0 liquidity=4666.91 spike=0.14
- NCCW.CA: score=26.31 buy_ready=False sector_rank=7 price=6.81 support=5.82 resistance=7.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:43 AM market time freshness=DELAYED_CURRENT RSI=73.8 liquidity=11018488.0 spike=0.41
- NEDA.CA: score=9.57 buy_ready=False sector_rank=7 price=2.75 support=2.7 resistance=3.02 source=Yahoo Finance as_of=2026-07-27T21:00:00+00:00 freshness=FRESH RSI=43.9 liquidity=261426.0 spike=0.36
- NHPS.CA: score=5.17 buy_ready=False sector_rank=7 price=82.94 support=82.25 resistance=87.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:43 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=5862461.0 spike=0.07
- NINH.CA: score=14.89 buy_ready=False sector_rank=7 price=21.43 support=17.4 resistance=23.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:43 AM market time freshness=DELAYED_CURRENT RSI=75.5 liquidity=3586224.25 spike=0.08
- NIPH.CA: score=21.08 buy_ready=False sector_rank=9 price=217.43 support=157.01 resistance=242.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:42 AM market time freshness=DELAYED_CURRENT RSI=80.94 liquidity=39841012.0 spike=0.26
- OBRI.CA: score=14.8 buy_ready=False sector_rank=7 price=33.16 support=31.5 resistance=39.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:42 AM market time freshness=DELAYED_CURRENT RSI=38.98 liquidity=5490885.0 spike=0.13
- OCDI.CA: score=26.4 buy_ready=True sector_rank=2 price=28.0 support=23.91 resistance=28.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:39 AM market time freshness=DELAYED_CURRENT RSI=57.83 liquidity=24152596.0 spike=0.27
- OCPH.CA: score=15.63 buy_ready=False sector_rank=7 price=461.57 support=341.4 resistance=496.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:43 AM market time freshness=DELAYED_CURRENT RSI=94.23 liquidity=2324217.0 spike=0.09
- ODIN.CA: score=24.31 buy_ready=True sector_rank=7 price=2.66 support=2.05 resistance=2.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:42 AM market time freshness=DELAYED_CURRENT RSI=65.22 liquidity=10831259.0 spike=0.66
- OFH.CA: score=9.31 buy_ready=False sector_rank=7 price=0.69 support=0.69 resistance=0.71 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:43 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=10138181.0 spike=0.15
- OIH.CA: score=19.74 buy_ready=False sector_rank=14 price=1.47 support=1.4 resistance=1.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:41 AM market time freshness=DELAYED_CURRENT RSI=73.33 liquidity=4334658.5 spike=0.06
- OLFI.CA: score=17.2 buy_ready=True sector_rank=18 price=22.89 support=21.0 resistance=23.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:41 AM market time freshness=DELAYED_CURRENT RSI=53.91 liquidity=2550042.75 spike=0.07
- ORAS.CA: score=7.6 buy_ready=False sector_rank=20 price=708.9 support=708.01 resistance=719.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:41 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=24080360.0 spike=1.0
- ORHD.CA: score=26.4 buy_ready=False sector_rank=2 price=38.75 support=37.2 resistance=40.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:41 AM market time freshness=DELAYED_CURRENT RSI=54.71 liquidity=25493000.0 spike=0.17
- ORWE.CA: score=20.26 buy_ready=False sector_rank=1 price=22.64 support=21.95 resistance=23.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:42 AM market time freshness=DELAYED_CURRENT RSI=47.9 liquidity=5855471.0 spike=0.24
- PHAR.CA: score=11.32 buy_ready=False sector_rank=9 price=98.99 support=95.75 resistance=101.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:42 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=105038160.0 spike=2.12
- PHDC.CA: score=21.4 buy_ready=False sector_rank=2 price=14.43 support=14.3 resistance=15.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:41 AM market time freshness=DELAYED_CURRENT RSI=44.13 liquidity=26474118.0 spike=0.11
- PHTV.CA: score=14.07 buy_ready=False sector_rank=7 price=321.63 support=255.0 resistance=327.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:41 AM market time freshness=DELAYED_CURRENT RSI=84.68 liquidity=761865.31 spike=0.14
- POUL.CA: score=8.14 buy_ready=False sector_rank=18 price=36.99 support=36.52 resistance=41.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:41 AM market time freshness=DELAYED_CURRENT RSI=32.01 liquidity=5496518.5 spike=0.16
- PRCL.CA: score=16.7 buy_ready=True sector_rank=10 price=35.31 support=30.21 resistance=38.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:40 AM market time freshness=DELAYED_CURRENT RSI=50.12 liquidity=2672552.0 spike=0.05
- PRDC.CA: score=26.4 buy_ready=True sector_rank=2 price=9.2 support=7.0 resistance=10.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:40 AM market time freshness=DELAYED_CURRENT RSI=56.05 liquidity=11871684.0 spike=0.1
- PRMH.CA: score=13.24 buy_ready=False sector_rank=7 price=2.56 support=2.36 resistance=2.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:41 AM market time freshness=DELAYED_CURRENT RSI=54.39 liquidity=3931926.75 spike=0.23
- RACC.CA: score=14.67 buy_ready=False sector_rank=7 price=9.96 support=9.36 resistance=10.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:43 AM market time freshness=DELAYED_CURRENT RSI=49.27 liquidity=2365908.5 spike=0.11
- RAKT.CA: score=12.8 buy_ready=False sector_rank=7 price=22.63 support=21.25 resistance=23.7 source=Yahoo Finance as_of=2026-07-27T21:00:00+00:00 freshness=FRESH RSI=47.93 liquidity=316254.24 spike=1.09
- RAYA.CA: score=16.46 buy_ready=False sector_rank=21 price=7.43 support=7.01 resistance=8.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:41 AM market time freshness=DELAYED_CURRENT RSI=35.81 liquidity=11070279.0 spike=0.08
- RMDA.CA: score=23.5 buy_ready=True sector_rank=9 price=5.15 support=4.81 resistance=5.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:40 AM market time freshness=DELAYED_CURRENT RSI=57.14 liquidity=7421762.0 spike=0.29
- ROTO.CA: score=21.13 buy_ready=True sector_rank=7 price=42.52 support=38.0 resistance=46.71 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:43 AM market time freshness=DELAYED_CURRENT RSI=58.75 liquidity=2818848.5 spike=0.14
- RREI.CA: score=25.37 buy_ready=False sector_rank=7 price=4.64 support=3.34 resistance=4.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:43 AM market time freshness=DELAYED_CURRENT RSI=82.91 liquidity=87372504.0 spike=2.03
- RTVC.CA: score=12.72 buy_ready=False sector_rank=7 price=3.84 support=3.55 resistance=4.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:43 AM market time freshness=DELAYED_CURRENT RSI=52.17 liquidity=1408288.38 spike=0.31
- RUBX.CA: score=15.54 buy_ready=False sector_rank=7 price=12.6 support=11.07 resistance=14.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:43 AM market time freshness=DELAYED_CURRENT RSI=50.28 liquidity=3229768.0 spike=0.05
- SAUD.CA: score=19.08 buy_ready=True sector_rank=5 price=21.98 support=20.0 resistance=22.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:40 AM market time freshness=DELAYED_CURRENT RSI=57.75 liquidity=2680140.5 spike=0.28
- SCEM.CA: score=23.02 buy_ready=False sector_rank=10 price=83.48 support=60.14 resistance=87.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:41 AM market time freshness=DELAYED_CURRENT RSI=87.72 liquidity=18675178.0 spike=0.27
- SCFM.CA: score=9.31 buy_ready=False sector_rank=7 price=298.19 support=283.1 resistance=309.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:43 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=17488812.0 spike=0.81
- SCTS.CA: score=13.89 buy_ready=False sector_rank=3 price=610.5 support=540.0 resistance=649.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:40 AM market time freshness=DELAYED_CURRENT RSI=44.86 liquidity=488959.22 spike=0.07
- SDTI.CA: score=18.1 buy_ready=False sector_rank=7 price=58.8 support=45.55 resistance=58.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:42 AM market time freshness=DELAYED_CURRENT RSI=85.44 liquidity=4787436.0 spike=0.38
- SEIG.CA: score=14.88 buy_ready=False sector_rank=7 price=245.21 support=183.0 resistance=285.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:43 AM market time freshness=DELAYED_CURRENT RSI=59.26 liquidity=572801.0 spike=0.02
- SIPC.CA: score=20.5 buy_ready=False sector_rank=7 price=3.86 support=3.25 resistance=4.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:43 AM market time freshness=DELAYED_CURRENT RSI=75.26 liquidity=9194777.0 spike=0.4
- SKPC.CA: score=18.9 buy_ready=False sector_rank=16 price=15.86 support=14.8 resistance=16.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:41 AM market time freshness=DELAYED_CURRENT RSI=49.88 liquidity=19624326.0 spike=0.56
- SMFR.CA: score=22.05 buy_ready=True sector_rank=7 price=234.76 support=189.3 resistance=277.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:43 AM market time freshness=DELAYED_CURRENT RSI=66.44 liquidity=7746710.0 spike=0.37
- SNFC.CA: score=10.58 buy_ready=False sector_rank=7 price=11.09 support=11.04 resistance=12.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:42 AM market time freshness=DELAYED_CURRENT RSI=44.54 liquidity=1270001.25 spike=0.11
- SPIN.CA: score=22.94 buy_ready=False sector_rank=1 price=15.71 support=14.0 resistance=17.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:42 AM market time freshness=DELAYED_CURRENT RSI=77.36 liquidity=8540356.0 spike=0.37
- SPMD.CA: score=20.93 buy_ready=False sector_rank=7 price=0.45 support=0.41 resistance=0.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:43 AM market time freshness=DELAYED_CURRENT RSI=74.24 liquidity=4617216.0 spike=0.18
- SUGR.CA: score=10.35 buy_ready=False sector_rank=18 price=46.71 support=45.31 resistance=47.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:42 AM market time freshness=DELAYED_CURRENT RSI=46.03 liquidity=1704700.13 spike=0.31
- SVCE.CA: score=13.95 buy_ready=False sector_rank=7 price=9.15 support=8.8 resistance=10.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:43 AM market time freshness=DELAYED_CURRENT RSI=44.85 liquidity=4645621.5 spike=0.09
- SWDY.CA: score=20.97 buy_ready=False sector_rank=8 price=92.34 support=84.3 resistance=97.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:41 AM market time freshness=DELAYED_CURRENT RSI=70.73 liquidity=6684458.5 spike=0.32
- TALM.CA: score=10.76 buy_ready=False sector_rank=3 price=17.63 support=17.62 resistance=18.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:41 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=19633750.0 spike=1.18
- TMGH.CA: score=23.4 buy_ready=False sector_rank=2 price=96.04 support=92.1 resistance=103.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:41 AM market time freshness=DELAYED_CURRENT RSI=54.91 liquidity=76863712.0 spike=0.21
- TRTO.CA: score=10.31 buy_ready=False sector_rank=7 price=0.03 support=0.03 resistance=0.03 source=Yahoo Finance as_of=2026-07-27T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=170.0 spike=0.15
- UEFM.CA: score=17.03 buy_ready=True sector_rank=7 price=553.55 support=462.0 resistance=625.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:43 AM market time freshness=DELAYED_CURRENT RSI=68.07 liquidity=2726401.5 spike=0.64
- UEGC.CA: score=6.93 buy_ready=False sector_rank=7 price=2.24 support=2.22 resistance=2.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:43 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=7621054.0 spike=0.15
- UNIP.CA: score=2.65 buy_ready=False sector_rank=7 price=0.38 support=0.38 resistance=0.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:43 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=3344479.75 spike=0.13
- UNIT.CA: score=16.8 buy_ready=False sector_rank=2 price=17.84 support=12.0 resistance=21.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:39 AM market time freshness=DELAYED_CURRENT RSI=53.41 liquidity=396575.69 spike=0.01
- WCDF.CA: score=17.3 buy_ready=False sector_rank=7 price=580.04 support=504.0 resistance=634.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:37 AM market time freshness=DELAYED_CURRENT RSI=64.97 liquidity=993580.88 spike=0.41
- WKOL.CA: score=21.29 buy_ready=True sector_rank=7 price=315.34 support=273.1 resistance=340.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:43 AM market time freshness=DELAYED_CURRENT RSI=43.6 liquidity=4986413.0 spike=0.49
- ZEOT.CA: score=24.31 buy_ready=False sector_rank=7 price=12.41 support=10.6 resistance=12.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:44 AM market time freshness=DELAYED_CURRENT RSI=71.56 liquidity=29499810.0 spike=0.88
- ZMID.CA: score=26.4 buy_ready=False sector_rank=2 price=7.35 support=6.19 resistance=7.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:42 AM market time freshness=DELAYED_CURRENT RSI=70.62 liquidity=57886548.0 spike=0.23

## Backtesting Lite
- COMI.CA: 180d return=34.26%, max drawdown=-18.04%, MA20>MA50 days last20=4, as_of=2026-07-27T21:00:00+00:00
- GSSC.CA: 180d return=10.1%, max drawdown=-19.21%, MA20>MA50 days last20=5, as_of=2026-07-27T21:00:00+00:00
- ATQA.CA: 180d return=-1.56%, max drawdown=-22.5%, MA20>MA50 days last20=1, as_of=2026-07-27T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- COMI.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Commercial International Bank Egypt summary=Evidence rejected for COMI.CA: source text did not clearly match COMI.CA / Commercial International Bank Egypt.
- GSSC.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=General Co. For Silos & Storage summary=General Company for Silos generates nearly EGP 62m net profits in Q1-25/26 audited financials; General Company for Silos to set up new firm with EGP 500m capital; General Company for Silos’ EGM nods to EGP 25m capital hike
  - General Company for Silos generates nearly EGP 62m net profits in Q1-25/26 audited financials: https://english.mubasher.info/news/4529067/General-Company-for-Silos-generates-nearly-EGP-62m-net-profits-in-Q1-25-26-audited-financials/
  - General Company for Silos to set up new firm with EGP 500m capital: https://english.mubasher.info/news/4043715/General-Company-for-Silos-to-set-up-new-firm-with-EGP-500m-capital/
  - General Company for Silos’ EGM nods to EGP 25m capital hike: https://english.mubasher.info/news/4018676/General-Company-for-Silos-EGM-nods-to-EGP-25m-capital-hike/
- ATQA.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Misr National Steel Ataqa summary=Evidence rejected for ATQA.CA: source text did not clearly match ATQA.CA / Misr National Steel Ataqa.
- MPCO.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=575 sources=3 expected=Mansoura Poultry summary=Mansoura Poultry’s consolidated net profits drop in 2025; revenues near EGP 857m; Mansoura Poultry’s stock rebounds from key support level; Mansoura Poultry stock witnesses clear emergence of buying power
  - Mansoura Poultry’s consolidated net profits drop in 2025; revenues near EGP 857m: https://english.mubasher.info/news/4596342/Mansoura-Poultry-s-consolidated-net-profits-drop-in-2025-revenues-near-EGP-857m/
  - Mansoura Poultry’s stock rebounds from key support level: https://english.mubasher.info/news/4554482/Mansoura-Poultry-s-stock-rebounds-from-key-support-level/
  - Mansoura Poultry stock witnesses clear emergence of buying power: https://english.mubasher.info/news/4539119/Mansoura-Poultry-stock-witnesses-clear-emergence-of-buying-power/
- ADIB.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Abu Dhabi Islamic Bank Egypt summary=ADIB Egypt’s consolidated profits leap to EGP 3.6bn in Q1-26; ADIB Egypt stock approaches breakout above EGP 41; ADIB Egypt’s stock holds uptrend despite corrections
  - ADIB Egypt’s consolidated profits leap to EGP 3.6bn in Q1-26: https://english.mubasher.info/news/4607278/ADIB-Egypt-s-consolidated-profits-leap-to-EGP-3-6bn-in-Q1-26/
  - ADIB Egypt stock approaches breakout above EGP 41: https://english.mubasher.info/news/4591391/ADIB-Egypt-stock-approaches-breakout-above-EGP-41/
  - ADIB Egypt’s stock holds uptrend despite corrections: https://english.mubasher.info/news/4562331/ADIB-Egypt-s-stock-holds-uptrend-despite-corrections/
- OCDI.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Sixth of October Development and Investment summary=Evidence rejected for OCDI.CA: source text did not clearly match OCDI.CA / Sixth of October Development and Investment.
- ORHD.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Orascom Development Egypt summary=Evidence rejected for ORHD.CA: source text did not clearly match ORHD.CA / Orascom Development Egypt.
- ETEL.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Telecom Egypt summary=Evidence rejected for ETEL.CA: source text did not clearly match ETEL.CA / Telecom Egypt.

## Warnings
- Evidence rejected for COMI.CA: source text did not clearly match COMI.CA / Commercial International Bank Egypt.
- Gemini batch evidence failed: Server disconnected without sending a response.
- Evidence for GSSC.CA matches the company but no source/report date was detected.
- Evidence rejected for ATQA.CA: source text did not clearly match ATQA.CA / Misr National Steel Ataqa.
- Evidence for MPCO.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for ADIB.CA matches the company but no source/report date was detected.
- Evidence rejected for OCDI.CA: source text did not clearly match OCDI.CA / Sixth of October Development and Investment.
- Evidence rejected for ORHD.CA: source text did not clearly match ORHD.CA / Orascom Development Egypt.
- Evidence rejected for ETEL.CA: source text did not clearly match ETEL.CA / Telecom Egypt.
