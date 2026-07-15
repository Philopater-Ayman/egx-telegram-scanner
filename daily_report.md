# Telegram-First EGX Scanner Report

Scan phase: Intraday liquidity update
Generated UTC: 2026-07-15T10:02:44.836375+00:00
Generated Cairo: 2026-07-15 13:02
Run timing: target 11:00 Cairo | generated Cairo 2026-07-15 13:02 | cron 0 8 * * 0-4
Trigger: scheduled cron=0 8 * * 0-4 mapped to intraday; Cairo now 2026-07-15 12:56

## Control Center
- Action tickets: 1 prioritized signal(s)
- BUY-ready candidates: 82
- Data quality issues: 1
- Tradeable price/liquidity tickers: 173/189
- Top sector: Technology & Distribution

## Market Context
- Market trend: Bullish
- Source: Mubasher EGX market page (delayed public data)
- As of: Wednesday, July 15
- Freshness: DELAYED
- EGX30 regime: MIXED / above MA20 60.0% / above MA50 45.0%
- EGX70 regime: MIXED / above MA20 75.68% / above MA50 72.97%
- Sector breadth: 38.1%
- Risk mode: SELECTIVE_SWING_TRADES_ONLY

## Top Liquidity
- CCAP.CA: liquidity=304418752.0 spike=0.46 score=26.4
- FWRY.CA: liquidity=231259840.0 spike=1.4 score=20.87
- TMGH.CA: liquidity=205462896.0 spike=0.59 score=26.4
- NIPH.CA: liquidity=197346416.0 spike=2.11 score=28.53
- PRDC.CA: liquidity=182719824.0 spike=1.16 score=9.72

## AI Narrative
- Provider: OpenRouter OK
- Model: nvidia/nemotron-3-super-120b-a12b:free
- Summary: We need to output JSON with keys summary and bullets (3-5 short strings). Must not make trade decision, not invent live data, not mention quantities or position sizing. Explain why scanner selected prioritized tickets, what liquidity/sector/support/resistance/outlook means for next 1-3 days, and how EGX30/EGX70 market regime changes risk mode, and include uncertainty.

We have data: primary ticket UNIP.CA, tickets list includes same. Market regime: EGX30 MIXED, EGX70 MIXED, risk mode SELECTIVE_SWING_TRADES_ONLY. Sector breadth 38.1%, leading sectors: Technology & Distribution, Industrial Goods & Cables, Automotive & Distribution.

We need to explain why scanner selected prioritized tickets: 
- Scanner flagged UNIP.CA as a low‑confidence BUY SETUP amid mixed EGX30/EGX70 conditions and selective swing‑trade risk mode.
- Price sits above MA20/MA50 with RSI ~61, but is far above the 0.29 support and fl support and near the 0.35 resistance, limiting near‑term upside.
- Liquidity shows an accumulation spike (~2x average) indicating buying interest, yet the sector (General/Verified EGX Expansion) is not among the leading groups.
- Outlook label BULLISH_WATCH with high outlook score suggests cautious optimism, but confidence is LOW due to weak sector breadth (38.1%) and mixed market regime.
- EGX30 and EGX70 both MIXED, triggering SELECTIVE_SWING_TRADES_ONLY risk mode, which raises uncertainty and requires verification before acting.

## Top Liquidity Spikes
- SMFR.CA: spike=17.59 liquidity=120141152.0 outlook=CONSTRUCTIVE score=64.97 buy_ready=False
- OCPH.CA: spike=14.25 liquidity=133137808.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- CPCI.CA: spike=11.61 liquidity=66424744.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- CAED.CA: spike=11.12 liquidity=126261056.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- NEDA.CA: spike=6.52 liquidity=2454723.75 outlook=BULLISH_WATCH score=88.97 buy_ready=True

## Sector Leaderboard
- #1 Technology & Distribution: score=10.42 5d=0.99% 20d=16.14% aboveMA50=100.0%
- #2 Industrial Goods & Cables: score=10.27 5d=0.26% 20d=2.28% aboveMA50=100.0%
- #3 Automotive & Distribution: score=9.86 5d=2.21% 20d=7.8% aboveMA50=100.0%
- #4 Transportation & Logistics: score=8.38 5d=0.32% 20d=2.7% aboveMA50=100.0%
- #5 Energy & Petrochemicals: score=8.06 5d=5.07% 20d=5.05% aboveMA50=75.0%
- #6 Telecommunications: score=7.64 5d=-0.07% 20d=3.37% aboveMA50=100.0%
- #7 Textiles: score=7.58 5d=1.67% 20d=4.98% aboveMA50=100.0%
- #8 General / Verified EGX Expansion: score=6.97 5d=1.43% 20d=3.33% aboveMA50=75.73%

## Today's Prioritized Action Tickets
- Priority #1: BUY UNIP.CA
  - Entry: 0.35 | Take profit: 0.37 | Stop loss: 0.34
  - Confidence: LOW | score=30.38 | outlook=BULLISH_WATCH 86.97
  - Reason: BUY SETUP: UNIP.CA has aligned current price data, liquidity above threshold, price above MA20/MA50, RSI 61.36, support 0.29, resistance 0.35, and evidence sources. Macro trend is Bullish; market regime is SELECTIVE_SWING_TRADES_ONLY; verify price action in Thndr before treating it as a swing entry.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- SWDY.CA: BULLISH_WATCH score=100 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=close to resistance
- ELEC.CA: BULLISH_WATCH score=96 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=close to resistance
- MILS.CA: BULLISH_WATCH score=94.97 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- MEPA.CA: BULLISH_WATCH score=88.97 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- NEDA.CA: BULLISH_WATCH score=88.97 liquidity=TRADEABLE sector=IMPROVING risk=sector is not leading
- GBCO.CA: BULLISH_WATCH score=88.86 liquidity=TRADEABLE sector=LEADING risk=No major short-term scanner risk flags.
- PHAR.CA: BULLISH_WATCH score=87.77 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- UNIP.CA: BULLISH_WATCH score=86.97 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=far above support; sector is not leading
- EGAS.CA: BULLISH_WATCH score=84.06 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- OFH.CA: BULLISH_WATCH score=82.97 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended; sector is not leading

## BUY-Ready Candidates
- SWDY.CA: rank=32.5 outlook=BULLISH_WATCH outlook_score=100 sector_rank=2 price=89.91 support=84.3 resistance=90.97 liquidity=39103648.0
- OFH.CA: rank=32.02 outlook=BULLISH_WATCH outlook_score=82.97 sector_rank=8 price=0.65 support=0.57 resistance=0.65 liquidity=66501364.0
- UNIP.CA: rank=30.38 outlook=BULLISH_WATCH outlook_score=86.97 sector_rank=8 price=0.35 support=0.29 resistance=0.35 liquidity=30388400.0
- MEPA.CA: rank=30.0 outlook=BULLISH_WATCH outlook_score=88.97 sector_rank=8 price=1.7 support=1.52 resistance=1.74 liquidity=31419764.0
- AFMC.CA: rank=29.8 outlook=BULLISH_WATCH outlook_score=76.97 sector_rank=8 price=75.93 support=66.0 resistance=76.5 liquidity=10449011.0
- NINH.CA: rank=29.4 outlook=BULLISH_WATCH outlook_score=82.97 sector_rank=8 price=18.5 support=17.03 resistance=18.85 liquidity=40338568.0
- ELEC.CA: rank=29.18 outlook=BULLISH_WATCH outlook_score=96 sector_rank=2 price=2.18 support=2.04 resistance=2.21 liquidity=52374612.0
- NIPH.CA: rank=28.53 outlook=BULLISH_WATCH outlook_score=77.77 sector_rank=13 price=191.0 support=157.01 resistance=185.5 liquidity=197346416.0
- GDWA.CA: rank=28.4 outlook=BULLISH_WATCH outlook_score=75.97 sector_rank=8 price=0.85 support=0.76 resistance=0.87 liquidity=92861800.0
- SIPC.CA: rank=27.92 outlook=BULLISH_WATCH outlook_score=82.97 sector_rank=8 price=3.59 support=3.25 resistance=3.6 liquidity=12330374.0

## Data Quality Issues
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=26.42 buy_ready=True sector_rank=8 price=232.44 support=196.0 resistance=247.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=63.12 liquidity=13902683.0 spike=1.01
- ABUK.CA: score=23.0 buy_ready=False sector_rank=14 price=72.5 support=66.66 resistance=73.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=65.59 liquidity=139064320.0 spike=0.84
- ACAMD.CA: score=22.4 buy_ready=False sector_rank=8 price=2.31 support=2.14 resistance=2.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT RSI=54.29 liquidity=21889616.0 spike=0.25
- ACGC.CA: score=21.01 buy_ready=True sector_rank=7 price=9.89 support=8.92 resistance=10.16 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=63.37 liquidity=4612466.5 spike=0.23
- ADCI.CA: score=26.02 buy_ready=True sector_rank=8 price=245.66 support=223.15 resistance=248.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT RSI=41.79 liquidity=20255586.0 spike=1.81
- ADIB.CA: score=20.21 buy_ready=False sector_rank=16 price=46.5 support=44.1 resistance=48.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=53.63 liquidity=31036424.0 spike=0.33
- ADPC.CA: score=26.4 buy_ready=True sector_rank=8 price=3.82 support=3.32 resistance=3.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT RSI=57.47 liquidity=15453433.0 spike=0.72
- AFDI.CA: score=19.72 buy_ready=True sector_rank=8 price=46.97 support=41.84 resistance=48.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=51.25 liquidity=3324730.5 spike=0.24
- AFMC.CA: score=29.8 buy_ready=True sector_rank=8 price=75.93 support=66.0 resistance=76.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=60.05 liquidity=10449011.0 spike=2.7
- AJWA.CA: score=18.91 buy_ready=False sector_rank=8 price=177.01 support=172.1 resistance=192.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=52.08 liquidity=6506343.5 spike=0.34
- ALCN.CA: score=26.12 buy_ready=True sector_rank=4 price=29.98 support=27.7 resistance=30.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=65.35 liquidity=34761004.0 spike=1.86
- ALUM.CA: score=20.86 buy_ready=False sector_rank=8 price=22.94 support=20.55 resistance=23.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT RSI=48.19 liquidity=7116055.5 spike=1.17
- AMER.CA: score=9.86 buy_ready=False sector_rank=11 price=3.42 support=3.18 resistance=3.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=95447208.0 spike=1.23
- AMES.CA: score=13.0 buy_ready=False sector_rank=8 price=144.94 support=127.0 resistance=144.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=180260128.0 spike=2.8
- AMIA.CA: score=17.17 buy_ready=True sector_rank=8 price=8.9 support=8.4 resistance=9.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=53.85 liquidity=2766311.25 spike=0.32
- AMOC.CA: score=26.4 buy_ready=False sector_rank=5 price=8.18 support=7.42 resistance=8.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=70.95 liquidity=32127972.0 spike=0.55
- APSW.CA: score=11.16 buy_ready=False sector_rank=8 price=8.41 support=8.0 resistance=8.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=45.67 liquidity=763739.31 spike=0.82
- ARAB.CA: score=23.6 buy_ready=False sector_rank=11 price=0.26 support=0.2 resistance=0.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT RSI=80.56 liquidity=101707840.0 spike=1.1
- ARCC.CA: score=15.87 buy_ready=False sector_rank=20 price=54.5 support=53.0 resistance=56.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT RSI=47.2 liquidity=8578494.0 spike=0.44
- AREH.CA: score=27.3 buy_ready=True sector_rank=8 price=1.63 support=1.51 resistance=1.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=68.29 liquidity=51580984.0 spike=1.45
- ARVA.CA: score=14.16 buy_ready=False sector_rank=8 price=10.67 support=10.5 resistance=12.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=38.99 liquidity=1757616.13 spike=0.09
- ASCM.CA: score=24.4 buy_ready=True sector_rank=8 price=61.72 support=56.29 resistance=73.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT RSI=46.48 liquidity=12361457.0 spike=0.16
- ASPI.CA: score=22.78 buy_ready=False sector_rank=8 price=0.32 support=0.3 resistance=0.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT RSI=45.45 liquidity=26681156.0 spike=1.19
- ATLC.CA: score=14.71 buy_ready=True sector_rank=15 price=5.25 support=4.92 resistance=5.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:30 AM market time freshness=DELAYED_CURRENT RSI=54.31 liquidity=1064351.75 spike=0.15
- ATQA.CA: score=17.04 buy_ready=False sector_rank=14 price=9.51 support=9.21 resistance=9.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT RSI=59.29 liquidity=7039631.5 spike=0.22
- AXPH.CA: score=22.78 buy_ready=True sector_rank=8 price=1235.96 support=1073.0 resistance=1342.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT RSI=64.09 liquidity=5240668.5 spike=1.57
- BINV.CA: score=17.53 buy_ready=True sector_rank=10 price=48.88 support=45.01 resistance=51.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=54.25 liquidity=3131220.5 spike=0.5
- BIOC.CA: score=14.4 buy_ready=False sector_rank=8 price=80.76 support=73.23 resistance=80.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=16647892.0 spike=5.07
- BTFH.CA: score=21.64 buy_ready=False sector_rank=15 price=3.04 support=2.91 resistance=3.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=51.43 liquidity=44915036.0 spike=0.23
- CAED.CA: score=14.4 buy_ready=False sector_rank=8 price=107.16 support=93.2 resistance=107.16 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=126261056.0 spike=11.12
- CANA.CA: score=13.14 buy_ready=False sector_rank=16 price=35.91 support=34.7 resistance=38.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=40.96 liquidity=2931356.0 spike=0.29
- CCAP.CA: score=26.4 buy_ready=True sector_rank=10 price=5.45 support=4.65 resistance=5.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT RSI=66.94 liquidity=304418752.0 spike=0.46
- CCRS.CA: score=26.4 buy_ready=True sector_rank=8 price=2.56 support=2.18 resistance=2.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT RSI=56.76 liquidity=11933870.0 spike=0.89
- CEFM.CA: score=11.22 buy_ready=False sector_rank=8 price=109.43 support=103.01 resistance=111.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:31 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=7223602.5 spike=3.3
- CERA.CA: score=25.3 buy_ready=True sector_rank=8 price=1.36 support=1.17 resistance=1.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=65.22 liquidity=29895166.0 spike=1.45
- CFGH.CA: score=12.65 buy_ready=False sector_rank=8 price=0.11 support=0.1 resistance=0.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:02 AM market time freshness=DELAYED_CURRENT RSI=88.89 liquidity=8934.0 spike=1.12
- CICH.CA: score=15.52 buy_ready=True sector_rank=15 price=12.08 support=11.45 resistance=12.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=47.95 liquidity=1878815.25 spike=0.47
- CIEB.CA: score=17.32 buy_ready=True sector_rank=16 price=24.3 support=23.3 resistance=24.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=50.52 liquidity=2115184.5 spike=0.32
- CIRA.CA: score=29.0 buy_ready=False sector_rank=9 price=32.76 support=26.0 resistance=32.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=71.78 liquidity=66583088.0 spike=2.3
- CLHO.CA: score=24.31 buy_ready=True sector_rank=13 price=16.29 support=15.25 resistance=17.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=47.18 liquidity=21493754.0 spike=0.56
- CNFN.CA: score=22.71 buy_ready=True sector_rank=15 price=4.88 support=4.4 resistance=5.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=35.8 liquidity=7067241.0 spike=0.15
- COMI.CA: score=25.21 buy_ready=True sector_rank=16 price=134.96 support=126.21 resistance=137.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=52.61 liquidity=99057040.0 spike=0.23
- COPR.CA: score=23.4 buy_ready=True sector_rank=8 price=0.38 support=0.35 resistance=0.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT RSI=64.58 liquidity=20370624.0 spike=0.92
- COSG.CA: score=26.4 buy_ready=True sector_rank=8 price=1.66 support=1.47 resistance=1.71 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT RSI=68.75 liquidity=15480936.0 spike=0.37
- CPCI.CA: score=14.4 buy_ready=False sector_rank=8 price=504.8 support=430.03 resistance=512.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=66424744.0 spike=11.61
- CSAG.CA: score=19.5 buy_ready=True sector_rank=4 price=32.47 support=30.87 resistance=33.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=67.16 liquidity=7097612.5 spike=0.42
- DAPH.CA: score=18.69 buy_ready=True sector_rank=8 price=84.0 support=77.52 resistance=87.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=55.12 liquidity=2289545.25 spike=0.26
- DEIN.CA: score=-0.6 buy_ready=False sector_rank=8 price=11.38 support=13.65 resistance=13.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 June 12:11 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=40.95 spike=0.01
- DOMT.CA: score=14.59 buy_ready=True sector_rank=18 price=26.71 support=24.26 resistance=27.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=38.95 liquidity=1861341.25 spike=0.38
- DSCW.CA: score=24.88 buy_ready=True sector_rank=8 price=1.85 support=1.71 resistance=1.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=60.0 liquidity=9478005.0 spike=0.29
- DTPP.CA: score=21.4 buy_ready=False sector_rank=8 price=204.0 support=114.67 resistance=234.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=84.84 liquidity=11924009.0 spike=0.3
- EALR.CA: score=27.34 buy_ready=True sector_rank=8 price=375.0 support=332.0 resistance=425.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=54.11 liquidity=17370410.0 spike=1.47
- EASB.CA: score=20.98 buy_ready=False sector_rank=8 price=7.12 support=5.9 resistance=10.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=43.73 liquidity=8581634.0 spike=0.47
- EAST.CA: score=11.73 buy_ready=False sector_rank=18 price=36.3 support=36.33 resistance=40.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=34.03 liquidity=14835129.0 spike=0.3
- EBSC.CA: score=15.74 buy_ready=False sector_rank=8 price=1.89 support=1.71 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT RSI=54.05 liquidity=3340836.25 spike=0.53
- ECAP.CA: score=19.38 buy_ready=True sector_rank=8 price=33.09 support=31.3 resistance=34.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT RSI=48.09 liquidity=4979472.0 spike=0.58
- EDFM.CA: score=16.98 buy_ready=False sector_rank=8 price=360.29 support=310.2 resistance=363.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:32 AM market time freshness=DELAYED_CURRENT RSI=76.81 liquidity=1780026.88 spike=1.9
- EEII.CA: score=24.4 buy_ready=True sector_rank=8 price=2.79 support=2.35 resistance=2.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=67.78 liquidity=10564714.0 spike=0.53
- EFIC.CA: score=22.26 buy_ready=False sector_rank=14 price=190.03 support=180.02 resistance=213.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=45.66 liquidity=12630742.0 spike=2.13
- EFID.CA: score=19.73 buy_ready=False sector_rank=18 price=27.71 support=25.5 resistance=28.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=53.6 liquidity=14671157.0 spike=0.31
- EFIH.CA: score=23.48 buy_ready=True sector_rank=17 price=22.06 support=20.0 resistance=23.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=58.35 liquidity=8412322.0 spike=0.19
- EGAL.CA: score=26.72 buy_ready=False sector_rank=14 price=303.58 support=272.28 resistance=303.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=60.9 liquidity=86079944.0 spike=1.86
- EGAS.CA: score=25.93 buy_ready=True sector_rank=5 price=52.01 support=46.51 resistance=54.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT RSI=57.16 liquidity=9533479.0 spike=0.79
- EGBE.CA: score=10.27 buy_ready=False sector_rank=16 price=0.44 support=-0.34 resistance=0.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:17 AM market time freshness=DELAYED_CURRENT RSI=96.16 liquidity=66685.61 spike=-1.6
- EGCH.CA: score=23.0 buy_ready=False sector_rank=14 price=13.4 support=12.13 resistance=13.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=63.16 liquidity=35006928.0 spike=0.68
- EGSA.CA: score=14.73 buy_ready=False sector_rank=6 price=8.97 support=8.67 resistance=9.13 source=Yahoo Finance as_of=2026-07-13T21:00:00+00:00 freshness=FRESH RSI=70.21 liquidity=5812.56 spike=1.16
- EGTS.CA: score=24.4 buy_ready=True sector_rank=11 price=18.88 support=15.1 resistance=19.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT RSI=56.05 liquidity=48441112.0 spike=0.95
- EHDR.CA: score=26.52 buy_ready=True sector_rank=8 price=2.77 support=2.37 resistance=2.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=58.54 liquidity=36380996.0 spike=1.06
- EKHO.CA: score=8.4 buy_ready=False sector_rank=5 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-07-13T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=29.18 buy_ready=True sector_rank=2 price=2.18 support=2.04 resistance=2.21 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=53.57 liquidity=52374612.0 spike=1.89
- ELKA.CA: score=23.46 buy_ready=False sector_rank=8 price=1.83 support=1.19 resistance=1.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT RSI=83.12 liquidity=56316996.0 spike=1.03
- ELNA.CA: score=16.51 buy_ready=False sector_rank=8 price=39.47 support=35.55 resistance=40.65 source=Yahoo Finance as_of=2026-07-13T21:00:00+00:00 freshness=FRESH RSI=58.32 liquidity=107989.92 spike=0.21
- ELSH.CA: score=24.4 buy_ready=False sector_rank=8 price=14.6 support=11.1 resistance=15.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=70.1 liquidity=30980274.0 spike=0.22
- ELWA.CA: score=17.82 buy_ready=True sector_rank=8 price=2.05 support=1.87 resistance=2.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:33 AM market time freshness=DELAYED_CURRENT RSI=48.72 liquidity=1418009.75 spike=0.79
- EMFD.CA: score=20.3 buy_ready=False sector_rank=11 price=11.7 support=11.24 resistance=12.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=52.52 liquidity=7901791.0 spike=0.06
- ENGC.CA: score=26.4 buy_ready=False sector_rank=8 price=43.0 support=33.91 resistance=44.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=74.33 liquidity=11652687.0 spike=0.48
- EOSB.CA: score=14.42 buy_ready=False sector_rank=8 price=1.48 support=1.42 resistance=1.55 source=Yahoo Finance as_of=2026-07-13T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=22083.08 spike=0.35
- EPCO.CA: score=26.8 buy_ready=False sector_rank=8 price=10.16 support=8.5 resistance=10.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=71.05 liquidity=16577912.0 spike=1.2
- EPPK.CA: score=16.3 buy_ready=True sector_rank=8 price=14.74 support=11.75 resistance=15.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=69.3 liquidity=1316132.38 spike=1.29
- ETEL.CA: score=26.4 buy_ready=True sector_rank=6 price=97.98 support=89.01 resistance=101.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=54.82 liquidity=11900467.0 spike=0.17
- ETRS.CA: score=18.0 buy_ready=True sector_rank=8 price=10.87 support=9.84 resistance=11.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=56.91 liquidity=3601772.75 spike=0.05
- EXPA.CA: score=25.93 buy_ready=True sector_rank=16 price=18.81 support=18.03 resistance=18.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT RSI=62.09 liquidity=8725086.0 spike=0.35
- FAIT.CA: score=16.03 buy_ready=False sector_rank=16 price=36.87 support=35.06 resistance=37.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT RSI=54.36 liquidity=820142.69 spike=0.3
- FAITA.CA: score=8.58 buy_ready=False sector_rank=16 price=0.99 support=0.98 resistance=1.0 source=Yahoo Finance as_of=2026-07-13T21:00:00+00:00 freshness=FRESH RSI=47.37 liquidity=33967.73 spike=1.17
- FERC.CA: score=19.26 buy_ready=False sector_rank=14 price=76.5 support=72.75 resistance=80.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=53.89 liquidity=4952524.0 spike=1.15
- FWRY.CA: score=20.87 buy_ready=False sector_rank=17 price=18.6 support=18.13 resistance=19.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=50.19 liquidity=231259840.0 spike=1.4
- GBCO.CA: score=26.22 buy_ready=True sector_rank=3 price=33.0 support=27.77 resistance=32.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT RSI=55.44 liquidity=98984016.0 spike=1.41
- GDWA.CA: score=28.4 buy_ready=True sector_rank=8 price=0.85 support=0.76 resistance=0.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=66.67 liquidity=92861800.0 spike=3.52
- GGCC.CA: score=13.56 buy_ready=False sector_rank=8 price=0.68 support=0.64 resistance=0.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=59936868.0 spike=3.08
- GIHD.CA: score=14.04 buy_ready=False sector_rank=8 price=52.65 support=48.72 resistance=55.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:44 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=85005296.0 spike=3.32
- GMCI.CA: score=15.14 buy_ready=False sector_rank=8 price=2.02 support=1.66 resistance=2.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=68.06 liquidity=744121.88 spike=0.65
- GRCA.CA: score=16.69 buy_ready=False sector_rank=8 price=54.05 support=48.0 resistance=58.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:44 AM market time freshness=DELAYED_CURRENT RSI=42.56 liquidity=3293358.5 spike=0.92
- GSSC.CA: score=20.92 buy_ready=True sector_rank=8 price=260.89 support=240.0 resistance=263.63 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=63.14 liquidity=4500510.5 spike=1.01
- GTWL.CA: score=9.4 buy_ready=False sector_rank=8 price=104.33 support=103.1 resistance=111.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:44 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=62255048.0 spike=0.61
- HDBK.CA: score=10.73 buy_ready=False sector_rank=16 price=77.94 support=75.3 resistance=172.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=6.93 liquidity=8518167.0 spike=0.21
- HELI.CA: score=21.4 buy_ready=False sector_rank=11 price=7.62 support=6.34 resistance=7.62 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=78.44 liquidity=135295664.0 spike=0.9
- HRHO.CA: score=17.64 buy_ready=False sector_rank=15 price=26.39 support=26.09 resistance=27.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=44.62 liquidity=19301658.0 spike=0.15
- ICID.CA: score=16.79 buy_ready=True sector_rank=8 price=8.0 support=6.55 resistance=8.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT RSI=60.6 liquidity=2393070.5 spike=0.28
- IDRE.CA: score=22.66 buy_ready=True sector_rank=8 price=45.59 support=41.1 resistance=47.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=49.67 liquidity=6262453.5 spike=0.46
- IFAP.CA: score=14.81 buy_ready=False sector_rank=12 price=19.52 support=18.47 resistance=20.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT RSI=63.03 liquidity=1482419.63 spike=0.32
- INFI.CA: score=19.74 buy_ready=True sector_rank=8 price=101.99 support=88.51 resistance=106.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=61.67 liquidity=4337238.0 spike=0.43
- IRON.CA: score=12.0 buy_ready=False sector_rank=14 price=32.0 support=30.45 resistance=33.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=56.09 liquidity=1993728.63 spike=0.25
- ISMA.CA: score=11.3 buy_ready=False sector_rank=8 price=27.33 support=26.54 resistance=36.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT RSI=20.05 liquidity=3895229.5 spike=0.15
- ISMQ.CA: score=22.0 buy_ready=True sector_rank=14 price=9.59 support=8.06 resistance=10.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT RSI=67.68 liquidity=80625888.0 spike=0.56
- ISPH.CA: score=14.31 buy_ready=False sector_rank=13 price=11.43 support=11.2 resistance=12.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT RSI=29.73 liquidity=17567530.0 spike=0.3
- JUFO.CA: score=15.55 buy_ready=False sector_rank=18 price=30.03 support=29.1 resistance=32.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=40.92 liquidity=4826018.5 spike=0.22
- KABO.CA: score=23.4 buy_ready=False sector_rank=7 price=7.79 support=6.04 resistance=7.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=95.56 liquidity=29416544.0 spike=0.96
- KWIN.CA: score=26.4 buy_ready=True sector_rank=8 price=73.59 support=65.0 resistance=79.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=63.72 liquidity=13297186.0 spike=0.94
- KZPC.CA: score=12.77 buy_ready=False sector_rank=8 price=8.61 support=8.26 resistance=9.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:44 AM market time freshness=DELAYED_CURRENT RSI=44.92 liquidity=2368772.75 spike=0.4
- LCSW.CA: score=7.31 buy_ready=False sector_rank=20 price=33.08 support=30.89 resistance=33.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=61018760.0 spike=1.01
- LUTS.CA: score=11.52 buy_ready=False sector_rank=8 price=0.77 support=0.75 resistance=0.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=100763168.0 spike=2.06
- MAAL.CA: score=18.93 buy_ready=False sector_rank=8 price=8.42 support=5.82 resistance=8.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT RSI=98.94 liquidity=5533261.0 spike=0.33
- MASR.CA: score=24.4 buy_ready=False sector_rank=8 price=8.26 support=6.71 resistance=8.21 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=73.52 liquidity=38085808.0 spike=0.46
- MBSC.CA: score=15.25 buy_ready=False sector_rank=20 price=235.25 support=222.66 resistance=254.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=40.9 liquidity=7955965.5 spike=0.38
- MCQE.CA: score=15.52 buy_ready=False sector_rank=20 price=176.1 support=166.66 resistance=182.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT RSI=57.42 liquidity=4227434.0 spike=0.31
- MCRO.CA: score=27.78 buy_ready=False sector_rank=8 price=1.37 support=1.17 resistance=1.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:44 AM market time freshness=DELAYED_CURRENT RSI=73.33 liquidity=105855248.0 spike=2.19
- MENA.CA: score=14.96 buy_ready=False sector_rank=11 price=7.06 support=6.59 resistance=7.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:30 AM market time freshness=DELAYED_CURRENT RSI=59.34 liquidity=563797.69 spike=0.08
- MEPA.CA: score=30.0 buy_ready=True sector_rank=8 price=1.7 support=1.52 resistance=1.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=53.12 liquidity=31419764.0 spike=2.8
- MFPC.CA: score=23.0 buy_ready=False sector_rank=14 price=38.01 support=34.22 resistance=38.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=65.91 liquidity=69415048.0 spike=0.64
- MFSC.CA: score=19.68 buy_ready=False sector_rank=8 price=47.3 support=44.0 resistance=56.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:34 AM market time freshness=DELAYED_CURRENT RSI=29.69 liquidity=9783632.0 spike=1.25
- MHOT.CA: score=2.6 buy_ready=False sector_rank=21 price=16.53 support=16.12 resistance=38.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=3.57 liquidity=3198906.25 spike=0.21
- MICH.CA: score=24.4 buy_ready=True sector_rank=8 price=38.02 support=34.0 resistance=39.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=49.35 liquidity=11396378.0 spike=0.87
- MILS.CA: score=27.56 buy_ready=True sector_rank=8 price=138.79 support=126.31 resistance=147.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:44 AM market time freshness=DELAYED_CURRENT RSI=60.35 liquidity=18427920.0 spike=1.58
- MIPH.CA: score=21.52 buy_ready=False sector_rank=13 price=734.66 support=630.13 resistance=725.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=71.55 liquidity=4152844.75 spike=1.53
- MOED.CA: score=25.4 buy_ready=True sector_rank=8 price=0.73 support=0.65 resistance=0.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=62.89 liquidity=12424139.0 spike=0.94
- MOIL.CA: score=14.45 buy_ready=False sector_rank=5 price=0.54 support=0.46 resistance=0.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:32 AM market time freshness=DELAYED_CURRENT RSI=72.36 liquidity=53286.9 spike=0.15
- MOIN.CA: score=12.83 buy_ready=False sector_rank=8 price=24.04 support=22.6 resistance=24.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:41 AM market time freshness=DELAYED_CURRENT RSI=60.72 liquidity=434107.34 spike=0.49
- MOSC.CA: score=23.4 buy_ready=False sector_rank=8 price=278.69 support=250.0 resistance=329.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=55.66 liquidity=11581547.0 spike=0.81
- MPCI.CA: score=24.4 buy_ready=True sector_rank=8 price=246.49 support=217.0 resistance=256.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:44 AM market time freshness=DELAYED_CURRENT RSI=44.17 liquidity=46032912.0 spike=0.47
- MPCO.CA: score=24.33 buy_ready=True sector_rank=12 price=1.92 support=1.7 resistance=2.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=47507284.0 spike=0.56
- MPRC.CA: score=21.4 buy_ready=False sector_rank=8 price=43.54 support=31.72 resistance=43.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=83.21 liquidity=27034340.0 spike=0.55
- MTIE.CA: score=27.4 buy_ready=True sector_rank=3 price=9.6 support=8.75 resistance=9.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT RSI=63.37 liquidity=11126063.0 spike=0.47
- NAHO.CA: score=8.42 buy_ready=False sector_rank=8 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance as_of=2026-07-13T21:00:00+00:00 freshness=FRESH RSI=42.86 liquidity=16421.5 spike=0.73
- NCCW.CA: score=24.96 buy_ready=True sector_rank=8 price=6.44 support=5.82 resistance=6.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:44 AM market time freshness=DELAYED_CURRENT RSI=50.77 liquidity=8559901.0 spike=0.39
- NEDA.CA: score=23.85 buy_ready=True sector_rank=8 price=2.92 support=2.7 resistance=2.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT RSI=57.14 liquidity=2454723.75 spike=6.52
- NHPS.CA: score=14.32 buy_ready=False sector_rank=8 price=91.77 support=82.1 resistance=95.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:44 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=159225360.0 spike=3.46
- NINH.CA: score=29.4 buy_ready=True sector_rank=8 price=18.5 support=17.03 resistance=18.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:44 AM market time freshness=DELAYED_CURRENT RSI=50.41 liquidity=40338568.0 spike=4.05
- NIPH.CA: score=28.53 buy_ready=True sector_rank=13 price=191.0 support=157.01 resistance=185.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT RSI=66.8 liquidity=197346416.0 spike=2.11
- OBRI.CA: score=26.4 buy_ready=True sector_rank=8 price=36.31 support=31.5 resistance=39.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:44 AM market time freshness=DELAYED_CURRENT RSI=55.1 liquidity=11027129.0 spike=0.34
- OCDI.CA: score=24.4 buy_ready=False sector_rank=11 price=27.28 support=20.66 resistance=28.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=72.62 liquidity=28669384.0 spike=0.29
- OCPH.CA: score=14.4 buy_ready=False sector_rank=8 price=445.0 support=384.8 resistance=447.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:44 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=133137808.0 spike=14.25
- ODIN.CA: score=15.57 buy_ready=False sector_rank=8 price=2.45 support=2.05 resistance=2.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=75.76 liquidity=4172120.0 spike=0.29
- OFH.CA: score=32.02 buy_ready=True sector_rank=8 price=0.65 support=0.57 resistance=0.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:44 AM market time freshness=DELAYED_CURRENT RSI=63.89 liquidity=66501364.0 spike=2.81
- OIH.CA: score=25.4 buy_ready=False sector_rank=10 price=1.41 support=1.35 resistance=1.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=57.14 liquidity=12176476.0 spike=0.18
- OLFI.CA: score=24.73 buy_ready=True sector_rank=18 price=22.61 support=21.0 resistance=23.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=64.53 liquidity=11589472.0 spike=0.34
- ORAS.CA: score=7.6 buy_ready=False sector_rank=19 price=695.76 support=685.21 resistance=697.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=65179736.0 spike=1.0
- ORHD.CA: score=24.4 buy_ready=True sector_rank=11 price=39.14 support=37.0 resistance=39.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=91724592.0 spike=0.61
- ORWE.CA: score=22.4 buy_ready=False sector_rank=7 price=22.78 support=21.95 resistance=23.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT RSI=40.58 liquidity=11042451.0 spike=0.6
- PHAR.CA: score=25.63 buy_ready=True sector_rank=13 price=87.38 support=83.5 resistance=89.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=46.5 liquidity=36252844.0 spike=1.66
- PHDC.CA: score=17.4 buy_ready=False sector_rank=11 price=14.71 support=14.26 resistance=16.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=27.27 liquidity=45767832.0 spike=0.15
- PHTV.CA: score=12.26 buy_ready=False sector_rank=8 price=297.15 support=216.31 resistance=308.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=80.32 liquidity=856186.44 spike=0.06
- POUL.CA: score=20.22 buy_ready=True sector_rank=18 price=39.8 support=35.28 resistance=41.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=45.97 liquidity=5495155.0 spike=0.12
- PRCL.CA: score=24.29 buy_ready=True sector_rank=20 price=34.46 support=24.5 resistance=36.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=56.1 liquidity=24950190.0 spike=0.54
- PRDC.CA: score=9.72 buy_ready=False sector_rank=11 price=9.36 support=9.05 resistance=9.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=182719824.0 spike=1.16
- PRMH.CA: score=23.31 buy_ready=True sector_rank=8 price=2.74 support=2.34 resistance=3.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:44 AM market time freshness=DELAYED_CURRENT RSI=51.19 liquidity=6910027.5 spike=0.21
- RACC.CA: score=22.97 buy_ready=True sector_rank=8 price=10.3 support=9.36 resistance=10.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=56.76 liquidity=6570090.5 spike=0.37
- RAKT.CA: score=15.21 buy_ready=False sector_rank=8 price=22.22 support=21.25 resistance=23.79 source=Yahoo Finance as_of=2026-07-13T21:00:00+00:00 freshness=FRESH RSI=40.22 liquidity=806697.08 spike=3.0
- RAYA.CA: score=27.4 buy_ready=True sector_rank=1 price=8.06 support=6.8 resistance=8.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT RSI=67.94 liquidity=63498840.0 spike=0.53
- RMDA.CA: score=14.23 buy_ready=False sector_rank=13 price=4.96 support=4.81 resistance=5.16 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=44.26 liquidity=4917857.0 spike=0.25
- ROTO.CA: score=24.4 buy_ready=True sector_rank=8 price=42.02 support=34.5 resistance=47.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=47.72 liquidity=10044949.0 spike=0.3
- RREI.CA: score=28.16 buy_ready=False sector_rank=8 price=3.99 support=3.34 resistance=3.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:44 AM market time freshness=DELAYED_CURRENT RSI=78.57 liquidity=74325984.0 spike=3.38
- RTVC.CA: score=15.18 buy_ready=False sector_rank=8 price=3.85 support=3.55 resistance=3.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=52.31 liquidity=1778050.38 spike=0.46
- RUBX.CA: score=23.84 buy_ready=False sector_rank=8 price=14.6 support=9.8 resistance=14.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:44 AM market time freshness=DELAYED_CURRENT RSI=81.44 liquidity=79339384.0 spike=1.22
- SAUD.CA: score=12.15 buy_ready=False sector_rank=16 price=21.4 support=19.99 resistance=22.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=1945290.38 spike=0.32
- SCEM.CA: score=11.45 buy_ready=False sector_rank=20 price=62.06 support=60.14 resistance=67.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT RSI=52.98 liquidity=4157145.5 spike=0.24
- SCFM.CA: score=26.74 buy_ready=False sector_rank=8 price=256.37 support=226.5 resistance=269.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=59.84 liquidity=13821419.0 spike=2.67
- SCTS.CA: score=18.03 buy_ready=True sector_rank=9 price=615.07 support=540.0 resistance=649.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=62.19 liquidity=1626677.25 spike=0.33
- SDTI.CA: score=17.64 buy_ready=True sector_rank=8 price=47.04 support=45.55 resistance=49.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=53.91 liquidity=3237747.25 spike=0.49
- SEIG.CA: score=21.4 buy_ready=False sector_rank=8 price=242.64 support=181.35 resistance=285.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=79.95 liquidity=13340257.0 spike=0.65
- SIPC.CA: score=27.92 buy_ready=True sector_rank=8 price=3.59 support=3.25 resistance=3.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:44 AM market time freshness=DELAYED_CURRENT RSI=52.05 liquidity=12330374.0 spike=1.76
- SKPC.CA: score=24.0 buy_ready=False sector_rank=14 price=16.43 support=15.58 resistance=16.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=64.08 liquidity=16304690.0 spike=0.5
- SMFR.CA: score=28.4 buy_ready=False sector_rank=8 price=236.09 support=187.01 resistance=247.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:44 AM market time freshness=DELAYED_CURRENT RSI=83.7 liquidity=120141152.0 spike=17.59
- SNFC.CA: score=16.75 buy_ready=False sector_rank=8 price=11.5 support=11.26 resistance=12.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=44.12 liquidity=7352084.5 spike=0.68
- SPIN.CA: score=16.14 buy_ready=False sector_rank=7 price=14.63 support=13.3 resistance=14.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=81.95 liquidity=2736007.25 spike=0.29
- SPMD.CA: score=26.4 buy_ready=True sector_rank=8 price=0.45 support=0.41 resistance=0.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:44 AM market time freshness=DELAYED_CURRENT RSI=61.11 liquidity=11125633.0 spike=0.64
- SUGR.CA: score=12.28 buy_ready=False sector_rank=18 price=46.96 support=45.31 resistance=48.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=43.62 liquidity=3549942.25 spike=0.73
- SVCE.CA: score=24.4 buy_ready=True sector_rank=8 price=9.43 support=8.76 resistance=10.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=55.48 liquidity=51120356.0 spike=0.73
- SWDY.CA: score=32.5 buy_ready=True sector_rank=2 price=89.91 support=84.3 resistance=90.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=52.01 liquidity=39103648.0 spike=3.05
- TALM.CA: score=20.1 buy_ready=False sector_rank=9 price=15.8 support=15.27 resistance=16.53 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=38.86 liquidity=15889596.0 spike=1.35
- TMGH.CA: score=26.4 buy_ready=True sector_rank=11 price=99.33 support=92.1 resistance=99.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=60.07 liquidity=205462896.0 spike=0.59
- TRTO.CA: score=10.4 buy_ready=False sector_rank=8 price=0.03 support=0.03 resistance=0.03 source=Yahoo Finance as_of=2026-07-13T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- UEFM.CA: score=17.84 buy_ready=True sector_rank=8 price=518.28 support=460.0 resistance=529.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:44 AM market time freshness=DELAYED_CURRENT RSI=59.37 liquidity=1441449.75 spike=0.85
- UEGC.CA: score=24.52 buy_ready=False sector_rank=8 price=2.1 support=1.33 resistance=2.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=92.13 liquidity=45070032.0 spike=1.56
- UNIP.CA: score=30.38 buy_ready=True sector_rank=8 price=0.35 support=0.29 resistance=0.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=61.36 liquidity=30388400.0 spike=1.99
- UNIT.CA: score=21.4 buy_ready=False sector_rank=11 price=19.61 support=12.0 resistance=21.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=77.63 liquidity=14267668.0 spike=0.57
- WCDF.CA: score=13.72 buy_ready=False sector_rank=8 price=525.67 support=504.0 resistance=544.99 source=Yahoo Finance as_of=2026-07-13T21:00:00+00:00 freshness=FRESH RSI=46.24 liquidity=323287.04 spike=0.91
- WKOL.CA: score=21.59 buy_ready=True sector_rank=8 price=317.12 support=273.1 resistance=334.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:44 AM market time freshness=DELAYED_CURRENT RSI=60.52 liquidity=5192886.5 spike=0.75
- ZEOT.CA: score=23.63 buy_ready=True sector_rank=8 price=11.58 support=9.47 resistance=12.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:44 AM market time freshness=DELAYED_CURRENT RSI=49.86 liquidity=9233408.0 spike=0.2
- ZMID.CA: score=24.4 buy_ready=True sector_rank=11 price=7.27 support=6.11 resistance=7.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=65.74 liquidity=138432432.0 spike=0.64

## Backtesting Lite
- SWDY.CA: 180d return=19.14%, max drawdown=-20.2%, MA20>MA50 days last20=15, as_of=2026-07-13T21:00:00+00:00
- OFH.CA: 180d return=-2.29%, max drawdown=-25.3%, MA20>MA50 days last20=1, as_of=2026-07-13T21:00:00+00:00
- UNIP.CA: 180d return=35.43%, max drawdown=-19.12%, MA20>MA50 days last20=20, as_of=2026-07-13T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- SWDY.CA: status=RECENT_ACCEPTED latest=2026-07-14 age_days=1 sources=3 expected=Elsewedy Electric summary=Elsewedy Electric has reported strong financial results for Q1 2026 and full year 2025, with significant revenues and profits. The company is actively involved in major projects in Saudi Arabia and has secured financing for European investments. Recent market announcements include project updates and EGM/AGM resolutions.
  - Elsewedy Electric's consolidated revenues total EGP 75.2bn in Q1-26 (Q1 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFndmQAaYd73P5fatUglB2xEwtjWkEjA4DhAhjLm6PangQOG-e4KgIJt0IW6us2mN9JOk7fNgJh72iIEyvKikV1nG7tGSL47U-iHfy6teJeLkEHWOrf1LFCbtYBNhM01VBXsa4kqVntnCUYjReat07w
  - Elsewedy Electric's consolidated profits exceed EGP 19.1bn in 2025 (FY 2025): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFndmQAaYd73P5fatUglB2xEwtjWkEjA4DhAhjLm6PangQOG-e4KgIJt0IW6us2mN9JOk7fNgJh72iIEyvKikV1nG7tGSL47U-iHfy6teJeLkEHWOrf1LFCbtYBNhM01VBXsa4kqVntnCUYjReat07w
  - Elsewedy Electric accelerates power transformation project in KSA with 6 high-voltage substations (July 14, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFndmQAaYd73P5fatUglB2xEwtjWkEjA4DhAhjLm6PangQOG-e4KgIJt0IW6us2mN9JOk7fNgJh72iIEyvKikV1nG7tGSL47U-iHfy6teJeLkEHWOrf1LFCbtYBNhM01VBXsa4kqVntnCUYjReat07w
- OFH.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=O B Financial Holding S.A.E summary=Evidence rejected for OFH.CA: source text did not clearly match OFH.CA / O B Financial Holding S.A.E.
- UNIP.CA: status=RECENT_ACCEPTED latest=2026-03-31 age_days=106 sources=3 expected=Universal For Paper and Packaging Materials summary=Universal For Paper and Packaging Materials has shown revenue growth in Q1 2026, despite a slight decrease in annual revenue for 2025. The company has also released various board and shareholder disclosures.
  - Universal For Paper and Packaging Materials had revenue of 376.11M EGP in the quarter ending March 31, 2026, with 3.52% growth (March 31, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE_DQzziujn22Kt-hdCNg667eh22zXcKp66l5MmWGswcu6T4pwMsslgd0mExg8-BCfKcfowQgD2Szzye4QxVWWE3s6kse4j6HVbfueLYDIizZXWoDEtvmA06jWsJ2-juYvKsUK5iKBE9i3Z6g==
  - Company's revenue in the last twelve months to 1.36B EGP, down -3.80% year-over-year (March 31, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE_DQzziujn22Kt-hdCNg667eh22zXcKp66l5MmWGswcu6T4pwMsslgd0mExg8-BCfKcfowQgD2Szzye4QxVWWE3s6kse4j6HVbfueLYDIizZXWoDEtvmA06jWsJ2-juYvKsUK5iKBE9i3Z6g==
  - In 2025, EGX:UNIP's revenue was 1.37 billion, a decrease of -3.00% compared to the previous year's 1.42 billion (FY 2025): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGOKIb14_Qp2CrVLmfvHfVhhbGcFDOYv-iBU33ymmtba_GtkU2llUZ2mMpyC3VeE4erXssD-O9AEikXyGrNGAmcFlj8XSJaKXiwzRjv_xe25CxTSF_LjzA2I9U4BY803DMBFRU=
- MEPA.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=560 sources=3 expected=Medical Packaging Company summary=Medical Packaging Company experienced a decrease in revenue and earnings in 2025. The company specializes in glass packaging for medical and cosmetic products.
  - In 2025, Medical Packaging Company's revenue was 119.77 million, a decrease of -8.52% compared to the previous year's 130.92 million. Earnings were 24.23 million, a decrease of -33.76% (FY 2025): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGGtITY9LI-pTQipeuVCDOHYS55lFVaY6hgEOeOgypnCKP3ROBM3sKXv_BffzXRosEHD-P9O6I-f3ie1J9J-Eri9zhuMjBUwPd8he4Lq-agd1OsYz59bn7TCzQGb5g5D3BMUp4=
  - Medical Packaging Company produces and sells glass containers for medical, pharmaceutical, laboratory, and cosmetic purposes in Egypt and internationally: https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG07j-_IoEMNm-tIgwznDPGhs6Rs_dEu5NEpWH6AOEC7GO9Lj9TU_nIxHbEHzWMMSPdUVIIMbQjcJou6T0orXLQzNLoDKPcJtXZY5RcWsnku7ZVSafO2UIOOcmG9Dr9NFSM4I958Vj7LoduqYV6oFTQDzcB-cXz
  - The company was founded in 2006 and is headquartered in 10th of Ramadan City, Egypt: https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG07j-_IoEMNm-tIgwznDPGhs6Rs_dEu5NEpWH6AOEC7GO9Lj9TU_nIxHbEHzWMMSPdUVIIMbQjcJou6T0orXLQzNLoDKPcJtXZY5RcWsnku7ZVSafO2UIOOcmG9Dr9NFSM4I958Vj7LoduqYV6oFTQDzcB-cXz
- AFMC.CA: status=RECENT_ACCEPTED latest=2026-06-29 age_days=16 sources=3 expected=Alexandria Flour Mills summary=Alexandria Flour Mills reported positive revenue and profits in the last 12 months, with a significant stock price increase. However, a new major risk regarding earnings quality was identified in May 2026. The company has also issued several official replies and board decisions.
  - In the last 12 months (as of June 29, 2026), EGX:AFMC had revenue of EGP 392.46 million and earned 53.96 million in profits: https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQENcvjWtOyhoaFialo-KmSXdtQwIkBlKhw5qGXAZvKM0agJTgr-hHgPbQcScptyUgSWcq-fknM5-rORnwvTExhbuttm7qwdIPg3-InDghQBc5zVo8rKlVF5zYRyOF26JqGGMzFMsBmu8-7Uip3nMQ==
  - The stock price has increased by +138.71% in the last 52 weeks (as of June 29, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQENcvjWtOyhoaFialo-KmSXdtQwIkBlKhw5qGXAZvKM0agJTgr-hHgPbQcScptyUgSWcq-fknM5-rORnwvTExhbuttm7qwdIPg3-InDghQBc5zVo8rKlVF5zYRyOF26JqGGMzFMsBmu8-7Uip3nMQ==
  - In the last 12 months, operating cash flow was 3.30 million EGP and capital expenditures -14.79 million EGP, giving a free cash flow of -11.50 million EGP (as of June 29, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQENcvjWtOyhoaFialo-KmSXdtQwIkBlKhw5qGXAZvKM0agJTgr-hHgPbQcScptyUgSWcq-fknM5-rORnwvTExhbuttm7qwdIPg3-InDghQBc5zVo8rKlVF5zYRyOF26JqGGMzFMsBmu8-7Uip3nMQ==
- NINH.CA: status=RECENT_ACCEPTED latest=2026-07-13 age_days=2 sources=3 expected=Nozha International Hospital summary=Nozha International Hospital reported a significant increase in net profit and revenue in Q1 2026. The company provides a wide range of healthcare services and has issued several market announcements regarding shareholder disclosures and meeting minutes.
  - Nozha International Hospital (NINH) has reported a 19.29% year-on-year (YoY) increase in net profit after tax during the first quarter (Q1) of 2026, registering EGP 47.001 million, compared to EGP 39.400 million (May 5, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFYaBC7T6OjIFAQdFQ3jCVZqldRINWne1bm4oYDuznUT1WUc07H6-awPFTVbQB5fpNdUVcBwI3FjUVLxn_1TaSlrcjuiDf-xWcT5PhhHZokmGg1epvtAnC6pSwxh_UgDCTgawiB_l-9bziM33JtfQ==
  - The company's revenue surged to EGP 135.458 million in the three months ended March 31st, 2026, compared to EGP 124.070 million during the first three months of 2025 (May 5, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFYaBC7T6OjIFAQdFQ3jCVZqldRINWne1bm4oYDuznUT1WUc07H6-awPFTVbQB5fpNdUVcBwI3FjUVLxn_1TaSlrcjuiDf-xWcT5PhhHZokmGg1epvtAnC6pSwxh_UgDCTgawiB_l-9bziM33JtfQ==
  - Nozha International Hospital's net profits cross EGP 174m in 2025 (July 13, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGo0No_wq1k6rJbrx_T0bXSvW05ZMWEkYDSC2wcxvB29WSSFSI2gHQUgUcCOmbknJ1wtcRFKhJI3Rk-MxkbodVjGRVh717Rr6G82HPpAtF31OtPk7ZBRkPBTLsi9VkAz911USNS34q1h4CEoWmwm0l8
- ELEC.CA: status=RECENT_ACCEPTED latest=2026-07-05 age_days=10 sources=3 expected=Electro Cable Egypt summary=Electro Cable Egypt reported consolidated losses in Q1 2026 and a significant decrease in consolidated profits in 2025. The company has also seen several block-trading deals and changes in shareholder stakes.
  - Alhsn for Consulting cuts stake in Electro Cable Egypt to 19.8% (July 5, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF25d7bw4YHKOOAK-rFYv7_aCR6Ivk7RQq-bjjs2Rzyu_MXlm9joBshGyY6J7hmRoa2DfDNqPumNuEKbN71FW9E12lqvCRhhshRqEbTBOycziG06kRepkAZk5X59W6gpiDKoboB7B1UZ-U2IrEI0wqi6A==
  - Electro Cable incurs consolidated losses in Q1 2026 (June 30, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF25d7bw4YHKOOAK-rFYv7_aCR6Ivk7RQq-bjjs2Rzyu_MXlm9joBshGyY6J7hmRoa2DfDNqPumNuEKbN71FW9E12lqvCRhhshRqEbTBOycziG06kRepkAZk5X59W6gpiDKoboB7B1UZ-U2IrEI0wqi6A==
  - Electro Cable Egypt sees EGP 87.3M block-trading deal on April 16th, 2026: https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF25d7bw4YHKOOAK-rFYv7_aCR6Ivk7RQq-bjjs2Rzyu_MXlm9joBshGyY6J7hmRoa2DfDNqPumNuEKbN71FW9E12lqvCRhhshRqEbTBOycziG06kRepkAZk5X59W6gpiDKoboB7B1UZ-U2IrEI0wqi6A==
- CIRA.CA: status=RECENT_ACCEPTED latest=2026-07-07 age_days=8 sources=3 expected=Cairo Investment and Real Estate Development summary=Cairo Investment and Real Estate Development has demonstrated strong financial performance in the last 12 months, with significant revenue and profit growth, and a substantial increase in stock price. The company is involved in various sectors including education, real estate, and healthcare.
  - In the last 12 months (as of July 7, 2026), EGX:CIRA had revenue of EGP 5.19 billion and earned 594.75 million in profits. Earnings per share was 1.02: https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG3umgEXjEjD7LPO_b9bfsKBbq-O8v5Q0a-IRDIXcNUJiACgZG7_-bkC3T1YcpFQ8P0ipgBEQSkjMuIosp8bTmzApUc5t9J_p40XTsCUq_hpEZWdUOp37x0dg73XXjRiirBkR6_loVEzZiHXk6gCw==
  - The stock price has increased by +109.38% in the last 52 weeks (as of July 7, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG3umgEXjEjD7LPO_b9bfsKBbq-O8v5Q0a-IRDIXcNUJiACgZG7_-bkC3T1YcpFQ8P0ipgBEQSkjMuIosp8bTmzApUc5t9J_p40XTsCUq_hpEZWdUOp37x0dg73XXjRiirBkR6_loVEzZiHXk6gCw==
  - In the last 12 months, operating cash flow was 1.91 billion EGP and capital expenditures -500.33 million EGP, giving a free cash flow of 1.41 billion EGP (as of July 7, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG3umgEXjEjD7LPO_b9bfsKBbq-O8v5Q0a-IRDIXcNUJiACgZG7_-bkC3T1YcpFQ8P0ipgBEQSkjMuIosp8bTmzApUc5t9J_p40XTsCUq_hpEZWdUOp37x0dg73XXjRiirBkR6_loVEzZiHXk6gCw==

## Warnings
- Evidence rejected for OFH.CA: source text did not clearly match OFH.CA / O B Financial Holding S.A.E.
- Evidence for MEPA.CA matches the company but appears old; latest detected date is 2025-01-01.
