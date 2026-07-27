# Telegram-First EGX Scanner Report

Scan phase: Open liquidity confirmation
Generated UTC: 2026-07-27T10:10:33.864107+00:00
Generated Cairo: 2026-07-27 13:10
Run timing: target 09:15 Cairo | generated Cairo 2026-07-27 13:10 | cron 15 6 * * 0-4
Trigger: scheduled cron=15 6 * * 0-4 mapped to open_confirm; Cairo now 2026-07-27 13:06

## Control Center
- Action tickets: 3 prioritized signal(s)
- BUY-ready candidates: 71
- Data quality issues: 1
- Tradeable price/liquidity tickers: 176/189
- Top sector: Building Materials

## Market Context
- Market trend: Bullish
- Source: Mubasher EGX market page (delayed public data)
- As of: Monday, July 27
- Freshness: DELAYED
- EGX30 regime: MIXED / above MA20 65.0% / above MA50 55.0%
- EGX70 regime: MIXED / above MA20 75.68% / above MA50 75.68%
- Sector breadth: 52.38%
- Risk mode: SELECTIVE_SWING_TRADES_ONLY

## Top Liquidity
- CCAP.CA: liquidity=458775488.0 spike=0.66 score=26.4
- COMI.CA: liquidity=283864672.0 spike=0.69 score=24.4
- PHAR.CA: liquidity=262930704.0 spike=9.12 score=14.4
- ZMID.CA: liquidity=216795104.0 spike=0.91 score=24.4
- ADIB.CA: liquidity=210073232.0 spike=1.81 score=28.02

## AI Narrative
- Provider: OpenRouter OK
- Model: nvidia/nemotron-3-super-120b-a12b:free
- Summary: Scanner prioritized tickets (ARCC.CA, AJWA.CA, IFAP.CA) mixed 5‑day returns, advise verification before action.

We need 3-5 bullets; we can do 4 or 5. Let's do 4 bullets.

Make sure no mention of quantities or position sizing. No trade decision. Just narrative.

Return only JSON.

Let

{
  

## Top Liquidity Spikes
- PHAR.CA: spike=9.12 liquidity=262930704.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- AJWA.CA: spike=7.33 liquidity=105489856.0 outlook=BULLISH_WATCH score=89.21 buy_ready=True
- SPIN.CA: spike=6.63 liquidity=102521120.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- ASPI.CA: spike=4.7 liquidity=127759952.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- SIPC.CA: spike=3.76 liquidity=55007372.0 outlook=BULLISH_WATCH score=71.21 buy_ready=False

## Sector Leaderboard
- #1 Building Materials: score=10.11 5d=3.41% 20d=13.39% aboveMA50=83.33%
- #2 Industrial Goods & Cables: score=9.54 5d=2.93% 20d=7.02% aboveMA50=100.0%
- #3 Telecommunications: score=8.4 5d=2.4% 20d=5.67% aboveMA50=100.0%
- #4 Textiles: score=8.35 5d=3.06% 20d=5.9% aboveMA50=75.0%
- #5 General / Verified EGX Expansion: score=8.21 5d=1.85% 20d=9.19% aboveMA50=77.67%
- #6 Agriculture & Food Production: score=8.19 5d=1.81% 20d=1.8% aboveMA50=100.0%
- #7 Investment Holding: score=8.01 5d=1.84% 20d=6.43% aboveMA50=100.0%
- #8 Banking & Financials: score=7.96 5d=3.15% 20d=3.71% aboveMA50=80.0%

## Today's Prioritized Action Tickets
- Priority #1: BUY ARCC.CA
  - Entry: 56.5 | Take profit: 60.6 | Stop loss: 54.45
  - Confidence: LOW | score=29.4 | outlook=BULLISH_WATCH 90
  - Reason: BUY SETUP: ARCC.CA has aligned current price data, liquidity above threshold, price above MA20/MA50, RSI 53.22, support 53.5, resistance 58.5, and evidence sources. Macro trend is Bullish; market regime is SELECTIVE_SWING_TRADES_ONLY; verify price action in Thndr before treating it as a swing entry.
- Priority #2: BUY AJWA.CA
  - Entry: 187.49 | Take profit: 202.49 | Stop loss: 179.99
  - Confidence: LOW | score=29.4 | outlook=BULLISH_WATCH 89.21
  - Reason: BUY SETUP: AJWA.CA has aligned current price data, liquidity above threshold, price above MA20/MA50, RSI 50.49, support 161.0, resistance 192.0, and evidence sources. Macro trend is Bullish; market regime is SELECTIVE_SWING_TRADES_ONLY; verify price action in Thndr before treating it as a swing entry.
- Priority #3: BUY IFAP.CA
  - Entry: 19.76 | Take profit: 21.28 | Stop loss: 19.0
  - Confidence: LOW | score=28.66 | outlook=BULLISH_WATCH 91.19
  - Reason: BUY SETUP: IFAP.CA has aligned current price data, liquidity above threshold, price above MA20/MA50, RSI 57.38, support 18.47, resistance 20.28, and evidence sources. Macro trend is Bullish; market regime is SELECTIVE_SWING_TRADES_ONLY; verify price action in Thndr before treating it as a swing entry.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- IDRE.CA: BULLISH_WATCH score=91.21 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended; far above support
- IFAP.CA: BULLISH_WATCH score=91.19 liquidity=TRADEABLE sector=IMPROVING risk=No major short-term scanner risk flags.
- ARCC.CA: BULLISH_WATCH score=90 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- AJWA.CA: BULLISH_WATCH score=89.21 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=No major short-term scanner risk flags.
- EALR.CA: BULLISH_WATCH score=89.21 liquidity=TRADEABLE sector=IMPROVING risk=No major short-term scanner risk flags.
- WCDF.CA: BULLISH_WATCH score=87.21 liquidity=TRADEABLE sector=IMPROVING risk=momentum is extended
- ECAP.CA: BULLISH_WATCH score=86.21 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- MOED.CA: BULLISH_WATCH score=84.21 liquidity=TRADEABLE sector=IMPROVING risk=No major short-term scanner risk flags.
- CEFM.CA: BULLISH_WATCH score=83.21 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended; far above support
- EASB.CA: BULLISH_WATCH score=83.21 liquidity=TRADEABLE sector=IMPROVING risk=No major short-term scanner risk flags.

## BUY-Ready Candidates
- IDRE.CA: rank=30.22 outlook=BULLISH_WATCH outlook_score=91.21 sector_rank=5 price=49.92 support=41.1 resistance=52.68 liquidity=42923912.0
- ARCC.CA: rank=29.4 outlook=BULLISH_WATCH outlook_score=90 sector_rank=1 price=56.5 support=53.5 resistance=58.5 liquidity=14724846.0
- AJWA.CA: rank=29.4 outlook=BULLISH_WATCH outlook_score=89.21 sector_rank=5 price=187.49 support=161.0 resistance=192.0 liquidity=105489856.0
- RMDA.CA: rank=29.38 outlook=BULLISH_WATCH outlook_score=78.11 sector_rank=13 price=5.13 support=4.81 resistance=5.17 liquidity=30531938.0
- IFAP.CA: rank=28.66 outlook=BULLISH_WATCH outlook_score=91.19 sector_rank=6 price=19.76 support=18.47 resistance=20.28 liquidity=10008321.0
- ELSH.CA: rank=28.4 outlook=CONSTRUCTIVE outlook_score=68.21 sector_rank=5 price=15.08 support=11.1 resistance=15.59 liquidity=60095620.0
- ADIB.CA: rank=28.02 outlook=BULLISH_WATCH outlook_score=75.96 sector_rank=8 price=51.33 support=44.1 resistance=49.87 liquidity=210073232.0
- PRCL.CA: rank=27.4 outlook=BULLISH_WATCH outlook_score=80 sector_rank=1 price=36.5 support=29.15 resistance=38.25 liquidity=30732928.0
- TMGH.CA: rank=26.4 outlook=BULLISH_WATCH outlook_score=72.02 sector_rank=11 price=99.53 support=92.1 resistance=103.87 liquidity=58288116.0
- PRDC.CA: rank=26.4 outlook=CONSTRUCTIVE outlook_score=60.02 sector_rank=11 price=9.41 support=6.8 resistance=10.4 liquidity=31835490.0

## Data Quality Issues
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=26.4 buy_ready=False sector_rank=5 price=247.9 support=196.0 resistance=253.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=70.31 liquidity=18149636.0 spike=0.96
- ABUK.CA: score=22.19 buy_ready=False sector_rank=17 price=71.21 support=66.66 resistance=75.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=53.74 liquidity=41218180.0 spike=0.27
- ACAMD.CA: score=24.4 buy_ready=True sector_rank=5 price=2.41 support=2.14 resistance=2.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=66.67 liquidity=23662794.0 spike=0.31
- ACGC.CA: score=25.44 buy_ready=False sector_rank=4 price=10.85 support=8.92 resistance=11.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=74.82 liquidity=42661980.0 spike=1.52
- ADCI.CA: score=25.36 buy_ready=True sector_rank=5 price=262.2 support=230.0 resistance=266.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:47 AM market time freshness=DELAYED_CURRENT RSI=68.4 liquidity=15914994.0 spike=1.48
- ADIB.CA: score=28.02 buy_ready=True sector_rank=8 price=51.33 support=44.1 resistance=49.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=63.07 liquidity=210073232.0 spike=1.81
- ADPC.CA: score=21.4 buy_ready=False sector_rank=5 price=4.09 support=3.32 resistance=4.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=77.17 liquidity=19285504.0 spike=0.61
- AFDI.CA: score=25.1 buy_ready=True sector_rank=5 price=49.29 support=41.84 resistance=49.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:46 AM market time freshness=DELAYED_CURRENT RSI=69.03 liquidity=19445352.0 spike=1.35
- AFMC.CA: score=14.4 buy_ready=False sector_rank=5 price=114.89 support=102.11 resistance=116.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=99445192.0 spike=3.7
- AJWA.CA: score=29.4 buy_ready=True sector_rank=5 price=187.49 support=161.0 resistance=192.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=50.49 liquidity=105489856.0 spike=7.33
- ALCN.CA: score=21.81 buy_ready=True sector_rank=12 price=29.49 support=27.7 resistance=30.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=69.59 liquidity=7408915.5 spike=0.34
- ALUM.CA: score=17.13 buy_ready=True sector_rank=5 price=23.52 support=20.55 resistance=24.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:45 AM market time freshness=DELAYED_CURRENT RSI=67.09 liquidity=2731355.25 spike=0.41
- AMER.CA: score=23.4 buy_ready=False sector_rank=11 price=4.36 support=2.28 resistance=4.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=89.73 liquidity=61807020.0 spike=0.6
- AMES.CA: score=10.28 buy_ready=False sector_rank=5 price=129.07 support=118.25 resistance=136.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=142329392.0 spike=1.44
- AMIA.CA: score=18.21 buy_ready=False sector_rank=5 price=10.42 support=8.4 resistance=10.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=72.62 liquidity=3810635.5 spike=0.29
- AMOC.CA: score=24.4 buy_ready=True sector_rank=10 price=8.3 support=7.42 resistance=8.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=65.27 liquidity=24662132.0 spike=0.42
- APSW.CA: score=22.54 buy_ready=True sector_rank=5 price=9.16 support=8.0 resistance=9.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=55.83 liquidity=3522476.5 spike=2.31
- ARAB.CA: score=22.4 buy_ready=True sector_rank=11 price=0.25 support=0.2 resistance=0.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=66.67 liquidity=64458396.0 spike=0.49
- ARCC.CA: score=29.4 buy_ready=True sector_rank=1 price=56.5 support=53.5 resistance=58.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:47 AM market time freshness=DELAYED_CURRENT RSI=53.22 liquidity=14724846.0 spike=0.59
- AREH.CA: score=18.96 buy_ready=False sector_rank=5 price=1.49 support=1.44 resistance=1.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=41.82 liquidity=9562900.0 spike=0.29
- ARVA.CA: score=24.68 buy_ready=False sector_rank=5 price=12.35 support=10.5 resistance=12.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=76.51 liquidity=39411700.0 spike=1.64
- ASCM.CA: score=24.4 buy_ready=True sector_rank=5 price=61.99 support=56.29 resistance=64.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=55.41 liquidity=16792540.0 spike=0.34
- ASPI.CA: score=14.4 buy_ready=False sector_rank=5 price=0.45 support=0.39 resistance=0.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=127759952.0 spike=4.7
- ATLC.CA: score=14.03 buy_ready=False sector_rank=14 price=5.2 support=4.92 resistance=5.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:45 AM market time freshness=DELAYED_CURRENT RSI=45.07 liquidity=1938006.63 spike=0.28
- ATQA.CA: score=25.19 buy_ready=True sector_rank=17 price=9.89 support=9.35 resistance=10.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=66.09 liquidity=19534962.0 spike=0.58
- AXPH.CA: score=17.43 buy_ready=True sector_rank=5 price=1221.22 support=1075.0 resistance=1342.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=55.62 liquidity=1034560.31 spike=0.27
- BINV.CA: score=13.26 buy_ready=False sector_rank=7 price=47.49 support=44.98 resistance=51.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:47 AM market time freshness=DELAYED_CURRENT RSI=50.94 liquidity=863904.75 spike=0.12
- BIOC.CA: score=12.2 buy_ready=False sector_rank=5 price=142.8 support=119.32 resistance=142.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=76701096.0 spike=2.4
- BTFH.CA: score=22.09 buy_ready=True sector_rank=14 price=3.07 support=2.91 resistance=3.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=57.78 liquidity=197839184.0 spike=0.95
- CAED.CA: score=13.66 buy_ready=False sector_rank=5 price=136.58 support=120.02 resistance=143.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=164392512.0 spike=3.13
- CANA.CA: score=26.4 buy_ready=True sector_rank=8 price=38.29 support=34.7 resistance=38.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=66.3 liquidity=13645081.0 spike=0.86
- CCAP.CA: score=26.4 buy_ready=False sector_rank=7 price=5.47 support=4.65 resistance=5.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=72.22 liquidity=458775488.0 spike=0.66
- CCRS.CA: score=21.04 buy_ready=True sector_rank=5 price=2.66 support=2.18 resistance=2.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=69.01 liquidity=6637698.0 spike=0.38
- CEFM.CA: score=26.2 buy_ready=True sector_rank=5 price=125.53 support=95.75 resistance=152.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=65.03 liquidity=27360204.0 spike=1.9
- CERA.CA: score=22.86 buy_ready=True sector_rank=5 price=1.36 support=1.19 resistance=1.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:47 AM market time freshness=DELAYED_CURRENT RSI=65.79 liquidity=8460267.0 spike=0.34
- CFGH.CA: score=-0.59 buy_ready=False sector_rank=5 price=0.11 support=0.1 resistance=0.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=10699.81 spike=0.73
- CICH.CA: score=19.79 buy_ready=True sector_rank=14 price=12.21 support=11.52 resistance=12.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=54.58 liquidity=3701357.0 spike=0.71
- CIEB.CA: score=16.81 buy_ready=True sector_rank=8 price=24.22 support=23.3 resistance=24.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:47 AM market time freshness=DELAYED_CURRENT RSI=43.55 liquidity=2409035.5 spike=0.3
- CIRA.CA: score=10.5 buy_ready=False sector_rank=16 price=33.46 support=31.8 resistance=33.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=72522104.0 spike=2.04
- CLHO.CA: score=24.4 buy_ready=True sector_rank=13 price=16.95 support=15.9 resistance=17.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=56.49 liquidity=37459252.0 spike=0.86
- CNFN.CA: score=21.49 buy_ready=True sector_rank=14 price=4.86 support=4.61 resistance=5.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=60.0 liquidity=7403802.0 spike=0.32
- COMI.CA: score=24.4 buy_ready=True sector_rank=8 price=140.74 support=126.21 resistance=140.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=66.21 liquidity=283864672.0 spike=0.69
- COPR.CA: score=23.68 buy_ready=False sector_rank=5 price=0.41 support=0.35 resistance=0.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=83.91 liquidity=44524860.0 spike=1.64
- COSG.CA: score=21.4 buy_ready=False sector_rank=5 price=1.71 support=1.47 resistance=1.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=80.77 liquidity=13347964.0 spike=0.31
- CPCI.CA: score=17.27 buy_ready=False sector_rank=5 price=467.09 support=370.01 resistance=512.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=72.77 liquidity=2872569.75 spike=0.25
- CSAG.CA: score=19.69 buy_ready=True sector_rank=12 price=32.85 support=31.3 resistance=34.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=53.28 liquidity=3294170.25 spike=0.16
- DAPH.CA: score=23.4 buy_ready=False sector_rank=5 price=95.26 support=78.52 resistance=98.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=75.22 liquidity=17030888.0 spike=0.94
- DEIN.CA: score=-0.6 buy_ready=False sector_rank=5 price=11.38 support=13.65 resistance=13.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 June 12:11 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=40.95 spike=0.01
- DOMT.CA: score=12.1 buy_ready=False sector_rank=18 price=26.88 support=26.06 resistance=27.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=46.55 liquidity=980611.31 spike=0.27
- DSCW.CA: score=21.4 buy_ready=False sector_rank=5 price=1.94 support=1.71 resistance=2.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=87.1 liquidity=32851978.0 spike=0.65
- DTPP.CA: score=26.4 buy_ready=True sector_rank=5 price=244.14 support=114.67 resistance=273.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=68.78 liquidity=34842064.0 spike=0.5
- EALR.CA: score=26.4 buy_ready=True sector_rank=5 price=371.23 support=332.0 resistance=425.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=61.04 liquidity=16404717.0 spike=0.95
- EASB.CA: score=24.68 buy_ready=True sector_rank=5 price=7.88 support=6.88 resistance=8.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=61.65 liquidity=17629074.0 spike=1.14
- EAST.CA: score=19.12 buy_ready=False sector_rank=18 price=36.4 support=36.11 resistance=38.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:47 AM market time freshness=DELAYED_CURRENT RSI=45.39 liquidity=38045952.0 spike=0.64
- EBSC.CA: score=11.14 buy_ready=False sector_rank=5 price=1.98 support=1.87 resistance=2.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=13037022.0 spike=1.87
- ECAP.CA: score=20.07 buy_ready=True sector_rank=5 price=33.6 support=31.52 resistance=34.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=60.1 liquidity=1671416.75 spike=0.22
- EDFM.CA: score=12.44 buy_ready=False sector_rank=5 price=386.14 support=310.2 resistance=430.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:45 AM market time freshness=DELAYED_CURRENT RSI=82.59 liquidity=1041108.69 spike=0.25
- EEII.CA: score=24.4 buy_ready=True sector_rank=5 price=2.78 support=2.35 resistance=2.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=49.12 liquidity=15686723.0 spike=0.71
- EFIC.CA: score=11.83 buy_ready=False sector_rank=17 price=185.73 support=180.02 resistance=213.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:47 AM market time freshness=DELAYED_CURRENT RSI=53.18 liquidity=2641106.75 spike=0.24
- EFID.CA: score=18.12 buy_ready=False sector_rank=18 price=27.28 support=25.5 resistance=28.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=42.11 liquidity=27383810.0 spike=0.67
- EFIH.CA: score=24.4 buy_ready=True sector_rank=9 price=22.99 support=20.0 resistance=24.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=66.05 liquidity=47887500.0 spike=0.85
- EGAL.CA: score=22.19 buy_ready=False sector_rank=17 price=297.47 support=272.28 resistance=312.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=56.59 liquidity=29213336.0 spike=0.68
- EGAS.CA: score=22.73 buy_ready=True sector_rank=10 price=53.64 support=46.51 resistance=54.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:47 AM market time freshness=DELAYED_CURRENT RSI=67.8 liquidity=8326735.0 spike=0.66
- EGBE.CA: score=15.51 buy_ready=False sector_rank=8 price=0.49 support=-0.34 resistance=0.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=97.71 liquidity=52802.45 spike=2.03
- EGCH.CA: score=22.19 buy_ready=False sector_rank=17 price=13.07 support=12.13 resistance=13.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=55.68 liquidity=51481424.0 spike=0.9
- EGSA.CA: score=12.46 buy_ready=False sector_rank=3 price=8.91 support=8.67 resistance=9.21 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=65.71 liquidity=24990.79 spike=1.52
- EGTS.CA: score=11.53 buy_ready=False sector_rank=11 price=17.73 support=15.1 resistance=19.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=31.59 liquidity=7134733.0 spike=0.15
- EHDR.CA: score=27.38 buy_ready=False sector_rank=5 price=2.99 support=2.37 resistance=3.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=70.33 liquidity=55243776.0 spike=1.49
- EKHO.CA: score=8.4 buy_ready=False sector_rank=10 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-07-25T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=25.4 buy_ready=True sector_rank=2 price=2.22 support=2.04 resistance=2.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=66.67 liquidity=18280818.0 spike=0.28
- ELKA.CA: score=21.4 buy_ready=False sector_rank=5 price=1.95 support=1.19 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=79.21 liquidity=51974672.0 spike=0.75
- ELNA.CA: score=13.16 buy_ready=False sector_rank=5 price=38.58 support=35.55 resistance=40.5 source=Yahoo Finance as_of=2026-07-25T21:00:00+00:00 freshness=FRESH RSI=54.53 liquidity=659486.55 spike=1.05
- ELSH.CA: score=28.4 buy_ready=True sector_rank=5 price=15.08 support=11.1 resistance=15.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=63.2 liquidity=60095620.0 spike=0.44
- ELWA.CA: score=10.5 buy_ready=False sector_rank=5 price=1.91 support=1.87 resistance=2.14 source=Yahoo Finance as_of=2026-07-25T21:00:00+00:00 freshness=FRESH RSI=40.0 liquidity=1103044.08 spike=0.93
- EMFD.CA: score=22.4 buy_ready=False sector_rank=11 price=11.6 support=11.24 resistance=12.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=47.71 liquidity=25529248.0 spike=0.39
- ENGC.CA: score=17.79 buy_ready=False sector_rank=5 price=41.91 support=35.1 resistance=44.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:46 AM market time freshness=DELAYED_CURRENT RSI=70.98 liquidity=3388381.0 spike=0.13
- EOSB.CA: score=14.41 buy_ready=False sector_rank=5 price=1.48 support=1.5 resistance=1.55 source=Yahoo Finance as_of=2026-07-25T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=6979.68 spike=0.16
- EPCO.CA: score=23.4 buy_ready=False sector_rank=5 price=11.37 support=8.5 resistance=11.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=86.46 liquidity=15214169.0 spike=0.55
- EPPK.CA: score=19.37 buy_ready=False sector_rank=5 price=15.26 support=12.37 resistance=15.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT RSI=62.06 liquidity=968496.69 spike=0.72
- ETEL.CA: score=22.4 buy_ready=False sector_rank=3 price=104.32 support=89.01 resistance=106.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=77.8 liquidity=66521448.0 spike=0.89
- ETRS.CA: score=22.4 buy_ready=False sector_rank=5 price=10.72 support=10.25 resistance=11.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=51.11 liquidity=13403999.0 spike=0.23
- EXPA.CA: score=24.4 buy_ready=False sector_rank=8 price=19.9 support=18.03 resistance=20.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=74.78 liquidity=18508520.0 spike=0.61
- FAIT.CA: score=16.73 buy_ready=False sector_rank=8 price=37.41 support=35.06 resistance=38.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:46 AM market time freshness=DELAYED_CURRENT RSI=59.26 liquidity=330399.84 spike=0.11
- FAITA.CA: score=10.47 buy_ready=False sector_rank=8 price=0.96 support=0.96 resistance=0.99 source=Yahoo Finance as_of=2026-07-25T21:00:00+00:00 freshness=FRESH RSI=36.76 liquidity=93572.78 spike=1.99
- FERC.CA: score=24.71 buy_ready=True sector_rank=17 price=77.45 support=72.75 resistance=85.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=57.31 liquidity=13858999.0 spike=1.26
- FWRY.CA: score=23.4 buy_ready=False sector_rank=9 price=19.13 support=18.13 resistance=19.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=57.94 liquidity=36934684.0 spike=0.27
- GBCO.CA: score=21.46 buy_ready=False sector_rank=15 price=30.52 support=29.5 resistance=34.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=48.14 liquidity=20664530.0 spike=0.27
- GDWA.CA: score=20.78 buy_ready=False sector_rank=5 price=0.87 support=0.76 resistance=0.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=81.53 liquidity=96343120.0 spike=1.19
- GGCC.CA: score=23.4 buy_ready=False sector_rank=5 price=0.91 support=0.42 resistance=0.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=89.37 liquidity=32914500.0 spike=0.88
- GIHD.CA: score=23.4 buy_ready=False sector_rank=5 price=61.11 support=40.66 resistance=65.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=76.45 liquidity=30971378.0 spike=0.65
- GMCI.CA: score=15.07 buy_ready=False sector_rank=5 price=2.0 support=1.66 resistance=2.26 source=Yahoo Finance as_of=2026-07-25T21:00:00+00:00 freshness=FRESH RSI=53.33 liquidity=672628.0 spike=0.5
- GRCA.CA: score=24.66 buy_ready=True sector_rank=5 price=61.11 support=48.0 resistance=68.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=66.01 liquidity=16383646.0 spike=1.13
- GSSC.CA: score=16.19 buy_ready=True sector_rank=5 price=266.46 support=240.0 resistance=288.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=68.87 liquidity=1794635.63 spike=0.18
- GTWL.CA: score=24.4 buy_ready=True sector_rank=5 price=102.63 support=60.0 resistance=118.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=60.62 liquidity=30332002.0 spike=0.21
- HDBK.CA: score=20.4 buy_ready=False sector_rank=8 price=82.06 support=75.3 resistance=163.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=42.05 liquidity=16128400.0 spike=0.51
- HELI.CA: score=21.4 buy_ready=False sector_rank=11 price=8.32 support=6.36 resistance=8.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=89.9 liquidity=56877076.0 spike=0.32
- HRHO.CA: score=25.09 buy_ready=True sector_rank=14 price=26.9 support=26.09 resistance=27.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=49.81 liquidity=19239968.0 spike=0.18
- ICID.CA: score=23.03 buy_ready=True sector_rank=5 price=8.1 support=6.55 resistance=8.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:46 AM market time freshness=DELAYED_CURRENT RSI=52.87 liquidity=8391525.0 spike=1.12
- IDRE.CA: score=30.22 buy_ready=True sector_rank=5 price=49.92 support=41.1 resistance=52.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:46 AM market time freshness=DELAYED_CURRENT RSI=63.02 liquidity=42923912.0 spike=1.91
- IFAP.CA: score=28.66 buy_ready=True sector_rank=6 price=19.76 support=18.47 resistance=20.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=57.38 liquidity=10008321.0 spike=1.13
- INFI.CA: score=24.48 buy_ready=False sector_rank=5 price=107.0 support=88.51 resistance=111.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=74.8 liquidity=14953626.0 spike=1.04
- IRON.CA: score=8.74 buy_ready=False sector_rank=17 price=30.89 support=30.45 resistance=33.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=29.61 liquidity=6556863.0 spike=0.99
- ISMA.CA: score=29.02 buy_ready=False sector_rank=5 price=31.83 support=26.54 resistance=31.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=70.84 liquidity=51371916.0 spike=2.31
- ISMQ.CA: score=16.19 buy_ready=False sector_rank=17 price=9.31 support=8.6 resistance=10.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=30.41 liquidity=22034420.0 spike=0.2
- ISPH.CA: score=23.4 buy_ready=False sector_rank=13 price=11.63 support=11.2 resistance=12.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=51.54 liquidity=21575930.0 spike=0.4
- JUFO.CA: score=18.32 buy_ready=False sector_rank=18 price=29.29 support=28.5 resistance=31.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:47 AM market time freshness=DELAYED_CURRENT RSI=44.46 liquidity=25237108.0 spike=1.1
- KABO.CA: score=21.4 buy_ready=False sector_rank=4 price=8.68 support=6.04 resistance=8.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=89.21 liquidity=18953704.0 spike=0.41
- KWIN.CA: score=23.4 buy_ready=False sector_rank=5 price=98.97 support=65.0 resistance=109.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=93.14 liquidity=20397746.0 spike=0.45
- KZPC.CA: score=13.81 buy_ready=False sector_rank=5 price=8.6 support=8.26 resistance=9.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=51.69 liquidity=1410126.13 spike=0.27
- LCSW.CA: score=23.63 buy_ready=False sector_rank=1 price=34.65 support=27.01 resistance=37.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=77.83 liquidity=7231553.0 spike=0.09
- LUTS.CA: score=18.4 buy_ready=False sector_rank=5 price=0.59 support=0.59 resistance=0.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=24116802.0 spike=1.0
- MAAL.CA: score=17.57 buy_ready=False sector_rank=5 price=8.82 support=6.78 resistance=8.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:47 AM market time freshness=DELAYED_CURRENT RSI=83.78 liquidity=6170837.0 spike=0.34
- MASR.CA: score=24.4 buy_ready=False sector_rank=5 price=8.13 support=6.71 resistance=8.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=74.65 liquidity=65280820.0 spike=0.78
- MBSC.CA: score=24.23 buy_ready=False sector_rank=1 price=244.76 support=222.66 resistance=249.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=51.57 liquidity=7826346.0 spike=0.41
- MCQE.CA: score=23.77 buy_ready=True sector_rank=1 price=186.97 support=166.66 resistance=195.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:47 AM market time freshness=DELAYED_CURRENT RSI=66.84 liquidity=6373669.5 spike=0.35
- MCRO.CA: score=22.64 buy_ready=False sector_rank=5 price=1.5 support=1.17 resistance=1.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=83.72 liquidity=119366728.0 spike=1.12
- MENA.CA: score=15.63 buy_ready=True sector_rank=11 price=7.06 support=6.59 resistance=7.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=52.69 liquidity=1229012.75 spike=0.16
- MEPA.CA: score=24.4 buy_ready=False sector_rank=5 price=1.92 support=1.52 resistance=2.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=75.0 liquidity=41662332.0 spike=0.96
- MFPC.CA: score=20.19 buy_ready=False sector_rank=17 price=36.5 support=34.22 resistance=38.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=52.84 liquidity=32774986.0 spike=0.35
- MFSC.CA: score=5.64 buy_ready=False sector_rank=5 price=46.75 support=45.05 resistance=53.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=30.28 liquidity=1235257.75 spike=0.2
- MHOT.CA: score=3.45 buy_ready=False sector_rank=21 price=16.54 support=16.12 resistance=35.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=31.72 liquidity=2048759.38 spike=0.18
- MICH.CA: score=20.62 buy_ready=False sector_rank=5 price=40.98 support=34.0 resistance=43.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=83.28 liquidity=7223861.5 spike=0.47
- MILS.CA: score=24.7 buy_ready=True sector_rank=5 price=172.85 support=126.31 resistance=197.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=67.68 liquidity=38776792.0 spike=1.15
- MIPH.CA: score=14.96 buy_ready=False sector_rank=13 price=743.17 support=630.13 resistance=780.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=72.06 liquidity=562184.25 spike=0.16
- MOED.CA: score=22.52 buy_ready=True sector_rank=5 price=0.71 support=0.65 resistance=0.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=61.24 liquidity=20543052.0 spike=1.06
- MOIL.CA: score=14.77 buy_ready=False sector_rank=10 price=0.61 support=0.46 resistance=0.62 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:44 AM market time freshness=DELAYED_CURRENT RSI=86.93 liquidity=714593.81 spike=1.33
- MOIN.CA: score=10.87 buy_ready=False sector_rank=5 price=23.6 support=22.6 resistance=24.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 July 01:14 PM market time freshness=DELAYED_CURRENT RSI=46.84 liquidity=465703.44 spike=0.59
- MOSC.CA: score=17.69 buy_ready=True sector_rank=5 price=287.41 support=250.0 resistance=329.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:33 AM market time freshness=DELAYED_CURRENT RSI=63.16 liquidity=1288308.75 spike=0.1
- MPCI.CA: score=23.4 buy_ready=False sector_rank=5 price=283.24 support=222.55 resistance=289.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=78.68 liquidity=22750976.0 spike=0.23
- MPCO.CA: score=24.4 buy_ready=True sector_rank=6 price=1.87 support=1.7 resistance=1.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=56.41 liquidity=18555780.0 spike=0.35
- MPRC.CA: score=12.09 buy_ready=False sector_rank=5 price=43.46 support=36.7 resistance=45.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=75.27 liquidity=2693834.75 spike=0.07
- MTIE.CA: score=17.72 buy_ready=True sector_rank=15 price=9.36 support=8.75 resistance=9.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=44.06 liquidity=4265886.5 spike=0.2
- NAHO.CA: score=3.41 buy_ready=False sector_rank=5 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:42 AM market time freshness=DELAYED_CURRENT RSI=25.0 liquidity=6073.21 spike=0.18
- NCCW.CA: score=26.4 buy_ready=True sector_rank=5 price=6.7 support=5.82 resistance=6.91 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=62.33 liquidity=11494057.0 spike=0.54
- NEDA.CA: score=10.0 buy_ready=False sector_rank=5 price=2.75 support=2.7 resistance=3.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=51.11 liquidity=603318.94 spike=0.89
- NHPS.CA: score=21.4 buy_ready=False sector_rank=5 price=87.92 support=61.55 resistance=95.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=79.33 liquidity=11939518.0 spike=0.14
- NINH.CA: score=25.0 buy_ready=False sector_rank=5 price=22.4 support=17.4 resistance=23.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=72.36 liquidity=52544252.0 spike=1.3
- NIPH.CA: score=21.4 buy_ready=False sector_rank=13 price=225.53 support=157.01 resistance=242.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=89.55 liquidity=97333152.0 spike=0.67
- OBRI.CA: score=14.4 buy_ready=False sector_rank=5 price=34.35 support=31.5 resistance=39.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=29.55 liquidity=17174412.0 spike=0.45
- OCDI.CA: score=24.4 buy_ready=True sector_rank=11 price=27.4 support=23.75 resistance=28.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=61.06 liquidity=70248600.0 spike=0.69
- OCPH.CA: score=21.4 buy_ready=False sector_rank=5 price=474.33 support=341.4 resistance=496.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=90.9 liquidity=18764468.0 spike=0.8
- ODIN.CA: score=23.4 buy_ready=False sector_rank=5 price=2.68 support=2.05 resistance=2.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=76.81 liquidity=10435065.0 spike=0.65
- OFH.CA: score=21.4 buy_ready=False sector_rank=5 price=0.71 support=0.57 resistance=0.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=80.0 liquidity=14430216.0 spike=0.24
- OIH.CA: score=27.3 buy_ready=False sector_rank=7 price=1.49 support=1.4 resistance=1.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:45 AM market time freshness=DELAYED_CURRENT RSI=75.0 liquidity=95698328.0 spike=1.45
- OLFI.CA: score=20.19 buy_ready=True sector_rank=18 price=23.45 support=21.0 resistance=23.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=66.26 liquidity=7064955.5 spike=0.2
- ORAS.CA: score=7.6 buy_ready=False sector_rank=19 price=705.04 support=702.5 resistance=709.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=33851812.0 spike=1.0
- ORHD.CA: score=24.4 buy_ready=True sector_rank=11 price=40.11 support=37.0 resistance=40.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=61.59 liquidity=25112722.0 spike=0.16
- ORWE.CA: score=25.43 buy_ready=True sector_rank=4 price=23.0 support=21.95 resistance=23.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=56.03 liquidity=9034236.0 spike=0.38
- PHAR.CA: score=14.4 buy_ready=False sector_rank=13 price=95.0 support=92.1 resistance=97.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=262930704.0 spike=9.12
- PHDC.CA: score=19.4 buy_ready=False sector_rank=11 price=14.8 support=14.26 resistance=15.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=50.59 liquidity=121797512.0 spike=0.51
- PHTV.CA: score=11.83 buy_ready=False sector_rank=5 price=313.66 support=246.51 resistance=319.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=79.62 liquidity=431834.66 spike=0.07
- POUL.CA: score=21.24 buy_ready=False sector_rank=18 price=38.22 support=36.52 resistance=41.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=53.32 liquidity=34688988.0 spike=1.06
- PRCL.CA: score=27.4 buy_ready=True sector_rank=1 price=36.5 support=29.15 resistance=38.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=61.78 liquidity=30732928.0 spike=0.61
- PRDC.CA: score=26.4 buy_ready=True sector_rank=11 price=9.41 support=6.8 resistance=10.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:47 AM market time freshness=DELAYED_CURRENT RSI=63.96 liquidity=31835490.0 spike=0.26
- PRMH.CA: score=24.4 buy_ready=True sector_rank=5 price=2.72 support=2.34 resistance=2.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=56.86 liquidity=11936074.0 spike=0.69
- RACC.CA: score=17.2 buy_ready=False sector_rank=5 price=10.01 support=9.36 resistance=10.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=52.51 liquidity=4804885.0 spike=0.23
- RAKT.CA: score=12.56 buy_ready=False sector_rank=5 price=22.64 support=21.25 resistance=23.79 source=Yahoo Finance as_of=2026-07-25T21:00:00+00:00 freshness=FRESH RSI=62.22 liquidity=156465.04 spike=0.54
- RAYA.CA: score=16.9 buy_ready=False sector_rank=20 price=7.42 support=7.01 resistance=8.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=44.07 liquidity=67234456.0 spike=0.51
- RMDA.CA: score=29.38 buy_ready=True sector_rank=13 price=5.13 support=4.81 resistance=5.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=60.0 liquidity=30531938.0 spike=1.49
- ROTO.CA: score=18.31 buy_ready=True sector_rank=5 price=44.01 support=38.0 resistance=46.71 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT RSI=54.73 liquidity=3909178.0 spike=0.17
- RREI.CA: score=13.64 buy_ready=False sector_rank=5 price=4.12 support=3.85 resistance=4.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=90499592.0 spike=3.12
- RTVC.CA: score=19.32 buy_ready=True sector_rank=5 price=3.99 support=3.55 resistance=4.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=56.96 liquidity=2920331.25 spike=0.64
- RUBX.CA: score=19.64 buy_ready=True sector_rank=5 price=13.2 support=10.38 resistance=14.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=51.3 liquidity=5239481.0 spike=0.07
- SAUD.CA: score=24.98 buy_ready=True sector_rank=8 price=22.45 support=19.99 resistance=22.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=68.81 liquidity=8582317.0 spike=0.97
- SCEM.CA: score=24.4 buy_ready=False sector_rank=1 price=80.57 support=60.14 resistance=85.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:47 AM market time freshness=DELAYED_CURRENT RSI=80.14 liquidity=18510474.0 spike=0.32
- SCFM.CA: score=26.4 buy_ready=True sector_rank=5 price=280.78 support=230.0 resistance=325.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=61.36 liquidity=17867316.0 spike=0.92
- SCTS.CA: score=15.73 buy_ready=True sector_rank=16 price=619.76 support=540.0 resistance=649.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:44 AM market time freshness=DELAYED_CURRENT RSI=45.95 liquidity=2305969.5 spike=0.34
- SDTI.CA: score=18.62 buy_ready=False sector_rank=5 price=52.31 support=45.55 resistance=53.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:47 AM market time freshness=DELAYED_CURRENT RSI=80.99 liquidity=5222359.0 spike=0.69
- SEIG.CA: score=13.75 buy_ready=False sector_rank=5 price=246.17 support=182.01 resistance=285.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=71.54 liquidity=1350099.38 spike=0.06
- SIPC.CA: score=28.4 buy_ready=False sector_rank=5 price=3.99 support=3.25 resistance=3.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=79.17 liquidity=55007372.0 spike=3.76
- SKPC.CA: score=19.19 buy_ready=False sector_rank=17 price=15.98 support=14.8 resistance=16.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=47.96 liquidity=17635812.0 spike=0.49
- SMFR.CA: score=17.26 buy_ready=False sector_rank=5 price=231.55 support=187.01 resistance=277.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=71.36 liquidity=2861129.75 spike=0.14
- SNFC.CA: score=16.35 buy_ready=False sector_rank=5 price=11.17 support=11.2 resistance=12.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=38.97 liquidity=6954910.0 spike=0.62
- SPIN.CA: score=14.4 buy_ready=False sector_rank=4 price=16.67 support=15.05 resistance=17.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=102521120.0 spike=6.63
- SPMD.CA: score=18.0 buy_ready=True sector_rank=5 price=0.45 support=0.41 resistance=0.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=65.31 liquidity=5602400.5 spike=0.31
- SUGR.CA: score=16.24 buy_ready=False sector_rank=18 price=47.14 support=45.31 resistance=47.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=48.13 liquidity=5115460.5 spike=0.95
- SVCE.CA: score=21.68 buy_ready=False sector_rank=5 price=9.3 support=8.76 resistance=10.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=36.48 liquidity=9279411.0 spike=0.16
- SWDY.CA: score=25.42 buy_ready=False sector_rank=2 price=95.3 support=84.3 resistance=97.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=78.81 liquidity=20447004.0 spike=1.01
- TALM.CA: score=17.61 buy_ready=False sector_rank=16 price=15.74 support=15.27 resistance=16.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=42.69 liquidity=5187352.0 spike=0.37
- TMGH.CA: score=26.4 buy_ready=True sector_rank=11 price=99.53 support=92.1 resistance=103.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=58.65 liquidity=58288116.0 spike=0.16
- TRTO.CA: score=12.06 buy_ready=False sector_rank=5 price=0.03 support=0.03 resistance=0.03 source=Yahoo Finance as_of=2026-07-25T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=2036.5 spike=1.83
- UEFM.CA: score=15.61 buy_ready=True sector_rank=5 price=542.27 support=460.0 resistance=625.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:45 AM market time freshness=DELAYED_CURRENT RSI=67.95 liquidity=1214741.88 spike=0.29
- UEGC.CA: score=23.94 buy_ready=False sector_rank=5 price=2.6 support=1.33 resistance=2.53 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=90.91 liquidity=57132004.0 spike=1.27
- UNIP.CA: score=21.4 buy_ready=False sector_rank=5 price=0.41 support=0.3 resistance=0.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=80.45 liquidity=22415186.0 spike=0.97
- UNIT.CA: score=15.44 buy_ready=True sector_rank=11 price=18.1 support=12.0 resistance=21.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:46 AM market time freshness=DELAYED_CURRENT RSI=69.19 liquidity=3038395.25 spike=0.1
- WCDF.CA: score=24.62 buy_ready=True sector_rank=5 price=586.85 support=504.0 resistance=634.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:45 AM market time freshness=DELAYED_CURRENT RSI=64.42 liquidity=4904667.0 spike=2.66
- WKOL.CA: score=23.4 buy_ready=True sector_rank=5 price=317.19 support=273.1 resistance=340.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=66.08 liquidity=8998640.0 spike=0.95
- ZEOT.CA: score=18.52 buy_ready=True sector_rank=5 price=11.63 support=10.4 resistance=12.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=64.13 liquidity=4117120.25 spike=0.13
- ZMID.CA: score=24.4 buy_ready=False sector_rank=11 price=7.67 support=6.19 resistance=7.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=70.27 liquidity=216795104.0 spike=0.91

## Backtesting Lite
- IDRE.CA: 180d return=22.95%, max drawdown=-24.62%, MA20>MA50 days last20=20, as_of=2026-07-25T21:00:00+00:00
- ARCC.CA: 180d return=39.6%, max drawdown=-12.39%, MA20>MA50 days last20=8, as_of=2026-07-25T21:00:00+00:00
- AJWA.CA: 180d return=36.23%, max drawdown=-24.35%, MA20>MA50 days last20=20, as_of=2026-07-25T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- IDRE.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Ismailia Development and Real Estate Co summary=Evidence rejected for IDRE.CA: source text did not clearly match IDRE.CA / Ismailia Development and Real Estate Co.
- ARCC.CA: status=RECENT_ACCEPTED latest=2026-09-02 age_days=0 sources=3 expected=Arabian Cement Company summary=Arabian Cement Company (ARCC.CA) has shown strong financial performance in 2025 with increased revenue and earnings. The company has also declared dividends and received a 'Buy' analyst consensus. Recent disclosures and board meeting decisions have been reported by the EGX.
  - Arabian Cement Company S.A.E. (EGX:ARCC) Stock Price & Overview (Financial Performance in 2025, Analyst Summary as of Aug 13, 2026 earnings date): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEnPkl1NkvVyMnJ6YDBQbSUlvnkbGjpEb039ZAW16pnBFo9OSIEFxZXnQkc05WhrPl10Sjdutac4sW41Da55IUDOlC4Vrz5FihMv4bKh6nhj9cLDZ1uM4sTq0fI8U8dqt_0J8k=
  - Arabian Cement Co SAE - EGX:ARCC Financials (Latest Release May 31, 2026, TTM metrics): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFM3CmXEuyTpW7T7g20ZJGcTVvUR1wvooWJHa-jwkTgvslFkU0YmhR29DNaXs09Twl4pKrYq1UW80yqU84zm2IhgB-p2UqNaBo01TdgA97MpfWnwpOHqOgibUHdQf1rjEcAO6nb2SWPh-nXGisUOllo_--GgVY7cld1yrVVAqao-pMB2Dk=
  - ARCC Stock Price and Chart — EGX:ARCC - TradingView (Dividend information, Next earnings Sep 2, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHpFa-IEJbOLCI4XeEHH4kwd9WymTvvoBssHgVcLHw478tCYakO9Www0nfaZpqPVcJUNsSxPu4opESzBefnSrO1qVdwXWhwmnUfZQDe120q5Fvvag-An36UBwGNAj9z4F8PLiGzru4I
- AJWA.CA: status=RECENT_ACCEPTED latest=2026-05-12 age_days=76 sources=3 expected=AJWA For Food Industries Co. Egypt summary=AJWA For Food Industries Co. Egypt (AJWA.CA) has reported its financial results for the period ending December 31, 2025, and held its Annual General Meeting in July 2026. Recent quarterly performance data and board decisions are also available.
  - Ajwa Group for Food Industries - Egypt Announcements - Mubasher Info (Financial Results for the Period ending 31/12/2025 reported 30 June; AGM Invitation 8 July; BoD Decisions 1 July, 12 May 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEP5Fa0glVW-Hc_16XICeAGan7jeZK-A1gKxDS1OnldP5ZknW18OQSTN66uxdzIvSO4jrIgPMm-zAs-nCH0pB1qRu2txpKVKAWEqPm1lBKSKbWShtM7sxytpLioBqdRn0mWSghEXT4qXMeO58U2EK76dUDc_AbOKKlFAYRB0w==
  - EGX:AJWA Financials | AJWA for Food Industries company - Investing.com (Latest Release Mar 24, 2026, TTM metrics, Q1 2026 revenue and net income): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFg5Mg27-OKZoHAz0zHau91WvJYMsVNXucP9wPkV15PnbgVf8ffcp3VFQ3u9S86vpyhFGF_snrVn88kTXGhyfpPyiwB2YA0UPwKAWCfcda2W9CpoQxSa90kedIGkMW0pQ_DQRfURDOBWEgosAsWrn4OCHpfwWXsYlL4wvfs
  - AJWA For Food Industries Co. Egypt (EGX:AJWA) Stock Price & Overview - Stock Analysis (Financial Performance in 2024): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGP3JM4Ms_rOVEJVH8VXJf5MX28Sh0Yks25YtkoWVFx-RlFaf8yWLGqf-I9aB9s7OULvLT04kClw8NlQ3_gEyz1u_XsGlm7G_d_4TsikCGTHih0WgeaeyWQla2fhofkejxD09Q=
- RMDA.CA: status=RECENT_ACCEPTED latest=2026-08-13 age_days=0 sources=3 expected=Tenth of Ramadan Pharmaceutical Industries summary=Tenth of Ramadan Pharmaceutical Industries (RMDA.CA) has reported its financial performance for the last 12 months, showing significant revenue and profit. The stock has seen a substantial increase in the past year, and analysts have a 'Buy' rating. The company also declared dividends and has an upcoming earnings date in August 2026.
  - Tenth of Ramadan for Pharmaceutical Industries and Diagnostic Reagents (Rameda) (S.A.E) (EGX:RMDA) Statistics & Valuation Metrics (Financial performance in last 12 months as of July 22, 2026, 52-Week Price Change): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEz7jZl2SmBzG4LZkHuGxGjZMEq3nuRTeh4trlMwOi1ooGkG4ZQRg4mGwCpybiSCOjaDUgA4amCmdz5ToEJXugNBqHBrwcj4ZOM9kvIsAUj7zU2FAI65hGrUeUuJzV6pIGmQVAwfs5HkENzfU2CeA==
  - Tenth of Ramadan for Pharmaceutical Industries and Diagnostic Reagents (Rameda) (SAE) (EGX:RMDA) - Stock Analysis (Analyst Summary, Earnings Date Aug 13, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH_dc4PjtMAeuBItCzJhbn7InVfo-ffwElHZvoZgbDP6oAmGZqxQqyJbt5N9ybep0XCsVXNPzzTtdKSjLEv4-Pp2D5FtIrkypWplreaFpXQlJ8al8K9I7j9NXlX8lej2F950es=
  - EGX:RMDA Financials | Tenth of Ramadan for Pharmaceutical - Investing.com (Latest Release Jun 02, 2026, Q1 2026 revenue, net income, EPS, TTM metrics): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGUBzCdd3X0agec77FEjO-ZLpGm1KjiJBWXr2mjmmhbcTWdP3fF7910m0RPDPE6gRNbnnAjypQm6BlTq-ErXTMwQUVPygXiLHHZsG-BFxPgmMkM_WTgWj3czqjy0xm-a1xM-QUIFlbNSUTH23ihE7d-7grbouzyTb-hHsgK2gWy3Qa8-RLDh_iW-bR2z07EcV4qg==
- ISMA.CA: status=RECENT_ACCEPTED latest=2026-07-24 age_days=3 sources=3 expected=Ismailia / Misr Poultry Company S.A.E summary=Ismailia / Misr Poultry Company S.A.E (ISMA.CA) has demonstrated strong financial performance in the last 12 months, with significant profit and a substantial increase in stock price over the past year. The company has also reported its latest quarterly and full-year earnings.
  - Ismailia / Misr Poultry Company S.A.E (EGX:ISMA) Statistics & Valuation Metrics (Financial performance in last 12 months as of July 20, 2026, 52-Week Price Change): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHbTES07xrDgwq2ye_h6S7cnlX_s-EPRL5I1cpOShfOfA73qzMzTWar5zRt0cEk2nBJMegFZ5NRFle157a5vT6lT2XaXH-dNSdEONvn_CQpHQjtlFmHyVzOHX_1LeOnucrBWEYzO0XV4vBY3WgDEw==
  - Ismailia / Misr Poultry Company S.A.E Stock (ISMA) - Quote Egyptian Exchange (Q1 2026 earnings reported May 12, 2026; Full Year 2025 earnings reported Feb 11, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFvCnWnqXWX2jldVQUbC2GigNZ83nPJl_pJBgitSRCJ_ojY-5NU5uIrTfyTCT7PcDRTcoOAKHIf3-NzmFEO0Cdm_PS_Gi-PoXoZELkPOSQiObyXLUAnpR6D6TL8nHFjOw96E2c1PT9jOcP0gYlZJxlraUBVgApNb5bAQDqAsrVBC10kdY5ljT9G
  - Ismailia Misr Poultry Stock Price Today | EGX: ISMA Live - Investing.com (Current stock price and 52-week range as of Jul 24, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQETvPsDalLSm_Bko4AJdKDpKXFINmxRJLjKYCSDg46H8UU4ynJEZ5eZRw7_7UEfF1uKyWybz__U4hkhEkgHgQHJeTTi6lfcYSofOM9GkWFNfobqE1ndb0fOuzOFKnT8Ul_Sh4i67mmDLLZ8jA==
- IFAP.CA: status=RECENT_ACCEPTED latest=2026-07-09 age_days=18 sources=3 expected=International Agricultural Products summary=International Agricultural Products (IFAP.CA) has reported its financial performance for the last 12 months, including revenue and profits. The company's trailing twelve months (TTM) metrics for net profit margin, gross margin, and ROI are also available.
  - International Company for Agricultural Crops (EGX:IFAP) Statistics & Valuation Metrics (Financial performance in last 12 months as of June 21, 2026, 52-Week Price Change): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG3qDsBbnEojW4WEk4ympVjjk1jbnqQyftxqJrd3r2NoFeqWDmdRpWibE3RW6U1vxfq-KfBhM7suWpTXfgSDdFNhVS4jV6SQtyqjZN-Pu9s_sni1FQe2EVBCOtNAGpYPy0BOsh-Wg3xdkjebUDViw==
  - Int Agricultural Products - EGX:IFAP Financials - Investing.com (TTM net profit margin, gross margin, ROI, latest quarterly performance): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHFQJ-u6OX5ejY3pHq1MnCmKucX_p3Tmyk03lJtOCzcJsKI0UPYOfrtH4niXncfcr8gJo72Q7vm8bWDrMPLlhG5-rW708OTpKTz130LVJ65579qtljrNglF1qP06KdjjXiCDHX_wkiJKhVM-2SLaZ6Gw22BP9RpsRBdJt2otQ==
  - Int Agricultural Products Annual Report | EGX:IFAP Financials - Investing.com UK (TTM EPS as of July 09, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEkNzNLomxvOA12Ul6dq4Arryt6shkavIuQqc-_rQameZDmkn5AMIvdzeQ7LR2kQLnV5TBTmZqO1O6iSOZZYyuF3l_z_9LSskVdM1Y92CnSWECaHLj5AsS_QOEjYzWVIdhDchAPYikTRaX8Dgpd2qGYZZfufSZrxkdzf9PT
- ELSH.CA: status=RECENT_ACCEPTED latest=2026-07-16 age_days=11 sources=3 expected=Al Shams Housing and Urbanization SAE summary=Al Shams Housing and Urbanization SAE (ELSH.CA) has declared annual dividends payable in June and December 2026. The company's financial performance for 2025 has been reported, and recent market announcements include disclosures and AGM minutes.
  - Al-Shams Company for Housing and Urban Development (CASE:ELSH) - Stock Analysis (Annual dividend declared Jun 13, 2026, payable Jun 29, 2026; Annual dividend payable Dec 28, 2025; New minor risk - Share price stability Jun 02, 2026; Board Change May 20, 2026; Annual General Meeting Apr 28, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFIaagJ3IcSOpD24c8FYeel5QQo1vs4YzC7_py-702pMn52JJEV4uApLcb_KOemF0R5srDnU2a3PfDJF3wsR4CFs4JqIs3TVDdsGUDrBqndNgQlYUCC1gI-vxL4ECcA4ezm3KaujIA8PqGs9u8irSCR3FYZAYldfL004brFe6F1cETVwTpQFagkn3hlQa5hPXBwsShWpjqR5Xue2O7elxJdaifFweLb4reyfuMJkGeXIS7au9CPdx2WxSZt9LrOSP6l6oFSWw==
  - Al-Shams Company for Housing and Urban Development (EGX:ELSH) - Stock Analysis (Financial Performance in 2025): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHzgSbGdgwmF7Kqo5KAQV3D9ltj7NYL_jwhLTIrpmTYuIEE8ruydlu6kxQatCllHtClxUQJfpShIp8gOP3shUEwhhUMYMLHflTsyWcLfetabgVzTTsOcwf1FRozRS29kBxBXaQ=
  - El Shams Housing & Urbanization - Stock - Mubasher Info (Disclosure Form for the BoD & the Shareholders' Structure 16 July 2026; Declares Cash Dividends 11 June 2026; AGM Minutes 10 June 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGx1lC2AZ-HWGDIDoWId_BMnnsUGQXVQcSW8KiWHsP4b3E1Ny7mCpE86GksVgIT-vC67snQjf0_S-vQex8eOye26AfjyRxBOEZ5D0EhvnN1WFRa2IXY2SjaKL-Ef1zdndLbN3nQhhNYi9dKgvLhjsLN
- SIPC.CA: status=RECENT_ACCEPTED latest=2026-03-31 age_days=118 sources=3 expected=Sabaa International Company for Pharmaceutical and Chemical Industry summary=Sabaa International Company for Pharmaceutical and Chemical Industry (SIPC.CA) has detailed annual and quarterly financials available as of March 31, 2026. The company's trailing twelve months (TTM) gross margin, net profit margin, and ROI have also been reported.
  - Sabaa International Company for Pharmaceutical and Chemical Industry (EGX:SIPC) Financials & Income Statement - Stock Analysis (Detailed annual and quarterly financials as of March 31, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEAvjnj4bN8nKAsoHrZTP9LedqzJPb8k7b7U5rA-3N8t_C2phdbWLFiWODhlWSEblrLd-BdQv69I66BJmvuYdiTCbS5uEMRHrN86YT3cyJi2_FjNG8poOfGpB5VSMYOE9HL6hSq0-KM0s6rsDD-Lw==
  - EGX:SIPC Financials | Sabaa International Company for Pharmaceutical and Chemical Industries SAE - Investing.com (TTM gross margin, net profit margin, ROI, latest quarterly performance): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG1U4smk3zYmvBdJ4YMpDwYFXhlSoAH2ToZL3dJtDVDM1A0RpI04VIlNBsS9nqkoEOs83UYhWULAuGITeEDybWvhKgvoHJX_JVgmKZlZJ9sYvq7FWasZyTKJONuRGJsOXAXaiid-yMEnntBwlWv_AEm4bgL3GovNr10axaM-noX262ZlW9R9poQtTIHx7C5LKQ2
  - Sabaa International Company For Pharmaceutical and Chemical (SIPC.CA) Reports Year Ended 31/12/2024 Results - The Egyptian Exchange: https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGoDvPdGfLgkBRAshStjJ5_tcbrCRDnY2LulHeuO6bF0uJVHh3JL8kICxCJP6mjbJfYA7uPmhYVAJVIQajIM79yN9czPN-MfEy4H80apRRBqUCQ7fJzjb893Yn7WRxZ9COu612XGoXNaEP1Pmn_4Q==

## Warnings
- Evidence rejected for IDRE.CA: source text did not clearly match IDRE.CA / Ismailia Development and Real Estate Co.
