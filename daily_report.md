# Telegram-First EGX Scanner Report

Scan phase: Pre-market risk check
Generated UTC: 2026-08-12T07:01:18.602094+00:00
Generated Cairo: 2026-08-12 10:01
Run timing: target 08:45 Cairo | generated Cairo 2026-08-12 10:01 | cron 45 5 * * 0-4
Trigger: scheduled cron=45 5 * * 0-4 mapped to pre_market; Cairo now 2026-08-12 09:56

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 52
- Data quality issues: 1
- Tradeable price/liquidity tickers: 123/189
- Top sector: Tourism & Leisure

## Market Context
- Market trend: Bearish
- Source: Mubasher EGX market page (delayed public data)
- As of: Tuesday, August 11
- Freshness: DELAYED
- EGX30 regime: BULLISH / above MA20 77.78% / above MA50 66.67%
- EGX70 regime: BULLISH / above MA20 77.78% / above MA50 92.59%
- Sector breadth: 52.38%
- Risk mode: SELECTIVE_SWING_TRADES_ONLY

## Top Liquidity
- PHAR.CA: liquidity=1301346176.0 spike=4.8 score=14.4
- COMI.CA: liquidity=882964672.0 spike=2.12 score=26.64
- NIPH.CA: liquidity=690497728.0 spike=3.29 score=13.98
- SVCE.CA: liquidity=670879296.0 spike=18.62 score=13.59
- SCEM.CA: liquidity=626882304.0 spike=6.07 score=16.4

## AI Narrative
- Provider: OpenRouter OK
- Model: nvidia/nemotron-3-super-120b-a12b:free
- Summary: EGX30 and EGX70 are bullish with solid breadth, but the scanner found no ticket satisfying evidence, liquidity freshness and technical gates, resulting in a fallback HOLD stance.
- No ticket cleared the evidence/freshness/liquidity/technical filters, so the scanner defaults to HOLD.
- Liquidity shows accumulation spikes in several stocks, but most are in non‑leading sectors and show overheated RSI or proximity to resistance.
- Sector breadth is ~52% with Tourism & Leisure, Building Materials and Industrial Goods leading; however, top‑scored tickets lie outside these sectors, reducing confidence.
- With EGX30/EGX70 bullish, risk mode is set to SELECTIVE_SWING_TRADES_ONLY, meaning only high‑conviction setups are allowed; current uncertainty keeps exposure low.

## Top Liquidity Spikes
- SVCE.CA: spike=18.62 liquidity=670879296.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- ALUM.CA: spike=15.8 liquidity=114896160.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- ECAP.CA: spike=14.46 liquidity=87733880.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- MBSC.CA: spike=13.23 liquidity=276629728.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- EGAL.CA: spike=11.62 liquidity=481864160.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False

## Sector Leaderboard
- #1 Tourism & Leisure: score=17.22 5d=0.0% 20d=0.0% aboveMA50=0.0%
- #2 Building Materials: score=11.84 5d=0.0% 20d=0.0% aboveMA50=33.33%
- #3 Industrial Goods & Cables: score=10.87 5d=5.99% 20d=10.73% aboveMA50=100.0%
- #4 Automotive & Distribution: score=10.78 5d=5.64% 20d=5.58% aboveMA50=100.0%
- #5 Textiles: score=9.68 5d=3.27% 20d=11.43% aboveMA50=75.0%
- #6 Energy & Petrochemicals: score=8.67 5d=0.0% 20d=15.88% aboveMA50=75.0%
- #7 Food, Beverages & Tobacco: score=8.05 5d=4.43% 20d=2.01% aboveMA50=71.43%
- #8 Banking & Financials: score=7.71 5d=1.52% 20d=3.88% aboveMA50=80.0%

## Today's Prioritized Action Tickets
- HOLD: Local fallback HOLD: no candidate passed evidence, liquidity, freshness, and technical gates.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- EALR.CA: BULLISH_WATCH score=91.98 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- WKOL.CA: BULLISH_WATCH score=91.98 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- LCSW.CA: BULLISH_WATCH score=90 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- FAIT.CA: BULLISH_WATCH score=89.71 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended; sector is not leading
- MIPH.CA: BULLISH_WATCH score=89.29 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- SUGR.CA: BULLISH_WATCH score=89.05 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=close to resistance
- ACAMD.CA: BULLISH_WATCH score=87.98 liquidity=TRADEABLE sector=IMPROVING risk=sector is not leading
- GBCO.CA: BULLISH_WATCH score=86 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- CLHO.CA: BULLISH_WATCH score=83.29 liquidity=TRADEABLE sector=IMPROVING risk=sector is not leading
- EFIH.CA: BULLISH_WATCH score=82.14 liquidity=TRADEABLE sector=IMPROVING risk=sector is not leading

## BUY-Ready Candidates
- EALR.CA: rank=29.31 outlook=BULLISH_WATCH outlook_score=91.98 sector_rank=19 price=385.11 support=360.0 resistance=432.0 liquidity=83727496.0
- CNFN.CA: rank=28.4 outlook=BULLISH_WATCH outlook_score=71.24 sector_rank=11 price=4.93 support=4.68 resistance=5.05 liquidity=15766259.0
- SUGR.CA: rank=28.14 outlook=BULLISH_WATCH outlook_score=89.05 sector_rank=7 price=48.58 support=46.47 resistance=49.25 liquidity=16636489.0
- SAUD.CA: rank=27.58 outlook=BULLISH_WATCH outlook_score=75.71 sector_rank=8 price=22.49 support=21.25 resistance=22.8 liquidity=21921074.0
- MAAL.CA: rank=27.41 outlook=BULLISH_WATCH outlook_score=79.98 sector_rank=19 price=8.98 support=8.1 resistance=9.1 liquidity=44591100.0
- EFIH.CA: rank=27.24 outlook=BULLISH_WATCH outlook_score=82.14 sector_rank=12 price=23.56 support=21.87 resistance=25.0 liquidity=127992264.0
- CIEB.CA: rank=27.22 outlook=BULLISH_WATCH outlook_score=79.71 sector_rank=8 price=24.48 support=23.75 resistance=24.7 liquidity=8820973.0
- WKOL.CA: rank=26.97 outlook=BULLISH_WATCH outlook_score=91.98 sector_rank=19 price=330.29 support=307.0 resistance=363.56 liquidity=53026028.0
- COMI.CA: rank=26.64 outlook=BULLISH_WATCH outlook_score=81.71 sector_rank=8 price=139.09 support=132.81 resistance=142.88 liquidity=882964672.0
- PRMH.CA: rank=26.53 outlook=CONSTRUCTIVE outlook_score=67.98 sector_rank=19 price=2.85 support=2.56 resistance=2.86 liquidity=25519266.0

## Data Quality Issues
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=25.99 buy_ready=True sector_rank=19 price=297.28 support=225.1 resistance=317.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:26 PM market time freshness=DELAYED_CURRENT RSI=67.18 liquidity=79844040.0 spike=2.2
- ABUK.CA: score=26.16 buy_ready=True sector_rank=14 price=74.7 support=69.01 resistance=75.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=56.27 liquidity=92140896.0 spike=0.62
- ACAMD.CA: score=25.63 buy_ready=True sector_rank=19 price=2.28 support=2.19 resistance=2.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=59.95 liquidity=63616532.0 spike=1.02
- ACGC.CA: score=23.4 buy_ready=False sector_rank=5 price=11.71 support=9.75 resistance=11.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:26 PM market time freshness=DELAYED_CURRENT RSI=80.15 liquidity=31270374.0 spike=0.96
- ADCI.CA: score=12.83 buy_ready=False sector_rank=19 price=318.41 support=310.01 resistance=389.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=59532128.0 spike=3.12
- ADIB.CA: score=21.4 buy_ready=False sector_rank=8 price=53.51 support=46.02 resistance=53.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=81.93 liquidity=74982056.0 spike=0.63
- ADPC.CA: score=8.59 buy_ready=False sector_rank=19 price=4.38 support=4.36 resistance=4.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=45668536.0 spike=0.93
- AFDI.CA: score=9.01 buy_ready=False sector_rank=19 price=66.85 support=63.25 resistance=68.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=29293628.0 spike=1.21
- AFMC.CA: score=8.81 buy_ready=False sector_rank=19 price=250.0 support=201.0 resistance=255.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=154226112.0 spike=1.11
- AJWA.CA: score=21.59 buy_ready=False sector_rank=19 price=187.05 support=161.0 resistance=210.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=71.59 liquidity=12758423.0 spike=0.35
- ALCN.CA: score=25.92 buy_ready=True sector_rank=16 price=31.04 support=28.8 resistance=31.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=62.2 liquidity=16855424.0 spike=0.58
- ALUM.CA: score=13.59 buy_ready=False sector_rank=19 price=28.75 support=25.5 resistance=29.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=114896160.0 spike=15.8
- AMER.CA: score=8.72 buy_ready=False sector_rank=18 price=7.13 support=6.49 resistance=7.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=107677072.0 spike=0.94
- AMES.CA: score=23.59 buy_ready=True sector_rank=19 price=121.63 support=83.13 resistance=144.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=51.49 liquidity=52479328.0 spike=0.54
- AMIA.CA: score=23.59 buy_ready=False sector_rank=19 price=12.65 support=8.74 resistance=13.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=73.79 liquidity=16068854.0 spike=0.96
- AMOC.CA: score=24.58 buy_ready=True sector_rank=6 price=9.45 support=8.03 resistance=9.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=67.52 liquidity=106419072.0 spike=1.09
- APSW.CA: score=8.7 buy_ready=False sector_rank=19 price=8.69 support=8.1 resistance=9.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=37.2 liquidity=1103803.0 spike=0.6
- ARAB.CA: score=21.72 buy_ready=False sector_rank=18 price=0.24 support=0.23 resistance=0.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=52.83 liquidity=67122408.0 spike=0.53
- ARCC.CA: score=16.4 buy_ready=False sector_rank=2 price=76.44 support=63.7 resistance=76.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=341577952.0 spike=9.59
- AREH.CA: score=20.59 buy_ready=False sector_rank=19 price=1.51 support=1.38 resistance=1.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=54.0 liquidity=21161336.0 spike=0.53
- ARVA.CA: score=4.59 buy_ready=False sector_rank=19 price=12.35 support=12.35 resistance=12.35 source=Yahoo Finance as_of=2026-08-09T21:00:00+00:00 freshness=FRESH RSI=86.59 liquidity=0.0 spike=0.0
- ASCM.CA: score=23.95 buy_ready=False sector_rank=19 price=66.15 support=60.1 resistance=69.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=74.57 liquidity=75365696.0 spike=1.18
- ASPI.CA: score=9.73 buy_ready=False sector_rank=19 price=0.5 support=0.48 resistance=0.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=66521408.0 spike=1.57
- ATLC.CA: score=12.62 buy_ready=False sector_rank=11 price=5.72 support=5.47 resistance=5.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=37346196.0 spike=2.61
- ATQA.CA: score=14.16 buy_ready=False sector_rank=14 price=10.88 support=10.8 resistance=11.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=292825280.0 spike=7.5
- AXPH.CA: score=12.37 buy_ready=False sector_rank=19 price=1343.56 support=1325.0 resistance=1460.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=11794911.0 spike=2.89
- BINV.CA: score=18.82 buy_ready=True sector_rank=13 price=48.76 support=46.01 resistance=50.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:12 PM market time freshness=DELAYED_CURRENT RSI=49.28 liquidity=2585990.5 spike=0.36
- BIOC.CA: score=10.57 buy_ready=False sector_rank=19 price=555.0 support=525.0 resistance=609.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=331488384.0 spike=1.99
- BTFH.CA: score=24.42 buy_ready=False sector_rank=11 price=3.09 support=3.03 resistance=3.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=60.0 liquidity=229836048.0 spike=1.01
- CAED.CA: score=23.59 buy_ready=True sector_rank=19 price=121.01 support=73.7 resistance=143.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=50.78 liquidity=15185579.0 spike=0.21
- CANA.CA: score=24.4 buy_ready=False sector_rank=8 price=39.98 support=35.2 resistance=39.63 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=71.11 liquidity=15045022.0 spike=0.77
- CCAP.CA: score=19.23 buy_ready=False sector_rank=13 price=5.22 support=5.14 resistance=5.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=43.01 liquidity=282676800.0 spike=0.44
- CCRS.CA: score=17.29 buy_ready=False sector_rank=19 price=2.54 support=2.42 resistance=2.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=21.95 liquidity=26318026.0 spike=1.35
- CEFM.CA: score=25.59 buy_ready=True sector_rank=19 price=135.36 support=101.57 resistance=152.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=48.18 liquidity=11237273.0 spike=0.35
- CERA.CA: score=21.77 buy_ready=False sector_rank=19 price=1.33 support=1.25 resistance=1.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=43.48 liquidity=24544218.0 spike=1.09
- CFGH.CA: score=7.59 buy_ready=False sector_rank=19 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance as_of=2026-08-09T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- CICH.CA: score=13.74 buy_ready=False sector_rank=11 price=12.37 support=11.66 resistance=13.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:11 PM market time freshness=DELAYED_CURRENT RSI=79.45 liquidity=4335278.0 spike=0.53
- CIEB.CA: score=27.22 buy_ready=True sector_rank=8 price=24.48 support=23.75 resistance=24.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=58.13 liquidity=8820973.0 spike=0.85
- CIRA.CA: score=8.95 buy_ready=False sector_rank=15 price=38.98 support=38.06 resistance=39.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=19966438.0 spike=0.34
- CLHO.CA: score=26.4 buy_ready=True sector_rank=10 price=17.7 support=15.98 resistance=19.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=57.66 liquidity=40056432.0 spike=0.81
- CNFN.CA: score=28.4 buy_ready=True sector_rank=11 price=4.93 support=4.68 resistance=5.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=63.04 liquidity=15766259.0 spike=0.74
- COMI.CA: score=26.64 buy_ready=True sector_rank=8 price=139.09 support=132.81 resistance=142.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=63.86 liquidity=882964672.0 spike=2.12
- COPR.CA: score=23.59 buy_ready=True sector_rank=19 price=0.41 support=0.36 resistance=0.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=60.2 liquidity=16802392.0 spike=0.52
- COSG.CA: score=23.59 buy_ready=True sector_rank=19 price=1.7 support=1.6 resistance=1.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=51.52 liquidity=28904894.0 spike=0.74
- CPCI.CA: score=11.27 buy_ready=False sector_rank=19 price=552.62 support=531.2 resistance=644.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=31291784.0 spike=2.34
- CSAG.CA: score=9.22 buy_ready=False sector_rank=16 price=40.0 support=38.8 resistance=40.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=23957704.0 spike=1.15
- DAPH.CA: score=13.59 buy_ready=False sector_rank=19 price=134.4 support=130.0 resistance=147.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=226105376.0 spike=8.92
- DEIN.CA: score=-1.41 buy_ready=False sector_rank=19 price=11.38 support=13.65 resistance=13.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 June 12:11 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=40.95 spike=0.01
- DOMT.CA: score=25.08 buy_ready=False sector_rank=7 price=28.0 support=26.01 resistance=32.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=71.14 liquidity=14926224.0 spike=1.34
- DSCW.CA: score=26.31 buy_ready=False sector_rank=19 price=2.13 support=1.81 resistance=2.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=70.97 liquidity=109652880.0 spike=1.36
- DTPP.CA: score=10.51 buy_ready=False sector_rank=19 price=311.84 support=295.0 resistance=325.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=114953656.0 spike=1.96
- EALR.CA: score=29.31 buy_ready=True sector_rank=19 price=385.11 support=360.0 resistance=432.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=50.62 liquidity=83727496.0 spike=2.86
- EASB.CA: score=14.87 buy_ready=False sector_rank=19 price=7.19 support=6.71 resistance=8.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=43.0 liquidity=3277292.75 spike=0.28
- EAST.CA: score=20.4 buy_ready=False sector_rank=7 price=36.2 support=36.01 resistance=37.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=47.12 liquidity=39335596.0 spike=0.58
- EBSC.CA: score=19.15 buy_ready=False sector_rank=19 price=1.92 support=1.85 resistance=2.06 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=72.0 liquidity=3555142.0 spike=0.54
- ECAP.CA: score=13.59 buy_ready=False sector_rank=19 price=40.7 support=38.11 resistance=43.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=87733880.0 spike=14.46
- EDFM.CA: score=14.92 buy_ready=True sector_rank=19 price=398.48 support=340.03 resistance=430.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:09 PM market time freshness=DELAYED_CURRENT RSI=57.93 liquidity=1330111.88 spike=0.23
- EEII.CA: score=11.49 buy_ready=False sector_rank=19 price=2.97 support=2.95 resistance=3.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=34529560.0 spike=2.45
- EFIC.CA: score=26.98 buy_ready=False sector_rank=14 price=210.28 support=183.05 resistance=225.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=71.45 liquidity=35855716.0 spike=1.41
- EFID.CA: score=23.4 buy_ready=False sector_rank=7 price=31.21 support=26.64 resistance=32.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:26 PM market time freshness=DELAYED_CURRENT RSI=83.8 liquidity=42293672.0 spike=0.51
- EFIH.CA: score=27.24 buy_ready=True sector_rank=12 price=23.56 support=21.87 resistance=25.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=61.82 liquidity=127992264.0 spike=1.42
- EGAL.CA: score=14.16 buy_ready=False sector_rank=14 price=326.41 support=303.26 resistance=338.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=481864160.0 spike=11.62
- EGAS.CA: score=25.94 buy_ready=False sector_rank=6 price=60.06 support=50.0 resistance=67.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=74.42 liquidity=45335220.0 spike=1.77
- EGBE.CA: score=14.31 buy_ready=False sector_rank=8 price=0.56 support=0.44 resistance=0.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:14 PM market time freshness=DELAYED_CURRENT RSI=78.63 liquidity=269145.12 spike=2.32
- EGCH.CA: score=24.16 buy_ready=True sector_rank=14 price=14.1 support=12.69 resistance=14.62 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=67.45 liquidity=88726304.0 spike=0.88
- EGSA.CA: score=3.73 buy_ready=False sector_rank=17 price=8.8 support=8.8 resistance=9.21 source=Yahoo Finance as_of=2026-08-09T21:00:00+00:00 freshness=FRESH RSI=18.75 liquidity=0.0 spike=0.0
- EGTS.CA: score=13.26 buy_ready=False sector_rank=18 price=19.26 support=18.2 resistance=19.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=120017648.0 spike=3.27
- EHDR.CA: score=13.33 buy_ready=False sector_rank=19 price=3.05 support=2.94 resistance=3.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=139481840.0 spike=3.37
- EKHO.CA: score=8.4 buy_ready=False sector_rank=6 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-08-09T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=17.4 buy_ready=False sector_rank=3 price=2.17 support=2.12 resistance=2.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=33.33 liquidity=71634408.0 spike=0.9
- ELKA.CA: score=17.29 buy_ready=False sector_rank=19 price=1.73 support=1.59 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=15.87 liquidity=110025480.0 spike=1.35
- ELNA.CA: score=2.59 buy_ready=False sector_rank=19 price=37.44 support=36.5 resistance=39.93 source=Yahoo Finance as_of=2026-08-09T21:00:00+00:00 freshness=FRESH RSI=30.65 liquidity=0.0 spike=0.0
- ELSH.CA: score=21.59 buy_ready=False sector_rank=19 price=14.03 support=13.31 resistance=15.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=48.7 liquidity=41384660.0 spike=0.35
- ELWA.CA: score=5.08 buy_ready=False sector_rank=19 price=1.74 support=1.65 resistance=2.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:26 PM market time freshness=DELAYED_CURRENT RSI=8.33 liquidity=1485130.5 spike=0.96
- EMFD.CA: score=26.02 buy_ready=True sector_rank=18 price=11.89 support=11.08 resistance=12.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=54.92 liquidity=67069964.0 spike=1.15
- ENGC.CA: score=10.01 buy_ready=False sector_rank=19 price=50.0 support=45.95 resistance=50.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=56434428.0 spike=1.71
- EOSB.CA: score=17.59 buy_ready=False sector_rank=19 price=1.55 support=1.53 resistance=1.62 source=Yahoo Finance as_of=2026-08-09T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- EPCO.CA: score=8.59 buy_ready=False sector_rank=19 price=12.67 support=12.45 resistance=13.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=32284810.0 spike=1.0
- EPPK.CA: score=10.54 buy_ready=False sector_rank=19 price=13.25 support=13.87 resistance=15.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:10 PM market time freshness=DELAYED_CURRENT RSI=41.67 liquidity=1192447.88 spike=1.38
- ETEL.CA: score=25.73 buy_ready=True sector_rank=17 price=109.15 support=96.0 resistance=114.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=64.16 liquidity=65827472.0 spike=0.66
- ETRS.CA: score=23.59 buy_ready=True sector_rank=19 price=10.68 support=10.21 resistance=10.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:26 PM market time freshness=DELAYED_CURRENT RSI=52.37 liquidity=20884082.0 spike=0.79
- EXPA.CA: score=24.4 buy_ready=False sector_rank=8 price=21.02 support=18.61 resistance=20.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=70.11 liquidity=27365608.0 spike=0.78
- FAIT.CA: score=25.63 buy_ready=True sector_rank=8 price=38.69 support=36.1 resistance=38.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:14 PM market time freshness=DELAYED_CURRENT RSI=62.5 liquidity=5506590.5 spike=1.86
- FAITA.CA: score=13.43 buy_ready=False sector_rank=8 price=0.98 support=0.96 resistance=0.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 12:49 PM market time freshness=DELAYED_CURRENT RSI=56.79 liquidity=31659.57 spike=0.76
- FERC.CA: score=12.9 buy_ready=False sector_rank=14 price=82.67 support=82.11 resistance=87.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=40538556.0 spike=2.87
- FWRY.CA: score=22.74 buy_ready=False sector_rank=12 price=18.75 support=18.43 resistance=19.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=51.0 liquidity=194061104.0 spike=1.67
- GBCO.CA: score=24.4 buy_ready=True sector_rank=4 price=32.0 support=29.53 resistance=34.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=42.16 liquidity=43767508.0 spike=0.67
- GDWA.CA: score=12.59 buy_ready=False sector_rank=19 price=0.81 support=0.8 resistance=0.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=20.43 liquidity=51781148.0 spike=0.43
- GGCC.CA: score=8.67 buy_ready=False sector_rank=19 price=1.18 support=1.16 resistance=1.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=46239596.0 spike=1.04
- GIHD.CA: score=8.59 buy_ready=False sector_rank=19 price=67.31 support=60.66 resistance=73.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=52008424.0 spike=0.93
- GMCI.CA: score=11.98 buy_ready=False sector_rank=19 price=1.96 support=1.91 resistance=2.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:12 PM market time freshness=DELAYED_CURRENT RSI=42.22 liquidity=390370.25 spike=0.42
- GRCA.CA: score=15.48 buy_ready=False sector_rank=19 price=57.08 support=48.74 resistance=68.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=32.16 liquidity=8885295.0 spike=0.49
- GSSC.CA: score=19.18 buy_ready=True sector_rank=19 price=274.63 support=258.15 resistance=300.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:13 PM market time freshness=DELAYED_CURRENT RSI=57.18 liquidity=5584248.5 spike=0.31
- GTWL.CA: score=9.39 buy_ready=False sector_rank=19 price=127.04 support=125.03 resistance=139.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=137106752.0 spike=1.4
- HDBK.CA: score=19.4 buy_ready=False sector_rank=8 price=85.15 support=76.9 resistance=85.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:26 PM market time freshness=DELAYED_CURRENT RSI=76.46 liquidity=14893044.0 spike=0.39
- HELI.CA: score=23.72 buy_ready=True sector_rank=18 price=8.32 support=7.28 resistance=8.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=53.44 liquidity=113152624.0 spike=0.57
- HRHO.CA: score=26.4 buy_ready=True sector_rank=11 price=27.2 support=25.95 resistance=28.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=60.26 liquidity=93556904.0 spike=0.96
- ICID.CA: score=10.81 buy_ready=False sector_rank=19 price=9.82 support=9.0 resistance=9.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:13 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=15540092.0 spike=2.11
- IDRE.CA: score=8.59 buy_ready=False sector_rank=19 price=57.31 support=55.51 resistance=57.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=21800358.0 spike=0.71
- IFAP.CA: score=22.32 buy_ready=False sector_rank=9 price=21.65 support=18.96 resistance=21.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=79.88 liquidity=28338324.0 spike=1.46
- INFI.CA: score=13.59 buy_ready=False sector_rank=19 price=168.49 support=164.0 resistance=178.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=154834240.0 spike=3.63
- IRON.CA: score=11.52 buy_ready=False sector_rank=14 price=31.33 support=30.61 resistance=32.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=17162358.0 spike=2.18
- ISMA.CA: score=13.59 buy_ready=False sector_rank=19 price=34.64 support=33.0 resistance=36.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=84696424.0 spike=3.52
- ISMQ.CA: score=11.54 buy_ready=False sector_rank=14 price=9.8 support=9.36 resistance=9.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=144236288.0 spike=2.19
- ISPH.CA: score=29.4 buy_ready=False sector_rank=10 price=14.01 support=11.2 resistance=16.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=71.87 liquidity=579868032.0 spike=3.83
- JUFO.CA: score=20.4 buy_ready=False sector_rank=7 price=26.21 support=22.78 resistance=36.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=45.58 liquidity=44894200.0 spike=0.87
- KABO.CA: score=9.94 buy_ready=False sector_rank=5 price=8.6 support=8.47 resistance=8.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=48547940.0 spike=1.27
- KWIN.CA: score=23.59 buy_ready=True sector_rank=19 price=90.1 support=68.07 resistance=111.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=36.99 liquidity=20579520.0 spike=0.35
- KZPC.CA: score=13.59 buy_ready=False sector_rank=19 price=9.64 support=9.0 resistance=9.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=48294776.0 spike=8.19
- LCSW.CA: score=26.4 buy_ready=True sector_rank=2 price=34.99 support=30.2 resistance=37.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=50.88 liquidity=37589728.0 spike=0.71
- LUTS.CA: score=13.59 buy_ready=False sector_rank=19 price=0.94 support=0.81 resistance=0.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=212667216.0 spike=4.81
- MAAL.CA: score=27.41 buy_ready=True sector_rank=19 price=8.98 support=8.1 resistance=9.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=61.11 liquidity=44591100.0 spike=2.91
- MASR.CA: score=10.51 buy_ready=False sector_rank=19 price=7.57 support=7.45 resistance=7.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=145776368.0 spike=1.96
- MBSC.CA: score=16.4 buy_ready=False sector_rank=2 price=318.01 support=265.51 resistance=318.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=276629728.0 spike=13.23
- MCQE.CA: score=16.4 buy_ready=False sector_rank=2 price=243.6 support=201.0 resistance=243.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=155604608.0 spike=7.71
- MCRO.CA: score=10.35 buy_ready=False sector_rank=19 price=1.58 support=1.57 resistance=1.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=331767264.0 spike=1.88
- MENA.CA: score=15.85 buy_ready=True sector_rank=18 price=7.1 support=6.83 resistance=7.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=39.13 liquidity=2130997.0 spike=0.57
- MEPA.CA: score=23.67 buy_ready=True sector_rank=19 price=1.92 support=1.64 resistance=2.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=56.92 liquidity=63314436.0 spike=1.04
- MFPC.CA: score=23.24 buy_ready=False sector_rank=14 price=37.65 support=35.37 resistance=38.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=38.52 liquidity=80746664.0 spike=1.04
- MFSC.CA: score=25.29 buy_ready=True sector_rank=19 price=48.97 support=45.7 resistance=65.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:13 PM market time freshness=DELAYED_CURRENT RSI=62.19 liquidity=9696447.0 spike=0.82
- MHOT.CA: score=17.4 buy_ready=False sector_rank=1 price=20.71 support=17.4 resistance=20.71 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=106867096.0 spike=11.48
- MICH.CA: score=8.59 buy_ready=False sector_rank=19 price=46.49 support=46.3 resistance=49.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=17538860.0 spike=0.55
- MILS.CA: score=26.15 buy_ready=True sector_rank=19 price=192.0 support=135.2 resistance=211.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=51.52 liquidity=78600608.0 spike=1.28
- MIPH.CA: score=24.98 buy_ready=True sector_rank=10 price=786.34 support=692.16 resistance=831.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=56.43 liquidity=7464019.5 spike=1.56
- MOED.CA: score=12.59 buy_ready=False sector_rank=19 price=0.68 support=0.65 resistance=0.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=15.94 liquidity=23727340.0 spike=0.79
- MOIL.CA: score=11.56 buy_ready=False sector_rank=6 price=0.68 support=0.52 resistance=0.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:26 PM market time freshness=DELAYED_CURRENT RSI=91.67 liquidity=157169.91 spike=0.24
- MOIN.CA: score=9.15 buy_ready=False sector_rank=19 price=34.92 support=34.7 resistance=36.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=28469270.0 spike=1.28
- MOSC.CA: score=25.59 buy_ready=False sector_rank=19 price=309.09 support=275.0 resistance=329.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=72.1 liquidity=12208779.0 spike=0.77
- MPCI.CA: score=12.73 buy_ready=False sector_rank=19 price=400.21 support=370.0 resistance=460.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=377620864.0 spike=3.07
- MPCO.CA: score=11.52 buy_ready=False sector_rank=9 price=2.21 support=2.08 resistance=2.23 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=188083232.0 spike=2.06
- MPRC.CA: score=13.49 buy_ready=False sector_rank=19 price=51.99 support=46.11 resistance=52.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=83591800.0 spike=3.45
- MTIE.CA: score=23.8 buy_ready=False sector_rank=4 price=11.2 support=9.3 resistance=11.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=86.38 liquidity=44307652.0 spike=1.2
- NAHO.CA: score=10.36 buy_ready=False sector_rank=19 price=0.1 support=0.1 resistance=0.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=66.67 liquidity=29069.07 spike=1.37
- NCCW.CA: score=8.59 buy_ready=False sector_rank=19 price=5.89 support=5.76 resistance=6.03 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=33187390.0 spike=0.93
- NEDA.CA: score=3.59 buy_ready=False sector_rank=19 price=2.7 support=2.7 resistance=3.02 source=Yahoo Finance as_of=2026-08-09T21:00:00+00:00 freshness=FRESH RSI=13.64 liquidity=0.0 spike=0.0
- NHPS.CA: score=8.59 buy_ready=False sector_rank=19 price=93.03 support=92.64 resistance=98.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=80409048.0 spike=0.99
- NINH.CA: score=23.59 buy_ready=True sector_rank=19 price=22.69 support=17.7 resistance=25.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=53.46 liquidity=29881612.0 spike=0.53
- NIPH.CA: score=13.98 buy_ready=False sector_rank=10 price=453.69 support=381.0 resistance=516.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=690497728.0 spike=3.29
- OBRI.CA: score=12.59 buy_ready=False sector_rank=19 price=33.01 support=31.61 resistance=37.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=12.04 liquidity=34981212.0 spike=0.96
- OCDI.CA: score=13.68 buy_ready=False sector_rank=18 price=34.9 support=30.8 resistance=36.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=369072576.0 spike=3.48
- OCPH.CA: score=12.49 buy_ready=False sector_rank=19 price=310.0 support=289.92 resistance=341.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=88493048.0 spike=2.95
- ODIN.CA: score=13.59 buy_ready=False sector_rank=19 price=3.69 support=3.3 resistance=3.92 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=214002688.0 spike=9.75
- OFH.CA: score=8.59 buy_ready=False sector_rank=19 price=0.89 support=0.86 resistance=0.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=72643920.0 spike=0.83
- OIH.CA: score=26.87 buy_ready=False sector_rank=13 price=1.69 support=1.41 resistance=1.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=82.76 liquidity=247178992.0 spike=2.82
- OLFI.CA: score=23.52 buy_ready=False sector_rank=7 price=23.8 support=22.25 resistance=26.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=79.62 liquidity=43003072.0 spike=1.06
- ORAS.CA: score=7.6 buy_ready=False sector_rank=20 price=717.23 support=711.02 resistance=723.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=109226968.0 spike=1.0
- ORHD.CA: score=22.72 buy_ready=False sector_rank=18 price=42.29 support=38.0 resistance=44.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=75.86 liquidity=102145504.0 spike=0.63
- ORWE.CA: score=21.7 buy_ready=False sector_rank=5 price=26.21 support=22.42 resistance=27.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=77.89 liquidity=73780552.0 spike=1.15
- PHAR.CA: score=14.4 buy_ready=False sector_rank=10 price=154.26 support=151.1 resistance=178.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=1301346176.0 spike=4.8
- PHDC.CA: score=23.72 buy_ready=True sector_rank=18 price=15.3 support=14.32 resistance=15.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=69.08 liquidity=172057168.0 spike=0.71
- PHTV.CA: score=6.05 buy_ready=False sector_rank=19 price=412.58 support=382.49 resistance=447.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=6242361.0 spike=1.61
- POUL.CA: score=24.7 buy_ready=True sector_rank=7 price=39.75 support=36.5 resistance=40.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=44.49 liquidity=35606380.0 spike=1.15
- PRCL.CA: score=24.4 buy_ready=False sector_rank=2 price=34.7 support=32.76 resistance=38.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=45.45 liquidity=25006110.0 spike=0.65
- PRDC.CA: score=21.72 buy_ready=False sector_rank=18 price=9.0 support=8.2 resistance=10.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=44.6 liquidity=50001936.0 spike=0.44
- PRMH.CA: score=26.53 buy_ready=True sector_rank=19 price=2.85 support=2.56 resistance=2.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=52.17 liquidity=25519266.0 spike=1.47
- RACC.CA: score=21.59 buy_ready=False sector_rank=19 price=10.13 support=9.8 resistance=10.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=51.02 liquidity=18177084.0 spike=0.83
- RAKT.CA: score=11.11 buy_ready=False sector_rank=19 price=23.02 support=21.66 resistance=23.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:14 PM market time freshness=DELAYED_CURRENT RSI=79.63 liquidity=474012.78 spike=1.52
- RAYA.CA: score=11.32 buy_ready=False sector_rank=21 price=7.27 support=7.3 resistance=8.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=31.25 liquidity=68503200.0 spike=0.62
- RMDA.CA: score=12.02 buy_ready=False sector_rank=10 price=6.65 support=6.61 resistance=7.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=222695360.0 spike=2.31
- ROTO.CA: score=10.97 buy_ready=False sector_rank=19 price=49.68 support=48.66 resistance=51.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=45903140.0 spike=2.19
- RREI.CA: score=23.59 buy_ready=True sector_rank=19 price=4.68 support=3.72 resistance=4.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=68.32 liquidity=63786512.0 spike=1.0
- RTVC.CA: score=7.2 buy_ready=False sector_rank=19 price=3.8 support=3.73 resistance=4.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=34.12 liquidity=3606858.5 spike=0.7
- RUBX.CA: score=16.17 buy_ready=False sector_rank=19 price=12.27 support=12.02 resistance=14.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=31.87 liquidity=9575595.0 spike=0.27
- SAUD.CA: score=27.58 buy_ready=True sector_rank=8 price=22.49 support=21.25 resistance=22.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=62.72 liquidity=21921074.0 spike=1.59
- SCEM.CA: score=16.4 buy_ready=False sector_rank=2 price=98.38 support=82.34 resistance=98.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=626882304.0 spike=6.07
- SCFM.CA: score=23.99 buy_ready=True sector_rank=19 price=286.49 support=250.12 resistance=319.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=39.78 liquidity=29215246.0 spike=1.2
- SCTS.CA: score=22.69 buy_ready=True sector_rank=15 price=616.99 support=602.0 resistance=685.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=46.64 liquidity=8656725.0 spike=1.04
- SDTI.CA: score=8.59 buy_ready=False sector_rank=19 price=73.41 support=71.99 resistance=75.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=22532350.0 spike=0.83
- SEIG.CA: score=15.06 buy_ready=False sector_rank=19 price=271.83 support=237.0 resistance=295.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:26 PM market time freshness=DELAYED_CURRENT RSI=86.15 liquidity=6466513.0 spike=0.34
- SIPC.CA: score=24.95 buy_ready=False sector_rank=19 price=4.82 support=3.45 resistance=5.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=73.18 liquidity=86697176.0 spike=1.68
- SKPC.CA: score=25.16 buy_ready=True sector_rank=14 price=16.58 support=14.8 resistance=16.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=68.45 liquidity=27054058.0 spike=0.6
- SMFR.CA: score=27.77 buy_ready=False sector_rank=19 price=264.65 support=202.61 resistance=282.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=74.2 liquidity=73170440.0 spike=2.09
- SNFC.CA: score=21.15 buy_ready=False sector_rank=19 price=10.81 support=10.7 resistance=11.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=39.78 liquidity=15295328.0 spike=1.28
- SPIN.CA: score=26.4 buy_ready=True sector_rank=5 price=15.6 support=14.57 resistance=17.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=64.44 liquidity=11927274.0 spike=0.42
- SPMD.CA: score=25.59 buy_ready=True sector_rank=19 price=0.48 support=0.44 resistance=0.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=62.62 liquidity=25666900.0 spike=0.78
- SUGR.CA: score=28.14 buy_ready=True sector_rank=7 price=48.58 support=46.47 resistance=49.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=60.85 liquidity=16636489.0 spike=1.87
- SVCE.CA: score=13.59 buy_ready=False sector_rank=19 price=11.26 support=9.37 resistance=11.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=670879296.0 spike=18.62
- SWDY.CA: score=23.46 buy_ready=False sector_rank=3 price=109.01 support=87.41 resistance=114.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=75.39 liquidity=87549152.0 spike=1.53
- TALM.CA: score=23.95 buy_ready=False sector_rank=15 price=18.53 support=15.45 resistance=19.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=70.36 liquidity=22889198.0 spike=0.59
- TMGH.CA: score=19.12 buy_ready=False sector_rank=18 price=97.12 support=95.2 resistance=103.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=36.93 liquidity=401507840.0 spike=1.2
- TRTO.CA: score=9.59 buy_ready=False sector_rank=19 price=0.03 support=0.03 resistance=0.04 source=Yahoo Finance as_of=2026-08-09T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- UEFM.CA: score=15.73 buy_ready=True sector_rank=19 price=552.21 support=491.0 resistance=625.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:12 PM market time freshness=DELAYED_CURRENT RSI=42.89 liquidity=2138436.75 spike=0.45
- UEGC.CA: score=23.59 buy_ready=True sector_rank=19 price=2.71 support=1.87 resistance=2.82 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=57.89 liquidity=21643142.0 spike=0.4
- UNIP.CA: score=23.59 buy_ready=True sector_rank=19 price=0.41 support=0.34 resistance=0.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=46.79 liquidity=12737277.0 spike=0.43
- UNIT.CA: score=11.82 buy_ready=False sector_rank=18 price=20.89 support=17.8 resistance=20.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=62558696.0 spike=2.55
- WCDF.CA: score=7.69 buy_ready=False sector_rank=19 price=613.97 support=591.02 resistance=620.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=7322167.0 spike=1.89
- WKOL.CA: score=26.97 buy_ready=True sector_rank=19 price=330.29 support=307.0 resistance=363.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=55.32 liquidity=53026028.0 spike=2.69
- ZEOT.CA: score=24.09 buy_ready=True sector_rank=19 price=13.03 support=11.22 resistance=13.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=62.38 liquidity=36783856.0 spike=1.25
- ZMID.CA: score=8.72 buy_ready=False sector_rank=18 price=7.64 support=7.59 resistance=7.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11 August 01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=243673680.0 spike=0.91

## Backtesting Lite
- ISPH.CA: 180d return=24.99%, max drawdown=-23.92%, MA20>MA50 days last20=6, as_of=2026-08-09T21:00:00+00:00
- EALR.CA: 180d return=-2.18%, max drawdown=-24.6%, MA20>MA50 days last20=12, as_of=2026-08-09T21:00:00+00:00
- CNFN.CA: 180d return=7.3%, max drawdown=-27.78%, MA20>MA50 days last20=20, as_of=2026-08-09T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- ISPH.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=588 sources=3 expected=Ibn Sina Pharma summary=Ibnsina Pharma’s consolidated profits jump to EGP 952m in 2025; EBRD grants EGP 1.3bn loan to Ibnsina Pharma for new warehouse; Ibnsina Pharma pens import, distribution deal with OMRON Healthcare
  - Ibnsina Pharma’s consolidated profits jump to EGP 952m in 2025: https://english.mubasher.info/news/4563237/Ibnsina-Pharma-s-consolidated-profits-jump-to-EGP-952m-in-2025/
  - EBRD grants EGP 1.3bn loan to Ibnsina Pharma for new warehouse: https://english.mubasher.info/news/4552027/EBRD-grants-EGP-1-3bn-loan-to-Ibnsina-Pharma-for-new-warehouse/
  - Ibnsina Pharma pens import, distribution deal with OMRON Healthcare: https://english.mubasher.info/news/4028068/Ibnsina-Pharma-pens-import-distribution-deal-with-OMRON-Healthcare/
- EALR.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Arab Company For Land Reclamation summary=El Arabia for Land Reclamation targets EGP 2.5m profits in FY22/23; El Arabia for Land Reclamation starts work on Bahariya Oasis project; El Arabia for Land Reclamation H1 losses down 16%
  - El Arabia for Land Reclamation targets EGP 2.5m profits in FY22/23: https://english.mubasher.info/news/3938373/El-Arabia-for-Land-Reclamation-targets-EGP-2-5m-profits-in-FY22-23/
  - El Arabia for Land Reclamation starts work on Bahariya Oasis project: https://english.mubasher.info/news/3493569/El-Arabia-for-Land-Reclamation-starts-work-on-Bahariya-Oasis-project/
  - El Arabia for Land Reclamation H1 losses down 16%: https://english.mubasher.info/news/3058199/El-Arabia-for-Land-Reclamation-H1-losses-down-16-/
- CNFN.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=588 sources=3 expected=Contact Financial Holding summary=Contact’s consolidated profits approach EGP 471m in 2025; Contact logs lower consolidated net profits at EGP 291m in 9M-25; Contact, e&amp; money forge partnership to boost Egypt’s financial ecosystem
  - Contact’s consolidated profits approach EGP 471m in 2025: https://english.mubasher.info/news/4582855/Contact-s-consolidated-profits-approach-EGP-471m-in-2025/
  - Contact logs lower consolidated net profits at EGP 291m in 9M-25: https://english.mubasher.info/news/4526894/Contact-logs-lower-consolidated-net-profits-at-EGP-291m-in-9M-25/
  - Contact, e&amp; money forge partnership to boost Egypt’s financial ecosystem: https://english.mubasher.info/news/4509412/Contact-e-money-forge-partnership-to-boost-Egypt-s-financial-ecosystem/
- SUGR.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=588 sources=3 expected=Delta Sugar summary=Delta Sugar’s net profits fall 74% in Q1-26; Delta Sugar stock tests key resistance near EGP 50 amid downtrend; Delta Sugar turns to EGP 346m net losses in 2025
  - Delta Sugar’s net profits fall 74% in Q1-26: https://english.mubasher.info/news/4604921/Delta-Sugar-s-net-profits-fall-74-in-Q1-26/
  - Delta Sugar stock tests key resistance near EGP 50 amid downtrend: https://english.mubasher.info/news/4584932/Delta-Sugar-stock-tests-key-resistance-near-EGP-50-amid-downtrend/
  - Delta Sugar turns to EGP 346m net losses in 2025: https://english.mubasher.info/news/4557875/Delta-Sugar-turns-to-EGP-346m-net-losses-in-2025/
- SMFR.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Samad Misr EGYFERT.S.A.E summary=Evidence rejected for SMFR.CA: source text did not clearly match SMFR.CA / Samad Misr EGYFERT.S.A.E.
- SAUD.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=588 sources=3 expected=Al Baraka Bank Egypt summary=Al Baraka Bank Egypt records EGP 2.2bn operating income in Q1-26; Al Baraka Bank Egypt files MTO to acquire majority stake in A.T. LEASE; Al Baraka Bank Egypt to pay EGP 1.1/share dividends for 2025
  - Al Baraka Bank Egypt records EGP 2.2bn operating income in Q1-26: https://english.mubasher.info/news/4611927/Al-Baraka-Bank-Egypt-records-EGP-2-2bn-operating-income-in-Q1-26/
  - Al Baraka Bank Egypt files MTO to acquire majority stake in A.T. LEASE: https://english.mubasher.info/news/4583822/Al-Baraka-Bank-Egypt-files-MTO-to-acquire-majority-stake-in-A-T-LEASE/
  - Al Baraka Bank Egypt to pay EGP 1.1/share dividends for 2025: https://english.mubasher.info/news/4583458/Al-Baraka-Bank-Egypt-to-pay-EGP-1-1-share-dividends-for-2025/
- MAAL.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Marseille Almasreia Alkhalegeya For Holding Investment SAE summary=Evidence rejected for MAAL.CA: source text did not clearly match MAAL.CA / Marseille Almasreia Alkhalegeya For Holding Investment SAE.
- EFIH.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=E-Finance For Digital and Financial Investments summary=Evidence rejected for EFIH.CA: source text did not clearly match EFIH.CA / E-Finance For Digital and Financial Investments.

## Warnings
- Evidence for ISPH.CA matches the company but appears old; latest detected date is 2025-01-01.
- Gemini batch evidence failed: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.', 'status': 'UNAVAILABLE'}}
- Evidence for EALR.CA matches the company but no source/report date was detected.
- Evidence for CNFN.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for SUGR.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for SMFR.CA: source text did not clearly match SMFR.CA / Samad Misr EGYFERT.S.A.E.
- Evidence for SAUD.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for MAAL.CA: source text did not clearly match MAAL.CA / Marseille Almasreia Alkhalegeya For Holding Investment SAE.
- Evidence rejected for EFIH.CA: source text did not clearly match EFIH.CA / E-Finance For Digital and Financial Investments.
