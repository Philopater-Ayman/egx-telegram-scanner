# Telegram-First EGX Scanner Report

Scan phase: Intraday liquidity update
Generated UTC: 2026-07-13T10:58:26.680597+00:00
Generated Cairo: 2026-07-13 13:58
Run timing: target 11:00 Cairo | generated Cairo 2026-07-13 13:58 | cron 0 8 * * 0-4
Trigger: scheduled cron=0 8 * * 0-4 mapped to intraday; Cairo now 2026-07-13 13:54

## Control Center
- Action tickets: 3 prioritized signal(s)
- BUY-ready candidates: 84
- Data quality issues: 1
- Tradeable price/liquidity tickers: 179/189
- Top sector: Technology & Distribution

## Market Context
- Market trend: Bullish
- Source: Mubasher EGX market page (delayed public data)
- As of: Monday, July 13
- Freshness: DELAYED
- EGX30 regime: CONSTRUCTIVE / above MA20 55.0% / above MA50 50.0%
- EGX70 regime: BULLISH / above MA20 77.5% / above MA50 70.0%
- Sector breadth: 52.38%
- Risk mode: SELECTIVE_SWING_TRADES_ONLY

## Top Liquidity
- CCAP.CA: liquidity=768302336.0 spike=1.18 score=26.76
- ZMID.CA: liquidity=302348896.0 spike=1.39 score=27.18
- COMI.CA: liquidity=261640064.0 spike=0.6 score=25.91
- AMES.CA: liquidity=223187344.0 spike=5.45 score=14.4
- ARAB.CA: liquidity=207592960.0 spike=2.3 score=29.0

## AI Narrative
- Provider: OpenRouter OK
- Model: openai/gpt-oss-120b:free
- Summary: The scanner highlights GDWA.CA as the top BUY candidate, followed by ALCN.CA and COSG.CA. All three show price above MA20/MA50, solid liquidity spikes, and bullish outlook scores above 90. EGX30 is in a constructive phase while EGX70 remains bullish, pushing the system into a SELECTIVE_SWING_TRADES_ONLY risk mode. This regime favors limited‑size swing entries on stocks with clear support/resistance and strong liquidity, but the overall market still carries uncertainty from sector‑specific weakness and low confidence scores.
- GDWA.CA: price 0.84, support 0.76, resistance 0.82, RSI 51.8, liquidity spike 6.8×, sector not leading.
- ALCN.CA: strong momentum (RSI 66), support 27.7, resistance 33.2, liquidity spike 2.5×, transportation sector in top‑3.
- COSG.CA: price near resistance 1.66, support 1.47, RSI 54.5, liquidity spike 1.8×, sector lagging.
- EGX30 constructive / EGX70 bullish → risk mode SELECTIVE_SWING_TRADES_ONLY; focus on swing setups with clear support.
- Uncertainty: low confidence on setups, sector weakness, and macro‑trend reliance require price‑action confirmation on Thndr.

## Top Liquidity Spikes
- CPCI.CA: spike=12.67 liquidity=33313898.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- RACC.CA: spike=11.26 liquidity=117765936.0 outlook=BULLISH_WATCH score=84.06 buy_ready=True
- MOSC.CA: spike=9.3 liquidity=85130776.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- OCPH.CA: spike=8.86 liquidity=55448052.0 outlook=BULLISH_WATCH score=76.06 buy_ready=True
- GDWA.CA: spike=6.82 liquidity=110909024.0 outlook=BULLISH_WATCH score=93.06 buy_ready=True

## Sector Leaderboard
- #1 Technology & Distribution: score=13.48 5d=4.42% 20d=18.68% aboveMA50=100.0%
- #2 Industrial Goods & Cables: score=12.43 5d=2.41% 20d=4.51% aboveMA50=100.0%
- #3 Transportation & Logistics: score=10.7 5d=3.01% 20d=7.21% aboveMA50=100.0%
- #4 Telecommunications: score=10.67 5d=5.07% 20d=6.67% aboveMA50=100.0%
- #5 Real Estate: score=10.62 5d=3.68% 20d=14.76% aboveMA50=100.0%
- #6 Automotive & Distribution: score=10.23 5d=-0.72% 20d=9.65% aboveMA50=100.0%
- #7 Fintech & Payments: score=8.75 5d=4.38% 20d=9.24% aboveMA50=50.0%
- #8 Textiles: score=8.48 5d=3.17% 20d=5.0% aboveMA50=100.0%

## Today's Prioritized Action Tickets
- Priority #1: BUY GDWA.CA
  - Entry: 0.84 | Take profit: 0.9 | Stop loss: 0.81
  - Confidence: LOW | score=32.4 | outlook=BULLISH_WATCH 93.06
  - Reason: BUY SETUP: GDWA.CA has aligned current price data, liquidity above threshold, price above MA20/MA50, RSI 51.8, support 0.76, resistance 0.82, and evidence sources. Macro trend is Bullish; market regime is SELECTIVE_SWING_TRADES_ONLY; verify price action in Thndr before treating it as a swing entry.
- Priority #2: BUY ALCN.CA
  - Entry: 30.25 | Take profit: 33.03 | Stop loss: 29.04
  - Confidence: LOW | score=30.34 | outlook=BULLISH_WATCH 100
  - Reason: WATCH/BUY SETUP: ALCN.CA has aligned current price data, liquidity above threshold, price above MA20/MA50, RSI 66.15, support 27.7, resistance 33.2, and evidence sources. Macro trend is Bullish; market regime is SELECTIVE_SWING_TRADES_ONLY; verify price action in Thndr before treating it as a swing entry.
- Priority #3: BUY COSG.CA
  - Entry: 1.66 | Take profit: 1.8 | Stop loss: 1.59
  - Confidence: LOW | score=30.06 | outlook=BULLISH_WATCH 92.06
  - Reason: BUY SETUP: COSG.CA has aligned current price data, liquidity above threshold, price above MA20/MA50, RSI 54.55, support 1.47, resistance 1.66, and evidence sources. Macro trend is Bullish; market regime is SELECTIVE_SWING_TRADES_ONLY; verify price action in Thndr before treating it as a swing entry.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- ELEC.CA: BULLISH_WATCH score=100 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=No major short-term scanner risk flags.
- ALCN.CA: BULLISH_WATCH score=100 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=momentum is extended
- GDWA.CA: BULLISH_WATCH score=93.06 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- AREH.CA: BULLISH_WATCH score=92.06 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- COSG.CA: BULLISH_WATCH score=92.06 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- CAED.CA: BULLISH_WATCH score=92.06 liquidity=TRADEABLE sector=IMPROVING risk=sector is not leading
- MTIE.CA: BULLISH_WATCH score=91 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=close to resistance
- NCCW.CA: BULLISH_WATCH score=90.06 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- SWDY.CA: BULLISH_WATCH score=90 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- MOED.CA: BULLISH_WATCH score=87.06 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading

## BUY-Ready Candidates
- ELEC.CA: rank=34.4 outlook=BULLISH_WATCH outlook_score=100 sector_rank=2 price=2.18 support=2.04 resistance=2.18 liquidity=110089368.0
- AREH.CA: rank=32.46 outlook=BULLISH_WATCH outlook_score=92.06 sector_rank=9 price=1.72 support=1.51 resistance=1.76 liquidity=107658224.0
- GDWA.CA: rank=32.4 outlook=BULLISH_WATCH outlook_score=93.06 sector_rank=9 price=0.84 support=0.76 resistance=0.82 liquidity=110909024.0
- RACC.CA: rank=31.4 outlook=BULLISH_WATCH outlook_score=84.06 sector_rank=9 price=10.45 support=9.36 resistance=10.57 liquidity=117765936.0
- MCRO.CA: rank=30.4 outlook=BULLISH_WATCH outlook_score=79.06 sector_rank=9 price=1.35 support=1.17 resistance=1.33 liquidity=163666448.0
- ALCN.CA: rank=30.34 outlook=BULLISH_WATCH outlook_score=100 sector_rank=3 price=30.25 support=27.7 resistance=33.2 liquidity=40869944.0
- COSG.CA: rank=30.06 outlook=BULLISH_WATCH outlook_score=92.06 sector_rank=9 price=1.66 support=1.47 resistance=1.66 liquidity=73405376.0
- RAYA.CA: rank=30.04 outlook=BULLISH_WATCH outlook_score=77 sector_rank=1 price=8.34 support=6.8 resistance=8.29 liquidity=151305424.0
- ADPC.CA: rank=29.84 outlook=CONSTRUCTIVE outlook_score=62.06 sector_rank=9 price=3.76 support=3.32 resistance=3.94 liquidity=43405768.0
- MOED.CA: rank=29.4 outlook=BULLISH_WATCH outlook_score=87.06 sector_rank=9 price=0.73 support=0.65 resistance=0.72 liquidity=45553992.0

## Data Quality Issues
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=26.4 buy_ready=False sector_rank=9 price=232.6 support=196.0 resistance=247.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:40 PM market time freshness=DELAYED_CURRENT RSI=70.14 liquidity=10924277.0 spike=0.73
- ABUK.CA: score=20.03 buy_ready=False sector_rank=19 price=69.28 support=66.66 resistance=77.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:39 PM market time freshness=DELAYED_CURRENT RSI=42.84 liquidity=84205032.0 spike=0.59
- ACAMD.CA: score=26.4 buy_ready=True sector_rank=9 price=2.33 support=2.14 resistance=2.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:40 PM market time freshness=DELAYED_CURRENT RSI=45.0 liquidity=35372580.0 spike=0.37
- ACGC.CA: score=29.18 buy_ready=True sector_rank=8 price=10.0 support=8.92 resistance=9.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:40 PM market time freshness=DELAYED_CURRENT RSI=54.07 liquidity=30354814.0 spike=1.39
- ADCI.CA: score=24.82 buy_ready=True sector_rank=9 price=239.31 support=223.0 resistance=248.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:39 PM market time freshness=DELAYED_CURRENT RSI=51.65 liquidity=14462767.0 spike=1.21
- ADIB.CA: score=20.91 buy_ready=False sector_rank=16 price=46.56 support=44.1 resistance=48.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:39 PM market time freshness=DELAYED_CURRENT RSI=49.79 liquidity=78554184.0 spike=0.83
- ADPC.CA: score=29.84 buy_ready=True sector_rank=9 price=3.76 support=3.32 resistance=3.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:38 PM market time freshness=DELAYED_CURRENT RSI=39.0 liquidity=43405768.0 spike=2.72
- AFDI.CA: score=28.94 buy_ready=True sector_rank=9 price=47.0 support=40.8 resistance=48.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:40 PM market time freshness=DELAYED_CURRENT RSI=59.42 liquidity=17230310.0 spike=1.27
- AFMC.CA: score=26.81 buy_ready=True sector_rank=9 price=74.4 support=66.0 resistance=76.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:36 PM market time freshness=DELAYED_CURRENT RSI=57.13 liquidity=7810749.5 spike=2.3
- AJWA.CA: score=18.15 buy_ready=True sector_rank=9 price=182.96 support=150.51 resistance=190.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:39 PM market time freshness=DELAYED_CURRENT RSI=57.66 liquidity=3754403.5 spike=0.14
- ALCN.CA: score=30.34 buy_ready=True sector_rank=3 price=30.25 support=27.7 resistance=33.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:39 PM market time freshness=DELAYED_CURRENT RSI=66.15 liquidity=40869944.0 spike=2.47
- ALUM.CA: score=15.7 buy_ready=False sector_rank=9 price=22.82 support=20.55 resistance=24.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:38 PM market time freshness=DELAYED_CURRENT RSI=44.37 liquidity=2295707.0 spike=0.29
- AMER.CA: score=23.4 buy_ready=False sector_rank=5 price=3.12 support=2.28 resistance=3.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:40 PM market time freshness=DELAYED_CURRENT RSI=76.8 liquidity=53340068.0 spike=0.65
- AMES.CA: score=14.4 buy_ready=False sector_rank=9 price=99.94 support=83.13 resistance=100.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:40 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=223187344.0 spike=5.45
- AMIA.CA: score=16.83 buy_ready=True sector_rank=9 price=8.92 support=8.4 resistance=9.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:38 PM market time freshness=DELAYED_CURRENT RSI=46.46 liquidity=2425339.75 spike=0.25
- AMOC.CA: score=23.22 buy_ready=False sector_rank=12 price=8.06 support=7.42 resistance=8.16 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:39 PM market time freshness=DELAYED_CURRENT RSI=56.63 liquidity=46687644.0 spike=0.9
- APSW.CA: score=14.96 buy_ready=False sector_rank=9 price=8.48 support=8.0 resistance=8.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:34 PM market time freshness=DELAYED_CURRENT RSI=45.6 liquidity=2002017.5 spike=2.28
- ARAB.CA: score=29.0 buy_ready=False sector_rank=5 price=0.25 support=0.2 resistance=0.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:40 PM market time freshness=DELAYED_CURRENT RSI=72.73 liquidity=207592960.0 spike=2.3
- ARCC.CA: score=16.52 buy_ready=False sector_rank=18 price=55.17 support=53.0 resistance=57.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:40 PM market time freshness=DELAYED_CURRENT RSI=46.04 liquidity=8048628.0 spike=0.39
- AREH.CA: score=32.46 buy_ready=True sector_rank=9 price=1.72 support=1.51 resistance=1.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 July 01:29 PM market time freshness=DELAYED_CURRENT RSI=56.0 liquidity=107658224.0 spike=3.03
- ARVA.CA: score=19.17 buy_ready=False sector_rank=9 price=10.78 support=10.5 resistance=13.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:39 PM market time freshness=DELAYED_CURRENT RSI=46.12 liquidity=6769024.5 spike=0.32
- ASCM.CA: score=24.4 buy_ready=True sector_rank=9 price=62.34 support=56.29 resistance=73.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:40 PM market time freshness=DELAYED_CURRENT RSI=57.49 liquidity=47492192.0 spike=0.58
- ASPI.CA: score=19.4 buy_ready=False sector_rank=9 price=0.31 support=0.3 resistance=0.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:39 PM market time freshness=DELAYED_CURRENT RSI=39.06 liquidity=17281964.0 spike=0.61
- ATLC.CA: score=16.44 buy_ready=True sector_rank=15 price=5.25 support=4.77 resistance=5.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:39 PM market time freshness=DELAYED_CURRENT RSI=44.85 liquidity=2432451.0 spike=0.35
- ATQA.CA: score=21.03 buy_ready=False sector_rank=19 price=9.6 support=9.21 resistance=9.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:40 PM market time freshness=DELAYED_CURRENT RSI=52.34 liquidity=13180220.0 spike=0.41
- AXPH.CA: score=25.95 buy_ready=True sector_rank=9 price=1209.31 support=1073.0 resistance=1342.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:39 PM market time freshness=DELAYED_CURRENT RSI=63.99 liquidity=6888688.0 spike=2.33
- BINV.CA: score=15.33 buy_ready=False sector_rank=10 price=48.66 support=45.01 resistance=51.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:33 PM market time freshness=DELAYED_CURRENT RSI=54.5 liquidity=931041.81 spike=0.15
- BIOC.CA: score=21.99 buy_ready=True sector_rank=9 price=73.85 support=66.75 resistance=76.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:40 PM market time freshness=DELAYED_CURRENT RSI=52.12 liquidity=3450954.0 spike=1.07
- BTFH.CA: score=22.01 buy_ready=False sector_rank=15 price=3.06 support=2.91 resistance=3.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:39 PM market time freshness=DELAYED_CURRENT RSI=43.9 liquidity=135284864.0 spike=0.7
- CAED.CA: score=24.96 buy_ready=True sector_rank=9 price=74.35 support=68.0 resistance=78.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:40 PM market time freshness=DELAYED_CURRENT RSI=51.31 liquidity=6543767.0 spike=1.01
- CANA.CA: score=16.31 buy_ready=False sector_rank=16 price=36.3 support=34.7 resistance=38.23 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:38 PM market time freshness=DELAYED_CURRENT RSI=41.44 liquidity=3404357.25 spike=0.33
- CCAP.CA: score=26.76 buy_ready=True sector_rank=10 price=5.36 support=4.65 resistance=5.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:40 PM market time freshness=DELAYED_CURRENT RSI=59.41 liquidity=768302336.0 spike=1.18
- CCRS.CA: score=14.4 buy_ready=False sector_rank=9 price=2.53 support=2.42 resistance=2.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:40 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=46775616.0 spike=4.16
- CEFM.CA: score=14.37 buy_ready=False sector_rank=9 price=104.52 support=95.75 resistance=110.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:35 PM market time freshness=DELAYED_CURRENT RSI=55.4 liquidity=969316.88 spike=0.44
- CERA.CA: score=23.8 buy_ready=True sector_rank=9 price=1.31 support=1.17 resistance=1.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:40 PM market time freshness=DELAYED_CURRENT RSI=62.5 liquidity=7395303.5 spike=0.35
- CFGH.CA: score=1.91 buy_ready=False sector_rank=9 price=0.11 support=0.1 resistance=0.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:16 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=14293.64 spike=2.25
- CICH.CA: score=17.61 buy_ready=False sector_rank=15 price=11.97 support=11.36 resistance=12.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:37 PM market time freshness=DELAYED_CURRENT RSI=34.72 liquidity=8924358.0 spike=2.34
- CIEB.CA: score=18.72 buy_ready=True sector_rank=16 price=24.33 support=23.3 resistance=24.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:37 PM market time freshness=DELAYED_CURRENT RSI=53.42 liquidity=2808683.75 spike=0.4
- CIRA.CA: score=27.8 buy_ready=False sector_rank=13 price=31.06 support=26.0 resistance=31.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:38 PM market time freshness=DELAYED_CURRENT RSI=70.57 liquidity=42189112.0 spike=1.81
- CLHO.CA: score=21.74 buy_ready=False sector_rank=17 price=15.99 support=14.85 resistance=17.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:40 PM market time freshness=DELAYED_CURRENT RSI=55.59 liquidity=34752368.0 spike=0.97
- CNFN.CA: score=26.15 buy_ready=True sector_rank=15 price=4.94 support=4.4 resistance=5.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:39 PM market time freshness=DELAYED_CURRENT RSI=51.85 liquidity=46468328.0 spike=1.07
- COMI.CA: score=25.91 buy_ready=True sector_rank=16 price=136.71 support=126.21 resistance=137.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:39 PM market time freshness=DELAYED_CURRENT RSI=45.96 liquidity=261640064.0 spike=0.6
- COPR.CA: score=22.38 buy_ready=False sector_rank=9 price=0.37 support=0.35 resistance=0.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:40 PM market time freshness=DELAYED_CURRENT RSI=32.73 liquidity=62747472.0 spike=2.99
- COSG.CA: score=30.06 buy_ready=True sector_rank=9 price=1.66 support=1.47 resistance=1.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:38 PM market time freshness=DELAYED_CURRENT RSI=54.55 liquidity=73405376.0 spike=1.83
- CPCI.CA: score=14.4 buy_ready=False sector_rank=9 price=470.41 support=400.03 resistance=482.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:40 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=33313898.0 spike=12.67
- CSAG.CA: score=22.03 buy_ready=True sector_rank=3 price=32.79 support=30.85 resistance=33.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:37 PM market time freshness=DELAYED_CURRENT RSI=64.2 liquidity=4632612.5 spike=0.27
- DAPH.CA: score=24.55 buy_ready=True sector_rank=9 price=84.05 support=77.12 resistance=87.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:37 PM market time freshness=DELAYED_CURRENT RSI=59.99 liquidity=6150382.5 spike=0.69
- DEIN.CA: score=-0.6 buy_ready=False sector_rank=9 price=11.38 support=13.65 resistance=13.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 June 12:11 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=40.95 spike=0.01
- DOMT.CA: score=17.5 buy_ready=True sector_rank=14 price=27.06 support=24.21 resistance=27.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:30 PM market time freshness=DELAYED_CURRENT RSI=60.17 liquidity=1348705.75 spike=0.26
- DSCW.CA: score=28.58 buy_ready=True sector_rank=9 price=1.83 support=1.71 resistance=1.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:40 PM market time freshness=DELAYED_CURRENT RSI=40.91 liquidity=71511152.0 spike=2.59
- DTPP.CA: score=23.4 buy_ready=False sector_rank=9 price=207.99 support=114.0 resistance=234.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:40 PM market time freshness=DELAYED_CURRENT RSI=89.03 liquidity=18179422.0 spike=0.49
- EALR.CA: score=26.84 buy_ready=True sector_rank=9 price=370.0 support=332.0 resistance=425.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:41 PM market time freshness=DELAYED_CURRENT RSI=57.03 liquidity=14408202.0 spike=1.22
- EASB.CA: score=22.4 buy_ready=False sector_rank=9 price=7.25 support=5.06 resistance=10.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:36 PM market time freshness=DELAYED_CURRENT RSI=36.74 liquidity=13969697.0 spike=0.81
- EAST.CA: score=13.15 buy_ready=False sector_rank=14 price=36.51 support=36.6 resistance=40.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:40 PM market time freshness=DELAYED_CURRENT RSI=29.64 liquidity=24947254.0 spike=0.56
- EBSC.CA: score=22.42 buy_ready=True sector_rank=9 price=1.93 support=1.71 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:38 PM market time freshness=DELAYED_CURRENT RSI=51.95 liquidity=5941370.5 spike=1.04
- ECAP.CA: score=14.97 buy_ready=False sector_rank=9 price=32.59 support=31.15 resistance=34.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:24 PM market time freshness=DELAYED_CURRENT RSI=35.35 liquidity=2571513.5 spike=0.28
- EDFM.CA: score=25.12 buy_ready=True sector_rank=9 price=356.63 support=310.2 resistance=349.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:39 PM market time freshness=DELAYED_CURRENT RSI=66.15 liquidity=3721370.25 spike=4.99
- EEII.CA: score=19.57 buy_ready=True sector_rank=9 price=2.79 support=2.35 resistance=2.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:41 PM market time freshness=DELAYED_CURRENT RSI=67.03 liquidity=5166761.5 spike=0.24
- EFIC.CA: score=11.03 buy_ready=False sector_rank=19 price=187.49 support=180.02 resistance=207.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:40 PM market time freshness=DELAYED_CURRENT RSI=19.85 liquidity=6218748.5 spike=2.39
- EFID.CA: score=26.15 buy_ready=True sector_rank=14 price=28.34 support=25.5 resistance=28.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:39 PM market time freshness=DELAYED_CURRENT RSI=52.8 liquidity=12626437.0 spike=0.26
- EFIH.CA: score=26.4 buy_ready=True sector_rank=7 price=22.44 support=20.0 resistance=23.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:39 PM market time freshness=DELAYED_CURRENT RSI=60.96 liquidity=27675698.0 spike=0.62
- EGAL.CA: score=20.03 buy_ready=False sector_rank=19 price=291.61 support=272.28 resistance=314.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:39 PM market time freshness=DELAYED_CURRENT RSI=45.96 liquidity=20589582.0 spike=0.42
- EGAS.CA: score=14.22 buy_ready=False sector_rank=12 price=52.88 support=50.01 resistance=53.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:39 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=50935748.0 spike=6.24
- EGBE.CA: score=13.99 buy_ready=False sector_rank=16 price=0.45 support=0.43 resistance=0.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:26 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=78377.73 spike=1.0
- EGCH.CA: score=22.63 buy_ready=False sector_rank=19 price=13.19 support=12.13 resistance=14.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:39 PM market time freshness=DELAYED_CURRENT RSI=40.88 liquidity=57898932.0 spike=1.3
- EGSA.CA: score=13.47 buy_ready=False sector_rank=4 price=8.97 support=8.67 resistance=9.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:27 PM market time freshness=DELAYED_CURRENT RSI=91.67 liquidity=9586.75 spike=1.03
- EGTS.CA: score=26.4 buy_ready=True sector_rank=5 price=18.24 support=15.1 resistance=19.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:37 PM market time freshness=DELAYED_CURRENT RSI=48.79 liquidity=13020345.0 spike=0.21
- EHDR.CA: score=26.4 buy_ready=True sector_rank=9 price=2.69 support=2.37 resistance=2.82 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:40 PM market time freshness=DELAYED_CURRENT RSI=51.76 liquidity=17988606.0 spike=0.43
- EKHO.CA: score=8.22 buy_ready=False sector_rank=12 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-07-11T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=34.4 buy_ready=True sector_rank=2 price=2.18 support=2.04 resistance=2.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:39 PM market time freshness=DELAYED_CURRENT RSI=51.85 liquidity=110089368.0 spike=5.81
- ELKA.CA: score=25.4 buy_ready=False sector_rank=9 price=1.62 support=1.19 resistance=1.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:41 PM market time freshness=DELAYED_CURRENT RSI=72.22 liquidity=22662964.0 spike=0.45
- ELNA.CA: score=17.23 buy_ready=False sector_rank=9 price=39.54 support=35.55 resistance=40.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:34 PM market time freshness=DELAYED_CURRENT RSI=46.25 liquidity=671039.38 spike=1.08
- ELSH.CA: score=28.4 buy_ready=True sector_rank=9 price=14.6 support=11.1 resistance=15.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:40 PM market time freshness=DELAYED_CURRENT RSI=64.31 liquidity=75228400.0 spike=0.43
- ELWA.CA: score=16.69 buy_ready=True sector_rank=9 price=2.06 support=1.87 resistance=2.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:25 PM market time freshness=DELAYED_CURRENT RSI=43.9 liquidity=2005658.5 spike=1.14
- EMFD.CA: score=22.4 buy_ready=False sector_rank=5 price=11.7 support=11.24 resistance=12.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:39 PM market time freshness=DELAYED_CURRENT RSI=43.69 liquidity=65073372.0 spike=0.45
- ENGC.CA: score=28.06 buy_ready=False sector_rank=9 price=41.13 support=33.91 resistance=44.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:40 PM market time freshness=DELAYED_CURRENT RSI=73.42 liquidity=43412960.0 spike=1.83
- EOSB.CA: score=14.44 buy_ready=False sector_rank=9 price=1.48 support=1.42 resistance=1.55 source=Yahoo Finance as_of=2026-07-11T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=35839.68 spike=0.47
- EPCO.CA: score=29.14 buy_ready=True sector_rank=9 price=9.58 support=8.5 resistance=9.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:41 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=15953343.0 spike=2.37
- EPPK.CA: score=14.91 buy_ready=False sector_rank=9 price=14.22 support=11.72 resistance=15.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:36 PM market time freshness=DELAYED_CURRENT RSI=69.3 liquidity=507830.19 spike=0.51
- ETEL.CA: score=28.4 buy_ready=True sector_rank=4 price=97.93 support=89.01 resistance=101.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:39 PM market time freshness=DELAYED_CURRENT RSI=64.17 liquidity=51444052.0 spike=0.71
- ETRS.CA: score=24.4 buy_ready=True sector_rank=9 price=10.8 support=9.15 resistance=11.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:41 PM market time freshness=DELAYED_CURRENT RSI=50.55 liquidity=11158116.0 spike=0.14
- EXPA.CA: score=23.89 buy_ready=True sector_rank=16 price=18.72 support=18.03 resistance=18.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:40 PM market time freshness=DELAYED_CURRENT RSI=56.44 liquidity=5977648.0 spike=0.23
- FAIT.CA: score=16.96 buy_ready=True sector_rank=16 price=37.1 support=35.06 resistance=37.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:31 PM market time freshness=DELAYED_CURRENT RSI=50.44 liquidity=1049698.13 spike=0.41
- FAITA.CA: score=8.93 buy_ready=False sector_rank=16 price=0.98 support=0.98 resistance=1.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:23 PM market time freshness=DELAYED_CURRENT RSI=44.83 liquidity=19696.03 spike=0.63
- FERC.CA: score=13.13 buy_ready=False sector_rank=19 price=75.44 support=72.75 resistance=80.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:40 PM market time freshness=DELAYED_CURRENT RSI=48.71 liquidity=2104583.25 spike=0.53
- FWRY.CA: score=23.4 buy_ready=False sector_rank=7 price=19.28 support=18.13 resistance=19.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:39 PM market time freshness=DELAYED_CURRENT RSI=60.28 liquidity=46534912.0 spike=0.25
- GBCO.CA: score=24.4 buy_ready=True sector_rank=6 price=31.95 support=27.77 resistance=32.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:39 PM market time freshness=DELAYED_CURRENT RSI=64.63 liquidity=84295312.0 spike=0.99
- GDWA.CA: score=32.4 buy_ready=True sector_rank=9 price=0.84 support=0.76 resistance=0.82 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:40 PM market time freshness=DELAYED_CURRENT RSI=51.8 liquidity=110909024.0 spike=6.82
- GGCC.CA: score=19.11 buy_ready=False sector_rank=9 price=0.57 support=0.41 resistance=0.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:40 PM market time freshness=DELAYED_CURRENT RSI=92.74 liquidity=5713121.5 spike=0.33
- GIHD.CA: score=26.82 buy_ready=True sector_rank=9 price=50.08 support=40.0 resistance=52.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:41 PM market time freshness=DELAYED_CURRENT RSI=69.42 liquidity=48072164.0 spike=2.21
- GMCI.CA: score=15.33 buy_ready=False sector_rank=9 price=2.01 support=1.66 resistance=2.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:31 PM market time freshness=DELAYED_CURRENT RSI=65.28 liquidity=932399.31 spike=0.86
- GRCA.CA: score=14.4 buy_ready=False sector_rank=9 price=51.71 support=48.74 resistance=54.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:38 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=12677412.0 spike=4.13
- GSSC.CA: score=21.06 buy_ready=True sector_rank=9 price=262.03 support=240.0 resistance=263.63 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:38 PM market time freshness=DELAYED_CURRENT RSI=65.51 liquidity=4597600.0 spike=1.03
- GTWL.CA: score=21.4 buy_ready=False sector_rank=9 price=109.83 support=46.0 resistance=117.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:40 PM market time freshness=DELAYED_CURRENT RSI=89.45 liquidity=80826192.0 spike=0.86
- HDBK.CA: score=12.91 buy_ready=False sector_rank=16 price=78.03 support=75.3 resistance=172.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:38 PM market time freshness=DELAYED_CURRENT RSI=10.6 liquidity=13847831.0 spike=0.35
- HELI.CA: score=23.4 buy_ready=False sector_rank=5 price=7.33 support=6.34 resistance=7.62 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:39 PM market time freshness=DELAYED_CURRENT RSI=75.72 liquidity=98793880.0 spike=0.63
- HRHO.CA: score=18.01 buy_ready=False sector_rank=15 price=26.6 support=26.09 resistance=27.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:39 PM market time freshness=DELAYED_CURRENT RSI=36.62 liquidity=85276736.0 spike=0.66
- ICID.CA: score=21.64 buy_ready=True sector_rank=9 price=8.27 support=6.55 resistance=8.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:39 PM market time freshness=DELAYED_CURRENT RSI=59.95 liquidity=7240607.0 spike=0.67
- IDRE.CA: score=28.4 buy_ready=True sector_rank=9 price=46.02 support=41.1 resistance=47.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:41 PM market time freshness=DELAYED_CURRENT RSI=57.98 liquidity=12599089.0 spike=0.97
- IFAP.CA: score=15.49 buy_ready=False sector_rank=11 price=19.53 support=18.47 resistance=20.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:40 PM market time freshness=DELAYED_CURRENT RSI=57.21 liquidity=2092021.0 spike=0.44
- INFI.CA: score=26.96 buy_ready=False sector_rank=9 price=104.06 support=88.51 resistance=106.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:35 PM market time freshness=DELAYED_CURRENT RSI=71.89 liquidity=12513171.0 spike=1.28
- IRON.CA: score=14.16 buy_ready=False sector_rank=19 price=32.01 support=30.51 resistance=33.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:36 PM market time freshness=DELAYED_CURRENT RSI=49.19 liquidity=5130203.5 spike=0.65
- ISMA.CA: score=12.95 buy_ready=False sector_rank=9 price=27.18 support=26.54 resistance=36.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:41 PM market time freshness=DELAYED_CURRENT RSI=16.02 liquidity=5551350.0 spike=0.19
- ISMQ.CA: score=23.03 buy_ready=False sector_rank=19 price=9.54 support=8.06 resistance=10.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:40 PM market time freshness=DELAYED_CURRENT RSI=72.31 liquidity=69577808.0 spike=0.48
- ISPH.CA: score=13.74 buy_ready=False sector_rank=17 price=11.45 support=11.2 resistance=12.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:40 PM market time freshness=DELAYED_CURRENT RSI=27.27 liquidity=42971256.0 spike=0.71
- JUFO.CA: score=17.85 buy_ready=False sector_rank=14 price=30.54 support=29.1 resistance=32.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:39 PM market time freshness=DELAYED_CURRENT RSI=40.22 liquidity=5693729.0 spike=0.23
- KABO.CA: score=23.4 buy_ready=False sector_rank=8 price=7.53 support=6.04 resistance=7.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:39 PM market time freshness=DELAYED_CURRENT RSI=88.76 liquidity=18836568.0 spike=0.65
- KWIN.CA: score=14.4 buy_ready=False sector_rank=9 price=69.08 support=65.0 resistance=79.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:41 PM market time freshness=DELAYED_CURRENT RSI=33.96 liquidity=12395361.0 spike=0.93
- KZPC.CA: score=18.54 buy_ready=False sector_rank=9 price=8.64 support=8.26 resistance=10.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:40 PM market time freshness=DELAYED_CURRENT RSI=29.44 liquidity=17063240.0 spike=2.57
- LCSW.CA: score=25.47 buy_ready=True sector_rank=18 price=31.62 support=26.41 resistance=32.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:40 PM market time freshness=DELAYED_CURRENT RSI=67.42 liquidity=13094601.0 spike=0.22
- LUTS.CA: score=22.4 buy_ready=False sector_rank=9 price=0.74 support=0.69 resistance=0.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:41 PM market time freshness=DELAYED_CURRENT RSI=42.08 liquidity=22792264.0 spike=0.46
- MAAL.CA: score=22.6 buy_ready=False sector_rank=9 price=8.29 support=5.72 resistance=8.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:39 PM market time freshness=DELAYED_CURRENT RSI=98.01 liquidity=26163380.0 spike=1.6
- MASR.CA: score=28.4 buy_ready=True sector_rank=9 price=8.11 support=6.71 resistance=7.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:41 PM market time freshness=DELAYED_CURRENT RSI=62.67 liquidity=76224232.0 spike=0.9
- MBSC.CA: score=20.47 buy_ready=False sector_rank=18 price=240.26 support=222.66 resistance=256.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:37 PM market time freshness=DELAYED_CURRENT RSI=39.92 liquidity=11494348.0 spike=0.5
- MCQE.CA: score=15.56 buy_ready=False sector_rank=18 price=176.79 support=166.66 resistance=182.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:39 PM market time freshness=DELAYED_CURRENT RSI=46.1 liquidity=3093807.5 spike=0.21
- MCRO.CA: score=30.4 buy_ready=True sector_rank=9 price=1.35 support=1.17 resistance=1.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:39 PM market time freshness=DELAYED_CURRENT RSI=65.52 liquidity=163666448.0 spike=4.82
- MENA.CA: score=19.09 buy_ready=True sector_rank=5 price=7.01 support=6.41 resistance=7.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:40 PM market time freshness=DELAYED_CURRENT RSI=58.06 liquidity=2691183.75 spike=0.34
- MEPA.CA: score=25.14 buy_ready=False sector_rank=9 price=1.67 support=1.52 resistance=1.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:40 PM market time freshness=DELAYED_CURRENT RSI=44.74 liquidity=20275398.0 spike=1.87
- MFPC.CA: score=22.03 buy_ready=False sector_rank=19 price=37.19 support=34.22 resistance=40.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:39 PM market time freshness=DELAYED_CURRENT RSI=49.84 liquidity=37191492.0 spike=0.37
- MFSC.CA: score=13.26 buy_ready=False sector_rank=9 price=45.98 support=44.0 resistance=56.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:32 PM market time freshness=DELAYED_CURRENT RSI=51.37 liquidity=3858136.5 spike=0.5
- MHOT.CA: score=3.07 buy_ready=False sector_rank=21 price=16.5 support=16.12 resistance=38.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:40 PM market time freshness=DELAYED_CURRENT RSI=15.69 liquidity=3666480.75 spike=0.23
- MICH.CA: score=20.17 buy_ready=True sector_rank=9 price=38.2 support=34.0 resistance=39.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:40 PM market time freshness=DELAYED_CURRENT RSI=38.69 liquidity=5768835.5 spike=0.35
- MILS.CA: score=24.56 buy_ready=True sector_rank=9 price=137.99 support=126.31 resistance=151.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:41 PM market time freshness=DELAYED_CURRENT RSI=48.18 liquidity=12006569.0 spike=1.08
- MIPH.CA: score=19.1 buy_ready=True sector_rank=17 price=708.72 support=630.13 resistance=710.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:37 PM market time freshness=DELAYED_CURRENT RSI=51.34 liquidity=2741935.25 spike=1.31
- MOED.CA: score=29.4 buy_ready=True sector_rank=9 price=0.73 support=0.65 resistance=0.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:40 PM market time freshness=DELAYED_CURRENT RSI=55.62 liquidity=45553992.0 spike=4.26
- MOIL.CA: score=18.61 buy_ready=False sector_rank=12 price=0.54 support=0.46 resistance=0.53 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:40 PM market time freshness=DELAYED_CURRENT RSI=69.47 liquidity=818115.81 spike=2.79
- MOIN.CA: score=12.82 buy_ready=False sector_rank=9 price=23.95 support=22.6 resistance=25.25 source=Yahoo Finance as_of=2026-07-11T21:00:00+00:00 freshness=FRESH RSI=48.18 liquidity=418933.41 spike=0.55
- MOSC.CA: score=14.4 buy_ready=False sector_rank=9 price=308.0 support=275.0 resistance=329.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:41 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=85130776.0 spike=9.3
- MPCI.CA: score=24.4 buy_ready=True sector_rank=9 price=241.91 support=215.0 resistance=256.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:41 PM market time freshness=DELAYED_CURRENT RSI=49.77 liquidity=48592452.0 spike=0.5
- MPCO.CA: score=24.4 buy_ready=True sector_rank=11 price=1.89 support=1.7 resistance=2.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:39 PM market time freshness=DELAYED_CURRENT RSI=41.67 liquidity=56909112.0 spike=0.68
- MPRC.CA: score=23.4 buy_ready=False sector_rank=9 price=42.18 support=31.72 resistance=43.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:41 PM market time freshness=DELAYED_CURRENT RSI=89.47 liquidity=32564108.0 spike=0.69
- MTIE.CA: score=29.32 buy_ready=True sector_rank=6 price=9.62 support=8.75 resistance=9.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:39 PM market time freshness=DELAYED_CURRENT RSI=55.23 liquidity=50544516.0 spike=2.46
- NAHO.CA: score=12.61 buy_ready=False sector_rank=9 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance as_of=2026-07-11T21:00:00+00:00 freshness=FRESH RSI=55.56 liquidity=48426.17 spike=2.08
- NCCW.CA: score=26.7 buy_ready=True sector_rank=9 price=6.59 support=5.82 resistance=6.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:40 PM market time freshness=DELAYED_CURRENT RSI=51.79 liquidity=53427892.0 spike=2.15
- NEDA.CA: score=16.75 buy_ready=False sector_rank=9 price=2.8 support=2.7 resistance=2.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:36 PM market time freshness=DELAYED_CURRENT RSI=57.14 liquidity=348320.91 spike=0.95
- NHPS.CA: score=28.4 buy_ready=False sector_rank=9 price=80.35 support=61.55 resistance=83.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:41 PM market time freshness=DELAYED_CURRENT RSI=75.67 liquidity=112465240.0 spike=3.54
- NINH.CA: score=26.4 buy_ready=False sector_rank=9 price=18.1 support=16.82 resistance=18.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:40 PM market time freshness=DELAYED_CURRENT RSI=51.8 liquidity=32938850.0 spike=4.49
- NIPH.CA: score=25.74 buy_ready=True sector_rank=17 price=177.96 support=157.01 resistance=185.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:40 PM market time freshness=DELAYED_CURRENT RSI=60.61 liquidity=70690344.0 spike=0.81
- OBRI.CA: score=26.4 buy_ready=True sector_rank=9 price=36.67 support=31.5 resistance=39.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:38 PM market time freshness=DELAYED_CURRENT RSI=55.18 liquidity=15951066.0 spike=0.48
- OCDI.CA: score=21.4 buy_ready=False sector_rank=5 price=26.84 support=20.24 resistance=28.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:30 PM market time freshness=DELAYED_CURRENT RSI=78.6 liquidity=27539858.0 spike=0.28
- OCPH.CA: score=29.4 buy_ready=True sector_rank=9 price=369.21 support=337.0 resistance=374.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:41 PM market time freshness=DELAYED_CURRENT RSI=65.84 liquidity=55448052.0 spike=8.86
- ODIN.CA: score=10.68 buy_ready=False sector_rank=9 price=2.49 support=2.36 resistance=2.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:41 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=23182122.0 spike=1.64
- OFH.CA: score=26.4 buy_ready=True sector_rank=9 price=0.63 support=0.57 resistance=0.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:40 PM market time freshness=DELAYED_CURRENT RSI=61.46 liquidity=13335752.0 spike=0.63
- OIH.CA: score=21.4 buy_ready=False sector_rank=10 price=1.41 support=1.35 resistance=1.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:39 PM market time freshness=DELAYED_CURRENT RSI=72.73 liquidity=29139278.0 spike=0.42
- OLFI.CA: score=26.15 buy_ready=True sector_rank=14 price=22.85 support=21.0 resistance=23.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:39 PM market time freshness=DELAYED_CURRENT RSI=58.56 liquidity=30940500.0 spike=0.94
- ORAS.CA: score=7.6 buy_ready=False sector_rank=20 price=684.14 support=681.14 resistance=691.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:39 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=59270096.0 spike=1.0
- ORHD.CA: score=24.4 buy_ready=True sector_rank=5 price=39.11 support=36.92 resistance=39.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:39 PM market time freshness=DELAYED_CURRENT RSI=47.12 liquidity=68033288.0 spike=0.41
- ORWE.CA: score=22.4 buy_ready=False sector_rank=8 price=22.69 support=21.95 resistance=23.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:40 PM market time freshness=DELAYED_CURRENT RSI=37.21 liquidity=12231677.0 spike=0.63
- PHAR.CA: score=18.74 buy_ready=False sector_rank=17 price=85.5 support=83.02 resistance=89.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:38 PM market time freshness=DELAYED_CURRENT RSI=39.19 liquidity=14423889.0 spike=0.66
- PHDC.CA: score=17.4 buy_ready=False sector_rank=5 price=14.75 support=14.26 resistance=16.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:39 PM market time freshness=DELAYED_CURRENT RSI=25.0 liquidity=145413904.0 spike=0.45
- PHTV.CA: score=15.69 buy_ready=False sector_rank=9 price=299.02 support=204.03 resistance=304.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:36 PM market time freshness=DELAYED_CURRENT RSI=89.79 liquidity=2285590.5 spike=0.16
- POUL.CA: score=24.15 buy_ready=True sector_rank=14 price=39.76 support=34.99 resistance=41.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:39 PM market time freshness=DELAYED_CURRENT RSI=69.01 liquidity=36224504.0 spike=0.84
- PRCL.CA: score=17.49 buy_ready=False sector_rank=18 price=34.73 support=24.14 resistance=36.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:39 PM market time freshness=DELAYED_CURRENT RSI=75.45 liquidity=7018945.0 spike=0.14
- PRDC.CA: score=26.4 buy_ready=True sector_rank=5 price=8.36 support=6.2 resistance=9.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:37 PM market time freshness=DELAYED_CURRENT RSI=59.52 liquidity=43030948.0 spike=0.3
- PRMH.CA: score=24.4 buy_ready=True sector_rank=9 price=2.73 support=2.34 resistance=3.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:41 PM market time freshness=DELAYED_CURRENT RSI=46.24 liquidity=20774496.0 spike=0.66
- RACC.CA: score=31.4 buy_ready=True sector_rank=9 price=10.45 support=9.36 resistance=10.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:41 PM market time freshness=DELAYED_CURRENT RSI=58.48 liquidity=117765936.0 spike=11.26
- RAKT.CA: score=10.99 buy_ready=False sector_rank=9 price=22.55 support=21.25 resistance=23.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=57.11 liquidity=334836.72 spike=1.13
- RAYA.CA: score=30.04 buy_ready=True sector_rank=1 price=8.34 support=6.8 resistance=8.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:39 PM market time freshness=DELAYED_CURRENT RSI=63.79 liquidity=151305424.0 spike=1.32
- RMDA.CA: score=18.74 buy_ready=False sector_rank=17 price=4.98 support=4.81 resistance=5.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:39 PM market time freshness=DELAYED_CURRENT RSI=42.86 liquidity=15639638.0 spike=0.71
- ROTO.CA: score=26.4 buy_ready=True sector_rank=9 price=43.45 support=33.7 resistance=47.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:41 PM market time freshness=DELAYED_CURRENT RSI=54.28 liquidity=12415998.0 spike=0.38
- RREI.CA: score=28.4 buy_ready=True sector_rank=9 price=3.85 support=3.34 resistance=3.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:41 PM market time freshness=DELAYED_CURRENT RSI=60.87 liquidity=13680708.0 spike=0.7
- RTVC.CA: score=15.81 buy_ready=False sector_rank=9 price=3.86 support=3.55 resistance=3.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:41 PM market time freshness=DELAYED_CURRENT RSI=44.44 liquidity=2405270.0 spike=0.56
- RUBX.CA: score=21.4 buy_ready=False sector_rank=9 price=13.47 support=9.8 resistance=14.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:41 PM market time freshness=DELAYED_CURRENT RSI=80.15 liquidity=37246228.0 spike=0.68
- SAUD.CA: score=14.79 buy_ready=False sector_rank=16 price=21.6 support=19.99 resistance=22.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:39 PM market time freshness=DELAYED_CURRENT RSI=49.15 liquidity=1882205.88 spike=0.28
- SCEM.CA: score=20.47 buy_ready=False sector_rank=18 price=61.92 support=60.14 resistance=67.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:38 PM market time freshness=DELAYED_CURRENT RSI=52.02 liquidity=16609518.0 spike=0.99
- SCFM.CA: score=20.89 buy_ready=False sector_rank=9 price=257.93 support=226.5 resistance=269.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:39 PM market time freshness=DELAYED_CURRENT RSI=54.22 liquidity=5470218.0 spike=1.01
- SCTS.CA: score=17.81 buy_ready=True sector_rank=13 price=615.26 support=540.0 resistance=649.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:38 PM market time freshness=DELAYED_CURRENT RSI=59.37 liquidity=1632954.63 spike=0.3
- SDTI.CA: score=16.66 buy_ready=True sector_rank=9 price=47.23 support=45.55 resistance=49.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:40 PM market time freshness=DELAYED_CURRENT RSI=49.44 liquidity=2257428.0 spike=0.28
- SEIG.CA: score=23.4 buy_ready=False sector_rank=9 price=258.2 support=180.6 resistance=285.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:39 PM market time freshness=DELAYED_CURRENT RSI=85.04 liquidity=17560258.0 spike=0.91
- SIPC.CA: score=20.81 buy_ready=True sector_rank=9 price=3.53 support=3.25 resistance=3.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:41 PM market time freshness=DELAYED_CURRENT RSI=46.75 liquidity=4413562.5 spike=0.53
- SKPC.CA: score=21.03 buy_ready=False sector_rank=19 price=16.4 support=15.58 resistance=16.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:38 PM market time freshness=DELAYED_CURRENT RSI=48.21 liquidity=15293507.0 spike=0.48
- SMFR.CA: score=25.7 buy_ready=True sector_rank=9 price=206.49 support=187.01 resistance=209.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:41 PM market time freshness=DELAYED_CURRENT RSI=51.46 liquidity=5415447.0 spike=2.94
- SNFC.CA: score=11.25 buy_ready=False sector_rank=9 price=11.77 support=11.26 resistance=12.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:41 PM market time freshness=DELAYED_CURRENT RSI=46.55 liquidity=1845885.0 spike=0.16
- SPIN.CA: score=15.41 buy_ready=False sector_rank=8 price=14.63 support=13.3 resistance=14.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:37 PM market time freshness=DELAYED_CURRENT RSI=80.0 liquidity=4005182.75 spike=0.44
- SPMD.CA: score=22.26 buy_ready=True sector_rank=9 price=0.45 support=0.4 resistance=0.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:40 PM market time freshness=DELAYED_CURRENT RSI=45.83 liquidity=5861664.0 spike=0.34
- SUGR.CA: score=11.63 buy_ready=False sector_rank=14 price=47.22 support=45.31 resistance=49.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:40 PM market time freshness=DELAYED_CURRENT RSI=33.33 liquidity=7413533.0 spike=1.53
- SVCE.CA: score=26.4 buy_ready=True sector_rank=9 price=9.35 support=8.35 resistance=10.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:41 PM market time freshness=DELAYED_CURRENT RSI=52.6 liquidity=20062580.0 spike=0.28
- SWDY.CA: score=21.95 buy_ready=True sector_rank=2 price=88.34 support=84.3 resistance=90.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:36 PM market time freshness=DELAYED_CURRENT RSI=56.06 liquidity=3552698.75 spike=0.27
- TALM.CA: score=14.18 buy_ready=False sector_rank=13 price=15.68 support=15.27 resistance=16.53 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:39 PM market time freshness=DELAYED_CURRENT RSI=30.07 liquidity=10304863.0 spike=0.89
- TMGH.CA: score=26.4 buy_ready=True sector_rank=5 price=97.4 support=92.1 resistance=99.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:39 PM market time freshness=DELAYED_CURRENT RSI=48.25 liquidity=156261568.0 spike=0.44
- TRTO.CA: score=13.36 buy_ready=False sector_rank=9 price=0.03 support=0.03 resistance=0.04 source=Yahoo Finance as_of=2026-07-11T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=751.23 spike=2.48
- UEFM.CA: score=17.1 buy_ready=False sector_rank=9 price=500.73 support=460.0 resistance=529.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=60.58 liquidity=698992.88 spike=0.45
- UEGC.CA: score=23.52 buy_ready=False sector_rank=9 price=1.89 support=1.33 resistance=1.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:41 PM market time freshness=DELAYED_CURRENT RSI=80.3 liquidity=24158046.0 spike=1.06
- UNIP.CA: score=27.06 buy_ready=True sector_rank=9 price=0.34 support=0.29 resistance=0.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:41 PM market time freshness=DELAYED_CURRENT RSI=52.0 liquidity=8659197.0 spike=0.49
- UNIT.CA: score=20.35 buy_ready=False sector_rank=5 price=19.18 support=12.0 resistance=20.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:40 PM market time freshness=DELAYED_CURRENT RSI=76.24 liquidity=8954598.0 spike=0.42
- WCDF.CA: score=12.57 buy_ready=False sector_rank=9 price=515.94 support=450.0 resistance=544.99 source=Yahoo Finance as_of=2026-07-11T21:00:00+00:00 freshness=FRESH RSI=39.17 liquidity=767718.72 spike=2.2
- WKOL.CA: score=22.98 buy_ready=True sector_rank=9 price=316.09 support=273.1 resistance=334.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:38 PM market time freshness=DELAYED_CURRENT RSI=68.75 liquidity=6575296.0 spike=0.89
- ZEOT.CA: score=28.52 buy_ready=True sector_rank=9 price=11.79 support=9.05 resistance=12.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:41 PM market time freshness=DELAYED_CURRENT RSI=42.32 liquidity=119866736.0 spike=3.06
- ZMID.CA: score=27.18 buy_ready=True sector_rank=5 price=7.28 support=6.11 resistance=7.16 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:40 PM market time freshness=DELAYED_CURRENT RSI=68.84 liquidity=302348896.0 spike=1.39

## Backtesting Lite
- ELEC.CA: 180d return=-25.35%, max drawdown=-35.96%, MA20>MA50 days last20=0, as_of=2026-07-11T21:00:00+00:00
- AREH.CA: 180d return=48.7%, max drawdown=-37.58%, MA20>MA50 days last20=20, as_of=2026-07-11T21:00:00+00:00
- GDWA.CA: 180d return=-30.17%, max drawdown=-39.84%, MA20>MA50 days last20=13, as_of=2026-07-11T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- ELEC.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=558 sources=3 expected=Electro Cable Egypt summary=Electro Cable Egypt sees lower profits in 2025; revenues exceed EGP 10.8bn; Mashareq reduces equity in Electro Cable Egypt to 0.77%; Electro Cable Egypt stock is testing significant demand zone, will it succeed to rebound? Gemini also reviewed web evidence but did not return ticker-specific citations.
  - Electro Cable Egypt sees lower profits in 2025; revenues exceed EGP 10.8bn: https://english.mubasher.info/news/4580607/Electro-Cable-Egypt-sees-lower-profits-in-2025-revenues-exceed-EGP-10-8bn/
  - Mashareq reduces equity in Electro Cable Egypt to 0.77%: https://english.mubasher.info/news/4561520/Mashareq-reduces-equity-in-Electro-Cable-Egypt-to-0-77-/
  - Electro Cable Egypt stock is testing significant demand zone, will it succeed to rebound?: https://english.mubasher.info/news/4556412/Electro-Cable-Egypt-stock-is-testing-significant-demand-zone-will-it-succeed-to-rebound-/
- AREH.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Real Estate Egyptian Consortium S.A.E summary=Real Estate Egyptian Consortium’s net profits approach EGP 2m in 9M-25; Shareholder ups stake in Real Estate Egyptian; Target for Real Estate Investment cuts stake in Real Estate Egyptian Gemini also reviewed web evidence but did not return ticker-specific citations.
  - Real Estate Egyptian Consortium’s net profits approach EGP 2m in 9M-25: https://english.mubasher.info/news/4528467/Real-Estate-Egyptian-Consortium-s-net-profits-approach-EGP-2m-in-9M-25/
  - Shareholder ups stake in Real Estate Egyptian: https://english.mubasher.info/news/4026301/Shareholder-ups-stake-in-Real-Estate-Egyptian/
  - Target for Real Estate Investment cuts stake in Real Estate Egyptian: https://english.mubasher.info/news/4010821/Target-for-Real-Estate-Investment-cuts-stake-in-Real-Estate-Egyptian/
- GDWA.CA: status=RECENT_ACCEPTED latest=2026-07-09 age_days=4 sources=3 expected=Gadwa for Industrial Development summary=Gadwa for Industrial Development (GDWA.CA) has reported its consolidated financial results for Q1 2026, showing a net loss of EGP 381.79 million, compared to a net comparative profit of EGP 635.40 million in Q1 2025. The company's revenue for Q1 2026 was approximately EGP 3.26 billion, with total assets of EGP 22.6 billion as of March 31, 2026. The stock price has decreased by -46.68% in the last 52 weeks as of July 09, 2026.
  - Gadwa For Industrial Development (GDWA.CA) Reports its Financial Results (Consolidated) for the Period from 01/01/2026 to 31/03/2026: https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFq8W6oCH5fHS8UFtXEBKUVGzsE4My7pbqkukjZJG45YD-fm_o_MfgLc6C-jeHyp1iZ6BNc8ddYlHAmaaXuHVb7viza0NB1Zc3Wc1alie-zd0mOFdAouZGmGHuAcy9XgYPjkEsy9FbRVtRlKq9jXSThcNg=
  - GADWA for Industrial Development Announces its Consolidated Results for the period ended on the 31st of March, 2026: https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFJdLX5o9bmU1QxMHng6sgSkSUNz67kqJVdZ7v_Xfat-9oB6ymRIgMZaq2xL1tO4etyQi-TMLef5nZDzx_VCRGEdZJivx01l4PaKI9s8ioex66ZQedGnzZIHpYnY4JpS0UEVBtAbc67eBOMAjx4
  - Gadwa for Industrial Development (EGX:GDWA) Statistics & Valuation Metrics: https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFyL7NeVXa8aULYQb-jTibvr1FPktwNZJ_70hy7SfjjeP3SqTVmmQq_Oj7_AC-fpcOnIJo6cWiY1NQcYSapMyMHzSuqIiiTvghQLzxiYMbP3ckHS4SEer5Pzq7Zu2hAwGHLh0PJO6iPmso1z7ySoA==
- RACC.CA: status=RECENT_ACCEPTED latest=2026-01-01 age_days=193 sources=3 expected=Raya Customer Experience summary=Raya Customer Experience (RACC.CA) reported consolidated revenues of EGP 854.5 million for Q1 2026, a 34.7% year-over-year increase, with net profit reaching EGP 80.2 million. For the full year 2025, revenues were EGP 2.88 billion, growing by 12.34%. Raya Holding has also proposed to acquire an additional 29.2% stake in Raya Customer Experience.
  - Raya Customer Experience Reports Q1 2026 Results: https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGp1x6moA89QFWkF0br2SCc5ygLa7HB2lzqWM8Tkv33DnbMus3Kxe8rGdZXptLWedrg-Gk_h8EXqLYrRrsqqKADU77SlPpWOhEF5RbM21rVwQiSDjfYXFdAnTt_XUKcY1mUoei3k9lxS3bo2ri-
  - Raya Customer Experience Reports FY2025 Results: https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHsAVCjHKjQ-febiFTOSbaksD6wlzhygKXACdcY8M3ycIfiNtMrpLRDrR4nPBgqLiB-LOlRDjv7T5rrJi4gt-zYoMxS5pQFORSFkUhbeAW3Sft2sy81XLKjLzsFJoK-tI1Hp7uihX_QVqGlgVCR
  - Raya Customer Experience Stock (RACC) - Quote Egyptian Exchange- MarketScreener - Latest news: https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHyvWNHPzgoBk6t_-qIoXt6Vpr5O6_IjL_A-ZVIoMKedJd0cGfgnnsfhDLoO0uTY6-XxCXycX17tNNLWTj15EbgqvrVMgETaIpGLTWKfXMa7SpaVr1kIasWFaAjEcyPV2CCLVwaLWz9goots2ZbFbnX-nQajOjMg0R0ju-VfcYH6ckJKcO1cA8=
- MCRO.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Macro Group Pharmaceuticals (Macro Capital) S.A.E summary=Macro Group’s EGP 570m capital increase nearly fully subscribed; Macro Group’s shareholders greenlight EGP 570m capital increase; Macro Group secures EGP 65m loan from FABMISR Gemini also reviewed web evidence but did not return ticker-specific citations.
  - Macro Group’s EGP 570m capital increase nearly fully subscribed: https://english.mubasher.info/news/4533695/Macro-Group-s-EGP-570m-capital-increase-nearly-fully-subscribed/
  - Macro Group’s shareholders greenlight EGP 570m capital increase: https://english.mubasher.info/news/4508284/Macro-Group-s-shareholders-greenlight-EGP-570m-capital-increase/
  - Macro Group secures EGP 65m loan from FABMISR: https://english.mubasher.info/news/4265398/Macro-Group-secures-EGP-65m-loan-from-FABMISR/
- ALCN.CA: status=RECENT_ACCEPTED latest=2026-07-11 age_days=2 sources=3 expected=Alexandria Containers and Cargo Handling summary=Alexandria Containers and Cargo Handling (ALCN.CA) reported Q1 2026 earnings results, with a quarterly net profit of EGP 1.94 billion. The company's revenue in the last 12 months was EGP 7.60 billion, with profits of EGP 6.79 billion. AD Ports is set to launch a tender offer to acquire an additional stake in the company. The stock price has increased by +23.38% in the last 52 weeks as of July 11, 2026.
  - Alexandria Container&Cargo Handling Company Reports Earnings Results for the First Quarter Ended March 31, 2026: https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHB6SV5bG-xtIBrzBKJ2As-g4uO3RBncxq_46DpEnD43ebGfzgAyJNbagiAiP5JZqhVgSNeH5F3dqalVUkfaDRar1y7IkkEyorDjwfKK66RhmKCyiUfdyO0W7zhds0tqXIg2YE060R6-DzKPGuMZ8QI20XpJNlJBZ0oDRTg1kGSQQqtqi9hfdk=
  - AD Ports to launch tender offer for Egypt's Alexandria Container & Cargo: https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHv2a_2A0rLwIb8gbjU3z2ydCxpzhsb_iCwMs6qJzGBsE1j6KYhtGc7EQcXrE-027eKdc3XbvW0HM_1LXN98tK0JtTH6wsXwq_wwtlpWNMI2QSUNJ79n0-UdW_sx_NfX2V7LkPptODhQ4jDLgAnSO-NgE0cRXNnu9MBg3yy
  - Alexandria Container&Cargo Handling Company (EGX:ALCN) Statistics & Valuation Metrics: https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFca7YvNQR3bubFEVh5ztqvBdNJKYJBmzUMF6XhtSsjjb9Cj01zVlc0Uit3JWhAqedDOQCdCHkJYdm0MTp7vwGq-74F6wytognE7UnIufu-0ch3a7-yEY05Bo3PNMmhmwxVlKRnxxT9jJFV1A13pw==
- COSG.CA: status=RECENT_ACCEPTED latest=2026-07-01 age_days=12 sources=3 expected=Cairo Oil & Soap Company summary=Cairo Oil & Soap Company (COSG.CA) reported a net income of EGP 5.89 million for the last quarter. In the last 12 months, the company had revenue of EGP 802.09 million and losses of EGP 60.34 million. The stock price has decreased by -4.15% in the last 52 weeks as of July 01, 2026.
  - Cairo Oil & Soap Company (EGX:COSG) Statistics & Valuation Metrics: https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEIhVMSnhLMI7Fye_5gB_7C7fs7qH1qgt8DgCpU9rbt_csxjqeYPlAowsJIlpDft6pHhNWoc4mGIF_aFLOjDPM6hGkhdf8Pz_8R5uR3OdUpTGtOR6sz_SgkyKgRU6O_4UBi2EJzBdfXQM0T5xbP6w==
  - EGX:COSG — TradingView - Cairo Oils & Soap (Net Income for last quarter): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGO3mW960JE-3YjzqFRRh1SV-ejfJ-SvNaPDNIpKO9QFTrQXM3Z0o_-9B9P3S18I-LAwlTByi-4BVloAj6GHOnksnIwI5sjO3WeoAVMglaxXlp8QEMQ0Ofi91V2AhumkRZ9QUV-L2gp
  - Cairo Oil & Soap Company (EGX:COSG) Balance Sheet: https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGnUP3Q5T2qoBW6agvsatryb63On06EHqnt1YCBQBwflMxWGDKEFKfqk0ZZgFg-i_Snsripg99dkWYMp9C8yHpxd9dWilI1y_jsapxm82SE27puA3ivBIIz00RBenrvkNk_6nSwD_SkhXN-gAn9Ga9YnCD0YcdLvP9LxADC
- RAYA.CA: status=RECENT_ACCEPTED latest=2026-07-12 age_days=1 sources=3 expected=Raya Holding summary=Raya Holding (RAYA.CA) reported revenue of EGP 66.76 billion and profits of EGP 2.60 billion in the last 12 months, with earnings per share of EGP 0.61. The stock price has increased by +142.42% in the last 52 weeks as of July 12, 2026. The company also proposed to acquire an additional 29.2% stake in Raya Customer Experience (RACC.CA) on August 31, 2025.
  - Raya Holding Company for Financial Investments (S.A.E) (EGX:RAYA) Statistics & Valuation Metrics: https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQENLkjH3JBrorVdAy5SnnwtCysaJ82bVGnvzlnfs7d8Ml-Y1CCzbdGVrxI5VR8P5Tw5iwsN3YkObBuUVuBHtYWDTENpxiAwmLE_gcqdn8f_yUDL0nSKG91Iff9e8WMf7KAf4G0OCt4uwTmeRKCoDA==
  - Raya Holding Company for Financial Investments (S.A.E) (CASE:RAYA) - Stock Analysis (mentions RACC acquisition proposal): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQETh3NgdtkTesI0YmMNAH0CEWF20IGLLQHA9yxcjERhpFMdEGvB_bcvcEuB8gO_n3kFBL7pgOecUvJccKu_0jV8eXbTJbnnKTcVtgbM2XJsPk5Fj-JUlvToMfKztfqpIpDTQIp-8Vop8PQZD7p9abMT-mk7vcQvhETA-7VEq__TDkaFihDCN4zFfHwrW7mcFlQ6Na6zgMsL_x2WA_hqZsXjE5AfpvGBOAafjbw=
  - Raya Holding For Financial Investments Corporate Video: https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFMFt9eyJ8bR6vigma-LWYTaOb6vg6NzQO9nVuBawBCwG7w0EGOGAjk8kOybmCvrE4fobgRbiVkRdkr6vJbhcXI_zHX7GZie33gPbjsZ20ihUTZ--5GbZd0aKgXY2hxoNGfC2B-BA==

## Warnings
- Evidence for ELEC.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for AREH.CA matches the company but no source/report date was detected.
- Evidence for MCRO.CA matches the company but no source/report date was detected.
