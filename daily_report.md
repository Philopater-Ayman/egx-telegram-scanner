# Telegram-First EGX Scanner Report

Scan phase: Pre-market risk check
Generated UTC: 2026-08-16T06:03:13.525304+00:00
Generated Cairo: 2026-08-16 09:03
Run timing: target 08:45 Cairo | generated Cairo 2026-08-16 09:03 | cron 45 5 * * 0-4
Trigger: scheduled cron=45 5 * * 0-4 mapped to pre_market; Cairo now 2026-08-16 08:58

## Control Center
- Action tickets: 3 prioritized signal(s)
- BUY-ready candidates: 62
- Data quality issues: 1
- Tradeable price/liquidity tickers: 187/189
- Top sector: Building Materials

## Market Context
- Market trend: Bullish
- Source: Mubasher EGX market page (delayed public data)
- As of: Thursday, August 13
- Freshness: DELAYED
- EGX30 regime: BULLISH / above MA20 70.0% / above MA50 75.0%
- EGX70 regime: BULLISH / above MA20 80.0% / above MA50 92.5%
- Sector breadth: 76.19%
- Risk mode: BROAD_RISK_ON

## Top Liquidity
- NIPH.CA: liquidity=757302592.0 spike=2.53 score=26.96
- OLFI.CA: liquidity=512471616.0 spike=7.9 score=32.9
- PHAR.CA: liquidity=447594752.0 spike=1.17 score=27.24
- ETEL.CA: liquidity=418255008.0 spike=3.38 score=34.66
- CCAP.CA: liquidity=345650112.0 spike=0.59 score=23.9

## AI Narrative
- Provider: OpenRouter OK
- Model: nvidia/nemotron-3-super-120b-a12b:free
- Summary: Scanner flagged COPR.CA, ETEL.CA and OLFI.CA as BUY setups under a broad risk‑on EGX regime, citing price above short‑term averages, adequate liquidity and defined support/resistance, while noting low confidence due to non‑leading sectors and extended momentum.
- COPR.CA: price 0.43 above MA20/MA50, RSI 55, support 0.37/resistance 0.45, liquidity spike 3.4×, sector not leading.
- ETEL.CA: price 113.97 above averages, RSI 64, support 97.5/resistance 116.3, liquidity spike 3.4×, momentum extended.
- OLFI.CA: price 25.06 above averages, RSI 63, support 22.3/resistance 26.5, liquidity spike 7.9×, momentum extended.
- EGX30/EGX70 both bullish with >70% above MA20, sector breadth 76%, risk mode BROAD_RISK_ON supports buys but adds uncertainty.

## Top Liquidity Spikes
- OLFI.CA: spike=7.9 liquidity=512471616.0 outlook=BULLISH_WATCH score=82.22 buy_ready=True
- NAHO.CA: spike=6.75 liquidity=196978.47 outlook=NEUTRAL score=36.52 buy_ready=False
- ICID.CA: spike=6.51 liquidity=94047928.0 outlook=CONSTRUCTIVE score=66.52 buy_ready=False
- COSG.CA: spike=6.26 liquidity=300308352.0 outlook=BULLISH_WATCH score=84.52 buy_ready=True
- TRTO.CA: spike=6.21 liquidity=14002.33 outlook=CONSTRUCTIVE score=53.52 buy_ready=False

## Sector Leaderboard
- #1 Building Materials: score=24.39 5d=22.62% 20d=38.78% aboveMA50=100.0%
- #2 Transportation & Logistics: score=14.97 5d=8.95% 20d=17.96% aboveMA50=100.0%
- #3 Healthcare: score=12.98 5d=1.24% 20d=25.09% aboveMA50=100.0%
- #4 Agriculture & Food Production: score=12.49 5d=6.85% 20d=13.02% aboveMA50=100.0%
- #5 Textiles: score=12.1 5d=4.6% 20d=14.03% aboveMA50=100.0%
- #6 Tourism & Leisure: score=11.8 5d=11.05% 20d=13.96% aboveMA50=0.0%
- #7 Education: score=11.77 5d=4.4% 20d=16.66% aboveMA50=100.0%
- #8 Basic Resources & Chemicals: score=10.61 5d=4.33% 20d=8.3% aboveMA50=90.0%

## Today's Prioritized Action Tickets
- Priority #1: BUY COPR.CA
  - Entry: 0.43 | Take profit: 0.47 | Stop loss: 0.41
  - Confidence: LOW | score=34.72 | outlook=BULLISH_WATCH 92.52
  - Reason: BUY SETUP: COPR.CA has aligned current price data, liquidity above threshold, price above MA20/MA50, RSI 55.17, support 0.37, resistance 0.45, and evidence sources. Macro trend is Bullish; market regime is BROAD_RISK_ON; verify price action in Thndr before treating it as a swing entry.
- Priority #2: BUY ETEL.CA
  - Entry: 113.97 | Take profit: 123.09 | Stop loss: 109.41
  - Confidence: LOW | score=34.66 | outlook=BULLISH_WATCH 83.68
  - Reason: BUY SETUP: ETEL.CA has aligned current price data, liquidity above threshold, price above MA20/MA50, RSI 64.46, support 97.54, resistance 116.25, and evidence sources. Macro trend is Bullish; market regime is BROAD_RISK_ON; verify price action in Thndr before treating it as a swing entry.
- Priority #3: BUY OLFI.CA
  - Entry: 25.06 | Take profit: 27.06 | Stop loss: 24.06
  - Confidence: LOW | score=32.9 | outlook=BULLISH_WATCH 82.22
  - Reason: BUY SETUP: OLFI.CA has aligned current price data, liquidity above threshold, price above MA20/MA50, RSI 62.63, support 22.25, resistance 26.52, and evidence sources. Macro trend is Bullish; market regime is BROAD_RISK_ON; verify price action in Thndr before treating it as a swing entry.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- CLHO.CA: BULLISH_WATCH score=100 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=No major short-term scanner risk flags.
- MPRC.CA: BULLISH_WATCH score=96.52 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- COPR.CA: BULLISH_WATCH score=92.52 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- RACC.CA: BULLISH_WATCH score=90.52 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended; sector is not leading
- EFIH.CA: BULLISH_WATCH score=89.96 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- MBSC.CA: BULLISH_WATCH score=89 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=overheated RSI; far above support
- SUGR.CA: BULLISH_WATCH score=88.22 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended; sector is not leading
- MIPH.CA: BULLISH_WATCH score=88 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; momentum is extended
- GGCC.CA: BULLISH_WATCH score=86.52 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=far above support; sector is not leading
- SCTS.CA: BULLISH_WATCH score=86 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling

## BUY-Ready Candidates
- COSG.CA: rank=34.9 outlook=BULLISH_WATCH outlook_score=84.52 sector_rank=11 price=1.84 support=1.6 resistance=1.93 liquidity=300308352.0
- COPR.CA: rank=34.72 outlook=BULLISH_WATCH outlook_score=92.52 sector_rank=11 price=0.43 support=0.37 resistance=0.45 liquidity=125282336.0
- ETEL.CA: rank=34.66 outlook=BULLISH_WATCH outlook_score=83.68 sector_rank=15 price=113.97 support=97.54 resistance=116.25 liquidity=418255008.0
- OLFI.CA: rank=32.9 outlook=BULLISH_WATCH outlook_score=82.22 sector_rank=12 price=25.06 support=22.25 resistance=26.52 liquidity=512471616.0
- SCEM.CA: rank=31.82 outlook=BULLISH_WATCH outlook_score=83 sector_rank=1 price=94.19 support=62.1 resistance=113.0 liquidity=262855520.0
- EEII.CA: rank=31.68 outlook=BULLISH_WATCH outlook_score=82.52 sector_rank=11 price=3.04 support=2.54 resistance=3.23 liquidity=57693856.0
- SAUD.CA: rank=30.88 outlook=BULLISH_WATCH outlook_score=73.85 sector_rank=9 price=23.51 support=21.3 resistance=23.62 liquidity=25219244.0
- RACC.CA: rank=30.46 outlook=BULLISH_WATCH outlook_score=90.52 sector_rank=11 price=10.39 support=9.8 resistance=10.6 liquidity=42794956.0
- GGCC.CA: rank=29.6 outlook=BULLISH_WATCH outlook_score=86.52 sector_rank=11 price=1.02 support=0.67 resistance=1.28 liquidity=91736384.0
- CIEB.CA: rank=29.08 outlook=BULLISH_WATCH outlook_score=85.85 sector_rank=9 price=24.46 support=23.75 resistance=24.7 liquidity=18793398.0

## Data Quality Issues
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=26.72 buy_ready=True sector_rank=11 price=299.87 support=227.0 resistance=325.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=68.47 liquidity=58903024.0 spike=1.41
- ABUK.CA: score=25.86 buy_ready=False sector_rank=8 price=77.89 support=70.6 resistance=78.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=78.91 liquidity=226852448.0 spike=1.48
- ACAMD.CA: score=20.9 buy_ready=False sector_rank=11 price=2.24 support=2.2 resistance=2.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=40.53 liquidity=30146108.0 spike=0.5
- ACGC.CA: score=24.9 buy_ready=False sector_rank=5 price=12.18 support=9.75 resistance=12.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=80.79 liquidity=33407628.0 spike=0.99
- ADCI.CA: score=25.9 buy_ready=True sector_rank=11 price=309.84 support=235.45 resistance=389.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=66.43 liquidity=14863111.0 spike=0.66
- ADIB.CA: score=24.9 buy_ready=False sector_rank=9 price=54.92 support=46.02 resistance=55.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=83.43 liquidity=99944696.0 spike=0.86
- ADPC.CA: score=26.2 buy_ready=True sector_rank=11 price=4.4 support=3.76 resistance=4.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=66.15 liquidity=58108556.0 spike=1.15
- AFDI.CA: score=22.9 buy_ready=False sector_rank=11 price=66.45 support=46.57 resistance=69.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=83.6 liquidity=15525131.0 spike=0.64
- AFMC.CA: score=22.9 buy_ready=False sector_rank=11 price=230.23 support=75.3 resistance=300.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=75.09 liquidity=70867960.0 spike=0.44
- AJWA.CA: score=27.9 buy_ready=False sector_rank=11 price=197.81 support=161.0 resistance=210.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=70.98 liquidity=38482224.0 spike=0.98
- ALCN.CA: score=26.9 buy_ready=False sector_rank=2 price=31.94 support=28.8 resistance=32.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=76.0 liquidity=18404880.0 spike=0.75
- ALUM.CA: score=23.74 buy_ready=False sector_rank=11 price=28.28 support=22.72 resistance=30.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=80.68 liquidity=26835288.0 spike=1.42
- AMER.CA: score=23.3 buy_ready=False sector_rank=16 price=6.55 support=3.58 resistance=8.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=75.81 liquidity=142406720.0 spike=1.2
- AMES.CA: score=25.9 buy_ready=True sector_rank=11 price=120.78 support=106.59 resistance=144.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:26 PM market time freshness=DELAYED_CURRENT RSI=54.58 liquidity=15851239.0 spike=0.22
- AMIA.CA: score=24.9 buy_ready=False sector_rank=11 price=12.99 support=9.04 resistance=13.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=85.42 liquidity=11292900.0 spike=0.64
- AMOC.CA: score=27.36 buy_ready=False sector_rank=10 price=10.24 support=8.16 resistance=10.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=78.87 liquidity=245900928.0 spike=2.23
- APSW.CA: score=13.75 buy_ready=False sector_rank=11 price=8.7 support=8.32 resistance=9.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:14 PM market time freshness=DELAYED_CURRENT RSI=48.85 liquidity=847075.44 spike=0.47
- ARAB.CA: score=23.9 buy_ready=False sector_rank=16 price=0.24 support=0.23 resistance=0.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=47.5 liquidity=62111572.0 spike=0.61
- ARCC.CA: score=27.86 buy_ready=False sector_rank=1 price=74.5 support=54.3 resistance=91.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=83.42 liquidity=183554576.0 spike=1.98
- AREH.CA: score=20.9 buy_ready=False sector_rank=11 price=1.51 support=1.38 resistance=1.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=52.27 liquidity=11057310.0 spike=0.28
- ARVA.CA: score=6.9 buy_ready=False sector_rank=11 price=12.35 support=10.68 resistance=12.6 source=Yahoo Finance as_of=2026-08-12T21:00:00+00:00 freshness=FRESH RSI=0.0 liquidity=0.0 spike=0.0
- ASCM.CA: score=23.9 buy_ready=True sector_rank=11 price=65.28 support=60.1 resistance=69.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=67.34 liquidity=49588144.0 spike=0.82
- ASPI.CA: score=25.9 buy_ready=False sector_rank=11 price=0.49 support=0.32 resistance=0.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=72.12 liquidity=12482226.0 spike=0.28
- ATLC.CA: score=25.26 buy_ready=True sector_rank=19 price=5.57 support=5.0 resistance=5.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=65.19 liquidity=10312066.0 spike=0.56
- ATQA.CA: score=25.9 buy_ready=False sector_rank=8 price=10.87 support=9.49 resistance=11.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=73.3 liquidity=54370216.0 spike=0.94
- AXPH.CA: score=20.86 buy_ready=True sector_rank=11 price=1305.43 support=1121.56 resistance=1460.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:14 PM market time freshness=DELAYED_CURRENT RSI=63.19 liquidity=2964432.0 spike=0.67
- BINV.CA: score=20.43 buy_ready=False sector_rank=18 price=49.24 support=46.01 resistance=50.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=73.07 liquidity=6531913.0 spike=0.91
- BIOC.CA: score=24.9 buy_ready=False sector_rank=11 price=521.88 support=97.25 resistance=563.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=84.67 liquidity=112206280.0 spike=0.52
- BTFH.CA: score=22.26 buy_ready=False sector_rank=19 price=3.08 support=3.05 resistance=3.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=51.22 liquidity=77343256.0 spike=0.34
- CAED.CA: score=25.9 buy_ready=True sector_rank=11 price=126.66 support=96.96 resistance=143.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=57.49 liquidity=29806002.0 spike=0.4
- CANA.CA: score=28.06 buy_ready=False sector_rank=9 price=42.77 support=35.2 resistance=43.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=79.9 liquidity=57989688.0 spike=2.58
- CCAP.CA: score=23.9 buy_ready=False sector_rank=18 price=5.3 support=5.14 resistance=5.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=38.68 liquidity=345650112.0 spike=0.59
- CCRS.CA: score=13.99 buy_ready=False sector_rank=11 price=2.44 support=2.44 resistance=2.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=26.09 liquidity=8086997.0 spike=0.45
- CEFM.CA: score=20.38 buy_ready=True sector_rank=11 price=133.1 support=107.25 resistance=152.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=63.74 liquidity=4475823.5 spike=0.13
- CERA.CA: score=24.2 buy_ready=False sector_rank=11 price=1.33 support=1.25 resistance=1.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:26 PM market time freshness=DELAYED_CURRENT RSI=45.0 liquidity=23763370.0 spike=1.15
- CFGH.CA: score=9.9 buy_ready=False sector_rank=11 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance as_of=2026-08-12T21:00:00+00:00 freshness=FRESH RSI=53.33 liquidity=809.79 spike=0.06
- CICH.CA: score=18.04 buy_ready=True sector_rank=19 price=12.62 support=11.8 resistance=13.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=61.68 liquidity=2782891.75 spike=0.36
- CIEB.CA: score=29.08 buy_ready=True sector_rank=9 price=24.46 support=23.75 resistance=24.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=56.5 liquidity=18793398.0 spike=1.59
- CIRA.CA: score=25.9 buy_ready=False sector_rank=7 price=38.23 support=30.91 resistance=40.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=73.97 liquidity=54578684.0 spike=0.91
- CLHO.CA: score=28.32 buy_ready=True sector_rank=3 price=17.25 support=16.0 resistance=19.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=55.53 liquidity=95175176.0 spike=1.71
- CNFN.CA: score=25.34 buy_ready=True sector_rank=19 price=4.92 support=4.68 resistance=5.03 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:26 PM market time freshness=DELAYED_CURRENT RSI=53.57 liquidity=21593270.0 spike=1.04
- COMI.CA: score=23.9 buy_ready=False sector_rank=9 price=139.07 support=132.81 resistance=142.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=52.62 liquidity=147265456.0 spike=0.33
- COPR.CA: score=34.72 buy_ready=True sector_rank=11 price=0.43 support=0.37 resistance=0.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=55.17 liquidity=125282336.0 spike=3.41
- COSG.CA: score=34.9 buy_ready=True sector_rank=11 price=1.84 support=1.6 resistance=1.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=64.29 liquidity=300308352.0 spike=6.26
- CPCI.CA: score=24.95 buy_ready=False sector_rank=11 price=534.19 support=440.01 resistance=644.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=71.17 liquidity=9054346.0 spike=0.69
- CSAG.CA: score=26.2 buy_ready=False sector_rank=2 price=42.16 support=31.35 resistance=43.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=83.67 liquidity=41743636.0 spike=1.65
- DAPH.CA: score=22.9 buy_ready=False sector_rank=11 price=124.45 support=84.31 resistance=147.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=80.08 liquidity=26883474.0 spike=0.68
- DEIN.CA: score=0.9 buy_ready=False sector_rank=11 price=11.38 support=13.65 resistance=13.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 June 12:11 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=40.95 spike=0.01
- DOMT.CA: score=28.52 buy_ready=True sector_rank=12 price=29.27 support=26.01 resistance=32.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=65.52 liquidity=33099780.0 spike=2.31
- DSCW.CA: score=25.9 buy_ready=True sector_rank=11 price=2.13 support=1.86 resistance=2.21 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=68.29 liquidity=48357664.0 spike=0.51
- DTPP.CA: score=25.9 buy_ready=True sector_rank=11 price=299.93 support=205.01 resistance=340.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=69.83 liquidity=54909260.0 spike=0.86
- EALR.CA: score=28.04 buy_ready=True sector_rank=11 price=388.03 support=360.0 resistance=432.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=60.24 liquidity=35864088.0 spike=1.07
- EASB.CA: score=18.33 buy_ready=False sector_rank=11 price=7.22 support=6.71 resistance=8.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:14 PM market time freshness=DELAYED_CURRENT RSI=20.37 liquidity=9432538.0 spike=0.94
- EAST.CA: score=21.9 buy_ready=False sector_rank=12 price=36.25 support=36.01 resistance=37.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:26 PM market time freshness=DELAYED_CURRENT RSI=41.3 liquidity=35195116.0 spike=0.53
- EBSC.CA: score=15.78 buy_ready=False sector_rank=11 price=1.91 support=1.85 resistance=2.06 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=56.25 liquidity=1879553.25 spike=0.33
- ECAP.CA: score=26.04 buy_ready=True sector_rank=11 price=38.56 support=32.12 resistance=43.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=69.38 liquidity=12396530.0 spike=1.07
- EDFM.CA: score=16.42 buy_ready=False sector_rank=11 price=410.59 support=352.0 resistance=430.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:12 PM market time freshness=DELAYED_CURRENT RSI=69.25 liquidity=515917.31 spike=0.09
- EEII.CA: score=31.68 buy_ready=True sector_rank=11 price=3.04 support=2.54 resistance=3.23 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=64.04 liquidity=57693856.0 spike=2.89
- EFIC.CA: score=29.9 buy_ready=False sector_rank=8 price=226.08 support=184.0 resistance=239.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=76.15 liquidity=173384432.0 spike=4.77
- EFID.CA: score=24.9 buy_ready=False sector_rank=12 price=32.79 support=26.64 resistance=32.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=84.63 liquidity=73187616.0 spike=0.83
- EFIH.CA: score=28.98 buy_ready=True sector_rank=14 price=24.03 support=21.9 resistance=25.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=57.46 liquidity=164269328.0 spike=1.54
- EGAL.CA: score=23.4 buy_ready=False sector_rank=8 price=334.48 support=292.0 resistance=358.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=77.82 liquidity=119253920.0 spike=1.25
- EGAS.CA: score=25.9 buy_ready=False sector_rank=10 price=59.07 support=50.0 resistance=67.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=71.1 liquidity=18549878.0 spike=0.72
- EGBE.CA: score=14.01 buy_ready=False sector_rank=9 price=0.55 support=0.44 resistance=0.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=66.47 liquidity=113763.77 spike=0.7
- EGCH.CA: score=25.84 buy_ready=False sector_rank=8 price=14.35 support=12.69 resistance=14.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=77.14 liquidity=172124576.0 spike=1.47
- EGSA.CA: score=5.91 buy_ready=False sector_rank=15 price=8.66 support=8.65 resistance=9.21 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 12:55 PM market time freshness=DELAYED_CURRENT RSI=18.37 liquidity=7748.59 spike=0.38
- EGTS.CA: score=25.9 buy_ready=True sector_rank=16 price=18.78 support=17.11 resistance=20.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=66.38 liquidity=30987374.0 spike=0.77
- EHDR.CA: score=27.9 buy_ready=True sector_rank=11 price=2.97 support=2.69 resistance=3.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=53.09 liquidity=32200592.0 spike=0.68
- EKHO.CA: score=9.9 buy_ready=False sector_rank=10 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-08-12T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=22.9 buy_ready=False sector_rank=17 price=2.16 support=2.12 resistance=2.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=37.5 liquidity=43559424.0 spike=0.57
- ELKA.CA: score=18.9 buy_ready=False sector_rank=11 price=1.77 support=1.69 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=26.79 liquidity=42674268.0 spike=0.51
- ELNA.CA: score=12.15 buy_ready=False sector_rank=11 price=37.88 support=36.5 resistance=39.49 source=Yahoo Finance as_of=2026-08-12T21:00:00+00:00 freshness=FRESH RSI=36.33 liquidity=253796.01 spike=0.53
- ELSH.CA: score=18.9 buy_ready=False sector_rank=11 price=13.93 support=13.31 resistance=15.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=33.78 liquidity=41652308.0 spike=0.47
- ELWA.CA: score=8.47 buy_ready=False sector_rank=11 price=1.75 support=1.65 resistance=2.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=28.95 liquidity=571912.06 spike=0.37
- EMFD.CA: score=24.9 buy_ready=False sector_rank=16 price=11.75 support=11.08 resistance=12.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=52.69 liquidity=46635240.0 spike=0.81
- ENGC.CA: score=24.9 buy_ready=False sector_rank=11 price=49.68 support=40.11 resistance=51.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=75.88 liquidity=11777169.0 spike=0.46
- EOSB.CA: score=19.93 buy_ready=False sector_rank=11 price=1.55 support=1.52 resistance=1.62 source=Yahoo Finance as_of=2026-08-12T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=30970.55 spike=0.63
- EPCO.CA: score=28.18 buy_ready=True sector_rank=11 price=11.88 support=10.32 resistance=13.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=56.69 liquidity=38690320.0 spike=1.14
- EPPK.CA: score=6.21 buy_ready=False sector_rank=11 price=13.18 support=12.62 resistance=15.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:08 PM market time freshness=DELAYED_CURRENT RSI=11.85 liquidity=306200.94 spike=0.34
- ETEL.CA: score=34.66 buy_ready=True sector_rank=15 price=113.97 support=97.54 resistance=116.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=64.46 liquidity=418255008.0 spike=3.38
- ETRS.CA: score=27.3 buy_ready=False sector_rank=11 price=10.91 support=10.21 resistance=10.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=72.75 liquidity=41405436.0 spike=1.7
- EXPA.CA: score=25.46 buy_ready=False sector_rank=9 price=21.29 support=19.25 resistance=21.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=76.36 liquidity=47902996.0 spike=1.28
- FAIT.CA: score=29.06 buy_ready=False sector_rank=9 price=40.81 support=36.1 resistance=40.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=82.34 liquidity=11406148.0 spike=3.08
- FAITA.CA: score=12.93 buy_ready=False sector_rank=9 price=0.98 support=0.96 resistance=0.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:06 PM market time freshness=DELAYED_CURRENT RSI=61.73 liquidity=30972.97 spike=0.68
- FERC.CA: score=25.9 buy_ready=False sector_rank=8 price=81.9 support=75.01 resistance=87.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:26 PM market time freshness=DELAYED_CURRENT RSI=72.32 liquidity=13301047.0 spike=0.75
- FWRY.CA: score=23.9 buy_ready=False sector_rank=14 price=19.02 support=18.65 resistance=19.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=51.74 liquidity=125534736.0 spike=0.98
- GBCO.CA: score=27.9 buy_ready=True sector_rank=13 price=31.53 support=29.53 resistance=33.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=53.93 liquidity=23459548.0 spike=0.38
- GDWA.CA: score=14.9 buy_ready=False sector_rank=11 price=0.81 support=0.8 resistance=0.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=20.62 liquidity=31186406.0 spike=0.27
- GGCC.CA: score=29.6 buy_ready=True sector_rank=11 price=1.02 support=0.67 resistance=1.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=58.32 liquidity=91736384.0 spike=1.85
- GIHD.CA: score=25.9 buy_ready=True sector_rank=11 price=66.97 support=49.32 resistance=76.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=67.23 liquidity=18399120.0 spike=0.39
- GMCI.CA: score=11.57 buy_ready=False sector_rank=11 price=1.9 support=1.88 resistance=2.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=39.13 liquidity=673759.88 spike=0.92
- GRCA.CA: score=17.15 buy_ready=False sector_rank=11 price=55.46 support=52.26 resistance=68.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=36.93 liquidity=6252848.5 spike=0.34
- GSSC.CA: score=19.25 buy_ready=True sector_rank=11 price=280.66 support=263.6 resistance=300.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=65.23 liquidity=5345865.5 spike=0.3
- GTWL.CA: score=27.82 buy_ready=False sector_rank=11 price=134.0 support=85.0 resistance=139.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=77.71 liquidity=228619088.0 spike=2.46
- HDBK.CA: score=20.9 buy_ready=False sector_rank=9 price=87.11 support=77.03 resistance=87.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=84.98 liquidity=38223096.0 spike=1.0
- HELI.CA: score=24.9 buy_ready=False sector_rank=16 price=7.82 support=7.71 resistance=8.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=36.53 liquidity=262553008.0 spike=1.5
- HRHO.CA: score=21.76 buy_ready=False sector_rank=19 price=26.66 support=25.95 resistance=28.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=48.5 liquidity=122057880.0 spike=1.25
- ICID.CA: score=29.9 buy_ready=False sector_rank=11 price=13.35 support=7.83 resistance=13.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=93.87 liquidity=94047928.0 spike=6.51
- IDRE.CA: score=25.9 buy_ready=True sector_rank=11 price=55.0 support=44.52 resistance=58.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=67.41 liquidity=15236519.0 spike=0.53
- IFAP.CA: score=22.9 buy_ready=False sector_rank=4 price=21.88 support=18.96 resistance=22.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=76.55 liquidity=17314540.0 spike=0.75
- INFI.CA: score=23.5 buy_ready=False sector_rank=11 price=152.26 support=101.0 resistance=178.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=77.19 liquidity=68313848.0 spike=1.3
- IRON.CA: score=19.99 buy_ready=False sector_rank=8 price=31.02 support=30.14 resistance=34.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=49.69 liquidity=9913762.0 spike=1.09
- ISMA.CA: score=24.88 buy_ready=False sector_rank=11 price=34.88 support=27.1 resistance=36.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=77.86 liquidity=9982380.0 spike=0.35
- ISMQ.CA: score=27.9 buy_ready=True sector_rank=8 price=9.47 support=8.96 resistance=9.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=53.85 liquidity=38398064.0 spike=0.57
- ISPH.CA: score=26.9 buy_ready=True sector_rank=3 price=13.58 support=11.3 resistance=16.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=67.78 liquidity=115268864.0 spike=0.63
- JUFO.CA: score=25.28 buy_ready=False sector_rank=12 price=27.26 support=22.78 resistance=30.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=40.64 liquidity=69945200.0 spike=1.19
- KABO.CA: score=25.9 buy_ready=True sector_rank=5 price=8.77 support=7.56 resistance=8.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=54.34 liquidity=36496760.0 spike=0.98
- KWIN.CA: score=18.15 buy_ready=False sector_rank=11 price=86.8 support=73.0 resistance=111.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=28.43 liquidity=9253221.0 spike=0.15
- KZPC.CA: score=29.9 buy_ready=False sector_rank=11 price=10.37 support=8.42 resistance=10.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=87.35 liquidity=62765316.0 spike=5.64
- LCSW.CA: score=26.9 buy_ready=False sector_rank=1 price=32.69 support=30.2 resistance=37.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=41.64 liquidity=42629528.0 spike=0.91
- LUTS.CA: score=23.02 buy_ready=False sector_rank=11 price=0.98 support=0.54 resistance=1.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=83.89 liquidity=66734112.0 spike=1.06
- MAAL.CA: score=20.32 buy_ready=False sector_rank=11 price=8.75 support=8.22 resistance=9.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=47.78 liquidity=6415584.5 spike=0.43
- MASR.CA: score=19.2 buy_ready=False sector_rank=11 price=7.64 support=7.45 resistance=8.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=29.49 liquidity=87770400.0 spike=1.15
- MBSC.CA: score=32.9 buy_ready=False sector_rank=1 price=380.55 support=231.51 resistance=399.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=96.78 liquidity=245895904.0 spike=3.7
- MCQE.CA: score=30.14 buy_ready=False sector_rank=1 price=252.39 support=175.55 resistance=292.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=80.96 liquidity=135090816.0 spike=3.12
- MCRO.CA: score=25.9 buy_ready=True sector_rank=11 price=1.55 support=1.32 resistance=1.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=53.33 liquidity=71294368.0 spike=0.39
- MENA.CA: score=26.1 buy_ready=True sector_rank=16 price=7.24 support=6.83 resistance=7.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=61.02 liquidity=7675954.5 spike=1.26
- MEPA.CA: score=23.9 buy_ready=False sector_rank=11 price=1.87 support=1.68 resistance=2.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=47.73 liquidity=14483275.0 spike=0.23
- MFPC.CA: score=27.74 buy_ready=False sector_rank=8 price=39.93 support=35.37 resistance=40.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=77.82 liquidity=213179072.0 spike=2.42
- MFSC.CA: score=20.33 buy_ready=True sector_rank=11 price=49.4 support=45.95 resistance=65.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=56.01 liquidity=4432114.0 spike=0.36
- MHOT.CA: score=24.02 buy_ready=False sector_rank=6 price=18.69 support=16.2 resistance=21.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=63.66 liquidity=17830824.0 spike=1.06
- MICH.CA: score=25.9 buy_ready=True sector_rank=11 price=47.6 support=37.6 resistance=53.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=67.37 liquidity=15479279.0 spike=0.45
- MILS.CA: score=25.9 buy_ready=True sector_rank=11 price=190.25 support=137.23 resistance=211.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:26 PM market time freshness=DELAYED_CURRENT RSI=60.57 liquidity=12944334.0 spike=0.19
- MIPH.CA: score=18.65 buy_ready=True sector_rank=3 price=773.73 support=722.7 resistance=828.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=62.17 liquidity=1753046.0 spike=0.35
- MOED.CA: score=14.9 buy_ready=False sector_rank=11 price=0.69 support=0.65 resistance=0.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=32.0 liquidity=25052076.0 spike=0.76
- MOIL.CA: score=14.14 buy_ready=False sector_rank=10 price=0.67 support=0.54 resistance=0.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=74.14 liquidity=239014.41 spike=0.38
- MOIN.CA: score=22.9 buy_ready=False sector_rank=11 price=34.0 support=23.03 resistance=40.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=78.54 liquidity=13946595.0 spike=0.54
- MOSC.CA: score=29.9 buy_ready=False sector_rank=11 price=321.69 support=280.4 resistance=370.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=87.05 liquidity=61258456.0 spike=4.02
- MPCI.CA: score=26.98 buy_ready=False sector_rank=11 price=380.88 support=242.02 resistance=460.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=73.12 liquidity=239588480.0 spike=1.54
- MPCO.CA: score=25.9 buy_ready=False sector_rank=4 price=2.16 support=1.82 resistance=2.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=74.58 liquidity=80495912.0 spike=0.78
- MPRC.CA: score=27.02 buy_ready=True sector_rank=11 price=46.16 support=42.6 resistance=52.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=56.52 liquidity=42393828.0 spike=1.56
- MTIE.CA: score=28.12 buy_ready=True sector_rank=13 price=9.63 support=8.68 resistance=10.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=52.29 liquidity=52652228.0 spike=1.11
- NAHO.CA: score=19.1 buy_ready=False sector_rank=11 price=0.11 support=0.1 resistance=0.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=84.62 liquidity=196978.47 spike=6.75
- NCCW.CA: score=20.9 buy_ready=False sector_rank=11 price=5.98 support=5.67 resistance=7.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=43.37 liquidity=17247774.0 spike=0.51
- NEDA.CA: score=11.24 buy_ready=False sector_rank=11 price=2.71 support=2.7 resistance=3.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:10 PM market time freshness=DELAYED_CURRENT RSI=35.29 liquidity=341660.69 spike=0.44
- NHPS.CA: score=25.9 buy_ready=True sector_rank=11 price=88.92 support=82.25 resistance=98.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=41070236.0 spike=0.65
- NINH.CA: score=23.9 buy_ready=False sector_rank=11 price=21.99 support=19.49 resistance=25.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=51.29 liquidity=10080660.0 spike=0.18
- NIPH.CA: score=26.96 buy_ready=False sector_rank=3 price=412.71 support=193.0 resistance=450.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=79.34 liquidity=757302592.0 spike=2.53
- OBRI.CA: score=16.9 buy_ready=False sector_rank=11 price=32.7 support=31.61 resistance=36.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=31.61 liquidity=15463038.0 spike=0.48
- OCDI.CA: score=24.98 buy_ready=False sector_rank=16 price=35.0 support=26.6 resistance=36.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=93.51 liquidity=141356768.0 spike=1.04
- OCPH.CA: score=21.4 buy_ready=False sector_rank=11 price=290.0 support=225.0 resistance=496.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=39.56 liquidity=43207064.0 spike=1.25
- ODIN.CA: score=27.54 buy_ready=False sector_rank=11 price=3.43 support=2.42 resistance=3.92 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=73.42 liquidity=63915716.0 spike=1.82
- OFH.CA: score=22.9 buy_ready=False sector_rank=11 price=0.9 support=0.67 resistance=0.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=80.0 liquidity=45444148.0 spike=0.48
- OIH.CA: score=26.28 buy_ready=False sector_rank=18 price=1.83 support=1.41 resistance=1.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=92.5 liquidity=196326112.0 spike=1.69
- OLFI.CA: score=32.9 buy_ready=True sector_rank=12 price=25.06 support=22.25 resistance=26.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=62.63 liquidity=512471616.0 spike=7.9
- ORAS.CA: score=9.1 buy_ready=False sector_rank=20 price=743.55 support=727.0 resistance=761.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=295101792.0 spike=1.0
- ORHD.CA: score=27.9 buy_ready=False sector_rank=16 price=42.88 support=38.0 resistance=44.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=74.71 liquidity=144680176.0 spike=0.86
- ORWE.CA: score=22.9 buy_ready=False sector_rank=5 price=26.1 support=22.55 resistance=27.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=79.01 liquidity=59977552.0 spike=0.8
- PHAR.CA: score=27.24 buy_ready=False sector_rank=3 price=142.0 support=88.05 resistance=178.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=73.1 liquidity=447594752.0 spike=1.17
- PHDC.CA: score=25.9 buy_ready=True sector_rank=16 price=15.25 support=14.32 resistance=15.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=66.28 liquidity=59238196.0 spike=0.26
- PHTV.CA: score=16.74 buy_ready=False sector_rank=11 price=390.0 support=291.51 resistance=447.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:13 PM market time freshness=DELAYED_CURRENT RSI=78.16 liquidity=3304668.0 spike=1.27
- POUL.CA: score=27.9 buy_ready=True sector_rank=12 price=39.29 support=36.5 resistance=40.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=57.73 liquidity=12714970.0 spike=0.47
- PRCL.CA: score=21.9 buy_ready=False sector_rank=1 price=32.99 support=32.8 resistance=38.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=31.31 liquidity=20922374.0 spike=0.56
- PRDC.CA: score=23.9 buy_ready=False sector_rank=16 price=8.83 support=8.7 resistance=10.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=37.67 liquidity=42173856.0 spike=0.39
- PRMH.CA: score=28.58 buy_ready=True sector_rank=11 price=2.75 support=2.56 resistance=2.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=55.56 liquidity=18384556.0 spike=1.34
- RACC.CA: score=30.46 buy_ready=True sector_rank=11 price=10.39 support=9.8 resistance=10.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=66.0 liquidity=42794956.0 spike=2.28
- RAKT.CA: score=12.13 buy_ready=False sector_rank=11 price=22.63 support=21.66 resistance=24.0 source=Yahoo Finance as_of=2026-08-12T21:00:00+00:00 freshness=FRESH RSI=49.49 liquidity=229219.26 spike=0.84
- RAYA.CA: score=12.8 buy_ready=False sector_rank=21 price=7.06 support=6.97 resistance=8.06 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=19.77 liquidity=109563224.0 spike=1.14
- RMDA.CA: score=26.9 buy_ready=False sector_rank=3 price=6.5 support=4.95 resistance=7.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=73.31 liquidity=88865032.0 spike=0.78
- ROTO.CA: score=25.38 buy_ready=False sector_rank=11 price=50.9 support=40.5 resistance=51.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=79.44 liquidity=28737458.0 spike=1.24
- RREI.CA: score=25.9 buy_ready=True sector_rank=11 price=4.43 support=3.72 resistance=4.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=63.16 liquidity=23043430.0 spike=0.36
- RTVC.CA: score=12.25 buy_ready=False sector_rank=11 price=3.76 support=3.73 resistance=4.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:12 PM market time freshness=DELAYED_CURRENT RSI=36.99 liquidity=2353494.75 spike=0.44
- RUBX.CA: score=18.9 buy_ready=False sector_rank=11 price=12.38 support=12.02 resistance=14.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=30.98 liquidity=12834261.0 spike=0.4
- SAUD.CA: score=30.88 buy_ready=True sector_rank=9 price=23.51 support=21.3 resistance=23.62 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=63.37 liquidity=25219244.0 spike=1.49
- SCEM.CA: score=31.82 buy_ready=True sector_rank=1 price=94.19 support=62.1 resistance=113.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=63.85 liquidity=262855520.0 spike=1.46
- SCFM.CA: score=21.21 buy_ready=False sector_rank=11 price=280.32 support=256.5 resistance=325.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=55.04 liquidity=7311731.0 spike=0.24
- SCTS.CA: score=20.77 buy_ready=True sector_rank=7 price=617.71 support=602.01 resistance=685.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:11 PM market time freshness=DELAYED_CURRENT RSI=51.27 liquidity=2871122.25 spike=0.34
- SDTI.CA: score=19.03 buy_ready=False sector_rank=11 price=72.42 support=46.6 resistance=75.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=80.95 liquidity=6134630.0 spike=0.22
- SEIG.CA: score=18.71 buy_ready=False sector_rank=11 price=278.04 support=237.0 resistance=295.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=87.07 liquidity=3809889.25 spike=0.3
- SIPC.CA: score=25.9 buy_ready=False sector_rank=11 price=4.61 support=3.72 resistance=5.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=70.19 liquidity=19808990.0 spike=0.35
- SKPC.CA: score=27.26 buy_ready=True sector_rank=8 price=16.62 support=15.61 resistance=16.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=64.85 liquidity=56171288.0 spike=1.18
- SMFR.CA: score=25.9 buy_ready=False sector_rank=11 price=269.47 support=223.0 resistance=309.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=71.76 liquidity=29758152.0 spike=0.73
- SNFC.CA: score=23.64 buy_ready=False sector_rank=11 price=11.02 support=10.6 resistance=11.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=37.61 liquidity=16963224.0 spike=1.37
- SPIN.CA: score=25.9 buy_ready=True sector_rank=5 price=16.39 support=14.57 resistance=17.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=63.21 liquidity=29525932.0 spike=0.96
- SPMD.CA: score=25.9 buy_ready=True sector_rank=11 price=0.48 support=0.44 resistance=0.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=65.09 liquidity=16696723.0 spike=0.49
- SUGR.CA: score=27.28 buy_ready=True sector_rank=12 price=49.36 support=46.47 resistance=51.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=67.01 liquidity=23619692.0 spike=1.69
- SVCE.CA: score=27.06 buy_ready=False sector_rank=11 price=10.81 support=9.06 resistance=12.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=73.96 liquidity=152117072.0 spike=1.58
- SWDY.CA: score=25.9 buy_ready=True sector_rank=17 price=107.57 support=90.52 resistance=114.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=68.7 liquidity=31109394.0 spike=0.48
- TALM.CA: score=22.9 buy_ready=False sector_rank=7 price=18.8 support=15.61 resistance=19.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=75.35 liquidity=18885280.0 spike=0.45
- TMGH.CA: score=23.9 buy_ready=False sector_rank=16 price=97.85 support=95.2 resistance=103.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=45.62 liquidity=286441216.0 spike=0.83
- TRTO.CA: score=24.91 buy_ready=False sector_rank=11 price=0.04 support=0.03 resistance=0.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:14 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=14002.33 spike=6.21
- UEFM.CA: score=18.89 buy_ready=True sector_rank=11 price=568.44 support=511.3 resistance=625.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:00 PM market time freshness=DELAYED_CURRENT RSI=68.89 liquidity=2993171.25 spike=0.48
- UEGC.CA: score=25.9 buy_ready=True sector_rank=11 price=2.57 support=2.08 resistance=2.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=51.35 liquidity=13370835.0 spike=0.26
- UNIP.CA: score=25.8 buy_ready=False sector_rank=11 price=0.4 support=0.36 resistance=0.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=49.04 liquidity=62260604.0 spike=1.95
- UNIT.CA: score=18.14 buy_ready=True sector_rank=16 price=20.18 support=17.32 resistance=23.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=67.27 liquidity=2238967.25 spike=0.12
- WCDF.CA: score=17.64 buy_ready=False sector_rank=11 price=630.79 support=519.26 resistance=700.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:14 PM market time freshness=DELAYED_CURRENT RSI=79.39 liquidity=4738897.0 spike=0.89
- WKOL.CA: score=25.9 buy_ready=True sector_rank=11 price=323.4 support=307.0 resistance=363.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=54.23 liquidity=23374184.0 spike=0.98
- ZEOT.CA: score=32.9 buy_ready=False sector_rank=11 price=13.62 support=11.51 resistance=14.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=74.69 liquidity=104720432.0 spike=3.59
- ZMID.CA: score=25.9 buy_ready=True sector_rank=16 price=7.61 support=7.06 resistance=7.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=13 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=55.12 liquidity=155240224.0 spike=0.64

## Backtesting Lite
- COSG.CA: 180d return=33.33%, max drawdown=-18.87%, MA20>MA50 days last20=20, as_of=2026-08-12T21:00:00+00:00
- COPR.CA: 180d return=-21.64%, max drawdown=-53.47%, MA20>MA50 days last20=20, as_of=2026-08-12T21:00:00+00:00
- ETEL.CA: 180d return=80.99%, max drawdown=-30.44%, MA20>MA50 days last20=18, as_of=2026-08-12T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- COSG.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Cairo Oil & Soap Company summary=Cairo Oils stock stabilizes above EGP 1.50 resistance level; EGX approves capital increase, reduction of several listed firms; Cairo oils incurs EGP 25m losses in H1-19 Gemini also reviewed web evidence but did not return ticker-specific citations.
  - Cairo Oils stock stabilizes above EGP 1.50 resistance level: https://english.mubasher.info/news/4546423/Cairo-Oils-stock-stabilizes-above-EGP-1-50-resistance-level/
  - EGX approves capital increase, reduction of several listed firms: https://english.mubasher.info/news/3828111/EGX-approves-capital-increase-reduction-of-several-listed-firms/
  - Cairo oils incurs EGP 25m losses in H1-19: https://english.mubasher.info/news/3521392/Cairo-oils-incurs-EGP-25m-losses-in-H1-19/
- COPR.CA: status=RECENT_ACCEPTED latest=2026-01-01 age_days=227 sources=3 expected=Copper for Commercial Investment & Real Estate Development summary=Recent disclosures and financial updates from Copper for Commercial Investment & Real Estate Development (COPR.CA) on the Egyptian Exchange.
  - Copper For Commercial Investment & Real Estate Development (COPR.CA) - Release Regarding a Disclosure Form (03/08/2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEh4M32ZppnCZXC9M7FUczWC_HJ4e8nu28MAf1ZFp2wAo-bPv7wd8GQVxgppfTjKkTdIg5XToEwVrE17I8MmCs-FMoJ8d7HgDrIbeeAo84Yi9In9puE6j8IETF9jScPvKIyRM-Ee9sVyyGLXLe_
  - Copper For Commercial Investment & Real Estate Development (COPR.CA) - Release Regarding a Disclosure Form (10/08/2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFSNk4nXcmhqMnr7T0d7HDh4SUw2a18aY8zgnXbUXbkISVkA0YISHkkvp2ORoEVPImZW88wa3-f4pMOcOu6XgOd721n2nDBY1umd2Pxig_5VFC1IF99GVWYLStDrae8vJUfiomLIHJq-nxd2G7pRNo=
  - Copper for Commercial Investment & Real Estate Development (COPR.CA) - Release Regarding a Disclosure Form (30/07/2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFSNk4nXcmhqMnr7T0d7HDh4SUw2a18aY8zgnXbUXbkISVkA0YISHkkvp2ORoEVPImZW88wa3-f4pMOcOu6XgOd721n2nDBY1umd2Pxig_5VFC1IF99GVWYLStDrae8vJUfiomLIHJq-nxd2G7pRNo=
- ETEL.CA: status=RECENT_ACCEPTED latest=2026-08-13 age_days=3 sources=3 expected=Telecom Egypt summary=Telecom Egypt (ETEL.CA) has released several financial results, disclosures, and corporate news, including a decision not to proceed with a data center stake sale.
  - Q2 2026 Results: Telecom Egypt Reports Improved Profitability and Efficiency in H1 2026 (13 August 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH7_ciqLqEdPAlrCYhBe47e9gt9tpbDDT-EgvlOCP6AYN0x30u9TUdQi_7kKj8xI2GNvwZVFZ2kNTiZ2zIbgss7IovyHLH63BkWQQ==
  - TE Q2 2026 Notice of Results (30 July 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFwECBpNxzj8j-JNuefsYTxEZIjsz4quVs4uqK99Z_w7xGR50F_XjVvS-R9BHeTEE1XTecGyhnPZuLEF4hu2MXqoEY9GVRcdMV4WG9v2iY3s_GeLFa7Neo25w_bWWW55Zv0JMnVCPDX1W6WhBe5kECVz9RxZNiGSUjOpVBp9oW1qnbwdyIs6xrO6Q==
  - Release from Telecom Egypt (ETEL.CA) Regarding the Financial Statements (30 July 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH2bUrShSrQouIpxRzY7FD9jEeKC5j9NGHLq9PCYqDeMo3xJnsOOGVru1UsiuKBA31Ca8PeW6z2FyQEoQbJeR7PXucIEV7iPHZ_LOgKufoWXl8_T6ACgTBV6Jr1gWDSzKR1P6NHxWGk9T31a4gY6Qg=
- OLFI.CA: status=RECENT_ACCEPTED latest=2026-08-11 age_days=5 sources=3 expected=Obour Land For Food Industries summary=Obour Land For Food Industries (OLFI.CA) has provided several recent disclosures and financial reports, including Q2 2026 results and dividend information.
  - Release from Obour Land For Food Industries (OLFI.CA) Regarding the Financial Results Report (in English) (11 August 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFRuEcfBBuMqZk5lqifEwIz4CT2AoAORQ_jYbUMZeRAAwr7Gdl1ZbhCqxW0jMslHG3V8-oXcPwxxXU5HZP49bZNu0C-elPwKgQGNgoQzPQHOj8g0bzH1KskjZcmNxzLUn6z9B166Ebw3qTID3Eh4iI571OpOM0bS1L4UTsZqelpPbKxEYPi0aMD4iYfrQeuVJKxP-SDEaa-mZYOeapqXfR3g4SVOc4-dFuscNm6uk9lnt5z8Buprk26RvUoUuXR6xMrtnS1dqtIPlpZ5vnodIkP1S3oVo0ZV_JzcDyRkCvicI3JGkTjukbQJuLksDg9wIy5KpRZXLuaIXvfeKS3SAx5k0XcHGnCjeh6
  - Obour Land For Food Industries (OLFI.CA) - Board of Directors' Meeting Minutes (11 August 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGCwizv_xoSXjlf_I_Y2GuvNrPA_W6MgmlvsVbQCJPsIfhXMe6vtHGTvL4StlJ_DJOc1ZZIp7yPyGCXIFY_C0flqA80liHOaW9ggOU5F-xCWHBx3Ifwer0i0CK5by5WjZb4WKMl70P1IpUv3lpz4Mc=
  - Obour Land For Food Industries (OLFI.CA) - Release Regarding a Disclosure Form (26/07/2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGyU6NGVZXBjEOFJc54f8Yaj3W0otBfhqe1VospFL2j5W0YWWsbuPglsDV7nT2tkRYB70j8NNtHd4XMrx4o3tur4-KEEyx28zwkpNinz_MtyIEaadq_YSxPmguyobJakvQucolYInlJUBRb4IL4
- MBSC.CA: status=RECENT_ACCEPTED latest=2026-07-30 age_days=17 sources=3 expected=Misr Beni Suef Cement summary=Misr Beni Suef Cement (MBSC.CA) has recently reported on treasury stock activities, financial results, and board disclosures.
  - Release from Misr Beni Suef Cement (MBSC.CA) Regarding the Purchase of Treasury Stocks (13-08-2026 for 12/08/2026 trading session): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGjTiisz5dR5RdIu1KAB0rF_9vuVIAn5J_CRg4PKIluEuf40y6TlKTQYQyg6LHVraoaeUtsU2pbDkXEwbkxzHY3MNgamKWoWjt75fzxkiiDRI0vgoMFYwhBAmbAIabPdGTb41J0qTRgm9M0u8wnnWTAucOGO078bYQDDPxmS64LGVxpkZQyUxw2KP38rQRw9Oc=
  - Release from Misr Beni Suef Cement (MBSC.CA) Concerning the Sale of Treasury Stocks (30 July 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEeQr9gVUdoV0bV44A45SwXCET6wucTricstNz5jSk-hfFv6pgMdPUimfbQoGJibZX2qO07WBxBN-37fNSWl6EvjW-A0kxNDSrTjkjgxFHqrwF71hjYqXsoYFY3P1hEfh_7N7DEeNAWhapbgj6kgF0=
  - Misr Beni Suef Cement (MBSC.CA) - Release Regarding a Disclosure Form (30 July 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEeQr9gVUdoV0bV44A45SwXCET6wucTricstNz5jSk-hfFv6pgMdPUimfbQoGJibZX2qO07WBxBN-37fNSWl6EvjW-A0kxNDSrTjkjgxFHqrwF71hjYqXsoYFY3P1hEfh_7N7DEeNAWhapbgj6kgF0=
- ZEOT.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Extracted Oil & Derivatives Co. summary=Extracted Oils stock nears record high on strong momentum; Extracted Oils stock witnesses increasing buying power amid current resistance – Analysis; Extracted Oils swings to nearly EGP 14.5m net profits in Q1-25/26 Gemini also reviewed web evidence but did not return ticker-specific citations.
  - Extracted Oils stock nears record high on strong momentum: https://english.mubasher.info/news/4599376/Extracted-Oils-stock-nears-record-high-on-strong-momentum/
  - Extracted Oils stock witnesses increasing buying power amid current resistance – Analysis: https://english.mubasher.info/news/4555925/Extracted-Oils-stock-witnesses-increasing-buying-power-amid-current-resistance-Analysis/
  - Extracted Oils swings to nearly EGP 14.5m net profits in Q1-25/26: https://english.mubasher.info/news/4537956/Extracted-Oils-swings-to-nearly-EGP-14-5m-net-profits-in-Q1-25-26/
- SCEM.CA: status=RECENT_ACCEPTED latest=2026-05-14 age_days=94 sources=3 expected=Sinai Cement summary=Sinai Cement (SCEM.CA) has issued recent disclosures regarding its board and shareholder structure, as well as financial results.
  - Sinai Cement (SCEM.CA) - Disclosure Form for the BoD & the Shareholders' Structure (22/07/2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF0sf8bj0Q8HoMJpy2rFcWAAnWtGeSliKt4yvXse2u8sX1Usie3PAXZM-21liBLz_UQuOEEniZ8lGuMWrIJtEF2u7zKVpMweXxuJiEHmLbapD_aHh77XeEM9R3LwaAW7dHmko5ySnUsBEKO4OeCHw==
  - Sinai Cement (SCEM.CA) - Disclosure Form Concerning the BoD & the Shareholders' Structure for the period 31/03/2026 (28/04/2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF-1rIWxpaGbRxpbVn3o1xxuyictb-fl-pFGxrKYvZLOeknSb83CfUwCAWo6lsLCllRzKc3zGEycvnJ60oyPRibvszo5fi3kTDI6Hi14WdhJANkyonMCsfZNFMbDdHXumRVyA_zJagmN1sPsUWS
  - Release from Sinai Cement (SCEM.CA) Concerning the Amendments in the Board of Directors (14 May 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGGiOuByj1oNlSyehJx9mUoJrk0g6ng4WFjygv5OiDmYByh-hiKe0yTuIuKeVvSpqNZOTZQoXnbi4mPWN2A9EU7OQSn62Uk-8LR560kl1PCCV411e3dKYIMpYqjS5cWO54GK5tAPTlpx3_ACPf67C4IIdjM1Z416k2-YZxRKA==
- EEII.CA: status=OLD_ACCEPTED latest=2019-01-01 age_days=2784 sources=3 expected=Arab Engineering Industries summary=Shareholder cuts stake in Arab Engineering Industries to 9%; Arab Moltaqa cuts stake in Arab Engineering Industries; Lower sales weigh on Arab Engineering Industries’ profit in 2019 Gemini also reviewed web evidence but did not return ticker-specific citations.
  - Shareholder cuts stake in Arab Engineering Industries to 9%: https://english.mubasher.info/news/4009461/Shareholder-cuts-stake-in-Arab-Engineering-Industries-to-9-/
  - Arab Moltaqa cuts stake in Arab Engineering Industries: https://english.mubasher.info/news/3707590/Arab-Moltaqa-cuts-stake-in-Arab-Engineering-Industries/
  - Lower sales weigh on Arab Engineering Industries’ profit in 2019: https://english.mubasher.info/news/3586813/Lower-sales-weigh-on-Arab-Engineering-Industries-profit-in-2019/

## Warnings
- Evidence for COSG.CA matches the company but no source/report date was detected.
- Evidence for ZEOT.CA matches the company but no source/report date was detected.
- Evidence for EEII.CA matches the company but appears old; latest detected date is 2019-01-01.
