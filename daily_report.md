# Telegram-First EGX Scanner Report

Scan phase: Open liquidity confirmation
Generated UTC: 2026-09-08T11:16:31.472448+00:00
Generated Cairo: 2026-09-08 14:16
Run timing: target 09:15 Cairo | generated Cairo 2026-09-08 14:16 | cron 15 6 * * 0-4
Trigger: scheduled cron=15 6 * * 0-4 mapped to open_confirm; Cairo now 2026-09-08 14:11

## Control Center
- Action tickets: 2 prioritized signal(s)
- BUY-ready candidates: 62
- Data quality issues: 1
- Tradeable price/liquidity tickers: 172/189
- Top sector: Textiles

## Market Context
- Market trend: Bearish
- Source: Mubasher EGX market page (delayed public data)
- As of: Tuesday, September 08
- Freshness: DELAYED
- EGX30 regime: BULLISH / above MA20 65.0% / above MA50 80.0%
- EGX70 regime: CONSTRUCTIVE / above MA20 58.97% / above MA50 69.23%
- Sector breadth: 66.67%
- Risk mode: BROAD_RISK_ON

## Top Liquidity
- AMES.CA: liquidity=1451968768.0 spike=12.19 score=15.26
- CCAP.CA: liquidity=919050176.0 spike=1.43 score=26.76
- EFIC.CA: liquidity=442699520.0 spike=9.3 score=15.9
- COMI.CA: liquidity=430515072.0 spike=0.81 score=29.9
- ETEL.CA: liquidity=369282976.0 spike=2.59 score=31.08

## AI Narrative
- Provider: OpenRouter OK
- Model: nvidia/nemotron-3-super-120b-a12b:free
- Summary: Scanner prioritized GIHD.CA and COMI.CA as watch/buy setups under a bullish EGX30, constructive EGX70, and broad risk‑on regime; liquidity spikes and price above key moving averages suggest near‑term upside, but mixed sector leadership and a bearish macro trend add uncertainty.

## Top Liquidity Spikes
- AMES.CA: spike=12.19 liquidity=1451968768.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- EFIC.CA: spike=9.3 liquidity=442699520.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- CERA.CA: spike=4.41 liquidity=173837840.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- ELNA.CA: spike=3.74 liquidity=1524571.5 outlook=WEAK_OR_RISKY score=21.39 buy_ready=False
- GIHD.CA: spike=3.71 liquidity=92418920.0 outlook=BULLISH_WATCH score=76.39 buy_ready=True

## Sector Leaderboard
- #1 Textiles: score=11.79 5d=2.9% 20d=19.62% aboveMA50=100.0%
- #2 Telecommunications: score=11.01 5d=2.78% 20d=5.46% aboveMA50=100.0%
- #3 Transportation & Logistics: score=10.86 5d=6.13% 20d=10.13% aboveMA50=100.0%
- #4 Building Materials: score=10.83 5d=0.61% 20d=25.92% aboveMA50=83.33%
- #5 Banking & Financials: score=9.31 5d=5.05% 20d=6.62% aboveMA50=90.0%
- #6 Investment Holding: score=8.98 5d=-2.74% 20d=14.39% aboveMA50=100.0%
- #7 Industrial Goods & Cables: score=8.62 5d=4.46% 20d=12.49% aboveMA50=50.0%
- #8 Education: score=8.53 5d=8.45% 20d=4.4% aboveMA50=100.0%

## Today's Prioritized Action Tickets
- Priority #1: BUY GIHD.CA
  - Entry: 73.2 | Take profit: 79.06 | Stop loss: 70.27
  - Confidence: LOW | score=32.26 | outlook=BULLISH_WATCH 76.39
  - Reason: WATCH/BUY SETUP: GIHD.CA has aligned current price data, liquidity above threshold, price above MA20/MA50, RSI 57.97, support 58.01, resistance 76.5, and evidence sources. Macro trend is Bearish; market regime is BROAD_RISK_ON; verify price action in Thndr before treating it as a swing entry.
- Priority #2: BUY COMI.CA
  - Entry: 139.64 | Take profit: 146.36 | Stop loss: 136.28
  - Confidence: LOW | score=29.9 | outlook=BULLISH_WATCH 92.31
  - Reason: WATCH/BUY SETUP: COMI.CA has aligned current price data, liquidity above threshold, price above MA20/MA50, RSI 58.65, support 135.35, resistance 142.5, and evidence sources. Macro trend is Bearish; market regime is BROAD_RISK_ON; verify price action in Thndr before treating it as a swing entry.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- ETEL.CA: BULLISH_WATCH score=100 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=No major short-term scanner risk flags.
- ALCN.CA: BULLISH_WATCH score=96 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- ELSH.CA: BULLISH_WATCH score=92.39 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- ASCM.CA: BULLISH_WATCH score=92.39 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- NEDA.CA: BULLISH_WATCH score=92.39 liquidity=TRADEABLE sector=IMPROVING risk=sector is not leading
- COMI.CA: BULLISH_WATCH score=92.31 liquidity=TRADEABLE sector=IMPROVING risk=No major short-term scanner risk flags.
- CSAG.CA: BULLISH_WATCH score=90 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- EXPA.CA: BULLISH_WATCH score=87.31 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- EDFM.CA: BULLISH_WATCH score=86.39 liquidity=TRADEABLE sector=IMPROVING risk=sector is not leading
- SPIN.CA: BULLISH_WATCH score=86 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; far above support

## BUY-Ready Candidates
- GIHD.CA: rank=32.26 outlook=BULLISH_WATCH outlook_score=76.39 sector_rank=16 price=73.2 support=58.01 resistance=76.5 liquidity=92418920.0
- ETEL.CA: rank=31.08 outlook=BULLISH_WATCH outlook_score=100 sector_rank=2 price=122.07 support=107.0 resistance=120.0 liquidity=369282976.0
- CANA.CA: rank=29.9 outlook=CONSTRUCTIVE outlook_score=67.31 sector_rank=5 price=43.81 support=38.79 resistance=44.0 liquidity=13602777.0
- COMI.CA: rank=29.9 outlook=BULLISH_WATCH outlook_score=92.31 sector_rank=5 price=139.64 support=135.35 resistance=142.5 liquidity=430515072.0
- FWRY.CA: rank=29.9 outlook=BULLISH_WATCH outlook_score=73.12 sector_rank=11 price=19.3 support=18.66 resistance=19.55 liquidity=95551432.0
- CIEB.CA: rank=29.9 outlook=BULLISH_WATCH outlook_score=78.31 sector_rank=5 price=25.8 support=24.0 resistance=26.27 liquidity=12354624.0
- EXPA.CA: rank=29.9 outlook=BULLISH_WATCH outlook_score=87.31 sector_rank=5 price=21.46 support=19.8 resistance=22.39 liquidity=12988580.0
- MOIN.CA: rank=29.3 outlook=BULLISH_WATCH outlook_score=78.39 sector_rank=16 price=40.83 support=32.5 resistance=43.79 liquidity=46260108.0
- FAIT.CA: rank=29.28 outlook=BULLISH_WATCH outlook_score=74.31 sector_rank=5 price=47.74 support=37.01 resistance=46.0 liquidity=9222160.0
- KABO.CA: rank=28.9 outlook=CONSTRUCTIVE outlook_score=68 sector_rank=1 price=9.24 support=8.0 resistance=9.75 liquidity=30749428.0

## Data Quality Issues
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=18.26 buy_ready=False sector_rank=16 price=307.17 support=288.0 resistance=375.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=11.38 liquidity=14745172.0 spike=0.35
- ABUK.CA: score=25.9 buy_ready=True sector_rank=10 price=90.08 support=73.2 resistance=94.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=67.36 liquidity=103405256.0 spike=0.68
- ACAMD.CA: score=10.26 buy_ready=False sector_rank=16 price=2.1 support=2.09 resistance=2.16 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=44480952.0 spike=0.77
- ACGC.CA: score=30.9 buy_ready=False sector_rank=1 price=15.43 support=10.36 resistance=15.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=71.01 liquidity=44680248.0 spike=1.0
- ADCI.CA: score=16.39 buy_ready=False sector_rank=16 price=292.24 support=280.0 resistance=389.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:53 PM market time freshness=DELAYED_CURRENT RSI=46.19 liquidity=3135489.75 spike=0.24
- ADIB.CA: score=18.9 buy_ready=False sector_rank=5 price=51.73 support=51.84 resistance=55.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:56 PM market time freshness=DELAYED_CURRENT RSI=34.3 liquidity=70033592.0 spike=1.0
- ADPC.CA: score=18.26 buy_ready=False sector_rank=16 price=3.99 support=3.85 resistance=4.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=28.85 liquidity=15628280.0 spike=0.38
- AFDI.CA: score=18.26 buy_ready=False sector_rank=16 price=55.01 support=53.54 resistance=69.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=29.67 liquidity=11116076.0 spike=0.35
- AFMC.CA: score=10.26 buy_ready=False sector_rank=16 price=170.0 support=170.0 resistance=184.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=96346472.0 spike=0.94
- AJWA.CA: score=12.78 buy_ready=False sector_rank=16 price=180.98 support=175.15 resistance=202.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=7.11 liquidity=7528006.5 spike=0.13
- ALCN.CA: score=28.86 buy_ready=True sector_rank=3 price=32.0 support=30.03 resistance=34.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:56 PM market time freshness=DELAYED_CURRENT RSI=60.53 liquidity=9962087.0 spike=0.29
- ALUM.CA: score=19.12 buy_ready=True sector_rank=16 price=28.58 support=24.4 resistance=30.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:56 PM market time freshness=DELAYED_CURRENT RSI=50.13 liquidity=3861111.5 spike=0.14
- AMER.CA: score=18.5 buy_ready=False sector_rank=15 price=5.6 support=5.3 resistance=8.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=31.45 liquidity=17255962.0 spike=0.19
- AMES.CA: score=15.26 buy_ready=False sector_rank=16 price=66.5 support=64.4 resistance=82.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=1451968768.0 spike=12.19
- AMIA.CA: score=23.26 buy_ready=False sector_rank=16 price=19.1 support=10.6 resistance=22.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT RSI=72.16 liquidity=27386978.0 spike=0.39
- AMOC.CA: score=25.45 buy_ready=False sector_rank=12 price=14.01 support=9.1 resistance=14.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:56 PM market time freshness=DELAYED_CURRENT RSI=75.19 liquidity=236034736.0 spike=1.4
- APSW.CA: score=4.76 buy_ready=False sector_rank=16 price=8.68 support=8.41 resistance=9.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=26.5 liquidity=508788.13 spike=0.36
- ARAB.CA: score=27.5 buy_ready=True sector_rank=15 price=0.26 support=0.23 resistance=0.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=64.41 liquidity=84545304.0 spike=0.88
- ARCC.CA: score=25.9 buy_ready=True sector_rank=4 price=76.58 support=59.0 resistance=91.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=54.99 liquidity=23186074.0 spike=0.21
- AREH.CA: score=24.26 buy_ready=False sector_rank=16 price=1.5 support=1.39 resistance=1.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:55 PM market time freshness=DELAYED_CURRENT RSI=47.37 liquidity=25249970.0 spike=0.92
- ARVA.CA: score=10.26 buy_ready=False sector_rank=16 price=14.99 support=14.45 resistance=14.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=16 August 01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=30473338.0 spike=0.56
- ASCM.CA: score=26.8 buy_ready=True sector_rank=16 price=64.81 support=62.01 resistance=69.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=43.36 liquidity=54231624.0 spike=1.77
- ASPI.CA: score=20.02 buy_ready=False sector_rank=16 price=0.46 support=0.43 resistance=0.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=23.83 liquidity=76682400.0 spike=1.88
- ATLC.CA: score=22.16 buy_ready=False sector_rank=18 price=7.26 support=5.2 resistance=8.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:56 PM market time freshness=DELAYED_CURRENT RSI=76.74 liquidity=8179440.5 spike=0.27
- ATQA.CA: score=26.38 buy_ready=False sector_rank=10 price=12.75 support=10.11 resistance=12.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=72.88 liquidity=130829096.0 spike=1.24
- AXPH.CA: score=15.41 buy_ready=False sector_rank=16 price=1686.73 support=1268.53 resistance=1768.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=89.79 liquidity=3154580.75 spike=0.26
- BINV.CA: score=20.93 buy_ready=True sector_rank=6 price=51.53 support=46.25 resistance=55.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=64.3 liquidity=3025141.75 spike=0.26
- BIOC.CA: score=18.26 buy_ready=False sector_rank=16 price=316.0 support=310.03 resistance=563.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=23.53 liquidity=60509492.0 spike=0.26
- BTFH.CA: score=20.98 buy_ready=False sector_rank=18 price=2.99 support=2.94 resistance=3.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=38.24 liquidity=49264464.0 spike=0.34
- CAED.CA: score=22.98 buy_ready=False sector_rank=16 price=137.83 support=119.03 resistance=185.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=59.17 liquidity=9722755.0 spike=0.27
- CANA.CA: score=29.9 buy_ready=True sector_rank=5 price=43.81 support=38.79 resistance=44.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:56 PM market time freshness=DELAYED_CURRENT RSI=63.48 liquidity=13602777.0 spike=0.75
- CCAP.CA: score=26.76 buy_ready=False sector_rank=6 price=6.18 support=5.18 resistance=6.16 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=74.29 liquidity=919050176.0 spike=1.43
- CCRS.CA: score=25.26 buy_ready=True sector_rank=16 price=2.62 support=2.4 resistance=3.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=53.52 liquidity=11501559.0 spike=0.22
- CEFM.CA: score=23.26 buy_ready=False sector_rank=16 price=147.18 support=132.0 resistance=168.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=70.43 liquidity=11890846.0 spike=0.66
- CERA.CA: score=15.26 buy_ready=False sector_rank=16 price=1.7 support=1.68 resistance=1.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=173837840.0 spike=4.41
- CFGH.CA: score=15.46 buy_ready=False sector_rank=16 price=0.12 support=0.1 resistance=0.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:58 AM market time freshness=DELAYED_CURRENT RSI=72.22 liquidity=23805.72 spike=1.09
- CICH.CA: score=22.67 buy_ready=True sector_rank=18 price=13.09 support=12.0 resistance=13.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:55 PM market time freshness=DELAYED_CURRENT RSI=56.19 liquidity=3690201.0 spike=0.76
- CIEB.CA: score=29.9 buy_ready=True sector_rank=5 price=25.8 support=24.0 resistance=26.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:56 PM market time freshness=DELAYED_CURRENT RSI=63.16 liquidity=12354624.0 spike=0.8
- CIRA.CA: score=25.9 buy_ready=True sector_rank=8 price=38.03 support=32.1 resistance=40.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:52 PM market time freshness=DELAYED_CURRENT RSI=52.92 liquidity=21492272.0 spike=0.65
- CLHO.CA: score=19.8 buy_ready=False sector_rank=20 price=16.81 support=16.95 resistance=18.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=52.09 liquidity=76295840.0 spike=1.07
- CNFN.CA: score=19.98 buy_ready=False sector_rank=18 price=4.84 support=4.73 resistance=5.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=42.86 liquidity=16223627.0 spike=0.89
- COMI.CA: score=29.9 buy_ready=True sector_rank=5 price=139.64 support=135.35 resistance=142.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:56 PM market time freshness=DELAYED_CURRENT RSI=58.65 liquidity=430515072.0 spike=0.81
- COPR.CA: score=25.26 buy_ready=True sector_rank=16 price=0.5 support=0.4 resistance=0.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=60.47 liquidity=19154848.0 spike=0.2
- COSG.CA: score=27.26 buy_ready=True sector_rank=16 price=1.92 support=1.69 resistance=2.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=66.67 liquidity=15470454.0 spike=0.27
- CPCI.CA: score=17.21 buy_ready=True sector_rank=16 price=540.04 support=484.82 resistance=644.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:48 PM market time freshness=DELAYED_CURRENT RSI=51.41 liquidity=1949591.75 spike=0.28
- CSAG.CA: score=22.33 buy_ready=True sector_rank=3 price=41.82 support=36.8 resistance=44.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:56 PM market time freshness=DELAYED_CURRENT RSI=50.3 liquidity=5428238.5 spike=0.21
- DAPH.CA: score=25.94 buy_ready=True sector_rank=16 price=131.1 support=104.6 resistance=157.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=48.33 liquidity=95591352.0 spike=1.34
- DEIN.CA: score=13.26 buy_ready=False sector_rank=16 price=10.35 support=10.35 resistance=12.42 source=Yahoo Finance as_of=2026-09-05T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- DOMT.CA: score=14.42 buy_ready=False sector_rank=17 price=28.51 support=27.79 resistance=30.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:53 PM market time freshness=DELAYED_CURRENT RSI=43.61 liquidity=1348920.63 spike=0.08
- DSCW.CA: score=20.26 buy_ready=False sector_rank=16 price=1.91 support=1.84 resistance=2.21 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=40.0 liquidity=18594744.0 spike=0.26
- DTPP.CA: score=25.26 buy_ready=True sector_rank=16 price=304.0 support=248.02 resistance=340.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=58.64 liquidity=11665716.0 spike=0.31
- EALR.CA: score=11.91 buy_ready=False sector_rank=16 price=378.33 support=340.0 resistance=471.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT RSI=11.1 liquidity=6654276.5 spike=0.19
- EASB.CA: score=11.55 buy_ready=False sector_rank=16 price=7.31 support=7.05 resistance=8.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:55 PM market time freshness=DELAYED_CURRENT RSI=47.97 liquidity=1289224.75 spike=0.17
- EAST.CA: score=21.07 buy_ready=False sector_rank=17 price=35.37 support=35.0 resistance=37.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:56 PM market time freshness=DELAYED_CURRENT RSI=44.19 liquidity=30671410.0 spike=0.49
- EBSC.CA: score=19.49 buy_ready=True sector_rank=16 price=2.07 support=1.88 resistance=2.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=62.07 liquidity=2235066.75 spike=0.16
- ECAP.CA: score=11.75 buy_ready=False sector_rank=16 price=33.52 support=31.16 resistance=43.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=28.74 liquidity=6498036.5 spike=0.36
- EDFM.CA: score=19.53 buy_ready=True sector_rank=16 price=418.7 support=394.0 resistance=432.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:55 PM market time freshness=DELAYED_CURRENT RSI=57.32 liquidity=3115056.5 spike=1.58
- EEII.CA: score=15.26 buy_ready=False sector_rank=16 price=2.35 support=2.33 resistance=3.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=26.19 liquidity=10837430.0 spike=0.36
- EFIC.CA: score=15.9 buy_ready=False sector_rank=10 price=230.21 support=206.0 resistance=239.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=442699520.0 spike=9.3
- EFID.CA: score=18.07 buy_ready=False sector_rank=17 price=31.4 support=29.71 resistance=34.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=32.43 liquidity=77113184.0 spike=0.85
- EFIH.CA: score=23.9 buy_ready=False sector_rank=11 price=23.84 support=22.16 resistance=25.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:56 PM market time freshness=DELAYED_CURRENT RSI=35.11 liquidity=39907116.0 spike=0.36
- EGAL.CA: score=25.9 buy_ready=True sector_rank=10 price=375.16 support=298.8 resistance=395.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=67.42 liquidity=70374448.0 spike=0.43
- EGAS.CA: score=23.65 buy_ready=False sector_rank=12 price=58.57 support=55.21 resistance=63.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=47.83 liquidity=10652528.0 spike=0.76
- EGBE.CA: score=14.01 buy_ready=False sector_rank=5 price=0.51 support=0.51 resistance=0.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:47 PM market time freshness=DELAYED_CURRENT RSI=43.04 liquidity=109523.17 spike=0.55
- EGCH.CA: score=27.9 buy_ready=True sector_rank=10 price=14.08 support=13.3 resistance=14.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=50.19 liquidity=124731136.0 spike=0.92
- EGSA.CA: score=15.21 buy_ready=False sector_rank=2 price=9.04 support=8.65 resistance=9.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:41 PM market time freshness=DELAYED_CURRENT RSI=85.71 liquidity=10849.0 spike=1.15
- EGTS.CA: score=15.48 buy_ready=False sector_rank=15 price=17.3 support=16.17 resistance=20.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:56 PM market time freshness=DELAYED_CURRENT RSI=28.11 liquidity=9981007.0 spike=0.28
- EHDR.CA: score=23.26 buy_ready=False sector_rank=16 price=2.94 support=2.81 resistance=3.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:56 PM market time freshness=DELAYED_CURRENT RSI=35.71 liquidity=14633542.0 spike=0.44
- EKHO.CA: score=11.65 buy_ready=False sector_rank=12 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-09-05T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=21.9 buy_ready=False sector_rank=7 price=2.08 support=2.04 resistance=2.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=41.67 liquidity=49602200.0 spike=0.76
- ELKA.CA: score=27.26 buy_ready=True sector_rank=16 price=1.82 support=1.7 resistance=1.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=64.58 liquidity=14566901.0 spike=0.22
- ELNA.CA: score=10.78 buy_ready=False sector_rank=16 price=37.03 support=36.1 resistance=38.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=30.85 liquidity=1524571.5 spike=3.74
- ELSH.CA: score=26.84 buy_ready=True sector_rank=16 price=13.78 support=12.97 resistance=14.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=47.04 liquidity=77518040.0 spike=1.79
- ELWA.CA: score=13.43 buy_ready=False sector_rank=16 price=1.76 support=1.62 resistance=1.99 source=Yahoo Finance as_of=2026-09-05T21:00:00+00:00 freshness=FRESH RSI=51.95 liquidity=1173145.59 spike=0.52
- EMFD.CA: score=24.5 buy_ready=False sector_rank=15 price=14.79 support=11.51 resistance=14.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:56 PM market time freshness=DELAYED_CURRENT RSI=97.02 liquidity=125985160.0 spike=0.79
- ENGC.CA: score=13.86 buy_ready=False sector_rank=16 price=44.79 support=41.8 resistance=54.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:56 PM market time freshness=DELAYED_CURRENT RSI=31.38 liquidity=5605980.0 spike=0.23
- EOSB.CA: score=21.56 buy_ready=False sector_rank=16 price=1.57 support=1.5 resistance=1.64 source=Yahoo Finance as_of=2026-09-05T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=166489.09 spike=3.07
- EPCO.CA: score=14.3 buy_ready=False sector_rank=16 price=10.99 support=10.8 resistance=13.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=34.54 liquidity=6045104.5 spike=0.37
- EPPK.CA: score=0.67 buy_ready=False sector_rank=16 price=10.29 support=10.29 resistance=10.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:52 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=416127.59 spike=0.3
- ETEL.CA: score=31.08 buy_ready=True sector_rank=2 price=122.07 support=107.0 resistance=120.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=56.21 liquidity=369282976.0 spike=2.59
- ETRS.CA: score=21.29 buy_ready=True sector_rank=16 price=11.41 support=10.52 resistance=11.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=45.3 liquidity=4033039.5 spike=0.16
- EXPA.CA: score=29.9 buy_ready=True sector_rank=5 price=21.46 support=19.8 resistance=22.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=60.48 liquidity=12988580.0 spike=0.33
- FAIT.CA: score=29.28 buy_ready=True sector_rank=5 price=47.74 support=37.01 resistance=46.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=63.38 liquidity=9222160.0 spike=1.08
- FAITA.CA: score=10.93 buy_ready=False sector_rank=5 price=0.99 support=0.98 resistance=1.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:32 PM market time freshness=DELAYED_CURRENT RSI=48.15 liquidity=32799.93 spike=0.59
- FERC.CA: score=26.27 buy_ready=True sector_rank=10 price=79.68 support=76.7 resistance=87.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=60.29 liquidity=8368604.0 spike=0.37
- FWRY.CA: score=29.9 buy_ready=True sector_rank=11 price=19.3 support=18.66 resistance=19.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:56 PM market time freshness=DELAYED_CURRENT RSI=59.41 liquidity=95551432.0 spike=0.58
- GBCO.CA: score=23.68 buy_ready=False sector_rank=19 price=30.16 support=27.51 resistance=32.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=44.04 liquidity=18690102.0 spike=0.37
- GDWA.CA: score=23.26 buy_ready=True sector_rank=16 price=0.81 support=0.77 resistance=0.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=52.2 liquidity=21531720.0 spike=0.44
- GGCC.CA: score=18.26 buy_ready=False sector_rank=16 price=0.86 support=0.83 resistance=1.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=32.63 liquidity=12572577.0 spike=0.23
- GIHD.CA: score=32.26 buy_ready=True sector_rank=16 price=73.2 support=58.01 resistance=76.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:56 PM market time freshness=DELAYED_CURRENT RSI=57.97 liquidity=92418920.0 spike=3.71
- GMCI.CA: score=5.47 buy_ready=False sector_rank=16 price=1.86 support=1.83 resistance=2.03 source=Yahoo Finance as_of=2026-09-05T21:00:00+00:00 freshness=FRESH RSI=28.57 liquidity=210622.68 spike=0.48
- GRCA.CA: score=25.26 buy_ready=False sector_rank=16 price=81.16 support=54.7 resistance=86.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=71.53 liquidity=52968304.0 spike=0.79
- GSSC.CA: score=22.68 buy_ready=True sector_rank=16 price=308.28 support=274.0 resistance=325.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=69.2 liquidity=5421852.5 spike=0.39
- GTWL.CA: score=24.26 buy_ready=False sector_rank=16 price=234.89 support=121.55 resistance=248.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=75.92 liquidity=134371664.0 spike=0.43
- HDBK.CA: score=23.94 buy_ready=False sector_rank=5 price=114.58 support=84.21 resistance=124.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:56 PM market time freshness=DELAYED_CURRENT RSI=83.19 liquidity=72616920.0 spike=1.52
- HELI.CA: score=25.5 buy_ready=True sector_rank=15 price=8.1 support=7.34 resistance=8.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:56 PM market time freshness=DELAYED_CURRENT RSI=65.73 liquidity=106686840.0 spike=0.66
- HRHO.CA: score=20.98 buy_ready=False sector_rank=18 price=26.0 support=25.33 resistance=27.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:56 PM market time freshness=DELAYED_CURRENT RSI=49.06 liquidity=81818808.0 spike=0.63
- ICID.CA: score=18.53 buy_ready=False sector_rank=16 price=18.2 support=8.27 resistance=19.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=74.0 liquidity=3278758.75 spike=0.11
- IDRE.CA: score=25.26 buy_ready=True sector_rank=16 price=54.73 support=51.02 resistance=58.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:56 PM market time freshness=DELAYED_CURRENT RSI=51.64 liquidity=10733120.0 spike=0.73
- IFAP.CA: score=25.9 buy_ready=True sector_rank=9 price=21.65 support=20.2 resistance=22.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=55.02 liquidity=17079928.0 spike=0.53
- INFI.CA: score=23.26 buy_ready=False sector_rank=16 price=149.67 support=135.99 resistance=178.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=40.68 liquidity=14392108.0 spike=0.22
- IRON.CA: score=18.79 buy_ready=False sector_rank=10 price=29.52 support=29.54 resistance=33.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=35.44 liquidity=8893821.0 spike=0.67
- ISMA.CA: score=23.26 buy_ready=False sector_rank=16 price=32.11 support=29.0 resistance=40.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=42.28 liquidity=11892849.0 spike=0.45
- ISMQ.CA: score=22.9 buy_ready=False sector_rank=10 price=9.25 support=9.0 resistance=9.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=48.0 liquidity=21415000.0 spike=0.51
- ISPH.CA: score=22.66 buy_ready=False sector_rank=20 price=13.14 support=12.75 resistance=16.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=38.85 liquidity=48836488.0 spike=0.35
- JUFO.CA: score=24.07 buy_ready=False sector_rank=17 price=27.46 support=26.07 resistance=27.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=50.67 liquidity=32702946.0 spike=0.62
- KABO.CA: score=28.9 buy_ready=True sector_rank=1 price=9.24 support=8.0 resistance=9.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:56 PM market time freshness=DELAYED_CURRENT RSI=37.5 liquidity=30749428.0 spike=0.66
- KWIN.CA: score=10.26 buy_ready=False sector_rank=16 price=93.09 support=91.5 resistance=98.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=16117810.0 spike=0.24
- KZPC.CA: score=11.64 buy_ready=False sector_rank=16 price=14.2 support=13.51 resistance=14.63 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=94072288.0 spike=1.69
- LCSW.CA: score=25.9 buy_ready=True sector_rank=4 price=35.0 support=32.12 resistance=37.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=64.22 liquidity=20149984.0 spike=0.6
- LUTS.CA: score=23.26 buy_ready=False sector_rank=16 price=0.91 support=0.79 resistance=1.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=44.38 liquidity=142543008.0 spike=0.53
- MAAL.CA: score=24.13 buy_ready=True sector_rank=16 price=9.41 support=8.32 resistance=10.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=63.8 liquidity=6871991.5 spike=0.5
- MASR.CA: score=24.26 buy_ready=False sector_rank=16 price=8.54 support=7.45 resistance=8.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=75.13 liquidity=75963816.0 spike=0.96
- MBSC.CA: score=27.9 buy_ready=True sector_rank=4 price=411.48 support=254.37 resistance=470.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:56 PM market time freshness=DELAYED_CURRENT RSI=52.03 liquidity=10732049.0 spike=0.11
- MCQE.CA: score=25.9 buy_ready=True sector_rank=4 price=246.29 support=192.0 resistance=292.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=52.67 liquidity=16797106.0 spike=0.26
- MCRO.CA: score=28.44 buy_ready=False sector_rank=16 price=1.67 support=1.44 resistance=1.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=70.73 liquidity=181770752.0 spike=1.59
- MENA.CA: score=7.57 buy_ready=False sector_rank=15 price=6.75 support=6.59 resistance=7.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:55 PM market time freshness=DELAYED_CURRENT RSI=31.96 liquidity=2066889.13 spike=0.34
- MEPA.CA: score=10.26 buy_ready=False sector_rank=16 price=2.06 support=2.02 resistance=2.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=25239806.0 spike=0.68
- MFPC.CA: score=22.9 buy_ready=False sector_rank=10 price=46.66 support=36.98 resistance=47.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:56 PM market time freshness=DELAYED_CURRENT RSI=81.63 liquidity=81387224.0 spike=0.63
- MFSC.CA: score=20.34 buy_ready=False sector_rank=16 price=51.0 support=48.0 resistance=58.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:56 PM market time freshness=DELAYED_CURRENT RSI=72.46 liquidity=3084061.25 spike=0.39
- MHOT.CA: score=19.27 buy_ready=False sector_rank=14 price=18.09 support=16.83 resistance=21.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=39.47 liquidity=4749917.0 spike=0.25
- MICH.CA: score=25.26 buy_ready=True sector_rank=16 price=50.43 support=46.3 resistance=53.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=57.74 liquidity=11479648.0 spike=0.28
- MILS.CA: score=23.26 buy_ready=False sector_rank=16 price=201.69 support=179.05 resistance=248.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=53.21 liquidity=27818258.0 spike=0.41
- MIPH.CA: score=18.75 buy_ready=True sector_rank=20 price=796.79 support=700.2 resistance=827.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:51 PM market time freshness=DELAYED_CURRENT RSI=62.43 liquidity=2083975.75 spike=0.45
- MOED.CA: score=25.26 buy_ready=False sector_rank=16 price=0.82 support=0.67 resistance=0.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=72.14 liquidity=60723064.0 spike=0.55
- MOIL.CA: score=15.84 buy_ready=False sector_rank=12 price=0.68 support=0.65 resistance=0.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=55.24 liquidity=190306.94 spike=0.79
- MOIN.CA: score=29.3 buy_ready=True sector_rank=16 price=40.83 support=32.5 resistance=43.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:56 PM market time freshness=DELAYED_CURRENT RSI=60.21 liquidity=46260108.0 spike=1.02
- MOSC.CA: score=10.05 buy_ready=False sector_rank=16 price=320.96 support=297.96 resistance=380.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=34.29 liquidity=1796690.38 spike=0.14
- MPCI.CA: score=23.26 buy_ready=True sector_rank=16 price=425.85 support=316.59 resistance=490.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=67.86 liquidity=77334552.0 spike=0.4
- MPCO.CA: score=23.9 buy_ready=False sector_rank=9 price=2.19 support=1.98 resistance=2.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=60.24 liquidity=41602020.0 spike=0.39
- MPRC.CA: score=20.26 buy_ready=False sector_rank=16 price=40.09 support=39.5 resistance=52.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=38.71 liquidity=15533065.0 spike=0.37
- MTIE.CA: score=16.68 buy_ready=False sector_rank=19 price=8.5 support=8.25 resistance=10.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=33.8 liquidity=23797988.0 spike=0.34
- NAHO.CA: score=0.28 buy_ready=False sector_rank=16 price=0.14 support=0.14 resistance=0.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:51 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=20469.36 spike=0.19
- NCCW.CA: score=27.26 buy_ready=True sector_rank=16 price=6.37 support=5.59 resistance=6.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=54.34 liquidity=18202204.0 spike=0.63
- NEDA.CA: score=23.12 buy_ready=True sector_rank=16 price=2.82 support=2.7 resistance=2.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:56 PM market time freshness=DELAYED_CURRENT RSI=42.86 liquidity=2865936.25 spike=3.58
- NHPS.CA: score=23.26 buy_ready=False sector_rank=16 price=84.98 support=84.21 resistance=98.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=38.2 liquidity=10864933.0 spike=0.35
- NINH.CA: score=25.26 buy_ready=True sector_rank=16 price=23.35 support=21.53 resistance=26.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:56 PM market time freshness=DELAYED_CURRENT RSI=61.53 liquidity=16600559.0 spike=0.5
- NIPH.CA: score=22.66 buy_ready=False sector_rank=20 price=336.2 support=326.51 resistance=450.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=40.49 liquidity=102265696.0 spike=0.32
- OBRI.CA: score=20.46 buy_ready=False sector_rank=16 price=32.93 support=31.64 resistance=34.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=48.79 liquidity=9199471.0 spike=0.35
- OCDI.CA: score=25.5 buy_ready=True sector_rank=15 price=33.8 support=30.03 resistance=36.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:56 PM market time freshness=DELAYED_CURRENT RSI=49.84 liquidity=26896970.0 spike=0.22
- OCPH.CA: score=17.63 buy_ready=False sector_rank=16 price=254.25 support=238.76 resistance=341.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=35.52 liquidity=6376231.0 spike=0.35
- ODIN.CA: score=23.16 buy_ready=False sector_rank=16 price=2.87 support=2.55 resistance=3.92 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=36.5 liquidity=9907543.0 spike=0.22
- OFH.CA: score=22.26 buy_ready=False sector_rank=16 price=1.09 support=0.83 resistance=1.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=75.31 liquidity=54269504.0 spike=0.43
- OIH.CA: score=23.9 buy_ready=False sector_rank=6 price=2.07 support=1.62 resistance=2.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:56 PM market time freshness=DELAYED_CURRENT RSI=71.67 liquidity=119632152.0 spike=0.8
- OLFI.CA: score=17.27 buy_ready=False sector_rank=17 price=23.19 support=22.07 resistance=26.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:56 PM market time freshness=DELAYED_CURRENT RSI=36.94 liquidity=7200802.0 spike=0.13
- ORAS.CA: score=9.1 buy_ready=False sector_rank=21 price=850.03 support=839.94 resistance=859.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:56 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=83107232.0 spike=1.0
- ORHD.CA: score=27.5 buy_ready=True sector_rank=15 price=42.3 support=40.28 resistance=43.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:56 PM market time freshness=DELAYED_CURRENT RSI=53.53 liquidity=91260696.0 spike=0.64
- ORWE.CA: score=30.9 buy_ready=False sector_rank=1 price=28.26 support=24.5 resistance=29.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=71.72 liquidity=26788142.0 spike=0.28
- PHAR.CA: score=22.66 buy_ready=False sector_rank=20 price=128.79 support=124.5 resistance=178.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=36.9 liquidity=93566864.0 spike=0.24
- PHDC.CA: score=20.5 buy_ready=False sector_rank=15 price=14.68 support=14.4 resistance=16.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:56 PM market time freshness=DELAYED_CURRENT RSI=36.72 liquidity=89479840.0 spike=0.37
- PHTV.CA: score=13.94 buy_ready=False sector_rank=16 price=349.07 support=311.27 resistance=447.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:46 PM market time freshness=DELAYED_CURRENT RSI=49.44 liquidity=687551.25 spike=0.29
- POUL.CA: score=27.07 buy_ready=True sector_rank=17 price=38.84 support=36.97 resistance=40.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:56 PM market time freshness=DELAYED_CURRENT RSI=59.81 liquidity=10305820.0 spike=0.43
- PRCL.CA: score=17.46 buy_ready=False sector_rank=4 price=32.82 support=30.9 resistance=36.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:56 PM market time freshness=DELAYED_CURRENT RSI=39.75 liquidity=6561131.5 spike=0.28
- PRDC.CA: score=20.5 buy_ready=False sector_rank=15 price=8.42 support=8.7 resistance=10.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=46.41 liquidity=24794324.0 spike=0.34
- PRMH.CA: score=20.04 buy_ready=True sector_rank=16 price=2.79 support=2.28 resistance=2.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=59.55 liquidity=2788477.5 spike=0.18
- RACC.CA: score=27.26 buy_ready=True sector_rank=16 price=10.13 support=9.4 resistance=10.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=46.97 liquidity=20818210.0 spike=0.83
- RAKT.CA: score=4.42 buy_ready=False sector_rank=16 price=22.2 support=21.4 resistance=24.0 source=Yahoo Finance as_of=2026-09-05T21:00:00+00:00 freshness=FRESH RSI=34.53 liquidity=160173.01 spike=0.58
- RAYA.CA: score=26.64 buy_ready=False sector_rank=13 price=7.25 support=6.95 resistance=7.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=60.0 liquidity=25918336.0 spike=0.36
- RMDA.CA: score=10.48 buy_ready=False sector_rank=20 price=6.5 support=6.27 resistance=6.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=128394592.0 spike=1.41
- ROTO.CA: score=8.6 buy_ready=False sector_rank=16 price=43.5 support=43.01 resistance=52.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=14.45 liquidity=3339040.5 spike=0.18
- RREI.CA: score=21.73 buy_ready=False sector_rank=16 price=4.38 support=4.24 resistance=5.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=41.61 liquidity=8471998.0 spike=0.24
- RTVC.CA: score=15.05 buy_ready=False sector_rank=16 price=4.01 support=3.76 resistance=4.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=61.61 liquidity=1796353.75 spike=0.23
- RUBX.CA: score=27.84 buy_ready=True sector_rank=16 price=13.04 support=12.2 resistance=13.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=37.46 liquidity=40541668.0 spike=2.29
- SAUD.CA: score=19.5 buy_ready=True sector_rank=5 price=23.62 support=22.13 resistance=24.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:56 PM market time freshness=DELAYED_CURRENT RSI=56.81 liquidity=3604761.0 spike=0.18
- SCEM.CA: score=20.9 buy_ready=False sector_rank=4 price=100.06 support=79.0 resistance=113.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=34.68 liquidity=82034808.0 spike=0.36
- SCFM.CA: score=19.83 buy_ready=False sector_rank=16 price=280.5 support=270.55 resistance=305.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=41.18 liquidity=6570456.0 spike=0.49
- SCTS.CA: score=15.13 buy_ready=False sector_rank=8 price=617.14 support=609.02 resistance=660.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:56 PM market time freshness=DELAYED_CURRENT RSI=51.58 liquidity=1229114.5 spike=0.14
- SDTI.CA: score=11.32 buy_ready=False sector_rank=16 price=75.0 support=72.0 resistance=75.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:56 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=35475696.0 spike=1.53
- SEIG.CA: score=14.86 buy_ready=False sector_rank=16 price=255.78 support=256.01 resistance=293.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:50 PM market time freshness=DELAYED_CURRENT RSI=39.18 liquidity=1608828.25 spike=0.49
- SIPC.CA: score=10.66 buy_ready=False sector_rank=16 price=5.78 support=5.75 resistance=6.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=60210564.0 spike=1.2
- SKPC.CA: score=24.8 buy_ready=False sector_rank=10 price=18.95 support=16.3 resistance=19.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:56 PM market time freshness=DELAYED_CURRENT RSI=76.84 liquidity=232752000.0 spike=1.95
- SMFR.CA: score=11.54 buy_ready=False sector_rank=16 price=260.66 support=252.0 resistance=274.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=42316012.0 spike=1.64
- SNFC.CA: score=24.03 buy_ready=False sector_rank=16 price=10.86 support=10.26 resistance=11.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=38.92 liquidity=9774461.0 spike=0.66
- SPIN.CA: score=24.88 buy_ready=True sector_rank=1 price=19.3 support=15.32 resistance=21.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:56 PM market time freshness=DELAYED_CURRENT RSI=45.17 liquidity=5977661.0 spike=0.15
- SPMD.CA: score=15.05 buy_ready=False sector_rank=16 price=0.46 support=0.44 resistance=0.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=44.33 liquidity=4792101.0 spike=0.33
- SUGR.CA: score=26.25 buy_ready=False sector_rank=17 price=62.96 support=47.74 resistance=62.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=70.13 liquidity=107034440.0 spike=1.59
- SVCE.CA: score=25.26 buy_ready=True sector_rank=16 price=12.65 support=9.27 resistance=13.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=69.57 liquidity=188685344.0 spike=0.99
- SWDY.CA: score=27.94 buy_ready=True sector_rank=7 price=134.7 support=106.51 resistance=139.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:56 PM market time freshness=DELAYED_CURRENT RSI=67.31 liquidity=117307304.0 spike=1.02
- TALM.CA: score=18.89 buy_ready=False sector_rank=8 price=18.6 support=17.11 resistance=20.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:53 PM market time freshness=DELAYED_CURRENT RSI=39.0 liquidity=4990299.0 spike=0.18
- TMGH.CA: score=27.5 buy_ready=True sector_rank=15 price=98.6 support=94.9 resistance=100.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:56 PM market time freshness=DELAYED_CURRENT RSI=68.42 liquidity=160875056.0 spike=0.58
- TRTO.CA: score=15.27 buy_ready=False sector_rank=16 price=0.07 support=0.03 resistance=0.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:40 PM market time freshness=DELAYED_CURRENT RSI=73.81 liquidity=18527.81 spike=0.65
- UEFM.CA: score=14.22 buy_ready=False sector_rank=16 price=539.93 support=516.1 resistance=540.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:52 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=11524900.0 spike=2.98
- UEGC.CA: score=15.26 buy_ready=False sector_rank=16 price=1.75 support=1.66 resistance=2.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=21.67 liquidity=23232866.0 spike=0.47
- UNIP.CA: score=25.26 buy_ready=True sector_rank=16 price=0.39 support=0.35 resistance=0.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=49.21 liquidity=16967038.0 spike=0.48
- UNIT.CA: score=18.43 buy_ready=False sector_rank=15 price=18.99 support=17.8 resistance=23.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:53 PM market time freshness=DELAYED_CURRENT RSI=43.58 liquidity=4930116.5 spike=0.47
- WCDF.CA: score=24.37 buy_ready=False sector_rank=16 price=690.48 support=582.69 resistance=700.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=75.97 liquidity=7876089.5 spike=2.12
- WKOL.CA: score=17.54 buy_ready=False sector_rank=16 price=345.47 support=321.01 resistance=390.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=28.84 liquidity=7287908.0 spike=0.3
- ZEOT.CA: score=19.68 buy_ready=True sector_rank=16 price=14.27 support=12.52 resistance=14.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:56 PM market time freshness=DELAYED_CURRENT RSI=47.22 liquidity=4422878.5 spike=0.24
- ZMID.CA: score=24.5 buy_ready=False sector_rank=15 price=9.4 support=7.25 resistance=9.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=85.23 liquidity=102868512.0 spike=0.4

## Backtesting Lite
- GIHD.CA: 180d return=38.0%, max drawdown=-34.73%, MA20>MA50 days last20=20, as_of=2026-09-05T21:00:00+00:00
- ETEL.CA: 180d return=91.22%, max drawdown=-30.44%, MA20>MA50 days last20=20, as_of=2026-09-05T21:00:00+00:00
- ACGC.CA: 180d return=79.14%, max drawdown=-15.74%, MA20>MA50 days last20=20, as_of=2026-09-05T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- GIHD.CA: status=RECENT_ACCEPTED latest=2026-08-12 age_days=27 sources=3 expected=Gharbia Islamic Housing Development Company summary=Gharbia Islamic Housing Development Company has shown positive financial performance and active corporate governance within the last 12 months. The company reported financial results for Q1 and H1 2026, and its stock price has seen significant appreciation.
  - GIHD Financials - Latest Release May 24, 2026 (EPS/Revenue): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEaAK9SYch6CVLDRN1pykMjlDMrRos1WTneth_WzuDQZ4iBYar_6VcuvzXm_TYf6n3wIhn5YUgBay4WylzPja2U8k6-bJpt-3YUxKq25N4tR9RMNkmVdvpqjTpMEFvroXRdY5H5sY1RZTs0ZT2ipYR469fadXUUGDcsg2XbCg==
  - Gharbia Islamic Housing Development (GIHD.CA) Reports Financial Results for H1 2026 (August 12, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFKcCf21hJ0xGDaBH2fYk4ETckaaa85pw7kdJinxd_Z81ppYSZDLGjmLFIjD2s0vIw40-aOCR7Nl2aQevo__zJAKzPBkeEXUBv-f6yiBCRvq0u0wA7SMh8SROhhhcjXes16L4vQrZ8=
  - Gharbia Islamic Housing Development (GIHD.CA) Reports Financial Results for Q1 2026 (May 25, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFKcCf21hJ0xGDaBH2fYk4ETckaaa85pw7kdJinxd_Z81ppYSZDLGjmLFIjD2s0vIw40-aOCR7Nl2aQevo__zJAKzPBkeEXUBv-f6yiBCRvq0u0wA7SMh8SROhhhcjXes16L4vQrZ8=
- ETEL.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Telecom Egypt summary=Evidence rejected for ETEL.CA: source text did not clearly match ETEL.CA / Telecom Egypt.
- ACGC.CA: status=RECENT_ACCEPTED latest=2026-08-11 age_days=28 sources=3 expected=Arab Cotton Ginning summary=Arab Cotton Ginning has experienced a significant stock price increase over the last year. However, the company faced a penalty from the EGX Listing Committee in June 2026 for delays in submitting financial statements.
  - Arabia Cotton Ginning Company (EGX:ACGC) Stock Price Increased by +32.43% in Last 52 Weeks (August 11, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGa6mDfGMshh9gXWNHtObJ58gJyDSMiSDA_qeItmNEZVjE4HG-3SxoEJR-b-C6J6vADhIpE5zb2c7px7vuQejhO12SNRtP9xhkUvkNfGKirhhpg0z15TOC_k_tLXT_hQazUwf6Xy0qT8w79knGxVQ==
  - Arab Cotton Ginning (ACGC.CA) - Listing Committee Decision on Penalty for Delayed Financial Statements (June 23, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHjrXvztfBrGsOopu_T8Xo8Sb1oENfcm442KN332V3gqmOD4fOfJ7knRW04WMTSUND481BYMiQiXYJkDkakTv7K4qmIOUhnP-gNiwKiYNDpamITYS1wwEIbrwXcK1fiEPymRBGO7XojVLg9pvg89ePmyyI=
  - Arabia Cotton Ginning Company (EGX:ACGC) Financials Overview (September 30, 2025): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFibYzm29PjbH8vQwBi7RQEcYsUF1NKLBDgEF2Ohj-YyGxJ6ndunXZQdoRC6Z466_E6NTyTODCul70pHYev2PB9SF2oaE3PnDI95HkAniItrYxlZli8sdbgucRnxMfH24SfVXyixwe7VD2YqvTgpw==
- ORWE.CA: status=RECENT_ACCEPTED latest=2026-09-04 age_days=4 sources=3 expected=Oriental Weavers summary=Oriental Weavers has shown a positive stock price change over the last 52 weeks and reported revenue and profits in the last 12 months.
  - Oriental Weavers Carpets Company (S.A.E) (EGX:ORWE) Stock Price Increased by +20.73% in Last 52 Weeks (September 04, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE46jH4AKsc55gbJCoxZjDCjQlA7KbuA3isaHI-Oaagqab9aDZacq6EwDtN15SUBvwiOdbEDWtpo17EXPX5zbPKTVpjM5b9KcIFvy_wR3ASEdp0Gx5PIFUZBL7U3YeShO1nA8sOCPDC-7EXX5drVA==
  - Oriental Weavers Carpets Company (S.A.E) (EGX:ORWE) Financials Overview (June 30, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEXBQJDNaRbMwVjK21LC3kcjdca5EAZ1sqhDRGub3AnkiKoJpJNROX4dZTaxjGcnbQkBAcJwRXEy5Qf08drdWmDKdmOVnSnlGcS8j-sZRBWT9oY715RaeM6YReOH7BXhXUYM5Zm25mfq3KCEAlVuQ==
  - Oriental Weavers (EGX:ORWE) Key Ratios including 5.82% Dividend Yield: https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGyOGYunMDgXRn5WQBLC1uypTYoJC7Sj8kgmZU1PTsRGYGj0blt6PZhqG7YAEBckfZOdLSXYnb8Shd8cAIZEIgxU_LObMgvXu3OyxccZVkd6ghNAp6mbim8oDsb9Fp51wBsWRGgVJ7e9Ik3Plpz25zsplRx5XQ9f6brt5WP8Q==
- CANA.CA: status=RECENT_ACCEPTED latest=2026-01-01 age_days=250 sources=3 expected=Suez Canal Bank summary=Suez Canal Bank has reported strong financial results for Q1 2026 and FY 2025, with significant profit increases. The stock has also seen substantial growth over the last year, and the bank is actively engaged in corporate announcements.
  - Suez Canal Bank (CANA.CA) - Market Announcements (August 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFuTBzJnVrAEgPdt6Ws65es0xWK6FHllY6qk9duwPNmxvZ1D3FpHd0qjVZuYQQSImN_riGqN1OkYKrYBG9fPsLgKNuL-IE2NJp-IFHCBng4PwN8RGtNKh6ERpciSOBF03QsqR6SZVuCtAGcCo_3ZOzN
  - Suez Canal Bank delivers EGP 1.6bn profits in Q1-26 (Mubasher Info): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFuTBzJnVrAEgPdt6Ws65es0xWK6FHllY6qk9duwPNmxvZ1D3FpHd0qjVZuYQQSImN_riGqN1OkYKrYBG9fPsLgKNuL-IE2NJp-IFHCBng4PwN8RGtNKh6ERpciSOBF03QsqR6SZVuCtAGcCo_3ZOzN
  - Suez Canal Bank's net profits hit EGP 6.4bn in 2025 (Mubasher Info): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFuTBzJnVrAEgPdt6Ws65es0xWK6FHllY6qk9duwPNmxvZ1D3FpHd0qjVZuYQQSImN_riGqN1OkYKrYBG9fPsLgKNuL-IE2NJp-IFHCBng4PwN8RGtNKh6ERpciSOBF03QsqR6SZVuCtAGcCo_3ZOzN
- COMI.CA: status=RECENT_ACCEPTED latest=2026-07-21 age_days=49 sources=3 expected=Commercial International Bank Egypt summary=Commercial International Bank Egypt has reported strong financial results for Q1 and H1 2026, demonstrating significant net income growth. The bank is actively engaged in market announcements and is a highly traded stock on the EGX.
  - Commercial International Bank (EGX:COMI) Reported H1 2026 Consolidated Net Income of EGP 39.3 Billion (July 21, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEfndmFg88NoYrgMg2s7-KusEol2wUptwQazEQUsAKMi-z9jhU1Oz6sKVE63NZw02f322pKoG9QfZ7Dqb3jKDwcNIJAZgN0L3cuh1VcoNhiGFs7arZQ5kqxXzhPkOpUnSkSKAmwnxpxrA==
  - Commercial International Bank (EGX:COMI) Reported Q1 2026 Net Income of EGP 17.8 Billion (May 12, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEfndmFg88NoYrgMg2s7-KusEol2wUptwQazEQUsAKMi-z9jhU1Oz6sKVE63NZw02f322pKoG9QfZ7Dqb3jKDwcNIJAZgN0L3cuh1VcoNhiGFs7arZQ5kqxXzhPkOpUnSkSKAmwnxpxrA==
  - Commercial International Bank-Egypt (CIB) (COMI.CA) Reports Financial Results (Consolidated) for H1 2026 (July 21, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGN8skOhsNe7zNAtu-4dpz7vZmHCLKEUKjq38LH5puPauYM6tMgKGWMM7O07ki-PYcesLuVD_MXpUIlqmBpGx3WuGpnAz0Gho9RfWlbt9nV4lA_PYWpwyzh6ZVAAOrBX34JjxDPb0ejOL6c8zyV3mSQNl9ibefePcTSZfp57uI=
- FWRY.CA: status=RECENT_ACCEPTED latest=2026-07-19 age_days=51 sources=3 expected=Fawry For Banking Technology and Electronic Payments summary=Fawry For Banking Technology and Electronic Payments has reported strong financial results for Q1 2026 and FY 2025, with significant revenue and profit growth. The company has also been active in strategic investments and securing financing facilities.
  - Fawry records EGP 2.4bn consolidated revenues in Q1-26 (Mubasher Info): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEisQcp6VLoxZua0w_ELzCKR53346MehM5gFTdtRpp9z7Ucu0JWSVMzlIZVjJhm_HtmnTKjyBbM-wfY8UA30NKKyE3_m_-AQGYtuulIxldkPp50okloAnozMwDc28x_CKoS_TXM745cpivlyN_EDYcD
  - Fawry logs higher consolidated profits at EGP 3bn in 2025 (Mubasher Info): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEisQcp6VLoxZua0w_ELzCKR53346MehM5gFTdtRpp9z7Ucu0JWSVMzlIZVjJhm_HtmnTKjyBbM-wfY8UA30NKKyE3_m_-AQGYtuulIxldkPp50okloAnozMwDc28x_CKoS_TXM745cpivlyN_EDYcD
  - Fawry For Banking Technology And Electronic Payment (FWRY.CA) - Release Regarding the Obtaining of a Financing Facility (July 19, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEisQcp6VLoxZua0w_ELzCKR53346MehM5gFTdtRpp9z7Ucu0JWSVMzlIZVjJhm_HtmnTKjyBbM-wfY8UA30NKKyE3_m_-AQGYtuulIxldkPp50okloAnozMwDc28x_CKoS_TXM745cpivlyN_EDYcD
- CIEB.CA: status=RECENT_ACCEPTED latest=2026-07-29 age_days=41 sources=3 expected=Credit Agricole Egypt summary=Credit Agricole Egypt has reported strong consolidated profits for Q1 2026 and disbursed dividends for 2025. The bank is actively engaged in corporate announcements and its shares are traded on the Egyptian Exchange.
  - Crédit Agricole Egypt's consolidated profits exceed EGP 1.7bn in Q1-26 (Mubasher Info): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHCjkH8o2csOTSiz95N2IRplSeRa5iglyTiyAXFQ64f2Dqun8aFC5rlCumtYpHe501YgESmZHDK5OM1umeClXix5XQhfQkS_NYg0vDiSH6P6ekT4NVB-botu1ohZ-ejnR3X1STKF1ezCH-Qos6iF9pA
  - Crédit Agricole Egypt to disburse EGP 4.1bn dividends for 2025 (Mubasher Info): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHCjkH8o2csOTSiz95N2IRplSeRa5iglyTiyAXFQ64f2Dqun8aFC5rlCumtYpHe501YgESmZHDK5OM1umeClXix5XQhfQkS_NYg0vDiSH6P6ekT4NVB-botu1ohZ-ejnR3X1STKF1ezCH-Qos6iF9pA
  - Release from Credit Agricole Egypt (CIEB.CA) Regarding the Financial Results (July 29, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHCjkH8o2csOTSiz95N2IRplSeRa5iglyTiyAXFQ64f2Dqun8aFC5rlCumtYpHe501YgESmZHDK5OM1umeClXix5XQhfQkS_NYg0vDiSH6P6ekT4NVB-botu1ohZ-ejnR3X1STKF1ezCH-Qos6iF9pA

## Warnings
- Evidence rejected for ETEL.CA: source text did not clearly match ETEL.CA / Telecom Egypt.
