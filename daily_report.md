# Telegram-First EGX Scanner Report

Scan phase: Intraday liquidity update
Generated UTC: 2026-08-10T09:18:31.661822+00:00
Generated Cairo: 2026-08-10 12:18
Run timing: target 11:00 Cairo | generated Cairo 2026-08-10 12:18 | cron 0 8 * * 0-4
Trigger: scheduled cron=0 8 * * 0-4 mapped to intraday; Cairo now 2026-08-10 12:13

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 67
- Data quality issues: 1
- Tradeable price/liquidity tickers: 150/189
- Top sector: Industrial Goods & Cables

## Market Context
- Market trend: Bearish
- Source: Mubasher EGX market page (delayed public data)
- As of: Monday, August 10
- Freshness: DELAYED
- EGX30 regime: BULLISH / above MA20 80.0% / above MA50 80.0%
- EGX70 regime: BULLISH / above MA20 81.82% / above MA50 93.94%
- Sector breadth: 57.14%
- Risk mode: BROAD_RISK_ON

## Top Liquidity
- PHAR.CA: liquidity=852238400.0 spike=3.15 score=14.9
- BIOC.CA: liquidity=407761152.0 spike=2.45 score=13.22
- NIPH.CA: liquidity=296721120.0 spike=1.41 score=11.42
- GTWL.CA: liquidity=282572512.0 spike=2.89 score=14.1
- INFI.CA: liquidity=245884832.0 spike=5.77 score=15.32

## AI Narrative
- Provider: OpenRouter OK
- Model: nvidia/nemotron-3-super-120b-a12b:free
- Summary: We need to produce a concise Telegram narrative for a personal EGX stock scanner. Must not make a new trade decision, not invent live data, not mention quantities or position sizing. Explain why the local scanner selected these prioritized tickets, what liquidity/sector/support/resistance/outlook means for next 1-3 days, and how the EGX30/EGX70 market regime changes risk mode, and include uncertainty. Return only valid compact JSON with keys summary and bullets, where bullets is 3 to 5 short strings.

We must not include any extra text outside JSON. The JSON must be compact (no extra whitespace? but can be normal). Provide summary string and bullets array of 3-5 short strings.

We need to ba
- Liquidity spikes in ATQA.CA and ALUM.CA suggest short‑term accumulation but evidence is weak.
- Sector strength in Industrial Goods & Cables and Transportation & Logistics supports bullish outlook, yet many tickets show extended momentum and cooling liquidity.
- EGX30 and EGX70 both bullish with >80% above MA20, shifting risk mode to BROAD_RISK_ON, increasing uncertainty for next 1‑3 days.
- Support/resistance distances indicate most stocks are near resistance, limiting upside in the near term.
- Overall uncertainty remains high due to mixed evidence and extended RSI readings.

## Top Liquidity Spikes
- FERC.CA: spike=6.56 liquidity=92590648.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- INFI.CA: spike=5.77 liquidity=245884832.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- ATQA.CA: spike=4.63 liquidity=180858064.0 outlook=BULLISH_WATCH score=74.77 buy_ready=True
- EEII.CA: spike=4.43 liquidity=62404428.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- DAPH.CA: spike=4.1 liquidity=103817752.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False

## Sector Leaderboard
- #1 Industrial Goods & Cables: score=11.81 5d=6.27% 20d=11.77% aboveMA50=100.0%
- #2 Automotive & Distribution: score=11.49 5d=7.65% 20d=8.35% aboveMA50=100.0%
- #3 Transportation & Logistics: score=11.01 5d=5.12% 20d=9.89% aboveMA50=100.0%
- #4 Textiles: score=8.4 5d=2.73% 20d=11.29% aboveMA50=75.0%
- #5 Non-bank Financial Services: score=8.23 5d=2.46% 20d=3.59% aboveMA50=100.0%
- #6 Food, Beverages & Tobacco: score=8.17 5d=7.42% 20d=1.79% aboveMA50=71.43%
- #7 Fintech & Payments: score=7.99 5d=1.88% 20d=2.62% aboveMA50=100.0%
- #8 Energy & Petrochemicals: score=7.85 5d=-0.93% 20d=17.59% aboveMA50=75.0%

## Today's Prioritized Action Tickets
- HOLD: Local fallback HOLD: no candidate passed evidence, liquidity, freshness, and technical gates.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- CSAG.CA: BULLISH_WATCH score=85 liquidity=TRADEABLE sector=LEADING risk=momentum is extended; far above support
- POUL.CA: BULLISH_WATCH score=84.17 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- ATLC.CA: BULLISH_WATCH score=83.23 liquidity=TRADEABLE sector=IMPROVING risk=No major short-term scanner risk flags.
- MFSC.CA: BULLISH_WATCH score=80.56 liquidity=TRADEABLE sector=IMPROVING risk=sector is not leading
- CNFN.CA: BULLISH_WATCH score=80.23 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; close to resistance
- HRHO.CA: BULLISH_WATCH score=78.23 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- BTFH.CA: BULLISH_WATCH score=78.23 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- FWRY.CA: BULLISH_WATCH score=77.99 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- ISMQ.CA: BULLISH_WATCH score=77.77 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; sector is not leading
- IRON.CA: BULLISH_WATCH score=77.77 liquidity=TRADEABLE sector=IMPROVING risk=sector is not leading

## BUY-Ready Candidates
- ATQA.CA: rank=30.9 outlook=BULLISH_WATCH outlook_score=74.77 sector_rank=9 price=10.6 support=9.43 resistance=10.37 liquidity=180858064.0
- CNFN.CA: rank=29.9 outlook=BULLISH_WATCH outlook_score=80.23 sector_rank=5 price=4.99 support=4.68 resistance=5.05 liquidity=13507000.0
- ALUM.CA: rank=29.14 outlook=BULLISH_WATCH outlook_score=72.56 sector_rank=16 price=25.47 support=22.41 resistance=25.15 liquidity=13905747.0
- CSAG.CA: rank=28.98 outlook=BULLISH_WATCH outlook_score=85 sector_rank=3 price=38.39 support=31.35 resistance=37.2 liquidity=21672154.0
- HRHO.CA: rank=27.9 outlook=BULLISH_WATCH outlook_score=78.23 sector_rank=5 price=27.52 support=25.95 resistance=28.1 liquidity=33133458.0
- EFIH.CA: rank=27.9 outlook=CONSTRUCTIVE outlook_score=69.99 sector_rank=7 price=23.9 support=21.87 resistance=25.0 liquidity=41372080.0
- FWRY.CA: rank=27.9 outlook=BULLISH_WATCH outlook_score=77.99 sector_rank=7 price=19.15 support=18.43 resistance=19.81 liquidity=56807124.0
- ABUK.CA: rank=27.9 outlook=BULLISH_WATCH outlook_score=71.77 sector_rank=9 price=73.74 support=69.01 resistance=75.59 liquidity=22352806.0
- EGCH.CA: rank=27.9 outlook=CONSTRUCTIVE outlook_score=62.77 sector_rank=9 price=14.28 support=12.69 resistance=14.62 liquidity=96896440.0
- BTFH.CA: rank=27.9 outlook=BULLISH_WATCH outlook_score=78.23 sector_rank=5 price=3.14 support=3.03 resistance=3.26 liquidity=54316988.0

## Data Quality Issues
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=25.32 buy_ready=True sector_rank=16 price=297.67 support=223.25 resistance=317.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:53 AM market time freshness=DELAYED_CURRENT RSI=69.22 liquidity=24211450.0 spike=0.67
- ABUK.CA: score=27.9 buy_ready=True sector_rank=9 price=73.74 support=69.01 resistance=75.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=48.32 liquidity=22352806.0 spike=0.15
- ACAMD.CA: score=19.32 buy_ready=False sector_rank=16 price=2.29 support=2.3 resistance=2.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:53 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=49301652.0 spike=1.0
- ACGC.CA: score=20.96 buy_ready=False sector_rank=4 price=11.4 support=9.55 resistance=11.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=78.1 liquidity=6063844.0 spike=0.19
- ADCI.CA: score=10.32 buy_ready=False sector_rank=16 price=312.25 support=291.0 resistance=319.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:50 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=18525416.0 spike=0.97
- ADIB.CA: score=22.9 buy_ready=False sector_rank=11 price=53.9 support=46.02 resistance=53.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=83.57 liquidity=18635464.0 spike=0.16
- ADPC.CA: score=10.32 buy_ready=False sector_rank=16 price=4.47 support=4.4 resistance=4.63 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:53 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=45669052.0 spike=0.92
- AFDI.CA: score=14.83 buy_ready=False sector_rank=16 price=60.89 support=46.19 resistance=61.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=79.55 liquidity=2506770.25 spike=0.1
- AFMC.CA: score=22.32 buy_ready=False sector_rank=16 price=228.0 support=72.0 resistance=250.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:53 AM market time freshness=DELAYED_CURRENT RSI=75.31 liquidity=41247456.0 spike=0.3
- AJWA.CA: score=20.36 buy_ready=True sector_rank=16 price=188.03 support=161.0 resistance=210.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:52 AM market time freshness=DELAYED_CURRENT RSI=63.87 liquidity=5039798.5 spike=0.14
- ALCN.CA: score=26.68 buy_ready=True sector_rank=3 price=30.8 support=28.8 resistance=31.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=62.2 liquidity=7784146.0 spike=0.27
- ALUM.CA: score=29.14 buy_ready=True sector_rank=16 price=25.47 support=22.41 resistance=25.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:52 AM market time freshness=DELAYED_CURRENT RSI=63.07 liquidity=13905747.0 spike=1.91
- AMER.CA: score=10.82 buy_ready=False sector_rank=13 price=6.3 support=6.15 resistance=6.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:52 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=42572668.0 spike=0.37
- AMES.CA: score=25.32 buy_ready=True sector_rank=16 price=123.12 support=72.1 resistance=144.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:52 AM market time freshness=DELAYED_CURRENT RSI=47.25 liquidity=14231317.0 spike=0.15
- AMIA.CA: score=21.93 buy_ready=False sector_rank=16 price=12.89 support=8.74 resistance=13.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:50 AM market time freshness=DELAYED_CURRENT RSI=78.49 liquidity=9605012.0 spike=0.58
- AMOC.CA: score=25.9 buy_ready=True sector_rank=8 price=9.11 support=7.95 resistance=9.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=65.29 liquidity=12722932.0 spike=0.13
- APSW.CA: score=12.76 buy_ready=False sector_rank=16 price=8.79 support=8.1 resistance=9.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=49.76 liquidity=439516.22 spike=0.24
- ARAB.CA: score=25.82 buy_ready=True sector_rank=13 price=0.25 support=0.23 resistance=0.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:52 AM market time freshness=DELAYED_CURRENT RSI=46.67 liquidity=63144264.0 spike=0.5
- ARCC.CA: score=9.89 buy_ready=False sector_rank=19 price=63.67 support=63.5 resistance=64.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:52 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=29359252.0 spike=0.82
- AREH.CA: score=22.32 buy_ready=False sector_rank=16 price=1.53 support=1.38 resistance=1.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:53 AM market time freshness=DELAYED_CURRENT RSI=54.9 liquidity=11487002.0 spike=0.29
- ARVA.CA: score=6.32 buy_ready=False sector_rank=16 price=12.35 support=12.35 resistance=12.35 source=Yahoo Finance as_of=2026-08-08T21:00:00+00:00 freshness=FRESH RSI=88.83 liquidity=0.0 spike=0.0
- ASCM.CA: score=25.32 buy_ready=False sector_rank=16 price=66.87 support=58.16 resistance=69.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:53 AM market time freshness=DELAYED_CURRENT RSI=70.12 liquidity=41426324.0 spike=0.65
- ASPI.CA: score=10.32 buy_ready=False sector_rank=16 price=0.5 support=0.49 resistance=0.53 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:53 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=22440836.0 spike=0.53
- ATLC.CA: score=25.9 buy_ready=True sector_rank=5 price=5.47 support=5.0 resistance=5.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=55.91 liquidity=13990785.0 spike=0.98
- ATQA.CA: score=30.9 buy_ready=True sector_rank=9 price=10.6 support=9.43 resistance=10.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:53 AM market time freshness=DELAYED_CURRENT RSI=65.54 liquidity=180858064.0 spike=4.63
- AXPH.CA: score=20.72 buy_ready=True sector_rank=16 price=1298.94 support=1121.56 resistance=1439.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:50 AM market time freshness=DELAYED_CURRENT RSI=58.23 liquidity=3398254.5 spike=0.83
- BINV.CA: score=19.33 buy_ready=True sector_rank=12 price=49.02 support=46.01 resistance=50.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=52.9 liquidity=1430506.63 spike=0.2
- BIOC.CA: score=13.22 buy_ready=False sector_rank=16 price=553.93 support=402.0 resistance=563.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:53 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=407761152.0 spike=2.45
- BTFH.CA: score=27.9 buy_ready=True sector_rank=5 price=3.14 support=3.03 resistance=3.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:52 AM market time freshness=DELAYED_CURRENT RSI=48.84 liquidity=54316988.0 spike=0.24
- CAED.CA: score=20.4 buy_ready=True sector_rank=16 price=120.74 support=73.25 resistance=143.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:52 AM market time freshness=DELAYED_CURRENT RSI=39.52 liquidity=5075853.0 spike=0.07
- CANA.CA: score=10.9 buy_ready=False sector_rank=11 price=41.12 support=40.67 resistance=41.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:52 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=15587709.0 spike=0.8
- CCAP.CA: score=20.9 buy_ready=False sector_rank=12 price=5.21 support=5.14 resistance=5.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:53 AM market time freshness=DELAYED_CURRENT RSI=38.46 liquidity=87764120.0 spike=0.14
- CCRS.CA: score=8.64 buy_ready=False sector_rank=16 price=2.43 support=2.35 resistance=2.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:50 AM market time freshness=DELAYED_CURRENT RSI=34.69 liquidity=3313341.0 spike=0.17
- CEFM.CA: score=20.43 buy_ready=True sector_rank=16 price=135.23 support=101.57 resistance=152.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:50 AM market time freshness=DELAYED_CURRENT RSI=55.81 liquidity=3104821.75 spike=0.1
- CERA.CA: score=16.68 buy_ready=False sector_rank=16 price=1.33 support=1.25 resistance=1.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:52 AM market time freshness=DELAYED_CURRENT RSI=43.48 liquidity=3352689.25 spike=0.15
- CFGH.CA: score=9.32 buy_ready=False sector_rank=16 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance as_of=2026-08-08T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- CICH.CA: score=15.82 buy_ready=False sector_rank=5 price=12.65 support=11.61 resistance=13.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:53 AM market time freshness=DELAYED_CURRENT RSI=78.91 liquidity=2922187.5 spike=0.35
- CIEB.CA: score=22.43 buy_ready=True sector_rank=11 price=24.37 support=23.75 resistance=24.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=59.64 liquidity=2527982.5 spike=0.24
- CIRA.CA: score=10.26 buy_ready=False sector_rank=17 price=39.15 support=38.25 resistance=39.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:52 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=31259592.0 spike=0.53
- CLHO.CA: score=27.6 buy_ready=True sector_rank=14 price=18.1 support=15.98 resistance=19.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=60.09 liquidity=29424588.0 spike=0.6
- CNFN.CA: score=29.9 buy_ready=True sector_rank=5 price=4.99 support=4.68 resistance=5.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:52 AM market time freshness=DELAYED_CURRENT RSI=61.7 liquidity=13507000.0 spike=0.63
- COMI.CA: score=23.9 buy_ready=True sector_rank=11 price=140.26 support=132.81 resistance=142.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=69.99 liquidity=90031640.0 spike=0.22
- COPR.CA: score=25.32 buy_ready=True sector_rank=16 price=0.41 support=0.36 resistance=0.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:52 AM market time freshness=DELAYED_CURRENT RSI=62.86 liquidity=10692096.0 spike=0.33
- COSG.CA: score=25.32 buy_ready=True sector_rank=16 price=1.71 support=1.6 resistance=1.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:53 AM market time freshness=DELAYED_CURRENT RSI=51.52 liquidity=11374093.0 spike=0.29
- CPCI.CA: score=24.34 buy_ready=True sector_rank=16 price=492.83 support=400.0 resistance=520.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:53 AM market time freshness=DELAYED_CURRENT RSI=63.95 liquidity=9019044.0 spike=0.67
- CSAG.CA: score=28.98 buy_ready=True sector_rank=3 price=38.39 support=31.35 resistance=37.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=67.54 liquidity=21672154.0 spike=1.04
- DAPH.CA: score=15.32 buy_ready=False sector_rank=16 price=128.94 support=108.0 resistance=128.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:49 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=103817752.0 spike=4.1
- DEIN.CA: score=0.32 buy_ready=False sector_rank=16 price=11.38 support=13.65 resistance=13.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 June 12:11 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=40.95 spike=0.01
- DOMT.CA: score=21.3 buy_ready=False sector_rank=6 price=28.91 support=26.01 resistance=32.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:48 AM market time freshness=DELAYED_CURRENT RSI=70.35 liquidity=5399576.0 spike=0.49
- DSCW.CA: score=27.32 buy_ready=False sector_rank=16 price=2.09 support=1.77 resistance=2.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:53 AM market time freshness=DELAYED_CURRENT RSI=72.73 liquidity=46114548.0 spike=0.57
- DTPP.CA: score=10.32 buy_ready=False sector_rank=16 price=283.89 support=280.01 resistance=292.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:53 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=49095112.0 spike=0.84
- EALR.CA: score=27.32 buy_ready=True sector_rank=16 price=390.25 support=360.0 resistance=432.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:53 AM market time freshness=DELAYED_CURRENT RSI=55.73 liquidity=13934787.0 spike=0.48
- EASB.CA: score=15.37 buy_ready=False sector_rank=16 price=7.24 support=6.71 resistance=8.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:53 AM market time freshness=DELAYED_CURRENT RSI=48.88 liquidity=2042300.38 spike=0.17
- EAST.CA: score=21.9 buy_ready=False sector_rank=6 price=36.53 support=36.01 resistance=37.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=48.86 liquidity=23890594.0 spike=0.35
- EBSC.CA: score=19.53 buy_ready=False sector_rank=16 price=1.96 support=1.85 resistance=2.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:53 AM market time freshness=DELAYED_CURRENT RSI=72.0 liquidity=2205743.75 spike=0.34
- ECAP.CA: score=19.34 buy_ready=True sector_rank=16 price=34.01 support=32.12 resistance=34.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:48 AM market time freshness=DELAYED_CURRENT RSI=64.84 liquidity=2012170.13 spike=0.33
- EDFM.CA: score=16.02 buy_ready=False sector_rank=16 price=394.91 support=337.96 resistance=430.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=48.98 liquidity=692244.38 spike=0.12
- EEII.CA: score=15.32 buy_ready=False sector_rank=16 price=2.92 support=2.68 resistance=2.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:53 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=62404428.0 spike=4.43
- EFIC.CA: score=27.9 buy_ready=True sector_rank=9 price=210.52 support=181.69 resistance=225.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:52 AM market time freshness=DELAYED_CURRENT RSI=69.15 liquidity=10279722.0 spike=0.41
- EFID.CA: score=24.9 buy_ready=False sector_rank=6 price=30.88 support=26.64 resistance=32.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:52 AM market time freshness=DELAYED_CURRENT RSI=83.88 liquidity=55397072.0 spike=0.66
- EFIH.CA: score=27.9 buy_ready=True sector_rank=7 price=23.9 support=21.87 resistance=25.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=62.61 liquidity=41372080.0 spike=0.46
- EGAL.CA: score=23.02 buy_ready=False sector_rank=9 price=306.04 support=290.0 resistance=312.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=31.1 liquidity=44007604.0 spike=1.06
- EGAS.CA: score=18.8 buy_ready=False sector_rank=8 price=60.32 support=48.95 resistance=67.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:53 AM market time freshness=DELAYED_CURRENT RSI=75.45 liquidity=5903318.5 spike=0.23
- EGBE.CA: score=13.06 buy_ready=False sector_rank=11 price=0.56 support=-0.34 resistance=0.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=81.06 liquidity=117610.2 spike=1.02
- EGCH.CA: score=27.9 buy_ready=True sector_rank=9 price=14.28 support=12.69 resistance=14.62 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:50 AM market time freshness=DELAYED_CURRENT RSI=63.0 liquidity=96896440.0 spike=0.96
- EGSA.CA: score=5.13 buy_ready=False sector_rank=18 price=8.73 support=8.8 resistance=9.21 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=31.58 liquidity=19286.18 spike=0.89
- EGTS.CA: score=24.82 buy_ready=False sector_rank=13 price=18.25 support=17.11 resistance=19.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:52 AM market time freshness=DELAYED_CURRENT RSI=54.09 liquidity=27074732.0 spike=0.74
- EHDR.CA: score=25.32 buy_ready=True sector_rank=16 price=2.93 support=2.64 resistance=3.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:53 AM market time freshness=DELAYED_CURRENT RSI=41.79 liquidity=16704420.0 spike=0.4
- EKHO.CA: score=9.9 buy_ready=False sector_rank=8 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-08-08T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=22.9 buy_ready=False sector_rank=1 price=2.21 support=2.1 resistance=2.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:53 AM market time freshness=DELAYED_CURRENT RSI=26.32 liquidity=52028524.0 spike=0.66
- ELKA.CA: score=18.32 buy_ready=False sector_rank=16 price=1.73 support=1.59 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:53 AM market time freshness=DELAYED_CURRENT RSI=15.87 liquidity=18607242.0 spike=0.22
- ELNA.CA: score=9.32 buy_ready=False sector_rank=16 price=37.44 support=36.5 resistance=40.5 source=Yahoo Finance as_of=2026-08-08T21:00:00+00:00 freshness=FRESH RSI=41.89 liquidity=0.0 spike=0.0
- ELSH.CA: score=23.32 buy_ready=False sector_rank=16 price=14.07 support=13.31 resistance=15.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=48.8 liquidity=11519543.0 spike=0.1
- ELWA.CA: score=5.86 buy_ready=False sector_rank=16 price=1.72 support=1.65 resistance=2.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=8.33 liquidity=531065.69 spike=0.34
- EMFD.CA: score=27.82 buy_ready=True sector_rank=13 price=11.77 support=11.08 resistance=12.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=55.15 liquidity=31071694.0 spike=0.53
- ENGC.CA: score=22.81 buy_ready=True sector_rank=16 price=47.46 support=38.15 resistance=47.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:53 AM market time freshness=DELAYED_CURRENT RSI=65.31 liquidity=7484202.0 spike=0.23
- EOSB.CA: score=19.32 buy_ready=False sector_rank=16 price=1.55 support=1.52 resistance=1.62 source=Yahoo Finance as_of=2026-08-08T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- EPCO.CA: score=12.08 buy_ready=False sector_rank=16 price=12.88 support=11.92 resistance=13.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:53 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=60710440.0 spike=1.88
- EPPK.CA: score=14.17 buy_ready=False sector_rank=16 price=13.83 support=13.87 resistance=15.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:46 AM market time freshness=DELAYED_CURRENT RSI=35.9 liquidity=845710.0 spike=0.98
- ETEL.CA: score=25.11 buy_ready=True sector_rank=18 price=110.15 support=96.0 resistance=114.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=65.27 liquidity=36784088.0 spike=0.37
- ETRS.CA: score=25.32 buy_ready=True sector_rank=16 price=10.66 support=10.21 resistance=10.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:52 AM market time freshness=DELAYED_CURRENT RSI=54.26 liquidity=11976215.0 spike=0.45
- EXPA.CA: score=19.49 buy_ready=False sector_rank=11 price=20.54 support=18.61 resistance=20.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=73.74 liquidity=3593847.25 spike=0.1
- FAIT.CA: score=21.55 buy_ready=True sector_rank=11 price=39.06 support=36.1 resistance=38.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=62.76 liquidity=1646373.25 spike=0.56
- FAITA.CA: score=14.92 buy_ready=False sector_rank=11 price=0.98 support=0.96 resistance=0.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:28 AM market time freshness=DELAYED_CURRENT RSI=56.1 liquidity=18720.68 spike=0.45
- FERC.CA: score=15.9 buy_ready=False sector_rank=9 price=85.29 support=83.1 resistance=87.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:52 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=92590648.0 spike=6.56
- FWRY.CA: score=27.9 buy_ready=True sector_rank=7 price=19.15 support=18.43 resistance=19.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=56.89 liquidity=56807124.0 spike=0.49
- GBCO.CA: score=27.9 buy_ready=True sector_rank=2 price=31.77 support=29.53 resistance=34.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=38.48 liquidity=12701918.0 spike=0.19
- GDWA.CA: score=22.32 buy_ready=False sector_rank=16 price=0.82 support=0.78 resistance=0.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:53 AM market time freshness=DELAYED_CURRENT RSI=41.27 liquidity=18604542.0 spike=0.16
- GGCC.CA: score=10.32 buy_ready=False sector_rank=16 price=1.24 support=1.16 resistance=1.31 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:54 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=32451228.0 spike=0.73
- GIHD.CA: score=19.94 buy_ready=False sector_rank=16 price=60.71 support=47.65 resistance=65.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:54 AM market time freshness=DELAYED_CURRENT RSI=72.14 liquidity=6615009.5 spike=0.12
- GMCI.CA: score=13.32 buy_ready=False sector_rank=16 price=1.98 support=1.91 resistance=2.2 source=Yahoo Finance as_of=2026-08-08T21:00:00+00:00 freshness=FRESH RSI=37.25 liquidity=0.0 spike=0.0
- GRCA.CA: score=23.55 buy_ready=True sector_rank=16 price=59.16 support=48.0 resistance=68.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:54 AM market time freshness=DELAYED_CURRENT RSI=40.29 liquidity=8222017.5 spike=0.45
- GSSC.CA: score=18.96 buy_ready=True sector_rank=16 price=274.03 support=257.0 resistance=300.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:52 AM market time freshness=DELAYED_CURRENT RSI=53.41 liquidity=1638992.88 spike=0.09
- GTWL.CA: score=14.1 buy_ready=False sector_rank=16 price=135.78 support=125.65 resistance=143.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:54 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=282572512.0 spike=2.89
- HDBK.CA: score=20.9 buy_ready=False sector_rank=11 price=85.75 support=76.9 resistance=85.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:50 AM market time freshness=DELAYED_CURRENT RSI=80.83 liquidity=12362970.0 spike=0.32
- HELI.CA: score=25.82 buy_ready=True sector_rank=13 price=8.26 support=7.24 resistance=8.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=58.78 liquidity=30164952.0 spike=0.15
- HRHO.CA: score=27.9 buy_ready=True sector_rank=5 price=27.52 support=25.95 resistance=28.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=60.26 liquidity=33133458.0 spike=0.34
- ICID.CA: score=22.36 buy_ready=True sector_rank=16 price=8.5 support=7.51 resistance=8.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:52 AM market time freshness=DELAYED_CURRENT RSI=50.39 liquidity=7035264.5 spike=0.95
- IDRE.CA: score=10.32 buy_ready=False sector_rank=16 price=57.0 support=55.7 resistance=57.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:54 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=18493276.0 spike=0.6
- IFAP.CA: score=19.96 buy_ready=False sector_rank=10 price=21.06 support=18.96 resistance=21.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:52 AM market time freshness=DELAYED_CURRENT RSI=76.22 liquidity=7062986.0 spike=0.36
- INFI.CA: score=15.32 buy_ready=False sector_rank=16 price=180.01 support=174.0 resistance=192.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:54 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=245884832.0 spike=5.77
- IRON.CA: score=24.54 buy_ready=True sector_rank=9 price=32.23 support=30.14 resistance=34.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:50 AM market time freshness=DELAYED_CURRENT RSI=61.84 liquidity=7643501.5 spike=0.97
- ISMA.CA: score=10.32 buy_ready=False sector_rank=16 price=32.48 support=32.1 resistance=32.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:54 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=21869098.0 spike=0.91
- ISMQ.CA: score=25.9 buy_ready=True sector_rank=9 price=9.44 support=8.96 resistance=9.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:53 AM market time freshness=DELAYED_CURRENT RSI=46.27 liquidity=33673676.0 spike=0.51
- ISPH.CA: score=11.18 buy_ready=False sector_rank=14 price=14.3 support=13.5 resistance=14.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:52 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=195235136.0 spike=1.29
- JUFO.CA: score=21.9 buy_ready=False sector_rank=6 price=26.68 support=22.78 resistance=31.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:52 AM market time freshness=DELAYED_CURRENT RSI=38.53 liquidity=15249138.0 spike=0.3
- KABO.CA: score=10.9 buy_ready=False sector_rank=4 price=8.6 support=8.57 resistance=8.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:52 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=31278596.0 spike=0.82
- KWIN.CA: score=25.32 buy_ready=True sector_rank=16 price=89.67 support=67.32 resistance=111.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:54 AM market time freshness=DELAYED_CURRENT RSI=58.3 liquidity=11098816.0 spike=0.19
- KZPC.CA: score=12.37 buy_ready=False sector_rank=16 price=8.89 support=8.4 resistance=9.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:52 AM market time freshness=DELAYED_CURRENT RSI=65.98 liquidity=1048702.88 spike=0.18
- LCSW.CA: score=22.91 buy_ready=True sector_rank=19 price=34.55 support=30.2 resistance=37.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:49 AM market time freshness=DELAYED_CURRENT RSI=45.37 liquidity=8022745.0 spike=0.15
- LUTS.CA: score=10.58 buy_ready=False sector_rank=16 price=0.82 support=0.79 resistance=0.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:54 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=49838472.0 spike=1.13
- MAAL.CA: score=5.08 buy_ready=False sector_rank=16 price=8.34 support=8.1 resistance=8.53 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:53 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=4759277.0 spike=0.32
- MASR.CA: score=18.32 buy_ready=False sector_rank=16 price=7.8 support=7.7 resistance=8.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:54 AM market time freshness=DELAYED_CURRENT RSI=28.4 liquidity=70703984.0 spike=0.95
- MBSC.CA: score=23.89 buy_ready=False sector_rank=19 price=262.55 support=231.51 resistance=259.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:52 AM market time freshness=DELAYED_CURRENT RSI=75.29 liquidity=13186981.0 spike=0.63
- MCQE.CA: score=11.85 buy_ready=False sector_rank=19 price=202.06 support=198.5 resistance=203.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:50 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=39879036.0 spike=1.98
- MCRO.CA: score=10.32 buy_ready=False sector_rank=16 price=1.59 support=1.56 resistance=1.62 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:53 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=98446968.0 spike=0.56
- MENA.CA: score=14.14 buy_ready=False sector_rank=13 price=7.0 support=6.83 resistance=7.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:20 AM market time freshness=DELAYED_CURRENT RSI=36.0 liquidity=322854.47 spike=0.09
- MEPA.CA: score=25.32 buy_ready=True sector_rank=16 price=1.94 support=1.64 resistance=2.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:54 AM market time freshness=DELAYED_CURRENT RSI=57.58 liquidity=19680878.0 spike=0.32
- MFPC.CA: score=17.9 buy_ready=False sector_rank=9 price=36.99 support=35.37 resistance=38.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:52 AM market time freshness=DELAYED_CURRENT RSI=34.32 liquidity=18591596.0 spike=0.24
- MFSC.CA: score=26.82 buy_ready=True sector_rank=16 price=48.97 support=45.05 resistance=65.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:52 AM market time freshness=DELAYED_CURRENT RSI=61.81 liquidity=9499907.0 spike=0.81
- MHOT.CA: score=21.48 buy_ready=False sector_rank=15 price=17.08 support=16.2 resistance=17.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:45 AM market time freshness=DELAYED_CURRENT RSI=60.21 liquidity=7989711.5 spike=0.86
- MICH.CA: score=21.97 buy_ready=False sector_rank=16 price=49.5 support=37.46 resistance=53.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:54 AM market time freshness=DELAYED_CURRENT RSI=83.87 liquidity=9641136.0 spike=0.3
- MILS.CA: score=27.32 buy_ready=True sector_rank=16 price=192.1 support=134.03 resistance=211.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:54 AM market time freshness=DELAYED_CURRENT RSI=59.54 liquidity=13025220.0 spike=0.21
- MIPH.CA: score=18.39 buy_ready=False sector_rank=14 price=788.63 support=690.01 resistance=831.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:50 AM market time freshness=DELAYED_CURRENT RSI=55.67 liquidity=791153.5 spike=0.17
- MOED.CA: score=14.32 buy_ready=False sector_rank=16 price=0.68 support=0.65 resistance=0.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:54 AM market time freshness=DELAYED_CURRENT RSI=19.44 liquidity=11418364.0 spike=0.38
- MOIL.CA: score=13.0 buy_ready=False sector_rank=8 price=0.68 support=0.51 resistance=0.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:18 AM market time freshness=DELAYED_CURRENT RSI=92.52 liquidity=97863.77 spike=0.15
- MOIN.CA: score=24.96 buy_ready=False sector_rank=16 price=36.47 support=23.03 resistance=40.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:54 AM market time freshness=DELAYED_CURRENT RSI=97.0 liquidity=29216872.0 spike=1.32
- MOSC.CA: score=18.72 buy_ready=True sector_rank=16 price=295.67 support=270.02 resistance=329.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:54 AM market time freshness=DELAYED_CURRENT RSI=68.12 liquidity=1397506.0 spike=0.09
- MPCI.CA: score=10.32 buy_ready=False sector_rank=16 price=343.52 support=328.11 resistance=349.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:54 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=100503920.0 spike=0.82
- MPCO.CA: score=12.72 buy_ready=False sector_rank=10 price=2.17 support=2.13 resistance=2.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:52 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=174865952.0 spike=1.91
- MPRC.CA: score=16.83 buy_ready=True sector_rank=16 price=45.64 support=41.0 resistance=47.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:50 AM market time freshness=DELAYED_CURRENT RSI=61.5 liquidity=1503449.25 spike=0.06
- MTIE.CA: score=26.9 buy_ready=False sector_rank=2 price=11.37 support=9.3 resistance=11.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=86.45 liquidity=30733234.0 spike=0.83
- NAHO.CA: score=11.32 buy_ready=False sector_rank=16 price=0.1 support=0.1 resistance=0.1 source=Yahoo Finance as_of=2026-08-08T21:00:00+00:00 freshness=FRESH RSI=66.67 liquidity=0.0 spike=0.0
- NCCW.CA: score=10.32 buy_ready=False sector_rank=16 price=5.97 support=5.93 resistance=6.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:54 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=20480678.0 spike=0.57
- NEDA.CA: score=5.32 buy_ready=False sector_rank=16 price=2.7 support=2.7 resistance=3.02 source=Yahoo Finance as_of=2026-08-08T21:00:00+00:00 freshness=FRESH RSI=13.04 liquidity=0.0 spike=0.0
- NHPS.CA: score=10.72 buy_ready=False sector_rank=16 price=95.0 support=88.35 resistance=96.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:54 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=96897720.0 spike=1.2
- NINH.CA: score=27.32 buy_ready=True sector_rank=16 price=23.5 support=17.52 resistance=25.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:52 AM market time freshness=DELAYED_CURRENT RSI=50.84 liquidity=10246417.0 spike=0.18
- NIPH.CA: score=11.42 buy_ready=False sector_rank=14 price=411.23 support=362.0 resistance=418.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:53 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=296721120.0 spike=1.41
- OBRI.CA: score=12.36 buy_ready=False sector_rank=16 price=33.75 support=32.05 resistance=34.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:54 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=73322216.0 spike=2.02
- OCDI.CA: score=28.06 buy_ready=False sector_rank=13 price=30.95 support=26.2 resistance=31.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:50 AM market time freshness=DELAYED_CURRENT RSI=71.17 liquidity=118423736.0 spike=1.12
- OCPH.CA: score=16.66 buy_ready=False sector_rank=16 price=242.61 support=225.0 resistance=496.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:54 AM market time freshness=DELAYED_CURRENT RSI=37.79 liquidity=7331444.0 spike=0.24
- ODIN.CA: score=17.45 buy_ready=False sector_rank=16 price=2.85 support=2.34 resistance=3.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:53 AM market time freshness=DELAYED_CURRENT RSI=79.73 liquidity=5123164.0 spike=0.23
- OFH.CA: score=24.32 buy_ready=False sector_rank=16 price=0.86 support=0.62 resistance=0.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:54 AM market time freshness=DELAYED_CURRENT RSI=76.65 liquidity=39064028.0 spike=0.45
- OIH.CA: score=24.9 buy_ready=False sector_rank=12 price=1.63 support=1.41 resistance=1.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:52 AM market time freshness=DELAYED_CURRENT RSI=84.85 liquidity=41435760.0 spike=0.47
- OLFI.CA: score=23.38 buy_ready=False sector_rank=6 price=24.84 support=22.25 resistance=26.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:52 AM market time freshness=DELAYED_CURRENT RSI=78.84 liquidity=8484356.0 spike=0.21
- ORAS.CA: score=9.1 buy_ready=False sector_rank=20 price=718.75 support=716.0 resistance=724.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=58762768.0 spike=1.0
- ORHD.CA: score=27.82 buy_ready=False sector_rank=13 price=42.89 support=38.0 resistance=44.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=74.79 liquidity=42224280.0 spike=0.26
- ORWE.CA: score=22.9 buy_ready=False sector_rank=4 price=26.55 support=22.42 resistance=27.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:52 AM market time freshness=DELAYED_CURRENT RSI=78.06 liquidity=29429760.0 spike=0.46
- PHAR.CA: score=14.9 buy_ready=False sector_rank=14 price=148.72 support=133.5 resistance=153.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:52 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=852238400.0 spike=3.15
- PHDC.CA: score=25.82 buy_ready=True sector_rank=13 price=15.33 support=14.32 resistance=15.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=67.45 liquidity=40904904.0 spike=0.17
- PHTV.CA: score=4.85 buy_ready=False sector_rank=16 price=376.93 support=348.0 resistance=397.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:54 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=4301280.5 spike=1.11
- POUL.CA: score=25.9 buy_ready=True sector_rank=6 price=39.39 support=36.5 resistance=41.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=45.76 liquidity=11368025.0 spike=0.37
- PRCL.CA: score=22.89 buy_ready=False sector_rank=19 price=34.9 support=32.76 resistance=38.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=38.12 liquidity=17393544.0 spike=0.45
- PRDC.CA: score=23.82 buy_ready=False sector_rank=13 price=9.11 support=8.2 resistance=10.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=35.13 liquidity=23252448.0 spike=0.21
- PRMH.CA: score=19.93 buy_ready=True sector_rank=16 price=2.78 support=2.56 resistance=2.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:54 AM market time freshness=DELAYED_CURRENT RSI=53.19 liquidity=2603533.25 spike=0.15
- RACC.CA: score=17.12 buy_ready=False sector_rank=16 price=10.15 support=9.8 resistance=10.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:54 AM market time freshness=DELAYED_CURRENT RSI=50.88 liquidity=3795715.5 spike=0.17
- RAKT.CA: score=11.32 buy_ready=False sector_rank=16 price=22.96 support=21.25 resistance=23.5 source=Yahoo Finance as_of=2026-08-08T21:00:00+00:00 freshness=FRESH RSI=89.22 liquidity=0.0 spike=0.0
- RAYA.CA: score=17.81 buy_ready=False sector_rank=21 price=7.4 support=7.3 resistance=8.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:52 AM market time freshness=DELAYED_CURRENT RSI=39.37 liquidity=26468612.0 spike=0.24
- RMDA.CA: score=24.6 buy_ready=False sector_rank=14 price=6.59 support=4.94 resistance=6.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:52 AM market time freshness=DELAYED_CURRENT RSI=75.67 liquidity=66036236.0 spike=0.69
- ROTO.CA: score=24.32 buy_ready=False sector_rank=16 price=47.34 support=40.5 resistance=47.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:54 AM market time freshness=DELAYED_CURRENT RSI=79.38 liquidity=19940370.0 spike=0.95
- RREI.CA: score=10.32 buy_ready=False sector_rank=16 price=4.8 support=4.76 resistance=4.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:54 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=31824366.0 spike=0.5
- RTVC.CA: score=12.22 buy_ready=False sector_rank=16 price=3.83 support=3.73 resistance=4.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:52 AM market time freshness=DELAYED_CURRENT RSI=46.15 liquidity=1898135.75 spike=0.37
- RUBX.CA: score=13.81 buy_ready=False sector_rank=16 price=12.32 support=12.02 resistance=14.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:54 AM market time freshness=DELAYED_CURRENT RSI=30.96 liquidity=5489906.5 spike=0.15
- SAUD.CA: score=22.31 buy_ready=True sector_rank=11 price=22.22 support=21.25 resistance=22.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=62.72 liquidity=4408985.0 spike=0.32
- SCEM.CA: score=9.89 buy_ready=False sector_rank=19 price=83.71 support=81.61 resistance=84.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:53 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=70143272.0 spike=0.68
- SCFM.CA: score=18.37 buy_ready=True sector_rank=16 price=280.79 support=250.12 resistance=325.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=39.78 liquidity=3041916.0 spike=0.1
- SCTS.CA: score=18.87 buy_ready=True sector_rank=17 price=615.02 support=602.0 resistance=685.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=53.82 liquidity=3616868.0 spike=0.44
- SDTI.CA: score=11.5 buy_ready=False sector_rank=16 price=73.7 support=69.98 resistance=77.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:54 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=43317304.0 spike=1.59
- SEIG.CA: score=13.1 buy_ready=False sector_rank=16 price=269.98 support=237.0 resistance=295.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:40 AM market time freshness=DELAYED_CURRENT RSI=75.66 liquidity=773021.75 spike=0.04
- SIPC.CA: score=10.32 buy_ready=False sector_rank=16 price=4.96 support=4.72 resistance=5.06 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:54 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=46711292.0 spike=0.91
- SKPC.CA: score=26.9 buy_ready=True sector_rank=9 price=16.54 support=14.8 resistance=16.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=67.37 liquidity=17710798.0 spike=0.4
- SMFR.CA: score=27.56 buy_ready=False sector_rank=16 price=263.79 support=202.61 resistance=282.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:54 AM market time freshness=DELAYED_CURRENT RSI=71.31 liquidity=39393932.0 spike=1.12
- SNFC.CA: score=8.98 buy_ready=False sector_rank=16 price=10.84 support=10.7 resistance=12.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:50 AM market time freshness=DELAYED_CURRENT RSI=34.91 liquidity=3659541.75 spike=0.31
- SPIN.CA: score=23.44 buy_ready=True sector_rank=4 price=15.77 support=14.55 resistance=17.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:50 AM market time freshness=DELAYED_CURRENT RSI=66.76 liquidity=7541532.5 spike=0.27
- SPMD.CA: score=22.82 buy_ready=True sector_rank=16 price=0.48 support=0.44 resistance=0.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:54 AM market time freshness=DELAYED_CURRENT RSI=61.47 liquidity=5500065.5 spike=0.17
- SUGR.CA: score=22.34 buy_ready=True sector_rank=6 price=48.3 support=46.47 resistance=49.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:53 AM market time freshness=DELAYED_CURRENT RSI=59.9 liquidity=4436027.5 spike=0.5
- SVCE.CA: score=25.32 buy_ready=True sector_rank=16 price=9.43 support=9.06 resistance=9.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:53 AM market time freshness=DELAYED_CURRENT RSI=48.62 liquidity=12487059.0 spike=0.35
- SWDY.CA: score=28.9 buy_ready=False sector_rank=1 price=107.72 support=87.41 resistance=114.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=73.84 liquidity=34080448.0 spike=0.6
- TALM.CA: score=25.26 buy_ready=True sector_rank=17 price=18.85 support=15.4 resistance=19.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:52 AM market time freshness=DELAYED_CURRENT RSI=69.57 liquidity=14470444.0 spike=0.37
- TMGH.CA: score=23.82 buy_ready=False sector_rank=13 price=98.98 support=95.2 resistance=103.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=46.72 liquidity=150870576.0 spike=0.45
- TRTO.CA: score=11.32 buy_ready=False sector_rank=16 price=0.03 support=0.03 resistance=0.04 source=Yahoo Finance as_of=2026-08-08T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- UEFM.CA: score=15.83 buy_ready=False sector_rank=16 price=545.63 support=491.0 resistance=625.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:42 AM market time freshness=DELAYED_CURRENT RSI=42.89 liquidity=507426.59 spike=0.09
- UEGC.CA: score=10.32 buy_ready=False sector_rank=16 price=2.79 support=2.69 resistance=2.82 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:54 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=10078432.0 spike=0.18
- UNIP.CA: score=25.32 buy_ready=True sector_rank=16 price=0.42 support=0.34 resistance=0.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:55 AM market time freshness=DELAYED_CURRENT RSI=59.15 liquidity=21352200.0 spike=0.71
- UNIT.CA: score=10.01 buy_ready=False sector_rank=13 price=17.85 support=17.32 resistance=21.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=29.77 liquidity=1185734.5 spike=0.05
- WCDF.CA: score=13.53 buy_ready=False sector_rank=16 price=585.64 support=508.0 resistance=634.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:52 AM market time freshness=DELAYED_CURRENT RSI=25.6 liquidity=1209848.25 spike=0.31
- WKOL.CA: score=25.32 buy_ready=True sector_rank=16 price=324.2 support=307.0 resistance=363.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:54 AM market time freshness=DELAYED_CURRENT RSI=54.89 liquidity=10352270.0 spike=0.5
- ZEOT.CA: score=20.01 buy_ready=True sector_rank=16 price=12.59 support=11.1 resistance=13.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:48 AM market time freshness=DELAYED_CURRENT RSI=64.38 liquidity=2686001.0 spike=0.09
- ZMID.CA: score=25.82 buy_ready=True sector_rank=13 price=7.59 support=6.9 resistance=7.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:52 AM market time freshness=DELAYED_CURRENT RSI=40.46 liquidity=168349552.0 spike=0.63

## Backtesting Lite
- ATQA.CA: 180d return=3.8%, max drawdown=-22.05%, MA20>MA50 days last20=9, as_of=2026-08-08T21:00:00+00:00
- CNFN.CA: 180d return=3.73%, max drawdown=-27.78%, MA20>MA50 days last20=20, as_of=2026-08-08T21:00:00+00:00
- ALUM.CA: 180d return=46.02%, max drawdown=-21.86%, MA20>MA50 days last20=4, as_of=2026-08-08T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- ATQA.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Misr National Steel Ataqa summary=Evidence rejected for ATQA.CA: source text did not clearly match ATQA.CA / Misr National Steel Ataqa.
- CNFN.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=586 sources=3 expected=Contact Financial Holding summary=Contact’s consolidated profits approach EGP 471m in 2025; Contact logs lower consolidated net profits at EGP 291m in 9M-25; Contact, e&amp; money forge partnership to boost Egypt’s financial ecosystem Gemini also reviewed web evidence but did not return ticker-specific citations.
  - Contact’s consolidated profits approach EGP 471m in 2025: https://english.mubasher.info/news/4582855/Contact-s-consolidated-profits-approach-EGP-471m-in-2025/
  - Contact logs lower consolidated net profits at EGP 291m in 9M-25: https://english.mubasher.info/news/4526894/Contact-logs-lower-consolidated-net-profits-at-EGP-291m-in-9M-25/
  - Contact, e&amp; money forge partnership to boost Egypt’s financial ecosystem: https://english.mubasher.info/news/4509412/Contact-e-money-forge-partnership-to-boost-Egypt-s-financial-ecosystem/
- ALUM.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Arab Aluminum Company (S.A.E) summary=Arab Aluminum’s stock holds steady as bullish pattern breaks; Arab Aluminum profits rise 7% in H1-17; Arab Aluminum OGM approves EGP 1/shr dividends Gemini also reviewed web evidence but did not return ticker-specific citations.
  - Arab Aluminum’s stock holds steady as bullish pattern breaks: https://english.mubasher.info/news/4564438/Arab-Aluminum-s-stock-holds-steady-as-bullish-pattern-breaks/
  - Arab Aluminum profits rise 7% in H1-17: https://english.mubasher.info/news/3144589/Arab-Aluminum-profits-rise-7-in-H1-17/
  - Arab Aluminum OGM approves EGP 1/shr dividends: https://english.mubasher.info/news/3076498/Arab-Aluminum-OGM-approves-EGP-1-shr-dividends/
- CSAG.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Canal Shipping Agencies summary=Canal Shipping Agencies targets EGP 970m net profits in FY26/27; Canal Shipping Agencies’ stock rebounds; Canal Shipping Agencies mulls EGP 100m capital raise Gemini also reviewed web evidence but did not return ticker-specific citations.
  - Canal Shipping Agencies targets EGP 970m net profits in FY26/27: https://english.mubasher.info/news/4582423/Canal-Shipping-Agencies-targets-EGP-970m-net-profits-in-FY26-27/
  - Canal Shipping Agencies’ stock rebounds: https://english.mubasher.info/news/4564447/Canal-Shipping-Agencies-stock-rebounds/
  - Canal Shipping Agencies mulls EGP 100m capital raise: https://english.mubasher.info/news/4191441/Canal-Shipping-Agencies-mulls-EGP-100m-capital-raise/
- SWDY.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Elsewedy Electric summary=Elsewedy Electric’s consolidated revenues total EGP 75.2bn in Q1-26; Elsewedy Electric accelerates power transformation project in KSA with 6 high-voltage substations; Elsewedy Electric’s subsidiary leads expansion of SAL project at Riyadh airport Gemini also reviewed web evidence but did not return ticker-specific citations.
  - Elsewedy Electric’s consolidated revenues total EGP 75.2bn in Q1-26: https://english.mubasher.info/news/4614341/Elsewedy-Electric-s-consolidated-revenues-total-EGP-75-2bn-in-Q1-26/
  - Elsewedy Electric accelerates power transformation project in KSA with 6 high-voltage substations: https://english.mubasher.info/news/4593166/Elsewedy-Electric-accelerates-power-transformation-project-in-KSA-with-6-high-voltage-substations/
  - Elsewedy Electric’s subsidiary leads expansion of SAL project at Riyadh airport: https://english.mubasher.info/news/4580464/Elsewedy-Electric-s-subsidiary-leads-expansion-of-SAL-project-at-Riyadh-airport/
- OCDI.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Sixth of October Development and Investment summary=Evidence rejected for OCDI.CA: source text did not clearly match OCDI.CA / Sixth of October Development and Investment.
- HRHO.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=EFG Holding summary=Evidence rejected for HRHO.CA: source text did not clearly match HRHO.CA / EFG Holding.
- EFIH.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=E-Finance For Digital and Financial Investments summary=Evidence rejected for EFIH.CA: source text did not clearly match EFIH.CA / E-Finance For Digital and Financial Investments.

## Warnings
- Evidence rejected for ATQA.CA: source text did not clearly match ATQA.CA / Misr National Steel Ataqa.
- Evidence for CNFN.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for ALUM.CA matches the company but no source/report date was detected.
- Evidence for CSAG.CA matches the company but no source/report date was detected.
- Evidence for SWDY.CA matches the company but no source/report date was detected.
- Evidence rejected for OCDI.CA: source text did not clearly match OCDI.CA / Sixth of October Development and Investment.
- Evidence rejected for HRHO.CA: source text did not clearly match HRHO.CA / EFG Holding.
- Evidence rejected for EFIH.CA: source text did not clearly match EFIH.CA / E-Finance For Digital and Financial Investments.
