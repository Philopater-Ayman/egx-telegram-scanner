# Telegram-First EGX Scanner Report

Scan phase: Open liquidity confirmation
Generated UTC: 2026-09-10T11:16:31.683207+00:00
Generated Cairo: 2026-09-10 14:16
Run timing: target 09:15 Cairo | generated Cairo 2026-09-10 14:16 | cron 15 6 * * 0-4
Trigger: scheduled cron=15 6 * * 0-4 mapped to open_confirm; Cairo now 2026-09-10 14:12

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 45
- Data quality issues: 1
- Tradeable price/liquidity tickers: 176/189
- Top sector: Telecommunications

## Market Context
- Market trend: Bullish
- Source: Mubasher EGX market page (delayed public data)
- As of: Thursday, September 10
- Freshness: DELAYED
- EGX30 regime: CONSTRUCTIVE / above MA20 55.0% / above MA50 80.0%
- EGX70 regime: BEARISH / above MA20 42.11% / above MA50 68.42%
- Sector breadth: 47.62%
- Risk mode: SELECTIVE_SWING_TRADES_ONLY

## Top Liquidity
- CCAP.CA: liquidity=753952384.0 spike=1.08 score=26.56
- COMI.CA: liquidity=636100032.0 spike=1.21 score=22.65
- MPCO.CA: liquidity=564572608.0 spike=5.17 score=14.26
- ETEL.CA: liquidity=443216608.0 spike=2.57 score=29.54
- AMES.CA: liquidity=345256544.0 spike=1.7 score=9.76

## AI Narrative
- Provider: OpenRouter OK
- Model: nvidia/nemotron-3-super-120b-a12b:free
- Summary: EGX30 shows a constructive trend while EGX70 is bearish, sector breadth is 47.6% and risk mode is SELECTIVE_SWING_TRADES_ONLY; the local scanner did not find any ticket that satisfied its evidence, liquidity, freshness and technical gates, so it maintains a HOLD stance.
- Liquidity spikes (e.g., EFIC.CA, EASB.CA, ETEL.CA) indicate accumulation interest, but many lack fresh evidence or fail technical filters, lowering confidence for near‑term action.
- Most candidates sit 8‑22% below their 20‑day support and hover close to resistance, limiting upside potential over the next 1‑3 days.
- Leading sectors – Telecommunications, Investment Holding and Textiles – show strong breadth, yet EGX70’s bearish MA20 bias keeps overall market risk selective.
- The EGX30‑constructive / EGX70‑bearish regime shifts the risk mode to SELECTIVE_SWING_TRADES_ONLY, adding uncertainty and justifying the current HOLD position.

## Top Liquidity Spikes
- EPCO.CA: spike=6.01 liquidity=94824264.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- MPCO.CA: spike=5.17 liquidity=564572608.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- EASB.CA: spike=4.06 liquidity=48360856.0 outlook=CONSTRUCTIVE score=69.39 buy_ready=True
- POUL.CA: spike=3.92 liquidity=75849656.0 outlook=BULLISH_WATCH score=72.01 buy_ready=True
- NCCW.CA: spike=3.5 liquidity=141560992.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False

## Sector Leaderboard
- #1 Telecommunications: score=12.75 5d=6.8% 20d=8.77% aboveMA50=100.0%
- #2 Investment Holding: score=11.79 5d=2.87% 20d=17.31% aboveMA50=100.0%
- #3 Textiles: score=10.23 5d=2.95% 20d=16.74% aboveMA50=100.0%
- #4 Basic Resources & Chemicals: score=7.06 5d=2.35% 20d=5.93% aboveMA50=80.0%
- #5 Fintech & Payments: score=6.36 5d=2.83% 20d=1.62% aboveMA50=100.0%
- #6 Education: score=5.85 5d=1.34% 20d=-1.59% aboveMA50=100.0%
- #7 Transportation & Logistics: score=5.81 5d=-0.03% 20d=4.16% aboveMA50=100.0%
- #8 Agriculture & Food Production: score=5.65 5d=0.86% 20d=-1.96% aboveMA50=50.0%

## Today's Prioritized Action Tickets
- HOLD: Local fallback HOLD: no candidate passed evidence, liquidity, freshness, and technical gates.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- EFIC.CA: BULLISH_WATCH score=94.06 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=No major short-term scanner risk flags.
- BINV.CA: BULLISH_WATCH score=88 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; momentum is extended
- KABO.CA: BULLISH_WATCH score=82 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; momentum is extended
- ORWE.CA: BULLISH_WATCH score=82 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; momentum is extended
- ALCN.CA: BULLISH_WATCH score=81.81 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- ETEL.CA: BULLISH_WATCH score=81 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=overheated RSI; close to resistance
- ORHD.CA: BULLISH_WATCH score=79.9 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=close to resistance; sector is not leading
- RUBX.CA: BULLISH_WATCH score=79.39 liquidity=TRADEABLE sector=IMPROVING risk=sector is not leading
- EXPA.CA: BULLISH_WATCH score=76.57 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; sector is not leading
- FWRY.CA: BULLISH_WATCH score=76.36 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling

## BUY-Ready Candidates
- EFIC.CA: rank=31.08 outlook=BULLISH_WATCH outlook_score=94.06 sector_rank=4 price=216.92 support=192.75 resistance=260.0 liquidity=275492576.0
- EASB.CA: rank=30.36 outlook=CONSTRUCTIVE outlook_score=69.39 sector_rank=13 price=8.6 support=7.05 resistance=8.72 liquidity=48360856.0
- POUL.CA: rank=28.6 outlook=BULLISH_WATCH outlook_score=72.01 sector_rank=11 price=39.99 support=36.97 resistance=40.69 liquidity=75849656.0
- FWRY.CA: rank=26.4 outlook=BULLISH_WATCH outlook_score=76.36 sector_rank=5 price=19.11 support=18.66 resistance=19.69 liquidity=40080344.0
- SKPC.CA: rank=26.4 outlook=CONSTRUCTIVE outlook_score=63.06 sector_rank=4 price=18.5 support=16.5 resistance=19.36 liquidity=71692048.0
- CIRA.CA: rank=26.34 outlook=BULLISH_WATCH outlook_score=75.85 sector_rank=6 price=37.0 support=32.1 resistance=40.8 liquidity=14368987.0
- EXPA.CA: rank=26.23 outlook=BULLISH_WATCH outlook_score=76.57 sector_rank=9 price=21.2 support=19.8 resistance=22.39 liquidity=24527286.0
- CANA.CA: rank=25.77 outlook=BULLISH_WATCH outlook_score=70.57 sector_rank=9 price=42.97 support=40.0 resistance=44.29 liquidity=9539130.0
- TMGH.CA: rank=25.56 outlook=CONSTRUCTIVE outlook_score=62.9 sector_rank=12 price=99.51 support=94.9 resistance=100.9 liquidity=157659456.0
- HELI.CA: rank=25.56 outlook=BULLISH_WATCH outlook_score=74.9 sector_rank=12 price=7.9 support=7.34 resistance=8.4 liquidity=65328948.0

## Data Quality Issues
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=15.71 buy_ready=False sector_rank=13 price=305.75 support=290.0 resistance=375.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=25.0 liquidity=9350020.0 spike=0.24
- ABUK.CA: score=23.4 buy_ready=False sector_rank=4 price=93.97 support=74.61 resistance=94.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=77.76 liquidity=76037648.0 spike=0.45
- ACAMD.CA: score=20.36 buy_ready=False sector_rank=13 price=2.1 support=1.95 resistance=2.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=46.97 liquidity=15769393.0 spike=0.27
- ACGC.CA: score=25.4 buy_ready=False sector_rank=3 price=15.2 support=10.73 resistance=16.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=72.23 liquidity=13118206.0 spike=0.3
- ADCI.CA: score=12.71 buy_ready=False sector_rank=13 price=291.07 support=280.0 resistance=328.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:56 PM market time freshness=DELAYED_CURRENT RSI=57.24 liquidity=1355373.13 spike=0.12
- ADIB.CA: score=22.23 buy_ready=False sector_rank=9 price=52.3 support=51.15 resistance=55.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=38.22 liquidity=43982296.0 spike=0.61
- ADPC.CA: score=18.36 buy_ready=False sector_rank=13 price=3.92 support=3.85 resistance=4.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=38.96 liquidity=17372400.0 spike=0.53
- AFDI.CA: score=13.81 buy_ready=False sector_rank=13 price=54.5 support=53.54 resistance=69.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=30.35 liquidity=7451495.5 spike=0.26
- AFMC.CA: score=16.36 buy_ready=False sector_rank=13 price=161.84 support=157.0 resistance=300.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=21.3 liquidity=18246948.0 spike=0.22
- AJWA.CA: score=13.36 buy_ready=False sector_rank=13 price=179.79 support=175.15 resistance=202.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=18.96 liquidity=14035774.0 spike=0.26
- ALCN.CA: score=23.76 buy_ready=True sector_rank=7 price=32.08 support=30.03 resistance=34.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=60.5 liquidity=7431429.0 spike=0.23
- ALUM.CA: score=17.39 buy_ready=False sector_rank=13 price=27.73 support=26.5 resistance=30.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=55.49 liquidity=6031691.5 spike=0.23
- AMER.CA: score=21.56 buy_ready=False sector_rank=12 price=5.26 support=5.3 resistance=8.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=40.65 liquidity=38162008.0 spike=0.48
- AMES.CA: score=9.76 buy_ready=False sector_rank=13 price=59.88 support=58.52 resistance=64.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=345256544.0 spike=1.7
- AMIA.CA: score=14.48 buy_ready=True sector_rank=13 price=18.78 support=12.12 resistance=22.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:53 PM market time freshness=DELAYED_CURRENT RSI=65.44 liquidity=3126195.25 spike=0.04
- AMOC.CA: score=8.78 buy_ready=False sector_rank=14 price=13.67 support=13.5 resistance=14.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=227299376.0 spike=1.24
- APSW.CA: score=7.76 buy_ready=False sector_rank=13 price=8.6 support=8.41 resistance=9.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:52 PM market time freshness=DELAYED_CURRENT RSI=42.27 liquidity=399573.63 spike=0.3
- ARAB.CA: score=23.56 buy_ready=True sector_rank=12 price=0.26 support=0.23 resistance=0.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=65.0 liquidity=70954888.0 spike=0.72
- ARCC.CA: score=20.9 buy_ready=False sector_rank=16 price=75.39 support=70.0 resistance=91.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=57.98 liquidity=12520628.0 spike=0.12
- AREH.CA: score=18.39 buy_ready=False sector_rank=13 price=1.48 support=1.39 resistance=1.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=8032433.0 spike=0.39
- ARVA.CA: score=8.36 buy_ready=False sector_rank=13 price=14.99 support=14.45 resistance=14.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=16 August 01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=30473338.0 spike=0.56
- ASCM.CA: score=21.01 buy_ready=True sector_rank=13 price=63.9 support=62.01 resistance=69.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=57.66 liquidity=7655766.0 spike=0.25
- ASPI.CA: score=14.32 buy_ready=False sector_rank=13 price=0.42 support=0.43 resistance=0.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=30.9 liquidity=74046648.0 spike=1.48
- ATLC.CA: score=22.84 buy_ready=False sector_rank=17 price=7.36 support=5.2 resistance=8.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=72.26 liquidity=22009310.0 spike=0.73
- ATQA.CA: score=23.4 buy_ready=False sector_rank=4 price=12.81 support=10.74 resistance=13.21 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=83.33 liquidity=101173632.0 spike=0.87
- AXPH.CA: score=15.64 buy_ready=False sector_rank=13 price=1675.71 support=1281.0 resistance=1768.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=84.78 liquidity=5283901.5 spike=0.43
- BINV.CA: score=25.15 buy_ready=True sector_rank=2 price=51.53 support=46.25 resistance=55.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=65.68 liquidity=8746930.0 spike=0.79
- BIOC.CA: score=8.36 buy_ready=False sector_rank=13 price=288.09 support=285.0 resistance=309.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=51691136.0 spike=0.23
- BTFH.CA: score=16.84 buy_ready=False sector_rank=17 price=2.96 support=2.94 resistance=3.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=43.33 liquidity=27385278.0 spike=0.21
- CAED.CA: score=16.58 buy_ready=False sector_rank=13 price=130.02 support=122.0 resistance=185.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=11.31 liquidity=40809668.0 spike=1.11
- CANA.CA: score=25.77 buy_ready=True sector_rank=9 price=42.97 support=40.0 resistance=44.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:55 PM market time freshness=DELAYED_CURRENT RSI=58.48 liquidity=9539130.0 spike=0.53
- CCAP.CA: score=26.56 buy_ready=False sector_rank=2 price=6.23 support=5.24 resistance=6.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=72.99 liquidity=753952384.0 spike=1.08
- CCRS.CA: score=18.98 buy_ready=False sector_rank=13 price=2.6 support=2.4 resistance=3.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=57.04 liquidity=7626089.0 spike=0.15
- CEFM.CA: score=16.13 buy_ready=True sector_rank=13 price=146.73 support=133.0 resistance=168.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:48 PM market time freshness=DELAYED_CURRENT RSI=54.27 liquidity=2778138.75 spike=0.17
- CERA.CA: score=22.16 buy_ready=False sector_rank=13 price=1.67 support=1.22 resistance=1.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=78.57 liquidity=104339160.0 spike=1.9
- CFGH.CA: score=13.36 buy_ready=False sector_rank=13 price=0.12 support=0.1 resistance=0.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:55 PM market time freshness=DELAYED_CURRENT RSI=68.42 liquidity=8614.49 spike=0.34
- CICH.CA: score=18.78 buy_ready=True sector_rank=17 price=13.0 support=12.0 resistance=13.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:55 PM market time freshness=DELAYED_CURRENT RSI=69.35 liquidity=5476116.5 spike=1.23
- CIEB.CA: score=20.11 buy_ready=True sector_rank=9 price=25.21 support=24.0 resistance=26.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=60.45 liquidity=3878200.0 spike=0.25
- CIRA.CA: score=26.34 buy_ready=True sector_rank=6 price=37.0 support=32.1 resistance=40.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=53.29 liquidity=14368987.0 spike=0.42
- CLHO.CA: score=18.14 buy_ready=False sector_rank=15 price=16.09 support=16.0 resistance=18.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=35.99 liquidity=83862064.0 spike=1.08
- CNFN.CA: score=12.23 buy_ready=False sector_rank=17 price=4.76 support=4.73 resistance=5.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=45.9 liquidity=4385409.0 spike=0.26
- COMI.CA: score=22.65 buy_ready=False sector_rank=9 price=138.53 support=135.35 resistance=142.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=58.22 liquidity=636100032.0 spike=1.21
- COPR.CA: score=21.36 buy_ready=False sector_rank=13 price=0.49 support=0.41 resistance=0.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=50.51 liquidity=13432749.0 spike=0.14
- COSG.CA: score=24.02 buy_ready=True sector_rank=13 price=1.87 support=1.71 resistance=2.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=60.47 liquidity=8668722.0 spike=0.15
- CPCI.CA: score=12.69 buy_ready=False sector_rank=13 price=536.14 support=520.0 resistance=569.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=59.85 liquidity=1336695.25 spike=0.21
- CSAG.CA: score=21.83 buy_ready=False sector_rank=7 price=40.56 support=38.13 resistance=44.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT RSI=61.63 liquidity=9502589.0 spike=0.43
- DAPH.CA: score=23.36 buy_ready=True sector_rank=13 price=127.28 support=108.11 resistance=157.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=56.75 liquidity=9999369.0 spike=0.14
- DEIN.CA: score=11.36 buy_ready=False sector_rank=13 price=10.35 support=10.35 resistance=12.42 source=Yahoo Finance as_of=2026-09-08T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- DOMT.CA: score=14.68 buy_ready=False sector_rank=11 price=28.01 support=27.79 resistance=30.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:55 PM market time freshness=DELAYED_CURRENT RSI=45.91 liquidity=3076698.75 spike=0.34
- DSCW.CA: score=18.36 buy_ready=False sector_rank=13 price=1.88 support=1.84 resistance=2.21 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=47.06 liquidity=13049692.0 spike=0.2
- DTPP.CA: score=22.5 buy_ready=True sector_rank=13 price=302.77 support=290.0 resistance=340.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=57.22 liquidity=9144953.0 spike=0.25
- EALR.CA: score=7.7 buy_ready=False sector_rank=13 price=374.81 support=340.0 resistance=471.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:56 PM market time freshness=DELAYED_CURRENT RSI=26.4 liquidity=4348678.0 spike=0.13
- EASB.CA: score=30.36 buy_ready=True sector_rank=13 price=8.6 support=7.05 resistance=8.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=65.63 liquidity=48360856.0 spike=4.06
- EAST.CA: score=19.6 buy_ready=False sector_rank=11 price=34.73 support=34.9 resistance=37.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=43.33 liquidity=44625664.0 spike=0.68
- EBSC.CA: score=23.36 buy_ready=True sector_rank=13 price=2.15 support=1.88 resistance=2.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=66.67 liquidity=10058737.0 spike=0.67
- ECAP.CA: score=7.67 buy_ready=False sector_rank=13 price=32.95 support=31.16 resistance=41.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=30.78 liquidity=4316003.0 spike=0.24
- EDFM.CA: score=12.79 buy_ready=False sector_rank=13 price=410.24 support=394.0 resistance=432.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:53 PM market time freshness=DELAYED_CURRENT RSI=63.59 liquidity=1431772.13 spike=0.72
- EEII.CA: score=7.24 buy_ready=False sector_rank=13 price=2.36 support=2.33 resistance=3.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=16.43 liquidity=3883697.75 spike=0.13
- EFIC.CA: score=31.08 buy_ready=True sector_rank=4 price=216.92 support=192.75 resistance=260.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:56 PM market time freshness=DELAYED_CURRENT RSI=44.02 liquidity=275492576.0 spike=3.34
- EFID.CA: score=21.6 buy_ready=False sector_rank=11 price=31.14 support=29.71 resistance=34.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=47.8 liquidity=51876348.0 spike=0.76
- EFIH.CA: score=22.4 buy_ready=False sector_rank=5 price=23.74 support=22.16 resistance=25.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=47.39 liquidity=24437892.0 spike=0.27
- EGAL.CA: score=24.4 buy_ready=False sector_rank=4 price=375.3 support=321.01 resistance=395.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:56 PM market time freshness=DELAYED_CURRENT RSI=72.97 liquidity=42824676.0 spike=0.26
- EGAS.CA: score=16.08 buy_ready=True sector_rank=14 price=58.94 support=55.21 resistance=62.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=57.88 liquidity=2775383.0 spike=0.21
- EGBE.CA: score=12.25 buy_ready=False sector_rank=9 price=0.51 support=0.51 resistance=0.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:48 PM market time freshness=DELAYED_CURRENT RSI=37.5 liquidity=19997.94 spike=0.1
- EGCH.CA: score=22.4 buy_ready=False sector_rank=4 price=13.83 support=13.3 resistance=14.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=48.13 liquidity=129151032.0 spike=1.0
- EGSA.CA: score=14.4 buy_ready=False sector_rank=1 price=9.04 support=8.65 resistance=9.1 source=Yahoo Finance as_of=2026-09-08T21:00:00+00:00 freshness=FRESH RSI=84.44 liquidity=2965.12 spike=0.46
- EGTS.CA: score=13.33 buy_ready=False sector_rank=12 price=17.13 support=16.17 resistance=20.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=48.18 liquidity=2772400.75 spike=0.08
- EHDR.CA: score=21.36 buy_ready=False sector_rank=13 price=2.92 support=2.81 resistance=3.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=43.48 liquidity=12996632.0 spike=0.41
- EKHO.CA: score=9.3 buy_ready=False sector_rank=14 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-09-08T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=18.21 buy_ready=False sector_rank=10 price=2.08 support=2.04 resistance=2.21 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=44.12 liquidity=43372172.0 spike=0.67
- ELKA.CA: score=21.36 buy_ready=False sector_rank=13 price=1.76 support=1.7 resistance=1.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:56 PM market time freshness=DELAYED_CURRENT RSI=55.56 liquidity=14453641.0 spike=0.25
- ELNA.CA: score=10.19 buy_ready=False sector_rank=13 price=35.74 support=36.1 resistance=38.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:52 PM market time freshness=DELAYED_CURRENT RSI=73.16 liquidity=896867.56 spike=1.97
- ELSH.CA: score=20.36 buy_ready=False sector_rank=13 price=13.48 support=12.97 resistance=14.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=53.53 liquidity=20327600.0 spike=0.46
- ELWA.CA: score=15.41 buy_ready=False sector_rank=13 price=1.8 support=1.62 resistance=1.99 source=Yahoo Finance as_of=2026-09-08T21:00:00+00:00 freshness=FRESH RSI=58.75 liquidity=3832795.7 spike=1.61
- EMFD.CA: score=20.56 buy_ready=False sector_rank=12 price=14.88 support=11.51 resistance=15.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=92.84 liquidity=102290312.0 spike=0.67
- ENGC.CA: score=13.14 buy_ready=False sector_rank=13 price=43.6 support=41.8 resistance=54.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=47.17 liquidity=4782814.0 spike=0.24
- EOSB.CA: score=15.41 buy_ready=False sector_rank=13 price=1.57 support=1.5 resistance=1.64 source=Yahoo Finance as_of=2026-09-08T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=49109.6 spike=0.84
- EPCO.CA: score=13.36 buy_ready=False sector_rank=13 price=11.85 support=11.07 resistance=12.21 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=94824264.0 spike=6.01
- EPPK.CA: score=-1.22 buy_ready=False sector_rank=13 price=10.29 support=10.29 resistance=10.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=8 September 01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=419183.72 spike=0.28
- ETEL.CA: score=29.54 buy_ready=False sector_rank=1 price=126.02 support=107.0 resistance=126.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=77.53 liquidity=443216608.0 spike=2.57
- ETRS.CA: score=17.95 buy_ready=True sector_rank=13 price=11.2 support=10.64 resistance=11.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=55.29 liquidity=4592147.5 spike=0.19
- EXPA.CA: score=26.23 buy_ready=True sector_rank=9 price=21.2 support=19.8 resistance=22.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=55.15 liquidity=24527286.0 spike=0.66
- FAIT.CA: score=16.19 buy_ready=False sector_rank=9 price=47.99 support=38.83 resistance=48.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=87.82 liquidity=2962302.75 spike=0.33
- FAITA.CA: score=9.76 buy_ready=False sector_rank=9 price=0.98 support=0.98 resistance=1.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=71009.09 spike=1.23
- FERC.CA: score=22.1 buy_ready=False sector_rank=4 price=78.98 support=76.7 resistance=86.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=59.95 liquidity=7697569.5 spike=0.33
- FWRY.CA: score=26.4 buy_ready=True sector_rank=5 price=19.11 support=18.66 resistance=19.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=55.88 liquidity=40080344.0 spike=0.27
- GBCO.CA: score=21.3 buy_ready=False sector_rank=19 price=30.31 support=27.51 resistance=32.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=50.81 liquidity=24463822.0 spike=0.46
- GDWA.CA: score=19.36 buy_ready=False sector_rank=13 price=0.79 support=0.77 resistance=0.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=51.88 liquidity=11072272.0 spike=0.24
- GGCC.CA: score=21.36 buy_ready=False sector_rank=13 price=0.86 support=0.83 resistance=1.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=36.7 liquidity=10715528.0 spike=0.22
- GIHD.CA: score=10.46 buy_ready=False sector_rank=13 price=77.41 support=73.66 resistance=78.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=60563420.0 spike=2.05
- GMCI.CA: score=8.71 buy_ready=False sector_rank=13 price=1.88 support=1.83 resistance=2.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:35 PM market time freshness=DELAYED_CURRENT RSI=43.75 liquidity=356662.69 spike=0.7
- GRCA.CA: score=8.36 buy_ready=False sector_rank=13 price=52.11 support=51.14 resistance=57.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=21284842.0 spike=1.0
- GSSC.CA: score=17.02 buy_ready=True sector_rank=13 price=297.81 support=275.5 resistance=325.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=66.98 liquidity=3665997.5 spike=0.27
- GTWL.CA: score=23.36 buy_ready=True sector_rank=13 price=241.8 support=121.55 resistance=248.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=65.32 liquidity=116988672.0 spike=0.38
- HDBK.CA: score=21.23 buy_ready=False sector_rank=9 price=109.18 support=84.36 resistance=124.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=76.32 liquidity=54430320.0 spike=1.0
- HELI.CA: score=25.56 buy_ready=True sector_rank=12 price=7.9 support=7.34 resistance=8.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=60.75 liquidity=65328948.0 spike=0.41
- HRHO.CA: score=18.84 buy_ready=False sector_rank=17 price=25.8 support=25.33 resistance=27.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=47.5 liquidity=24299280.0 spike=0.23
- ICID.CA: score=13.11 buy_ready=False sector_rank=13 price=18.23 support=9.51 resistance=19.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=73.69 liquidity=1749580.0 spike=0.06
- IDRE.CA: score=14.85 buy_ready=False sector_rank=13 price=54.03 support=51.02 resistance=58.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=54.79 liquidity=3496676.0 spike=0.26
- IFAP.CA: score=24.26 buy_ready=False sector_rank=8 price=20.64 support=20.2 resistance=22.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=56.23 liquidity=11666026.0 spike=0.43
- INFI.CA: score=21.1 buy_ready=False sector_rank=13 price=146.25 support=140.66 resistance=178.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:55 PM market time freshness=DELAYED_CURRENT RSI=48.83 liquidity=9747685.0 spike=0.15
- IRON.CA: score=13.62 buy_ready=False sector_rank=4 price=28.92 support=27.84 resistance=33.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=7.21 liquidity=15252005.0 spike=1.11
- ISMA.CA: score=25.82 buy_ready=False sector_rank=13 price=32.14 support=29.0 resistance=40.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=38.51 liquidity=84597080.0 spike=3.23
- ISMQ.CA: score=21.4 buy_ready=False sector_rank=4 price=9.15 support=9.0 resistance=9.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=56.07 liquidity=17974194.0 spike=0.43
- ISPH.CA: score=20.98 buy_ready=False sector_rank=15 price=12.91 support=12.75 resistance=14.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=47.79 liquidity=26176766.0 spike=0.25
- JUFO.CA: score=19.75 buy_ready=False sector_rank=11 price=27.18 support=26.07 resistance=27.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT RSI=56.37 liquidity=7148874.5 spike=0.22
- KABO.CA: score=25.4 buy_ready=True sector_rank=3 price=9.5 support=8.49 resistance=9.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=63.98 liquidity=32004928.0 spike=0.68
- KWIN.CA: score=18.36 buy_ready=False sector_rank=13 price=88.88 support=84.08 resistance=137.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=53.27 liquidity=14021818.0 spike=0.21
- KZPC.CA: score=25.36 buy_ready=True sector_rank=13 price=14.45 support=9.45 resistance=16.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=55.36 liquidity=23644220.0 spike=0.36
- LCSW.CA: score=20.9 buy_ready=False sector_rank=16 price=33.81 support=32.12 resistance=37.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=55.59 liquidity=16026957.0 spike=0.48
- LUTS.CA: score=8.72 buy_ready=False sector_rank=13 price=1.02 support=0.91 resistance=1.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=319496864.0 spike=1.18
- MAAL.CA: score=16.93 buy_ready=False sector_rank=13 price=8.87 support=8.18 resistance=10.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=56.87 liquidity=5578543.5 spike=0.4
- MASR.CA: score=25.36 buy_ready=True sector_rank=13 price=8.21 support=7.49 resistance=8.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=62.79 liquidity=46022032.0 spike=0.54
- MBSC.CA: score=22.9 buy_ready=True sector_rank=16 price=410.67 support=318.01 resistance=470.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=64.46 liquidity=14277804.0 spike=0.14
- MCQE.CA: score=20.9 buy_ready=False sector_rank=16 price=235.02 support=212.01 resistance=292.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=63.63 liquidity=12907999.0 spike=0.21
- MCRO.CA: score=22.36 buy_ready=False sector_rank=13 price=1.68 support=1.44 resistance=1.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=76.74 liquidity=69646744.0 spike=0.6
- MENA.CA: score=4.27 buy_ready=False sector_rank=12 price=6.71 support=6.58 resistance=7.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=32.99 liquidity=708876.63 spike=0.12
- MEPA.CA: score=23.36 buy_ready=True sector_rank=13 price=2.03 support=1.8 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=67.11 liquidity=14574213.0 spike=0.4
- MFPC.CA: score=23.4 buy_ready=False sector_rank=4 price=47.98 support=37.91 resistance=48.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=87.37 liquidity=61088528.0 spike=0.45
- MFSC.CA: score=18.74 buy_ready=True sector_rank=13 price=50.25 support=48.06 resistance=58.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:46 PM market time freshness=DELAYED_CURRENT RSI=60.44 liquidity=3386333.75 spike=0.55
- MHOT.CA: score=20.62 buy_ready=False sector_rank=21 price=17.91 support=17.72 resistance=21.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=40.72 liquidity=9785010.0 spike=0.53
- MICH.CA: score=23.29 buy_ready=True sector_rank=13 price=49.61 support=46.64 resistance=53.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=60.06 liquidity=9935090.0 spike=0.34
- MILS.CA: score=16.02 buy_ready=False sector_rank=13 price=201.66 support=188.0 resistance=248.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=39.46 liquidity=4659786.0 spike=0.07
- MIPH.CA: score=14.23 buy_ready=True sector_rank=15 price=799.34 support=700.2 resistance=820.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=68.59 liquidity=1245993.25 spike=0.29
- MOED.CA: score=24.36 buy_ready=True sector_rank=13 price=0.79 support=0.68 resistance=0.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=56.25 liquidity=28646268.0 spike=0.25
- MOIL.CA: score=13.34 buy_ready=False sector_rank=14 price=0.68 support=0.65 resistance=0.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:36 PM market time freshness=DELAYED_CURRENT RSI=64.21 liquidity=43095.07 spike=0.18
- MOIN.CA: score=23.36 buy_ready=True sector_rank=13 price=39.51 support=32.5 resistance=45.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=68.35 liquidity=18280830.0 spike=0.47
- MOSC.CA: score=20.0 buy_ready=False sector_rank=13 price=314.99 support=300.0 resistance=380.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=40.56 liquidity=8646869.0 spike=0.68
- MPCI.CA: score=21.36 buy_ready=True sector_rank=13 price=417.48 support=345.0 resistance=490.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=69.19 liquidity=34651340.0 spike=0.19
- MPCO.CA: score=14.26 buy_ready=False sector_rank=8 price=2.59 support=2.29 resistance=2.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=564572608.0 spike=5.17
- MPRC.CA: score=18.36 buy_ready=False sector_rank=13 price=39.5 support=39.5 resistance=51.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=43.82 liquidity=35813816.0 spike=0.86
- MTIE.CA: score=19.3 buy_ready=False sector_rank=19 price=8.52 support=8.25 resistance=10.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=50.7 liquidity=10176901.0 spike=0.17
- NAHO.CA: score=6.37 buy_ready=False sector_rank=13 price=0.14 support=0.1 resistance=0.16 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT RSI=28.57 liquidity=16892.15 spike=0.16
- NCCW.CA: score=13.36 buy_ready=False sector_rank=13 price=7.56 support=6.92 resistance=7.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=141560992.0 spike=3.5
- NEDA.CA: score=16.18 buy_ready=False sector_rank=13 price=2.78 support=2.7 resistance=2.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:52 PM market time freshness=DELAYED_CURRENT RSI=45.83 liquidity=826517.38 spike=0.87
- NHPS.CA: score=15.11 buy_ready=False sector_rank=13 price=82.21 support=82.1 resistance=98.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=37.18 liquidity=6753386.0 spike=0.22
- NINH.CA: score=20.53 buy_ready=False sector_rank=13 price=22.82 support=21.53 resistance=26.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=56.24 liquidity=9169984.0 spike=0.29
- NIPH.CA: score=20.98 buy_ready=False sector_rank=15 price=334.84 support=326.51 resistance=450.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=48.44 liquidity=107915344.0 spike=0.36
- OBRI.CA: score=18.55 buy_ready=False sector_rank=13 price=32.57 support=31.81 resistance=34.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=55.04 liquidity=9192786.0 spike=0.37
- OCDI.CA: score=21.56 buy_ready=False sector_rank=12 price=32.78 support=30.03 resistance=36.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=56.78 liquidity=29478778.0 spike=0.26
- OCPH.CA: score=10.94 buy_ready=False sector_rank=13 price=251.76 support=242.0 resistance=310.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=51.96 liquidity=1579229.88 spike=0.09
- ODIN.CA: score=12.92 buy_ready=False sector_rank=13 price=2.85 support=2.55 resistance=3.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=24.47 liquidity=6563864.5 spike=0.15
- OFH.CA: score=21.36 buy_ready=False sector_rank=13 price=1.08 support=0.86 resistance=1.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=72.01 liquidity=46996972.0 spike=0.39
- OIH.CA: score=28.4 buy_ready=False sector_rank=2 price=2.16 support=1.71 resistance=2.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=71.67 liquidity=63416988.0 spike=0.41
- OLFI.CA: score=18.6 buy_ready=False sector_rank=11 price=22.51 support=22.07 resistance=26.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=40.49 liquidity=11918257.0 spike=0.24
- ORAS.CA: score=7.6 buy_ready=False sector_rank=18 price=867.61 support=860.01 resistance=873.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=103797392.0 spike=1.0
- ORHD.CA: score=25.16 buy_ready=True sector_rank=12 price=42.98 support=40.28 resistance=43.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=56.96 liquidity=219789168.0 spike=1.8
- ORWE.CA: score=25.4 buy_ready=True sector_rank=3 price=27.9 support=24.5 resistance=29.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=65.59 liquidity=20648692.0 spike=0.3
- PHAR.CA: score=20.98 buy_ready=False sector_rank=15 price=125.84 support=124.5 resistance=157.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=46.53 liquidity=44055936.0 spike=0.14
- PHDC.CA: score=18.56 buy_ready=False sector_rank=12 price=14.5 support=14.4 resistance=16.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=36.15 liquidity=95526688.0 spike=0.45
- PHTV.CA: score=8.73 buy_ready=False sector_rank=13 price=356.05 support=311.27 resistance=420.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:27 PM market time freshness=DELAYED_CURRENT RSI=30.92 liquidity=2275112.75 spike=1.05
- POUL.CA: score=28.6 buy_ready=True sector_rank=11 price=39.99 support=36.97 resistance=40.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:56 PM market time freshness=DELAYED_CURRENT RSI=65.19 liquidity=75849656.0 spike=3.92
- PRCL.CA: score=10.89 buy_ready=False sector_rank=16 price=31.98 support=30.9 resistance=36.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:56 PM market time freshness=DELAYED_CURRENT RSI=42.48 liquidity=2985913.0 spike=0.13
- PRDC.CA: score=18.56 buy_ready=False sector_rank=12 price=8.22 support=8.28 resistance=10.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=38.48 liquidity=27369560.0 spike=0.4
- PRMH.CA: score=13.16 buy_ready=False sector_rank=13 price=2.73 support=2.28 resistance=2.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:48 PM market time freshness=DELAYED_CURRENT RSI=75.34 liquidity=2806438.5 spike=0.19
- RACC.CA: score=17.79 buy_ready=False sector_rank=13 price=9.88 support=9.4 resistance=10.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=45.37 liquidity=7438174.5 spike=0.3
- RAKT.CA: score=12.43 buy_ready=False sector_rank=13 price=22.7 support=21.4 resistance=23.99 source=Yahoo Finance as_of=2026-09-08T21:00:00+00:00 freshness=FRESH RSI=65.31 liquidity=78133.4 spike=0.3
- RAYA.CA: score=18.86 buy_ready=False sector_rank=20 price=7.16 support=6.95 resistance=7.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=54.36 liquidity=14608274.0 spike=0.22
- RMDA.CA: score=22.98 buy_ready=True sector_rank=15 price=6.23 support=5.77 resistance=6.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=57.89 liquidity=14452148.0 spike=0.18
- ROTO.CA: score=6.66 buy_ready=False sector_rank=13 price=42.73 support=42.85 resistance=52.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=14.07 liquidity=3299603.25 spike=0.18
- RREI.CA: score=11.16 buy_ready=False sector_rank=13 price=4.29 support=4.24 resistance=5.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=30.95 liquidity=4799568.0 spike=0.15
- RTVC.CA: score=13.28 buy_ready=False sector_rank=13 price=3.99 support=3.76 resistance=4.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT RSI=39.29 liquidity=1924891.75 spike=0.25
- RUBX.CA: score=25.36 buy_ready=True sector_rank=13 price=12.87 support=12.2 resistance=13.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=61.82 liquidity=16697576.0 spike=0.8
- SAUD.CA: score=17.55 buy_ready=False sector_rank=9 price=23.38 support=22.8 resistance=24.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:56 PM market time freshness=DELAYED_CURRENT RSI=36.27 liquidity=5323134.5 spike=0.29
- SCEM.CA: score=22.9 buy_ready=True sector_rank=16 price=99.62 support=90.6 resistance=113.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=50.22 liquidity=38977944.0 spike=0.18
- SCFM.CA: score=14.93 buy_ready=False sector_rank=13 price=275.99 support=270.55 resistance=305.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=49.69 liquidity=3570816.5 spike=0.29
- SCTS.CA: score=15.9 buy_ready=True sector_rank=6 price=621.98 support=610.0 resistance=660.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=41.79 liquidity=1557187.88 spike=0.17
- SDTI.CA: score=23.22 buy_ready=True sector_rank=13 price=71.95 support=67.0 resistance=76.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=61.43 liquidity=9868766.0 spike=0.47
- SEIG.CA: score=11.9 buy_ready=False sector_rank=13 price=252.74 support=252.5 resistance=293.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=36.54 liquidity=545457.94 spike=0.2
- SIPC.CA: score=23.36 buy_ready=False sector_rank=13 price=5.93 support=4.1 resistance=6.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=70.68 liquidity=34187988.0 spike=0.62
- SKPC.CA: score=26.4 buy_ready=True sector_rank=4 price=18.5 support=16.5 resistance=19.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=63.01 liquidity=71692048.0 spike=0.53
- SMFR.CA: score=17.78 buy_ready=False sector_rank=13 price=250.22 support=247.0 resistance=279.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:56 PM market time freshness=DELAYED_CURRENT RSI=37.23 liquidity=6422396.5 spike=0.25
- SNFC.CA: score=18.71 buy_ready=False sector_rank=13 price=10.85 support=10.26 resistance=11.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=42.57 liquidity=6356256.5 spike=0.43
- SPIN.CA: score=22.6 buy_ready=False sector_rank=3 price=18.42 support=15.32 resistance=21.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=51.21 liquidity=9200820.0 spike=0.25
- SPMD.CA: score=17.55 buy_ready=False sector_rank=13 price=0.44 support=0.44 resistance=0.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=43.88 liquidity=9191925.0 spike=0.75
- SUGR.CA: score=23.6 buy_ready=False sector_rank=11 price=62.65 support=48.61 resistance=64.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=72.1 liquidity=13438614.0 spike=0.19
- SVCE.CA: score=23.36 buy_ready=False sector_rank=13 price=12.4 support=10.28 resistance=13.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:00 PM market time freshness=DELAYED_CURRENT RSI=73.8 liquidity=156661792.0 spike=0.76
- SWDY.CA: score=22.21 buy_ready=False sector_rank=10 price=129.58 support=106.8 resistance=139.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=70.18 liquidity=91561424.0 spike=0.9
- TALM.CA: score=17.34 buy_ready=False sector_rank=6 price=18.05 support=17.11 resistance=20.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=34.13 liquidity=13582718.0 spike=0.54
- TMGH.CA: score=25.56 buy_ready=True sector_rank=12 price=99.51 support=94.9 resistance=100.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=58.36 liquidity=157659456.0 spike=0.56
- TRTO.CA: score=-1.63 buy_ready=False sector_rank=13 price=0.07 support=0.07 resistance=0.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=14254.29 spike=0.47
- UEFM.CA: score=8.94 buy_ready=False sector_rank=13 price=523.87 support=440.66 resistance=589.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:56 PM market time freshness=DELAYED_CURRENT RSI=43.47 liquidity=586244.38 spike=0.14
- UEGC.CA: score=10.7 buy_ready=False sector_rank=13 price=1.73 support=1.66 resistance=2.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:00 PM market time freshness=DELAYED_CURRENT RSI=30.59 liquidity=7344870.5 spike=0.16
- UNIP.CA: score=23.36 buy_ready=False sector_rank=13 price=0.38 support=0.35 resistance=0.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=57.94 liquidity=26306968.0 spike=0.74
- UNIT.CA: score=12.18 buy_ready=False sector_rank=12 price=18.51 support=18.11 resistance=23.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:50 PM market time freshness=DELAYED_CURRENT RSI=46.26 liquidity=624126.56 spike=0.07
- WCDF.CA: score=14.07 buy_ready=False sector_rank=13 price=692.74 support=619.99 resistance=729.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=76.51 liquidity=1712002.0 spike=0.43
- WKOL.CA: score=18.57 buy_ready=False sector_rank=13 price=340.03 support=321.01 resistance=390.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:00 PM market time freshness=DELAYED_CURRENT RSI=58.44 liquidity=7212927.5 spike=0.32
- ZEOT.CA: score=14.83 buy_ready=True sector_rank=13 price=13.91 support=12.73 resistance=14.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:52 PM market time freshness=DELAYED_CURRENT RSI=54.66 liquidity=1469843.13 spike=0.1
- ZMID.CA: score=20.56 buy_ready=False sector_rank=12 price=9.65 support=7.39 resistance=9.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=76.16 liquidity=67871096.0 spike=0.27

## Backtesting Lite
- EFIC.CA: 180d return=-4.44%, max drawdown=-20.44%, MA20>MA50 days last20=19, as_of=2026-09-08T21:00:00+00:00
- EASB.CA: 180d return=140.22%, max drawdown=-25.2%, MA20>MA50 days last20=10, as_of=2026-09-08T21:00:00+00:00
- ETEL.CA: 180d return=103.17%, max drawdown=-30.44%, MA20>MA50 days last20=20, as_of=2026-09-08T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- EFIC.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=617 sources=3 expected=Egyptian Financial and Industrial summary=EFIC’s consolidated profits near EGP 820m in 2025; dividends proposed; EFIC ordered to pay over EGP 126m as penalties; EFIC generates lower consolidated net profits at EGP 803m in 9M-25; net sales near EGP 8bn
  - EFIC’s consolidated profits near EGP 820m in 2025; dividends proposed: https://english.mubasher.info/news/4579891/EFIC-s-consolidated-profits-near-EGP-820m-in-2025-dividends-proposed/
  - EFIC ordered to pay over EGP 126m as penalties: https://english.mubasher.info/news/4535935/EFIC-ordered-to-pay-over-EGP-126m-as-penalties/
  - EFIC generates lower consolidated net profits at EGP 803m in 9M-25; net sales near EGP 8bn: https://english.mubasher.info/news/4528902/EFIC-generates-lower-consolidated-net-profits-at-EGP-803m-in-9M-25-net-sales-near-EGP-8bn/
- EASB.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Egyptian Arabian Company (Themar) for securities Brokerage EAC summary=Evidence rejected for EASB.CA: source text did not clearly match EASB.CA / Egyptian Arabian Company (Themar) for securities Brokerage EAC.
- ETEL.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Telecom Egypt summary=Evidence rejected for ETEL.CA: source text did not clearly match ETEL.CA / Telecom Egypt.
- POUL.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Cairo Poultry summary=Cairo Poultry stock approaching historic peak – Analysis; Cairo Poultry cancels commercial license in Dubai&#39;s JAFZA; Cairo Poultry sees EGP 871m block-trading deal
  - Cairo Poultry stock approaching historic peak – Analysis: https://english.mubasher.info/news/4539104/Cairo-Poultry-stock-approaching-historic-peak-Analysis/
  - Cairo Poultry cancels commercial license in Dubai&#39;s JAFZA: https://english.mubasher.info/news/3962334/Cairo-Poultry-cancels-commercial-license-in-Dubai-s-JAFZA/
  - Cairo Poultry sees EGP 871m block-trading deal: https://english.mubasher.info/news/3862165/Cairo-Poultry-sees-EGP-871m-block-trading-deal/
- OIH.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Orascom Investment Holding summary=Evidence rejected for OIH.CA: source text did not clearly match OIH.CA / Orascom Investment Holding.
- CCAP.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Qalaa Holdings summary=Evidence rejected for CCAP.CA: source text did not clearly match CCAP.CA / Qalaa Holdings.
- FWRY.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Fawry For Banking Technology and Electronic Payments summary=Evidence rejected for FWRY.CA: source text did not clearly match FWRY.CA / Fawry For Banking Technology and Electronic Payments.
- SKPC.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Sidi Kerir Petrochemicals summary=Evidence rejected for SKPC.CA: source text did not clearly match SKPC.CA / Sidi Kerir Petrochemicals.

## Warnings
- Evidence for EFIC.CA matches the company but appears old; latest detected date is 2025-01-01.
- Gemini batch evidence failed: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.', 'status': 'UNAVAILABLE'}}
- Evidence rejected for EASB.CA: source text did not clearly match EASB.CA / Egyptian Arabian Company (Themar) for securities Brokerage EAC.
- Evidence rejected for ETEL.CA: source text did not clearly match ETEL.CA / Telecom Egypt.
- Evidence for POUL.CA matches the company but no source/report date was detected.
- Evidence rejected for OIH.CA: source text did not clearly match OIH.CA / Orascom Investment Holding.
- Evidence rejected for CCAP.CA: source text did not clearly match CCAP.CA / Qalaa Holdings.
- Evidence rejected for FWRY.CA: source text did not clearly match FWRY.CA / Fawry For Banking Technology and Electronic Payments.
- Evidence rejected for SKPC.CA: source text did not clearly match SKPC.CA / Sidi Kerir Petrochemicals.
