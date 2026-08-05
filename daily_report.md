# Telegram-First EGX Scanner Report

Scan phase: Evening tomorrow plan
Generated UTC: 2026-08-05T18:05:39.082290+00:00
Generated Cairo: 2026-08-05 21:05
Run timing: target 19:30 Cairo | generated Cairo 2026-08-05 21:05 | cron 30 16 * * 0-4
Trigger: scheduled cron=30 16 * * 0-4 mapped to evening_plan; Cairo now 2026-08-05 21:00

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 79
- Data quality issues: 1
- Tradeable price/liquidity tickers: 170/189
- Top sector: Healthcare

## Market Context
- Market trend: Bullish
- Source: Mubasher EGX market page (delayed public data)
- As of: Wednesday, August 05
- Freshness: DELAYED
- EGX30 regime: BULLISH / above MA20 72.22% / above MA50 61.11%
- EGX70 regime: BULLISH / above MA20 78.95% / above MA50 97.37%
- Sector breadth: 61.9%
- Risk mode: BROAD_RISK_ON

## Top Liquidity
- PHAR.CA: liquidity=679587904.0 spike=3.41 score=30.72
- COMI.CA: liquidity=510197824.0 spike=1.25 score=26.4
- ORWE.CA: liquidity=425940704.0 spike=11.67 score=15.9
- PHDC.CA: liquidity=388923744.0 spike=1.66 score=30.49
- AFMC.CA: liquidity=358783904.0 spike=3.16 score=15.22

## AI Narrative
- Provider: OpenRouter OK
- Model: nvidia/nemotron-3-super-120b-a12b:free
- Summary: EGX30 and EGX70 are bullish with broad risk‑on, sector breadth ~62% led by Healthcare, Automotive & Distribution, and Industrial Goods & Cables; the scanner flagged several accumulation‑spike stocks with a bullish‑watch outlook but noted extended momentum, mixed proximity to resistance and lacking fresh evidence, so it issued a HOLD stance.
- Liquidity: accumulation spikes (liquidity_spike 2.5‑4.2×) show short‑term buying interest that could support upside over the next 1‑3 days if sustained.
- Sector tailwind: leading sectors (Healthcare, Automotive & Distribution, Industrial Goods & Cables) have 100% of constituents above MA20/MA50, providing a supportive backdrop for stocks in those groups.
- Technical stance: most tickets sit close to or just below their 20‑day resistance (support_distance_pct 6‑18%, resistance_distance_pct -3.5 to +0.7) with RSI ranging 54‑79, indicating some are extended or overheated and 
- Regime & uncertainty: EGX30/EGX70 bullishness and broad risk‑on raise appetite, but without clear evidence or fresh catalyst the scanner defaults to HOLD, highlighting the need for confirmation before acting.

## Top Liquidity Spikes
- MOIN.CA: spike=52.11 liquidity=167193888.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- ORWE.CA: spike=11.67 liquidity=425940704.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- IFAP.CA: spike=5.76 liquidity=82978184.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- EMFD.CA: spike=5.37 liquidity=279353760.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- LUTS.CA: spike=5.15 liquidity=174275040.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False

## Sector Leaderboard
- #1 Healthcare: score=16.05 5d=13.8% 20d=14.45% aboveMA50=100.0%
- #2 Automotive & Distribution: score=13.34 5d=7.28% 20d=6.33% aboveMA50=100.0%
- #3 Industrial Goods & Cables: score=12.11 5d=6.67% 20d=13.69% aboveMA50=100.0%
- #4 Energy & Petrochemicals: score=11.71 5d=7.29% 20d=17.79% aboveMA50=75.0%
- #5 Fintech & Payments: score=11.55 5d=4.56% 20d=1.48% aboveMA50=100.0%
- #6 Food, Beverages & Tobacco: score=9.33 5d=5.42% 20d=3.3% aboveMA50=71.43%
- #7 Investment Holding: score=8.91 5d=2.01% 20d=4.35% aboveMA50=100.0%
- #8 Building Materials: score=8.85 5d=-1.38% 20d=6.09% aboveMA50=100.0%

## Today's Prioritized Action Tickets
- HOLD: Local fallback HOLD: no candidate passed evidence, liquidity, freshness, and technical gates.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- GBCO.CA: BULLISH_WATCH score=96 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- BINV.CA: BULLISH_WATCH score=95.91 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=No major short-term scanner risk flags.
- WKOL.CA: BULLISH_WATCH score=94.78 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- PHDC.CA: BULLISH_WATCH score=94.18 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- SWDY.CA: BULLISH_WATCH score=93 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=overheated RSI
- FWRY.CA: BULLISH_WATCH score=91 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=close to resistance
- MCQE.CA: BULLISH_WATCH score=90.85 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- HRHO.CA: BULLISH_WATCH score=90.33 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended; sector is not leading
- EFID.CA: BULLISH_WATCH score=90.33 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended
- CNFN.CA: BULLISH_WATCH score=90.33 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading

## BUY-Ready Candidates
- HRHO.CA: rank=32.9 outlook=BULLISH_WATCH outlook_score=90.33 sector_rank=11 price=27.91 support=25.95 resistance=27.48 liquidity=347876512.0
- EFID.CA: rank=32.02 outlook=BULLISH_WATCH outlook_score=90.33 sector_rank=6 price=30.79 support=26.64 resistance=31.99 liquidity=194921456.0
- ALUM.CA: rank=31.56 outlook=BULLISH_WATCH outlook_score=82.78 sector_rank=16 price=24.69 support=22.08 resistance=24.85 liquidity=21289364.0
- FWRY.CA: rank=31.38 outlook=BULLISH_WATCH outlook_score=91 sector_rank=5 price=19.54 support=18.43 resistance=19.68 liquidity=290182208.0
- MFSC.CA: rank=31.08 outlook=BULLISH_WATCH outlook_score=88.78 sector_rank=16 price=51.58 support=45.05 resistance=65.0 liquidity=27557238.0
- IRON.CA: rank=30.56 outlook=BULLISH_WATCH outlook_score=81.2 sector_rank=17 price=34.21 support=30.14 resistance=32.7 liquidity=17736570.0
- PHDC.CA: rank=30.49 outlook=BULLISH_WATCH outlook_score=94.18 sector_rank=18 price=15.44 support=14.32 resistance=15.41 liquidity=388923744.0
- AREH.CA: rank=30.42 outlook=BULLISH_WATCH outlook_score=88.78 sector_rank=16 price=1.6 support=1.38 resistance=1.76 liquidity=107410680.0
- ENGC.CA: rank=30.38 outlook=CONSTRUCTIVE outlook_score=66.78 sector_rank=16 price=47.06 support=37.0 resistance=46.4 liquidity=40201328.0
- SAUD.CA: rank=29.96 outlook=BULLISH_WATCH outlook_score=89.4 sector_rank=14 price=22.76 support=21.03 resistance=22.75 liquidity=35438012.0

## Data Quality Issues
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=12.92 buy_ready=False sector_rank=16 price=303.06 support=274.0 resistance=312.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=75232088.0 spike=2.01
- ABUK.CA: score=24.58 buy_ready=False sector_rank=17 price=73.98 support=69.01 resistance=75.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=49.57 liquidity=133544328.0 spike=0.83
- ACAMD.CA: score=23.9 buy_ready=False sector_rank=16 price=2.34 support=2.28 resistance=2.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=56.1 liquidity=35025172.0 spike=0.5
- ACGC.CA: score=27.9 buy_ready=True sector_rank=13 price=10.95 support=9.42 resistance=11.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=68.13 liquidity=17388216.0 spike=0.53
- ADCI.CA: score=22.46 buy_ready=True sector_rank=16 price=276.47 support=230.0 resistance=325.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=66.23 liquidity=6560026.0 spike=0.36
- ADIB.CA: score=22.9 buy_ready=False sector_rank=14 price=51.59 support=46.0 resistance=53.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=75.46 liquidity=66009668.0 spike=0.48
- ADPC.CA: score=11.96 buy_ready=False sector_rank=16 price=4.23 support=4.01 resistance=4.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=65535236.0 spike=1.53
- AFDI.CA: score=25.32 buy_ready=False sector_rank=16 price=61.0 support=44.27 resistance=59.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=86.08 liquidity=28246618.0 spike=1.21
- AFMC.CA: score=15.22 buy_ready=False sector_rank=16 price=232.0 support=201.05 resistance=250.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=358783904.0 spike=3.16
- AJWA.CA: score=28.24 buy_ready=True sector_rank=16 price=191.9 support=161.0 resistance=210.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=59.12 liquidity=40094404.0 spike=1.17
- ALCN.CA: score=28.12 buy_ready=True sector_rank=9 price=31.19 support=28.62 resistance=30.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=65.77 liquidity=54183692.0 spike=2.11
- ALUM.CA: score=31.56 buy_ready=True sector_rank=16 price=24.69 support=22.08 resistance=24.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=68.98 liquidity=21289364.0 spike=2.83
- AMER.CA: score=10.69 buy_ready=False sector_rank=18 price=6.1 support=5.59 resistance=6.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=153284944.0 spike=1.26
- AMES.CA: score=11.02 buy_ready=False sector_rank=16 price=119.74 support=113.99 resistance=132.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=105785696.0 spike=1.06
- AMIA.CA: score=19.9 buy_ready=False sector_rank=16 price=12.86 support=8.74 resistance=13.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=83.69 liquidity=5000582.5 spike=0.29
- AMOC.CA: score=27.9 buy_ready=True sector_rank=4 price=9.19 support=7.7 resistance=9.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=64.59 liquidity=79858288.0 spike=0.8
- APSW.CA: score=17.93 buy_ready=True sector_rank=16 price=8.86 support=8.1 resistance=9.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=57.77 liquidity=1025394.75 spike=0.59
- ARAB.CA: score=23.17 buy_ready=False sector_rank=18 price=0.24 support=0.22 resistance=0.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=40.0 liquidity=79932152.0 spike=0.6
- ARCC.CA: score=28.62 buy_ready=True sector_rank=8 price=57.56 support=54.2 resistance=58.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=58.91 liquidity=71180328.0 spike=2.36
- AREH.CA: score=30.42 buy_ready=True sector_rank=16 price=1.6 support=1.38 resistance=1.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=43.75 liquidity=107410680.0 spike=3.26
- ARVA.CA: score=12.9 buy_ready=False sector_rank=16 price=12.35 support=10.56 resistance=12.6 source=Yahoo Finance as_of=2026-08-03T21:00:00+00:00 freshness=FRESH RSI=89.81 liquidity=0.0 spike=0.0
- ASCM.CA: score=27.9 buy_ready=False sector_rank=16 price=66.23 support=57.25 resistance=69.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=70.22 liquidity=24851490.0 spike=0.39
- ASPI.CA: score=22.9 buy_ready=False sector_rank=16 price=0.45 support=0.31 resistance=0.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=81.22 liquidity=14001317.0 spike=0.33
- ATLC.CA: score=25.13 buy_ready=True sector_rank=11 price=5.29 support=5.0 resistance=5.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=52.38 liquidity=9232338.0 spike=0.72
- ATQA.CA: score=28.14 buy_ready=True sector_rank=17 price=10.1 support=9.43 resistance=10.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=63.31 liquidity=48165488.0 spike=1.28
- AXPH.CA: score=19.81 buy_ready=True sector_rank=16 price=1259.56 support=1121.56 resistance=1439.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=60.71 liquidity=1910492.13 spike=0.46
- BINV.CA: score=28.42 buy_ready=True sector_rank=7 price=49.4 support=46.01 resistance=50.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=55.69 liquidity=15871408.0 spike=2.26
- BIOC.CA: score=11.16 buy_ready=False sector_rank=16 price=331.44 support=331.44 resistance=497.16 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=127536136.0 spike=1.13
- BTFH.CA: score=28.1 buy_ready=True sector_rank=11 price=3.19 support=3.03 resistance=3.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=58.33 liquidity=252303600.0 spike=1.1
- CAED.CA: score=22.5 buy_ready=True sector_rank=16 price=121.34 support=71.2 resistance=143.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=66.68 liquidity=8602435.0 spike=0.12
- CANA.CA: score=21.85 buy_ready=True sector_rank=14 price=38.54 support=35.2 resistance=39.63 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=69.08 liquidity=5950293.0 spike=0.31
- CCAP.CA: score=23.9 buy_ready=False sector_rank=7 price=5.26 support=5.06 resistance=5.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=41.23 liquidity=343744288.0 spike=0.5
- CCRS.CA: score=20.9 buy_ready=False sector_rank=16 price=2.45 support=2.3 resistance=2.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=16989188.0 spike=0.91
- CEFM.CA: score=26.6 buy_ready=True sector_rank=16 price=140.03 support=100.0 resistance=152.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=69.87 liquidity=40443060.0 spike=1.35
- CERA.CA: score=23.77 buy_ready=False sector_rank=16 price=1.32 support=1.23 resistance=1.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=9868392.0 spike=0.42
- CFGH.CA: score=9.9 buy_ready=False sector_rank=16 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance as_of=2026-08-03T21:00:00+00:00 freshness=FRESH RSI=43.75 liquidity=1085.66 spike=0.06
- CICH.CA: score=19.72 buy_ready=False sector_rank=11 price=12.92 support=11.6 resistance=13.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=72.08 liquidity=1818988.63 spike=0.22
- CIEB.CA: score=24.18 buy_ready=True sector_rank=14 price=24.45 support=23.75 resistance=24.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=47.28 liquidity=8275916.0 spike=0.89
- CIRA.CA: score=27.9 buy_ready=True sector_rank=12 price=35.62 support=28.4 resistance=37.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=64.3 liquidity=13598439.0 spike=0.23
- CLHO.CA: score=28.9 buy_ready=True sector_rank=1 price=17.46 support=15.98 resistance=19.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=67.12 liquidity=28251934.0 spike=0.55
- CNFN.CA: score=28.72 buy_ready=True sector_rank=11 price=4.91 support=4.68 resistance=5.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=49.09 liquidity=46018472.0 spike=2.41
- COMI.CA: score=26.4 buy_ready=True sector_rank=14 price=139.27 support=132.81 resistance=142.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=66.21 liquidity=510197824.0 spike=1.25
- COPR.CA: score=27.9 buy_ready=True sector_rank=16 price=0.41 support=0.35 resistance=0.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=64.91 liquidity=14960580.0 spike=0.47
- COSG.CA: score=25.9 buy_ready=True sector_rank=16 price=1.7 support=1.58 resistance=1.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=51.61 liquidity=14216774.0 spike=0.34
- CPCI.CA: score=19.24 buy_ready=False sector_rank=16 price=487.46 support=393.0 resistance=520.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=70.29 liquidity=3339800.25 spike=0.25
- CSAG.CA: score=15.9 buy_ready=False sector_rank=9 price=36.3 support=34.37 resistance=36.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=69458488.0 spike=4.25
- DAPH.CA: score=27.14 buy_ready=False sector_rank=16 price=103.82 support=81.0 resistance=103.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=83.08 liquidity=48356068.0 spike=2.12
- DEIN.CA: score=0.9 buy_ready=False sector_rank=16 price=11.38 support=13.65 resistance=13.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 June 12:11 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=40.95 spike=0.01
- DOMT.CA: score=27.54 buy_ready=False sector_rank=6 price=29.95 support=26.01 resistance=32.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=78.7 liquidity=22180794.0 spike=2.32
- DSCW.CA: score=25.9 buy_ready=False sector_rank=16 price=2.05 support=1.76 resistance=2.06 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=75.0 liquidity=64073056.0 spike=0.86
- DTPP.CA: score=25.9 buy_ready=True sector_rank=16 price=246.31 support=193.4 resistance=273.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=64.58 liquidity=19651286.0 spike=0.32
- EALR.CA: score=28.44 buy_ready=True sector_rank=16 price=384.62 support=353.3 resistance=432.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=52.69 liquidity=41969264.0 spike=1.27
- EASB.CA: score=16.68 buy_ready=False sector_rank=16 price=7.21 support=6.71 resistance=8.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=49.78 liquidity=2779279.75 spike=0.23
- EAST.CA: score=19.9 buy_ready=False sector_rank=6 price=36.48 support=36.01 resistance=37.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=47.29 liquidity=71001896.0 spike=0.96
- EBSC.CA: score=18.05 buy_ready=True sector_rank=16 price=1.92 support=1.85 resistance=2.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=52.0 liquidity=2151845.0 spike=0.35
- ECAP.CA: score=28.54 buy_ready=True sector_rank=16 price=34.38 support=32.12 resistance=34.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=66.67 liquidity=9459406.0 spike=1.59
- EDFM.CA: score=19.18 buy_ready=False sector_rank=16 price=397.17 support=325.59 resistance=430.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=70.67 liquidity=1281299.75 spike=0.23
- EEII.CA: score=24.82 buy_ready=False sector_rank=16 price=2.7 support=2.54 resistance=2.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=44.64 liquidity=23102042.0 spike=1.46
- EFIC.CA: score=13.54 buy_ready=False sector_rank=17 price=202.21 support=192.89 resistance=209.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=46406088.0 spike=2.48
- EFID.CA: score=32.02 buy_ready=True sector_rank=6 price=30.79 support=26.64 resistance=31.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=65.92 liquidity=194921456.0 spike=3.06
- EFIH.CA: score=29.56 buy_ready=False sector_rank=5 price=23.86 support=21.87 resistance=24.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=74.26 liquidity=154097360.0 spike=1.83
- EGAL.CA: score=20.58 buy_ready=False sector_rank=17 price=296.51 support=290.0 resistance=312.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=44.09 liquidity=40150620.0 spike=0.94
- EGAS.CA: score=25.9 buy_ready=False sector_rank=4 price=58.7 support=48.5 resistance=67.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=70.27 liquidity=17988666.0 spike=0.72
- EGBE.CA: score=14.85 buy_ready=False sector_rank=14 price=0.49 support=-0.34 resistance=0.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=69.23 liquidity=114637.8 spike=1.42
- EGCH.CA: score=29.04 buy_ready=True sector_rank=17 price=14.11 support=12.65 resistance=14.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=65.65 liquidity=165826816.0 spike=1.73
- EGSA.CA: score=11.71 buy_ready=False sector_rank=15 price=8.8 support=8.75 resistance=9.21 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=36.07 liquidity=27958.55 spike=1.39
- EGTS.CA: score=20.17 buy_ready=False sector_rank=18 price=17.84 support=17.11 resistance=19.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=39.29 liquidity=16899694.0 spike=0.42
- EHDR.CA: score=25.9 buy_ready=True sector_rank=16 price=2.85 support=2.56 resistance=3.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=54.55 liquidity=28713670.0 spike=0.68
- EKHO.CA: score=9.9 buy_ready=False sector_rank=4 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-08-03T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=23.9 buy_ready=False sector_rank=3 price=2.18 support=2.08 resistance=2.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=55.56 liquidity=49061992.0 spike=0.64
- ELKA.CA: score=25.16 buy_ready=False sector_rank=16 price=1.75 support=1.38 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=48.98 liquidity=124633272.0 spike=1.63
- ELNA.CA: score=5.37 buy_ready=False sector_rank=16 price=37.42 support=36.5 resistance=40.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=29.59 liquidity=473736.38 spike=0.68
- ELSH.CA: score=23.9 buy_ready=False sector_rank=16 price=13.88 support=13.13 resistance=15.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=45.74 liquidity=46637168.0 spike=0.37
- ELWA.CA: score=7.08 buy_ready=False sector_rank=16 price=1.67 support=1.7 resistance=2.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=5.41 liquidity=1183676.88 spike=0.78
- EMFD.CA: score=15.17 buy_ready=False sector_rank=18 price=12.1 support=11.51 resistance=12.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=279353760.0 spike=5.37
- ENGC.CA: score=30.38 buy_ready=True sector_rank=16 price=47.06 support=37.0 resistance=46.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=63.36 liquidity=40201328.0 spike=1.24
- EOSB.CA: score=21.72 buy_ready=False sector_rank=16 price=1.55 support=1.51 resistance=1.62 source=Yahoo Finance as_of=2026-08-03T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=101779.2 spike=1.86
- EPCO.CA: score=26.5 buy_ready=True sector_rank=16 price=11.15 support=8.9 resistance=11.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=64.0 liquidity=8598550.0 spike=0.27
- EPPK.CA: score=14.25 buy_ready=False sector_rank=16 price=14.62 support=13.64 resistance=15.93 source=Yahoo Finance as_of=2026-08-03T21:00:00+00:00 freshness=FRESH RSI=55.56 liquidity=354535.0 spike=0.43
- ETEL.CA: score=27.74 buy_ready=True sector_rank=15 price=110.0 support=94.9 resistance=114.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=68.06 liquidity=192562416.0 spike=1.92
- ETRS.CA: score=25.9 buy_ready=True sector_rank=16 price=10.53 support=10.21 resistance=10.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=49.18 liquidity=12106564.0 spike=0.39
- EXPA.CA: score=24.12 buy_ready=False sector_rank=14 price=20.58 support=18.34 resistance=20.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=87.1 liquidity=55750628.0 spike=1.61
- FAIT.CA: score=22.49 buy_ready=True sector_rank=14 price=37.46 support=36.1 resistance=38.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=51.84 liquidity=4833753.5 spike=1.88
- FAITA.CA: score=13.12 buy_ready=False sector_rank=14 price=0.98 support=0.96 resistance=0.99 source=Yahoo Finance as_of=2026-08-03T21:00:00+00:00 freshness=FRESH RSI=46.59 liquidity=43053.48 spike=1.09
- FERC.CA: score=23.34 buy_ready=True sector_rank=17 price=77.07 support=74.26 resistance=85.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=49.48 liquidity=8764805.0 spike=0.7
- FWRY.CA: score=31.38 buy_ready=True sector_rank=5 price=19.54 support=18.43 resistance=19.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=54.09 liquidity=290182208.0 spike=2.74
- GBCO.CA: score=27.9 buy_ready=True sector_rank=2 price=31.49 support=29.53 resistance=34.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=50.63 liquidity=39949808.0 spike=0.61
- GDWA.CA: score=22.9 buy_ready=False sector_rank=16 price=0.82 support=0.77 resistance=0.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=42.66 liquidity=62466060.0 spike=0.55
- GGCC.CA: score=12.7 buy_ready=False sector_rank=16 price=1.13 support=0.99 resistance=1.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=75832856.0 spike=1.9
- GIHD.CA: score=25.9 buy_ready=True sector_rank=16 price=59.65 support=43.0 resistance=65.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=69.87 liquidity=11737598.0 spike=0.21
- GMCI.CA: score=14.35 buy_ready=False sector_rank=16 price=1.97 support=1.9 resistance=2.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=49.21 liquidity=452688.69 spike=0.41
- GRCA.CA: score=23.32 buy_ready=True sector_rank=16 price=58.13 support=48.0 resistance=68.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=57.86 liquidity=7422019.5 spike=0.41
- GSSC.CA: score=23.58 buy_ready=True sector_rank=16 price=281.22 support=248.0 resistance=300.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=67.41 liquidity=7677547.0 spike=0.42
- GTWL.CA: score=18.9 buy_ready=False sector_rank=16 price=98.93 support=82.2 resistance=118.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=31.06 liquidity=41496592.0 spike=0.35
- HDBK.CA: score=18.9 buy_ready=False sector_rank=14 price=84.39 support=76.9 resistance=85.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=75.68 liquidity=12686790.0 spike=0.3
- HELI.CA: score=23.17 buy_ready=False sector_rank=18 price=8.27 support=6.66 resistance=8.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=73.0 liquidity=128374248.0 spike=0.61
- HRHO.CA: score=32.9 buy_ready=True sector_rank=11 price=27.91 support=25.95 resistance=27.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=68.15 liquidity=347876512.0 spike=4.24
- ICID.CA: score=20.56 buy_ready=True sector_rank=16 price=8.09 support=7.51 resistance=8.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=48.11 liquidity=4656066.0 spike=0.65
- IDRE.CA: score=28.42 buy_ready=True sector_rank=16 price=51.83 support=42.5 resistance=52.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=67.18 liquidity=34542176.0 spike=1.26
- IFAP.CA: score=15.9 buy_ready=False sector_rank=10 price=21.23 support=20.27 resistance=21.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=82978184.0 spike=5.76
- INFI.CA: score=22.9 buy_ready=False sector_rank=16 price=120.31 support=93.52 resistance=124.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=81.18 liquidity=26400022.0 spike=0.97
- IRON.CA: score=30.56 buy_ready=True sector_rank=17 price=34.21 support=30.14 resistance=32.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=58.82 liquidity=17736570.0 spike=2.49
- ISMA.CA: score=22.9 buy_ready=False sector_rank=16 price=31.2 support=26.54 resistance=32.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=77.55 liquidity=10601964.0 spike=0.43
- ISMQ.CA: score=23.58 buy_ready=False sector_rank=17 price=9.17 support=8.96 resistance=10.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=42.77 liquidity=43622044.0 spike=0.59
- ISPH.CA: score=30.12 buy_ready=False sector_rank=1 price=13.13 support=11.2 resistance=16.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=73.07 liquidity=216224272.0 spike=1.61
- JUFO.CA: score=25.86 buy_ready=False sector_rank=6 price=33.66 support=28.48 resistance=36.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=75.23 liquidity=70381136.0 spike=1.48
- KABO.CA: score=25.9 buy_ready=True sector_rank=13 price=8.19 support=6.97 resistance=8.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=61.45 liquidity=18399610.0 spike=0.42
- KWIN.CA: score=27.9 buy_ready=True sector_rank=16 price=89.8 support=66.1 resistance=111.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=64.8 liquidity=33850916.0 spike=0.58
- KZPC.CA: score=30.9 buy_ready=False sector_rank=16 price=9.05 support=8.36 resistance=8.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=53.73 liquidity=22209412.0 spike=4.24
- LCSW.CA: score=25.9 buy_ready=True sector_rank=8 price=34.79 support=29.65 resistance=37.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=65.23 liquidity=21483628.0 spike=0.34
- LUTS.CA: score=15.9 buy_ready=False sector_rank=16 price=0.75 support=0.65 resistance=0.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=174275040.0 spike=5.15
- MAAL.CA: score=20.92 buy_ready=True sector_rank=16 price=8.74 support=7.62 resistance=9.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=58.62 liquidity=5023595.5 spike=0.32
- MASR.CA: score=23.9 buy_ready=False sector_rank=16 price=7.99 support=7.4 resistance=8.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=42.0 liquidity=33014816.0 spike=0.43
- MBSC.CA: score=28.18 buy_ready=True sector_rank=8 price=253.22 support=231.51 resistance=249.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=66.0 liquidity=40269840.0 spike=2.14
- MCQE.CA: score=29.88 buy_ready=True sector_rank=8 price=189.0 support=175.01 resistance=195.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=61.1 liquidity=34192848.0 spike=1.99
- MCRO.CA: score=25.9 buy_ready=True sector_rank=16 price=1.49 support=1.23 resistance=1.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=66.0 liquidity=117705128.0 spike=0.7
- MENA.CA: score=13.69 buy_ready=False sector_rank=18 price=6.93 support=6.83 resistance=7.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=43.37 liquidity=522409.75 spike=0.09
- MEPA.CA: score=27.9 buy_ready=True sector_rank=16 price=1.85 support=1.62 resistance=2.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=63.64 liquidity=15574555.0 spike=0.26
- MFPC.CA: score=22.58 buy_ready=False sector_rank=17 price=36.97 support=35.37 resistance=38.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=37.46 liquidity=53708476.0 spike=0.6
- MFSC.CA: score=31.08 buy_ready=True sector_rank=16 price=51.58 support=45.05 resistance=65.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=58.26 liquidity=27557238.0 spike=2.59
- MHOT.CA: score=20.03 buy_ready=False sector_rank=19 price=16.91 support=16.2 resistance=18.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=59.75 liquidity=7400864.0 spike=0.65
- MICH.CA: score=26.36 buy_ready=False sector_rank=16 price=50.04 support=37.46 resistance=53.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=84.43 liquidity=52308984.0 spike=1.73
- MILS.CA: score=27.74 buy_ready=True sector_rank=16 price=201.24 support=129.03 resistance=211.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=66.38 liquidity=107656976.0 spike=1.92
- MIPH.CA: score=20.5 buy_ready=True sector_rank=1 price=794.0 support=673.0 resistance=831.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=66.88 liquidity=1604038.5 spike=0.32
- MOED.CA: score=14.9 buy_ready=False sector_rank=16 price=0.67 support=0.65 resistance=0.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=18.18 liquidity=20060280.0 spike=0.7
- MOIL.CA: score=13.08 buy_ready=False sector_rank=4 price=0.67 support=0.51 resistance=0.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=90.48 liquidity=184058.45 spike=0.27
- MOIN.CA: score=15.9 buy_ready=False sector_rank=16 price=35.0 support=30.4 resistance=36.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=167193888.0 spike=52.11
- MOSC.CA: score=21.49 buy_ready=True sector_rank=16 price=292.62 support=268.5 resistance=329.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=69.85 liquidity=5594077.5 spike=0.36
- MPCI.CA: score=22.9 buy_ready=False sector_rank=16 price=317.31 support=237.12 resistance=339.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=75.8 liquidity=83169672.0 spike=0.7
- MPCO.CA: score=27.9 buy_ready=True sector_rank=10 price=1.94 support=1.77 resistance=2.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=53.49 liquidity=47903180.0 spike=0.54
- MPRC.CA: score=21.27 buy_ready=True sector_rank=16 price=45.1 support=38.51 resistance=47.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=63.12 liquidity=5374019.5 spike=0.18
- MTIE.CA: score=31.9 buy_ready=False sector_rank=2 price=10.71 support=9.09 resistance=10.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=76.77 liquidity=101795112.0 spike=3.61
- NAHO.CA: score=11.9 buy_ready=False sector_rank=16 price=0.1 support=0.1 resistance=0.1 source=Yahoo Finance as_of=2026-08-03T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=1857.3 spike=0.08
- NCCW.CA: score=27.42 buy_ready=True sector_rank=16 price=7.2 support=6.01 resistance=7.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=68.07 liquidity=53075124.0 spike=1.76
- NEDA.CA: score=11.49 buy_ready=False sector_rank=16 price=2.71 support=2.7 resistance=3.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=41.67 liquidity=588282.38 spike=0.73
- NHPS.CA: score=25.9 buy_ready=True sector_rank=16 price=83.9 support=70.01 resistance=95.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=50.45 liquidity=25154516.0 spike=0.31
- NINH.CA: score=25.9 buy_ready=False sector_rank=16 price=23.63 support=17.4 resistance=25.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=70.38 liquidity=14761049.0 spike=0.26
- NIPH.CA: score=25.9 buy_ready=False sector_rank=1 price=271.21 support=173.5 resistance=290.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=76.87 liquidity=159328432.0 spike=0.85
- OBRI.CA: score=14.9 buy_ready=False sector_rank=16 price=32.18 support=31.61 resistance=38.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=19.86 liquidity=18730384.0 spike=0.51
- OCDI.CA: score=10.31 buy_ready=False sector_rank=18 price=30.5 support=29.05 resistance=30.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=111809776.0 spike=1.07
- OCPH.CA: score=22.9 buy_ready=False sector_rank=16 price=480.0 support=350.6 resistance=504.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=77.67 liquidity=12001892.0 spike=0.41
- ODIN.CA: score=24.9 buy_ready=False sector_rank=16 price=2.94 support=2.28 resistance=3.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=85.33 liquidity=18738070.0 spike=0.82
- OFH.CA: score=12.38 buy_ready=False sector_rank=16 price=0.8 support=0.76 resistance=0.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=127210248.0 spike=1.74
- OIH.CA: score=28.88 buy_ready=False sector_rank=7 price=1.56 support=1.4 resistance=1.53 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=75.0 liquidity=128220392.0 spike=1.49
- OLFI.CA: score=27.9 buy_ready=False sector_rank=6 price=24.77 support=22.25 resistance=26.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=72.32 liquidity=31054450.0 spike=0.73
- ORAS.CA: score=9.1 buy_ready=False sector_rank=20 price=724.28 support=695.2 resistance=725.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=113009744.0 spike=1.0
- ORHD.CA: score=27.49 buy_ready=True sector_rank=18 price=42.2 support=38.0 resistance=44.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=65.93 liquidity=195200080.0 spike=1.16
- ORWE.CA: score=15.9 buy_ready=False sector_rank=13 price=26.31 support=24.47 resistance=26.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=425940704.0 spike=11.67
- PHAR.CA: score=30.72 buy_ready=False sector_rank=1 price=130.27 support=85.4 resistance=156.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=79.08 liquidity=679587904.0 spike=3.41
- PHDC.CA: score=30.49 buy_ready=True sector_rank=18 price=15.44 support=14.32 resistance=15.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=59.86 liquidity=388923744.0 spike=1.66
- PHTV.CA: score=16.3 buy_ready=False sector_rank=16 price=343.0 support=262.5 resistance=330.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=82.64 liquidity=3400085.0 spike=0.72
- POUL.CA: score=23.9 buy_ready=False sector_rank=6 price=38.14 support=36.5 resistance=41.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=42.51 liquidity=32460040.0 spike=0.96
- PRCL.CA: score=23.9 buy_ready=False sector_rank=8 price=35.61 support=32.76 resistance=38.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=61.13 liquidity=23603142.0 spike=0.55
- PRDC.CA: score=23.17 buy_ready=False sector_rank=18 price=9.2 support=8.18 resistance=10.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=54.48 liquidity=83219264.0 spike=0.73
- PRMH.CA: score=25.9 buy_ready=True sector_rank=16 price=2.8 support=2.52 resistance=2.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=52.27 liquidity=10903927.0 spike=0.65
- RACC.CA: score=23.9 buy_ready=False sector_rank=16 price=10.11 support=9.8 resistance=10.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=46.67 liquidity=16444900.0 spike=0.7
- RAKT.CA: score=12.13 buy_ready=False sector_rank=16 price=22.96 support=21.25 resistance=23.7 source=Yahoo Finance as_of=2026-08-03T21:00:00+00:00 freshness=FRESH RSI=76.43 liquidity=233686.87 spike=0.73
- RAYA.CA: score=13.45 buy_ready=False sector_rank=21 price=7.48 support=7.3 resistance=8.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=31.45 liquidity=71594320.0 spike=0.61
- RMDA.CA: score=29.56 buy_ready=True sector_rank=1 price=5.83 support=4.94 resistance=6.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=69.81 liquidity=107852672.0 spike=1.33
- ROTO.CA: score=27.9 buy_ready=True sector_rank=16 price=45.52 support=40.5 resistance=46.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=67.0 liquidity=12999227.0 spike=0.63
- RREI.CA: score=27.9 buy_ready=True sector_rank=16 price=4.6 support=3.56 resistance=4.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=63.45 liquidity=50395220.0 spike=0.75
- RTVC.CA: score=19.28 buy_ready=False sector_rank=16 price=3.84 support=3.7 resistance=4.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=49.15 liquidity=7439065.5 spike=1.47
- RUBX.CA: score=18.9 buy_ready=False sector_rank=16 price=12.57 support=12.02 resistance=14.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=28.95 liquidity=12348067.0 spike=0.3
- SAUD.CA: score=29.96 buy_ready=True sector_rank=14 price=22.76 support=21.03 resistance=22.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=54.51 liquidity=35438012.0 spike=3.03
- SCEM.CA: score=27.08 buy_ready=False sector_rank=8 price=81.0 support=61.28 resistance=87.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=71.43 liquidity=147902320.0 spike=1.59
- SCFM.CA: score=27.9 buy_ready=True sector_rank=16 price=280.12 support=243.0 resistance=325.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=57.58 liquidity=22100780.0 spike=0.78
- SCTS.CA: score=12.88 buy_ready=False sector_rank=12 price=604.41 support=602.0 resistance=648.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=45.01 liquidity=1977629.63 spike=0.41
- SDTI.CA: score=13.9 buy_ready=False sector_rank=16 price=68.3 support=63.0 resistance=71.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=59145276.0 spike=2.5
- SEIG.CA: score=21.49 buy_ready=True sector_rank=16 price=263.55 support=188.19 resistance=295.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=61.25 liquidity=3590982.25 spike=0.12
- SIPC.CA: score=22.9 buy_ready=False sector_rank=16 price=4.8 support=3.42 resistance=5.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=83.84 liquidity=42719448.0 spike=0.88
- SKPC.CA: score=25.28 buy_ready=False sector_rank=17 price=16.22 support=14.8 resistance=16.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=39.61 liquidity=75228496.0 spike=1.85
- SMFR.CA: score=26.94 buy_ready=True sector_rank=16 price=235.04 support=202.0 resistance=277.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=36.35 liquidity=35198364.0 spike=1.52
- SNFC.CA: score=14.13 buy_ready=False sector_rank=16 price=10.92 support=10.7 resistance=12.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=16.1 liquidity=8233188.0 spike=0.71
- SPIN.CA: score=26.59 buy_ready=True sector_rank=13 price=15.55 support=14.49 resistance=17.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=64.92 liquidity=8691927.0 spike=0.33
- SPMD.CA: score=27.9 buy_ready=True sector_rank=16 price=0.47 support=0.43 resistance=0.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=64.41 liquidity=13911384.0 spike=0.41
- SUGR.CA: score=26.92 buy_ready=False sector_rank=6 price=47.57 support=46.47 resistance=49.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=60.77 liquidity=12258809.0 spike=1.51
- SVCE.CA: score=25.9 buy_ready=True sector_rank=16 price=9.36 support=9.06 resistance=9.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=42.42 liquidity=35178096.0 spike=1.0
- SWDY.CA: score=28.5 buy_ready=False sector_rank=3 price=104.48 support=87.41 resistance=114.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=85.7 liquidity=101615096.0 spike=2.3
- TALM.CA: score=22.9 buy_ready=False sector_rank=12 price=18.19 support=15.27 resistance=19.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=75.77 liquidity=30481992.0 spike=0.74
- TMGH.CA: score=23.17 buy_ready=False sector_rank=18 price=99.0 support=95.2 resistance=103.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=55.31 liquidity=191630496.0 spike=0.54
- TRTO.CA: score=11.9 buy_ready=False sector_rank=16 price=0.03 support=0.03 resistance=0.04 source=Yahoo Finance as_of=2026-08-03T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=750.86 spike=0.48
- UEFM.CA: score=18.6 buy_ready=True sector_rank=16 price=549.32 support=479.0 resistance=625.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=63.26 liquidity=2696607.75 spike=0.51
- UEGC.CA: score=27.9 buy_ready=False sector_rank=16 price=2.69 support=1.58 resistance=2.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=70.77 liquidity=39070216.0 spike=0.71
- UNIP.CA: score=25.9 buy_ready=True sector_rank=16 price=0.39 support=0.32 resistance=0.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=61.78 liquidity=10251223.0 spike=0.36
- UNIT.CA: score=14.96 buy_ready=False sector_rank=18 price=18.12 support=16.52 resistance=21.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=34.33 liquidity=6792683.5 spike=0.23
- WCDF.CA: score=20.6 buy_ready=True sector_rank=16 price=587.45 support=505.0 resistance=634.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=64.76 liquidity=2700259.0 spike=0.73
- WKOL.CA: score=29.08 buy_ready=True sector_rank=16 price=327.36 support=295.51 resistance=363.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=54.67 liquidity=35192208.0 spike=1.59
- ZEOT.CA: score=24.9 buy_ready=False sector_rank=16 price=12.71 support=10.91 resistance=13.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=81.14 liquidity=24126960.0 spike=0.79
- ZMID.CA: score=23.17 buy_ready=False sector_rank=18 price=7.21 support=6.63 resistance=7.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=50.32 liquidity=179595920.0 spike=0.65

## Backtesting Lite
- HRHO.CA: 180d return=1.14%, max drawdown=-18.92%, MA20>MA50 days last20=4, as_of=2026-08-03T21:00:00+00:00
- EFID.CA: 180d return=31.61%, max drawdown=-22.2%, MA20>MA50 days last20=0, as_of=2026-08-03T21:00:00+00:00
- MTIE.CA: 180d return=42.66%, max drawdown=-20.49%, MA20>MA50 days last20=20, as_of=2026-08-03T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- HRHO.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=EFG Holding summary=Evidence rejected for HRHO.CA: source text did not clearly match HRHO.CA / EFG Holding.
- EFID.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Edita Food Industries summary=Evidence rejected for EFID.CA: source text did not clearly match EFID.CA / Edita Food Industries.
- MTIE.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=MM Group For Industry and International Trade summary=Evidence rejected for MTIE.CA: source text did not clearly match MTIE.CA / MM Group For Industry and International Trade.
- ALUM.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Arab Aluminum Company (S.A.E) summary=Arab Aluminum’s stock holds steady as bullish pattern breaks; Arab Aluminum profits rise 7% in H1-17; Arab Aluminum OGM approves EGP 1/shr dividends
  - Arab Aluminum’s stock holds steady as bullish pattern breaks: https://english.mubasher.info/news/4564438/Arab-Aluminum-s-stock-holds-steady-as-bullish-pattern-breaks/
  - Arab Aluminum profits rise 7% in H1-17: https://english.mubasher.info/news/3144589/Arab-Aluminum-profits-rise-7-in-H1-17/
  - Arab Aluminum OGM approves EGP 1/shr dividends: https://english.mubasher.info/news/3076498/Arab-Aluminum-OGM-approves-EGP-1-shr-dividends/
- FWRY.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Fawry For Banking Technology and Electronic Payments summary=Evidence rejected for FWRY.CA: source text did not clearly match FWRY.CA / Fawry For Banking Technology and Electronic Payments.
- MFSC.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Egypt Free Shops Co. summary=Egypt Duty Free Shops posts lower consolidated net profits at nearly EGP 88m in Q1-25/26; Egypt Free Shops achieves higher profits in Q1-FY22/23; Egypt Free Shops’ earnings soar 26% in FY21/22
  - Egypt Duty Free Shops posts lower consolidated net profits at nearly EGP 88m in Q1-25/26: https://english.mubasher.info/news/4530712/Egypt-Duty-Free-Shops-posts-lower-consolidated-net-profits-at-nearly-EGP-88m-in-Q1-25-26/
  - Egypt Free Shops achieves higher profits in Q1-FY22/23: https://english.mubasher.info/news/4042863/Egypt-Free-Shops-achieves-higher-profits-in-Q1-FY22-23/
  - Egypt Free Shops’ earnings soar 26% in FY21/22: https://english.mubasher.info/news/3993622/Egypt-Free-Shops-earnings-soar-26-in-FY21-22/
- KZPC.CA: status=OLD_ACCEPTED latest=2024-01-01 age_days=947 sources=3 expected=Kafr El Zayat For Pesticides & Chemicals Co.(S.A.E) summary=Kafr El Zayat to set up fund with EGP 5m capital; Kafr El Zayat Pesticides targets EGP 1.73bn sales in 2024; Kafr El Zayat Pesticides’ EGM approves stock split, capital hike
  - Kafr El Zayat to set up fund with EGP 5m capital: https://english.mubasher.info/news/4201137/Kafr-El-Zayat-to-set-up-fund-with-EGP-5m-capital/
  - Kafr El Zayat Pesticides targets EGP 1.73bn sales in 2024: https://english.mubasher.info/news/4200526/Kafr-El-Zayat-Pesticides-targets-EGP-1-73bn-sales-in-2024/
  - Kafr El Zayat Pesticides’ EGM approves stock split, capital hike: https://english.mubasher.info/news/4052937/Kafr-El-Zayat-Pesticides-EGM-approves-stock-split-capital-hike/
- PHAR.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Egyptian International Pharmaceutical Industries summary=Evidence rejected for PHAR.CA: source text did not clearly match PHAR.CA / Egyptian International Pharmaceutical Industries.

## Warnings
- Evidence rejected for HRHO.CA: source text did not clearly match HRHO.CA / EFG Holding.
- Gemini batch evidence failed: 'NoneType' object has no attribute 'strip'
- Evidence rejected for EFID.CA: source text did not clearly match EFID.CA / Edita Food Industries.
- Evidence rejected for MTIE.CA: source text did not clearly match MTIE.CA / MM Group For Industry and International Trade.
- Evidence for ALUM.CA matches the company but no source/report date was detected.
- Evidence rejected for FWRY.CA: source text did not clearly match FWRY.CA / Fawry For Banking Technology and Electronic Payments.
- Evidence for MFSC.CA matches the company but no source/report date was detected.
- Evidence for KZPC.CA matches the company but appears old; latest detected date is 2024-01-01.
- Evidence rejected for PHAR.CA: source text did not clearly match PHAR.CA / Egyptian International Pharmaceutical Industries.
