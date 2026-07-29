# Telegram-First EGX Scanner Report

Scan phase: Open liquidity confirmation
Generated UTC: 2026-07-29T09:02:09.242893+00:00
Generated Cairo: 2026-07-29 12:02
Run timing: target 09:15 Cairo | generated Cairo 2026-07-29 12:02 | cron 15 6 * * 0-4
Trigger: scheduled cron=15 6 * * 0-4 mapped to open_confirm; Cairo now 2026-07-29 11:53

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 59
- Data quality issues: 1
- Tradeable price/liquidity tickers: 184/189
- Top sector: Agriculture & Food Production

## Market Context
- Market trend: Bullish
- Source: Mubasher EGX market page (delayed public data)
- As of: Wednesday, July 29
- Freshness: DELAYED
- EGX30 regime: MIXED / above MA20 55.0% / above MA50 45.0%
- EGX70 regime: BULLISH / above MA20 66.67% / above MA50 82.05%
- Sector breadth: 52.38%
- Risk mode: SELECTIVE_SMALL_MID_SWINGS

## Top Liquidity
- MPCO.CA: liquidity=318669472.0 spike=5.27 score=34.4
- BIOC.CA: liquidity=173225664.0 spike=3.39 score=14.18
- MCRO.CA: liquidity=164247312.0 spike=1.37 score=24.14
- TALM.CA: liquidity=156735616.0 spike=9.39 score=14.4
- COMI.CA: liquidity=142451536.0 spike=0.33 score=28.4

## AI Narrative
- Provider: OpenRouter OK
- Model: nvidia/nemotron-3-super-120b-a12b:free
- Summary: EGX30 shows a mixed trend with weak breadth below its 50‑day MA, while EGX70 is bullish with strong breadth; sector breadth is 52% and risk mode is SELECTIVE_SMALL_MID_SWINGS, prompting the scanner to favor stocks with accumulation spikes, solid support levels, and bullish‑watch outlooks in leading sectors (Agriculture & Food Production, Textiles, Building Materials).
- MPCO.CA – agriculture leader, accumulation spike 5.27×, price 17% below 20‑day support, bullish‑watch outlook; EGX30 mixed adds uncertainty.
- ATQA.CA – basic resources, accumulation spike 2.11×, price just below 20‑day resistance (‑0.6%), bullish‑watch, but momentum extended and sector not leading raises caution.
- ARCC.CA – building materials (sector rank 3), tradeable liquidity, price 1.3% above 20‑day resistance, bullish‑level supports outlook yet‑risk.
- ORWE.CA – textiles (sector 2), tradeable, price 4.8% above support and 2.0% above resistance, bullish‑watch, liquidity cooling introduces uncertainty.
- ORWE.CA – textiles (sector rank 2), tradeable liquidity, price 4.8% above support and 2.0% above resistance, bullish‑watch, dividend outlook, yet liquidity cooling introduces uncertainty.

## Top Liquidity Spikes
- TALM.CA: spike=9.39 liquidity=156735616.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- MPCO.CA: spike=5.27 liquidity=318669472.0 outlook=BULLISH_WATCH score=100 buy_ready=True
- BIOC.CA: spike=3.39 liquidity=173225664.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- ELWA.CA: spike=2.37 liquidity=3200567.25 outlook=WEAK_OR_RISKY score=33.42 buy_ready=False
- ATQA.CA: spike=2.11 liquidity=71817608.0 outlook=BULLISH_WATCH score=85.25 buy_ready=True

## Sector Leaderboard
- #1 Agriculture & Food Production: score=12.66 5d=3.72% 20d=5.58% aboveMA50=100.0%
- #2 Textiles: score=10.61 5d=3.67% 20d=13.7% aboveMA50=100.0%
- #3 Building Materials: score=8.92 5d=0.39% 20d=14.49% aboveMA50=83.33%
- #4 Industrial Goods & Cables: score=8.53 5d=1.41% 20d=8.41% aboveMA50=100.0%
- #5 General / Verified EGX Expansion: score=8.42 5d=0.52% 20d=15.25% aboveMA50=83.5%
- #6 Real Estate: score=8.06 5d=0.49% 20d=16.03% aboveMA50=76.92%
- #7 Education: score=7.75 5d=0.01% 20d=12.8% aboveMA50=66.67%
- #8 Banking & Financials: score=6.94 5d=1.31% 20d=7.08% aboveMA50=70.0%

## Today's Prioritized Action Tickets
- HOLD: Local fallback HOLD: no candidate passed evidence, liquidity, freshness, and technical gates.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- MPCO.CA: BULLISH_WATCH score=100 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=No major short-term scanner risk flags.
- ARCC.CA: BULLISH_WATCH score=95.92 liquidity=TRADEABLE sector=LEADING risk=close to resistance
- MCQE.CA: BULLISH_WATCH score=94.92 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- ORWE.CA: BULLISH_WATCH score=90 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- IFAP.CA: BULLISH_WATCH score=90 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- PRCL.CA: BULLISH_WATCH score=88.92 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- ROTO.CA: BULLISH_WATCH score=86.42 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- ATQA.CA: BULLISH_WATCH score=85.25 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended; sector is not leading
- ACAMD.CA: BULLISH_WATCH score=84.42 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- EALR.CA: BULLISH_WATCH score=84.42 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling

## BUY-Ready Candidates
- MPCO.CA: rank=34.4 outlook=BULLISH_WATCH outlook_score=100 sector_rank=1 price=1.99 support=1.7 resistance=1.95 liquidity=318669472.0
- ATQA.CA: rank=29.52 outlook=BULLISH_WATCH outlook_score=85.25 sector_rank=17 price=10.22 support=9.35 resistance=10.16 liquidity=71817608.0
- ARCC.CA: rank=29.4 outlook=BULLISH_WATCH outlook_score=95.92 sector_rank=3 price=57.77 support=53.5 resistance=58.5 liquidity=22059170.0
- COMI.CA: rank=28.4 outlook=CONSTRUCTIVE outlook_score=67.94 sector_rank=8 price=141.99 support=126.21 resistance=142.55 liquidity=142451536.0
- ORWE.CA: rank=26.84 outlook=BULLISH_WATCH outlook_score=90 sector_rank=2 price=23.0 support=21.95 resistance=23.47 liquidity=8436714.0
- ORHD.CA: rank=26.4 outlook=BULLISH_WATCH outlook_score=78.06 sector_rank=6 price=39.9 support=37.2 resistance=40.9 liquidity=34310716.0
- ADIB.CA: rank=26.4 outlook=CONSTRUCTIVE outlook_score=59.94 sector_rank=8 price=51.94 support=44.31 resistance=52.88 liquidity=43033960.0
- TMGH.CA: rank=26.4 outlook=BULLISH_WATCH outlook_score=78.06 sector_rank=6 price=99.78 support=92.1 resistance=103.87 liquidity=53835404.0
- ACAMD.CA: rank=26.4 outlook=BULLISH_WATCH outlook_score=84.42 sector_rank=5 price=2.37 support=2.15 resistance=2.52 liquidity=18806700.0
- BTFH.CA: rank=26.14 outlook=BULLISH_WATCH outlook_score=70.34 sector_rank=14 price=3.09 support=2.91 resistance=3.2 liquidity=30298566.0

## Data Quality Issues
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=18.79 buy_ready=True sector_rank=5 price=241.28 support=197.0 resistance=255.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=59.21 liquidity=2392354.75 spike=0.12
- ABUK.CA: score=21.03 buy_ready=False sector_rank=17 price=71.39 support=66.66 resistance=75.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=55.49 liquidity=8730461.0 spike=0.06
- ACAMD.CA: score=26.4 buy_ready=True sector_rank=5 price=2.37 support=2.15 resistance=2.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=51.43 liquidity=18806700.0 spike=0.25
- ACGC.CA: score=21.27 buy_ready=True sector_rank=2 price=10.69 support=8.92 resistance=11.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=68.85 liquidity=4872134.0 spike=0.16
- ADCI.CA: score=12.18 buy_ready=False sector_rank=5 price=258.81 support=230.0 resistance=269.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=76.53 liquidity=778566.5 spike=0.07
- ADIB.CA: score=26.4 buy_ready=True sector_rank=8 price=51.94 support=44.31 resistance=52.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=69.6 liquidity=43033960.0 spike=0.33
- ADPC.CA: score=24.4 buy_ready=False sector_rank=5 price=3.97 support=3.32 resistance=4.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=73.68 liquidity=14261302.0 spike=0.43
- AFDI.CA: score=19.09 buy_ready=True sector_rank=5 price=51.0 support=41.84 resistance=52.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:13 AM market time freshness=DELAYED_CURRENT RSI=67.14 liquidity=4689094.0 spike=0.28
- AFMC.CA: score=23.4 buy_ready=False sector_rank=5 price=127.02 support=66.0 resistance=144.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=80.91 liquidity=18217736.0 spike=0.38
- AJWA.CA: score=24.4 buy_ready=True sector_rank=5 price=188.79 support=161.0 resistance=210.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=60.64 liquidity=15565717.0 spike=0.63
- ALCN.CA: score=15.03 buy_ready=False sector_rank=18 price=29.03 support=27.7 resistance=30.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=53.97 liquidity=1858911.88 spike=0.08
- ALUM.CA: score=19.6 buy_ready=True sector_rank=5 price=23.7 support=20.55 resistance=24.09 source=Yahoo Finance as_of=2026-07-27T21:00:00+00:00 freshness=FRESH RSI=53.41 liquidity=3199642.3 spike=0.51
- AMER.CA: score=23.4 buy_ready=False sector_rank=6 price=4.68 support=2.28 resistance=4.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=89.78 liquidity=50365508.0 spike=0.46
- AMES.CA: score=24.4 buy_ready=False sector_rank=5 price=126.36 support=45.15 resistance=144.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=72.06 liquidity=14577448.0 spike=0.14
- AMIA.CA: score=21.86 buy_ready=False sector_rank=5 price=11.14 support=8.42 resistance=11.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=71.3 liquidity=5461259.5 spike=0.38
- AMOC.CA: score=23.18 buy_ready=True sector_rank=10 price=8.25 support=7.42 resistance=8.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=64.12 liquidity=6778027.0 spike=0.11
- APSW.CA: score=17.24 buy_ready=False sector_rank=5 price=8.98 support=8.0 resistance=9.34 source=Yahoo Finance as_of=2026-07-27T21:00:00+00:00 freshness=FRESH RSI=61.29 liquidity=839468.32 spike=0.5
- ARAB.CA: score=22.4 buy_ready=False sector_rank=6 price=0.24 support=0.2 resistance=0.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=62.5 liquidity=18733214.0 spike=0.14
- ARCC.CA: score=29.4 buy_ready=True sector_rank=3 price=57.77 support=53.5 resistance=58.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=59.77 liquidity=22059170.0 spike=0.84
- AREH.CA: score=12.25 buy_ready=False sector_rank=5 price=1.46 support=1.44 resistance=1.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=38.18 liquidity=2853810.75 spike=0.1
- ARVA.CA: score=14.4 buy_ready=False sector_rank=5 price=12.35 support=10.5 resistance=12.6 source=Yahoo Finance as_of=2026-07-27T21:00:00+00:00 freshness=FRESH RSI=70.61 liquidity=0.0 spike=0.0
- ASCM.CA: score=22.4 buy_ready=False sector_rank=5 price=64.47 support=57.1 resistance=66.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=71.17 liquidity=15877946.0 spike=0.29
- ASPI.CA: score=23.4 buy_ready=False sector_rank=5 price=0.45 support=0.3 resistance=0.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=93.41 liquidity=10832499.0 spike=0.29
- ATLC.CA: score=13.48 buy_ready=False sector_rank=14 price=5.15 support=4.92 resistance=5.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:13 AM market time freshness=DELAYED_CURRENT RSI=46.03 liquidity=1345971.0 spike=0.19
- ATQA.CA: score=29.52 buy_ready=True sector_rank=17 price=10.22 support=9.35 resistance=10.16 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=64.46 liquidity=71817608.0 spike=2.11
- AXPH.CA: score=10.4 buy_ready=False sector_rank=5 price=1201.2 support=1075.0 resistance=1342.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=79.08 liquidity=996953.06 spike=0.26
- BINV.CA: score=12.5 buy_ready=False sector_rank=13 price=47.22 support=44.98 resistance=51.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=42.4 liquidity=301087.0 spike=0.04
- BIOC.CA: score=14.18 buy_ready=False sector_rank=5 price=193.92 support=170.0 resistance=197.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=173225664.0 spike=3.39
- BTFH.CA: score=26.14 buy_ready=True sector_rank=14 price=3.09 support=2.91 resistance=3.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=52.5 liquidity=30298566.0 spike=0.14
- CAED.CA: score=21.4 buy_ready=False sector_rank=5 price=130.0 support=69.02 resistance=143.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=77.42 liquidity=34699472.0 spike=0.53
- CANA.CA: score=24.7 buy_ready=True sector_rank=8 price=38.79 support=34.7 resistance=39.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=67.38 liquidity=8298243.5 spike=0.49
- CCAP.CA: score=24.2 buy_ready=True sector_rank=13 price=5.29 support=4.65 resistance=5.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=57.29 liquidity=91049792.0 spike=0.13
- CCRS.CA: score=19.83 buy_ready=True sector_rank=5 price=2.6 support=2.18 resistance=2.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=64.47 liquidity=3434196.0 spike=0.19
- CEFM.CA: score=21.05 buy_ready=True sector_rank=5 price=126.01 support=95.75 resistance=152.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=64.12 liquidity=4649323.5 spike=0.25
- CERA.CA: score=17.68 buy_ready=True sector_rank=5 price=1.33 support=1.19 resistance=1.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=62.86 liquidity=3279427.5 spike=0.14
- CFGH.CA: score=15.41 buy_ready=False sector_rank=5 price=0.11 support=0.1 resistance=0.11 source=Yahoo Finance as_of=2026-07-27T21:00:00+00:00 freshness=FRESH RSI=60.61 liquidity=10295.54 spike=0.67
- CICH.CA: score=16.64 buy_ready=False sector_rank=14 price=12.15 support=11.6 resistance=12.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:13 AM market time freshness=DELAYED_CURRENT RSI=51.3 liquidity=500034.59 spike=0.1
- CIEB.CA: score=14.07 buy_ready=False sector_rank=8 price=24.1 support=23.3 resistance=24.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT RSI=38.46 liquidity=1669109.13 spike=0.19
- CIRA.CA: score=23.4 buy_ready=False sector_rank=7 price=36.85 support=27.45 resistance=36.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=81.31 liquidity=39431440.0 spike=0.79
- CLHO.CA: score=16.49 buy_ready=True sector_rank=9 price=16.76 support=15.9 resistance=17.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:13 AM market time freshness=DELAYED_CURRENT RSI=56.17 liquidity=2094686.0 spike=0.05
- CNFN.CA: score=17.32 buy_ready=True sector_rank=14 price=4.87 support=4.61 resistance=5.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=64.1 liquidity=3188105.75 spike=0.16
- COMI.CA: score=28.4 buy_ready=True sector_rank=8 price=141.99 support=126.21 resistance=142.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=58.92 liquidity=142451536.0 spike=0.33
- COPR.CA: score=18.8 buy_ready=False sector_rank=5 price=0.41 support=0.35 resistance=0.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=81.52 liquidity=8397952.0 spike=0.28
- COSG.CA: score=23.02 buy_ready=True sector_rank=5 price=1.69 support=1.47 resistance=1.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=65.22 liquidity=8623540.0 spike=0.19
- CPCI.CA: score=16.94 buy_ready=False sector_rank=5 price=469.08 support=370.1 resistance=512.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=73.91 liquidity=2540647.5 spike=0.22
- CSAG.CA: score=12.44 buy_ready=False sector_rank=18 price=32.58 support=31.57 resistance=34.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=50.22 liquidity=1268852.75 spike=0.08
- DAPH.CA: score=24.78 buy_ready=False sector_rank=5 price=97.69 support=78.8 resistance=98.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=72.96 liquidity=19597922.0 spike=1.19
- DEIN.CA: score=-0.6 buy_ready=False sector_rank=5 price=11.38 support=13.65 resistance=13.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 June 12:11 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=40.95 spike=0.01
- DOMT.CA: score=11.36 buy_ready=False sector_rank=19 price=26.72 support=26.06 resistance=27.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:10 AM market time freshness=DELAYED_CURRENT RSI=44.07 liquidity=536479.81 spike=0.16
- DSCW.CA: score=21.4 buy_ready=False sector_rank=5 price=1.96 support=1.71 resistance=2.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=82.76 liquidity=12784028.0 spike=0.24
- DTPP.CA: score=24.19 buy_ready=False sector_rank=5 price=246.85 support=120.0 resistance=273.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=71.42 liquidity=9790609.0 spike=0.13
- EALR.CA: score=18.01 buy_ready=True sector_rank=5 price=365.25 support=335.0 resistance=425.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=40.28 liquidity=1611240.13 spike=0.09
- EASB.CA: score=17.99 buy_ready=True sector_rank=5 price=7.53 support=6.88 resistance=8.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=62.87 liquidity=3586846.5 spike=0.25
- EAST.CA: score=3.5 buy_ready=False sector_rank=19 price=36.18 support=36.01 resistance=38.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=31.93 liquidity=1677096.13 spike=0.03
- EBSC.CA: score=8.32 buy_ready=False sector_rank=5 price=1.91 support=1.71 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=29.63 liquidity=920611.63 spike=0.11
- ECAP.CA: score=16.7 buy_ready=False sector_rank=5 price=33.75 support=31.52 resistance=34.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:02 AM market time freshness=DELAYED_CURRENT RSI=62.89 liquidity=300819.72 spike=0.05
- EDFM.CA: score=14.71 buy_ready=False sector_rank=5 price=380.58 support=310.2 resistance=430.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:10 AM market time freshness=DELAYED_CURRENT RSI=73.24 liquidity=307502.72 spike=0.07
- EEII.CA: score=15.81 buy_ready=True sector_rank=5 price=2.73 support=2.35 resistance=2.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=38.18 liquidity=1410295.13 spike=0.06
- EFIC.CA: score=10.17 buy_ready=False sector_rank=17 price=185.82 support=180.02 resistance=213.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT RSI=51.61 liquidity=868048.19 spike=0.08
- EFID.CA: score=13.52 buy_ready=False sector_rank=19 price=27.0 support=25.85 resistance=28.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:13 AM market time freshness=DELAYED_CURRENT RSI=29.81 liquidity=59952132.0 spike=1.35
- EFIH.CA: score=24.31 buy_ready=True sector_rank=15 price=22.83 support=20.1 resistance=24.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=42.67 liquidity=8414932.0 spike=0.14
- EGAL.CA: score=15.97 buy_ready=False sector_rank=17 price=297.34 support=272.28 resistance=312.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=48.3 liquidity=3671265.75 spike=0.09
- EGAS.CA: score=17.47 buy_ready=True sector_rank=10 price=52.49 support=48.1 resistance=54.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=61.84 liquidity=1068627.25 spike=0.08
- EGBE.CA: score=11.43 buy_ready=False sector_rank=8 price=0.48 support=-0.34 resistance=0.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=96.42 liquidity=27344.16 spike=0.56
- EGCH.CA: score=16.86 buy_ready=False sector_rank=17 price=12.98 support=12.13 resistance=13.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=56.22 liquidity=4558883.5 spike=0.07
- EGSA.CA: score=9.38 buy_ready=False sector_rank=11 price=8.85 support=8.67 resistance=9.21 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:57 AM market time freshness=DELAYED_CURRENT RSI=51.52 liquidity=6661.91 spike=0.37
- EGTS.CA: score=5.83 buy_ready=False sector_rank=6 price=17.86 support=15.1 resistance=19.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=33.42 liquidity=1433788.88 spike=0.03
- EHDR.CA: score=21.79 buy_ready=True sector_rank=5 price=2.88 support=2.37 resistance=3.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=65.52 liquidity=7389921.0 spike=0.18
- EKHO.CA: score=8.4 buy_ready=False sector_rank=10 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-07-27T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=24.18 buy_ready=True sector_rank=4 price=2.18 support=2.04 resistance=2.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=62.16 liquidity=8784039.0 spike=0.13
- ELKA.CA: score=24.4 buy_ready=False sector_rank=5 price=1.87 support=1.19 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=72.82 liquidity=23200482.0 spike=0.31
- ELNA.CA: score=16.56 buy_ready=False sector_rank=5 price=38.99 support=36.01 resistance=40.5 source=Yahoo Finance as_of=2026-07-27T21:00:00+00:00 freshness=FRESH RSI=50.7 liquidity=162939.22 spike=0.27
- ELSH.CA: score=24.4 buy_ready=True sector_rank=5 price=14.51 support=11.15 resistance=15.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=61.03 liquidity=24831566.0 spike=0.18
- ELWA.CA: score=15.34 buy_ready=False sector_rank=5 price=1.78 support=1.82 resistance=2.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=37.84 liquidity=3200567.25 spike=2.37
- EMFD.CA: score=17.49 buy_ready=False sector_rank=6 price=11.5 support=11.25 resistance=12.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=40.35 liquidity=8087788.5 spike=0.13
- ENGC.CA: score=20.39 buy_ready=False sector_rank=5 price=43.02 support=36.0 resistance=44.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=71.27 liquidity=3993425.0 spike=0.16
- EOSB.CA: score=14.4 buy_ready=False sector_rank=5 price=1.48 support=1.5 resistance=1.55 source=Yahoo Finance as_of=2026-07-27T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=3806.56 spike=0.1
- EPCO.CA: score=15.07 buy_ready=False sector_rank=5 price=11.15 support=8.5 resistance=11.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=77.19 liquidity=3669457.0 spike=0.13
- EPPK.CA: score=17.36 buy_ready=False sector_rank=5 price=15.09 support=12.81 resistance=15.93 source=Yahoo Finance as_of=2026-07-27T21:00:00+00:00 freshness=FRESH RSI=50.29 liquidity=956374.03 spike=0.78
- ETEL.CA: score=26.37 buy_ready=False sector_rank=11 price=106.34 support=89.01 resistance=107.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=72.61 liquidity=33096806.0 spike=0.4
- ETRS.CA: score=18.4 buy_ready=False sector_rank=5 price=10.39 support=10.39 resistance=10.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=11310121.0 spike=1.0
- EXPA.CA: score=15.58 buy_ready=False sector_rank=8 price=19.83 support=18.05 resistance=20.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT RSI=78.76 liquidity=4175616.25 spike=0.14
- FAIT.CA: score=12.49 buy_ready=False sector_rank=8 price=37.02 support=35.06 resistance=38.0 source=Yahoo Finance as_of=2026-07-27T21:00:00+00:00 freshness=FRESH RSI=61.71 liquidity=1086981.25 spike=0.37
- FAITA.CA: score=9.42 buy_ready=False sector_rank=8 price=0.97 support=0.96 resistance=0.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:01 AM market time freshness=DELAYED_CURRENT RSI=41.79 liquidity=16015.51 spike=0.38
- FERC.CA: score=15.6 buy_ready=True sector_rank=17 price=77.54 support=72.75 resistance=85.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=58.06 liquidity=1297530.63 spike=0.11
- FWRY.CA: score=20.29 buy_ready=False sector_rank=15 price=18.94 support=18.15 resistance=19.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=40.59 liquidity=9385883.0 spike=0.07
- GBCO.CA: score=21.89 buy_ready=False sector_rank=16 price=29.92 support=30.12 resistance=34.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=45.23 liquidity=15952929.0 spike=0.22
- GDWA.CA: score=23.4 buy_ready=False sector_rank=5 price=0.83 support=0.76 resistance=0.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=72.67 liquidity=32601508.0 spike=0.36
- GGCC.CA: score=20.04 buy_ready=False sector_rank=5 price=0.84 support=0.45 resistance=0.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=82.85 liquidity=8635683.0 spike=0.23
- GIHD.CA: score=23.4 buy_ready=False sector_rank=5 price=59.66 support=40.66 resistance=65.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=78.97 liquidity=27361568.0 spike=0.54
- GMCI.CA: score=15.22 buy_ready=False sector_rank=5 price=2.07 support=1.71 resistance=2.26 source=Yahoo Finance as_of=2026-07-27T21:00:00+00:00 freshness=FRESH RSI=49.28 liquidity=820034.61 spike=0.62
- GRCA.CA: score=15.92 buy_ready=False sector_rank=5 price=61.14 support=48.0 resistance=68.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=74.0 liquidity=1520022.38 spike=0.09
- GSSC.CA: score=17.79 buy_ready=True sector_rank=5 price=268.37 support=240.52 resistance=288.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=64.56 liquidity=1387645.0 spike=0.14
- GTWL.CA: score=24.4 buy_ready=True sector_rank=5 price=102.76 support=60.3 resistance=118.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=51.57 liquidity=23088582.0 spike=0.17
- HDBK.CA: score=17.37 buy_ready=False sector_rank=8 price=81.5 support=76.9 resistance=86.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=48.3 liquidity=4968581.0 spike=0.16
- HELI.CA: score=21.4 buy_ready=False sector_rank=6 price=7.95 support=6.36 resistance=8.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=85.71 liquidity=79515624.0 spike=0.42
- HRHO.CA: score=13.14 buy_ready=False sector_rank=14 price=26.5 support=26.09 resistance=27.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=33.73 liquidity=16363871.0 spike=0.19
- ICID.CA: score=16.98 buy_ready=True sector_rank=5 price=8.26 support=6.55 resistance=8.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:03 AM market time freshness=DELAYED_CURRENT RSI=54.66 liquidity=2583120.75 spike=0.37
- IDRE.CA: score=18.26 buy_ready=True sector_rank=5 price=48.15 support=41.1 resistance=52.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=66.32 liquidity=3862327.75 spike=0.15
- IFAP.CA: score=20.69 buy_ready=True sector_rank=1 price=19.71 support=18.47 resistance=20.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=54.42 liquidity=1293614.25 spike=0.14
- INFI.CA: score=15.77 buy_ready=False sector_rank=5 price=107.29 support=88.51 resistance=111.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=75.05 liquidity=2373516.5 spike=0.14
- IRON.CA: score=3.89 buy_ready=False sector_rank=17 price=31.06 support=30.45 resistance=33.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=27.59 liquidity=1586340.13 spike=0.23
- ISMA.CA: score=21.4 buy_ready=False sector_rank=5 price=32.17 support=26.54 resistance=32.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=79.46 liquidity=19392416.0 spike=0.78
- ISMQ.CA: score=23.3 buy_ready=True sector_rank=17 price=9.63 support=9.05 resistance=10.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=43.75 liquidity=40174928.0 spike=0.42
- ISPH.CA: score=21.4 buy_ready=False sector_rank=9 price=11.45 support=11.2 resistance=11.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=43.51 liquidity=12898848.0 spike=0.26
- JUFO.CA: score=8.0 buy_ready=False sector_rank=19 price=28.73 support=28.5 resistance=31.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=16.41 liquidity=5180990.5 spike=0.2
- KABO.CA: score=24.93 buy_ready=True sector_rank=2 price=8.14 support=6.04 resistance=8.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=68.56 liquidity=8530111.0 spike=0.18
- KWIN.CA: score=23.4 buy_ready=False sector_rank=5 price=102.13 support=65.0 resistance=111.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=89.58 liquidity=22614646.0 spike=0.45
- KZPC.CA: score=10.89 buy_ready=False sector_rank=5 price=8.52 support=8.26 resistance=8.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=55.36 liquidity=493531.38 spike=0.1
- LCSW.CA: score=25.4 buy_ready=False sector_rank=3 price=34.65 support=27.43 resistance=37.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:13 AM market time freshness=DELAYED_CURRENT RSI=71.46 liquidity=16360856.0 spike=0.22
- LUTS.CA: score=8.48 buy_ready=False sector_rank=5 price=0.56 support=0.57 resistance=0.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=19.38 liquidity=5077960.0 spike=0.15
- MAAL.CA: score=15.75 buy_ready=False sector_rank=5 price=8.75 support=6.92 resistance=8.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=78.06 liquidity=6345001.0 spike=0.38
- MASR.CA: score=24.4 buy_ready=True sector_rank=5 price=7.97 support=6.82 resistance=8.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=58.55 liquidity=19527880.0 spike=0.22
- MBSC.CA: score=18.82 buy_ready=False sector_rank=3 price=245.45 support=222.66 resistance=249.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=49.26 liquidity=4415626.0 spike=0.23
- MCQE.CA: score=22.05 buy_ready=True sector_rank=3 price=183.06 support=167.02 resistance=195.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=58.38 liquidity=4645097.0 spike=0.26
- MCRO.CA: score=24.14 buy_ready=False sector_rank=5 price=1.56 support=1.17 resistance=1.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=80.0 liquidity=164247312.0 spike=1.37
- MENA.CA: score=18.73 buy_ready=True sector_rank=6 price=7.13 support=6.61 resistance=7.59 source=Yahoo Finance as_of=2026-07-27T21:00:00+00:00 freshness=FRESH RSI=53.23 liquidity=4332323.54 spike=0.55
- MEPA.CA: score=24.4 buy_ready=True sector_rank=5 price=1.88 support=1.52 resistance=2.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=69.09 liquidity=21755476.0 spike=0.46
- MFPC.CA: score=20.3 buy_ready=False sector_rank=17 price=36.7 support=34.3 resistance=38.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=55.66 liquidity=11347250.0 spike=0.13
- MFSC.CA: score=9.9 buy_ready=False sector_rank=5 price=46.53 support=45.05 resistance=53.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:08 AM market time freshness=DELAYED_CURRENT RSI=35.76 liquidity=500355.75 spike=0.09
- MHOT.CA: score=14.87 buy_ready=False sector_rank=12 price=17.09 support=16.2 resistance=18.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=43.38 liquidity=2560923.75 spike=0.22
- MICH.CA: score=17.64 buy_ready=True sector_rank=5 price=40.15 support=34.0 resistance=43.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=68.11 liquidity=3239555.0 spike=0.2
- MILS.CA: score=17.94 buy_ready=True sector_rank=5 price=170.47 support=126.31 resistance=197.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=66.53 liquidity=3540981.0 spike=0.09
- MIPH.CA: score=15.64 buy_ready=False sector_rank=9 price=728.16 support=630.5 resistance=780.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:10 AM market time freshness=DELAYED_CURRENT RSI=71.65 liquidity=1235843.0 spike=0.36
- MOED.CA: score=18.4 buy_ready=False sector_rank=5 price=0.7 support=0.65 resistance=0.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:17 AM market time freshness=DELAYED_CURRENT RSI=46.9 liquidity=14299105.0 spike=0.64
- MOIL.CA: score=15.09 buy_ready=False sector_rank=10 price=0.68 support=0.46 resistance=0.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=88.24 liquidity=887560.75 spike=1.4
- MOIN.CA: score=8.59 buy_ready=False sector_rank=5 price=23.6 support=22.66 resistance=24.76 source=Yahoo Finance as_of=2026-07-27T21:00:00+00:00 freshness=FRESH RSI=41.28 liquidity=185661.2 spike=0.24
- MOSC.CA: score=18.33 buy_ready=True sector_rank=5 price=290.07 support=250.55 resistance=329.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=61.26 liquidity=1931047.25 spike=0.15
- MPCI.CA: score=23.4 buy_ready=False sector_rank=5 price=293.86 support=223.51 resistance=298.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=88.57 liquidity=13474667.0 spike=0.14
- MPCO.CA: score=34.4 buy_ready=True sector_rank=1 price=1.99 support=1.7 resistance=1.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=61.7 liquidity=318669472.0 spike=5.27
- MPRC.CA: score=17.29 buy_ready=False sector_rank=5 price=45.75 support=37.15 resistance=45.82 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:17 AM market time freshness=DELAYED_CURRENT RSI=73.54 liquidity=2889651.75 spike=0.09
- MTIE.CA: score=23.89 buy_ready=True sector_rank=16 price=9.5 support=8.75 resistance=9.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=51.91 liquidity=16443025.0 spike=0.73
- NAHO.CA: score=3.4 buy_ready=False sector_rank=5 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance as_of=2026-07-27T21:00:00+00:00 freshness=FRESH RSI=0.0 liquidity=4666.91 spike=0.14
- NCCW.CA: score=26.4 buy_ready=False sector_rank=5 price=7.0 support=5.82 resistance=7.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=73.8 liquidity=11432599.0 spike=0.43
- NEDA.CA: score=9.66 buy_ready=False sector_rank=5 price=2.75 support=2.7 resistance=3.02 source=Yahoo Finance as_of=2026-07-27T21:00:00+00:00 freshness=FRESH RSI=43.9 liquidity=261426.0 spike=0.36
- NHPS.CA: score=21.62 buy_ready=False sector_rank=5 price=87.4 support=61.55 resistance=95.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:17 AM market time freshness=DELAYED_CURRENT RSI=72.3 liquidity=7222071.0 spike=0.08
- NINH.CA: score=14.79 buy_ready=False sector_rank=5 price=22.1 support=17.4 resistance=23.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:17 AM market time freshness=DELAYED_CURRENT RSI=75.5 liquidity=3393389.5 spike=0.08
- NIPH.CA: score=21.4 buy_ready=False sector_rank=9 price=225.67 support=157.01 resistance=242.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=80.94 liquidity=38489780.0 spike=0.25
- OBRI.CA: score=13.97 buy_ready=False sector_rank=5 price=34.57 support=31.5 resistance=39.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=38.98 liquidity=4574264.5 spike=0.11
- OCDI.CA: score=24.4 buy_ready=True sector_rank=6 price=28.3 support=23.91 resistance=28.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=57.83 liquidity=43531612.0 spike=0.49
- OCPH.CA: score=15.85 buy_ready=False sector_rank=5 price=479.68 support=341.4 resistance=496.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:17 AM market time freshness=DELAYED_CURRENT RSI=94.23 liquidity=2449452.0 spike=0.1
- ODIN.CA: score=17.62 buy_ready=True sector_rank=5 price=2.6 support=2.05 resistance=2.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:13 AM market time freshness=DELAYED_CURRENT RSI=65.22 liquidity=3219231.5 spike=0.2
- OFH.CA: score=22.93 buy_ready=False sector_rank=5 price=0.72 support=0.57 resistance=0.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=81.48 liquidity=9531638.0 spike=0.14
- OIH.CA: score=23.96 buy_ready=False sector_rank=13 price=1.49 support=1.4 resistance=1.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=73.33 liquidity=7760689.0 spike=0.11
- OLFI.CA: score=18.53 buy_ready=True sector_rank=19 price=23.11 support=21.0 resistance=23.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=53.91 liquidity=3705071.75 spike=0.1
- ORAS.CA: score=7.6 buy_ready=False sector_rank=20 price=714.39 support=712.0 resistance=717.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=33057412.0 spike=1.0
- ORHD.CA: score=26.4 buy_ready=True sector_rank=6 price=39.9 support=37.2 resistance=40.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=54.71 liquidity=34310716.0 spike=0.23
- ORWE.CA: score=26.84 buy_ready=True sector_rank=2 price=23.0 support=21.95 resistance=23.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:13 AM market time freshness=DELAYED_CURRENT RSI=47.9 liquidity=8436714.0 spike=0.35
- PHAR.CA: score=26.86 buy_ready=False sector_rank=9 price=94.96 support=83.6 resistance=97.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=73.1 liquidity=61125412.0 spike=1.23
- PHDC.CA: score=19.4 buy_ready=False sector_rank=6 price=14.54 support=14.3 resistance=15.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=44.13 liquidity=55523228.0 spike=0.23
- PHTV.CA: score=17.29 buy_ready=False sector_rank=5 price=320.24 support=255.0 resistance=327.0 source=Yahoo Finance as_of=2026-07-27T21:00:00+00:00 freshness=FRESH RSI=84.68 liquidity=3885792.04 spike=0.72
- POUL.CA: score=13.56 buy_ready=False sector_rank=19 price=37.91 support=36.52 resistance=41.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=32.01 liquidity=7743936.0 spike=0.22
- PRCL.CA: score=19.01 buy_ready=True sector_rank=3 price=35.35 support=30.21 resistance=38.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=50.12 liquidity=3608731.25 spike=0.07
- PRDC.CA: score=24.4 buy_ready=True sector_rank=6 price=9.32 support=7.0 resistance=10.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=56.05 liquidity=21721050.0 spike=0.18
- PRMH.CA: score=13.97 buy_ready=False sector_rank=5 price=2.66 support=2.36 resistance=2.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=54.39 liquidity=1572849.25 spike=0.09
- RACC.CA: score=17.79 buy_ready=True sector_rank=5 price=10.11 support=9.36 resistance=10.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=49.27 liquidity=3391859.0 spike=0.16
- RAKT.CA: score=12.9 buy_ready=False sector_rank=5 price=22.63 support=21.25 resistance=23.7 source=Yahoo Finance as_of=2026-07-27T21:00:00+00:00 freshness=FRESH RSI=47.93 liquidity=316254.24 spike=1.09
- RAYA.CA: score=16.59 buy_ready=False sector_rank=21 price=7.41 support=7.01 resistance=8.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=35.81 liquidity=39104988.0 spike=0.29
- RMDA.CA: score=24.36 buy_ready=True sector_rank=9 price=5.14 support=4.81 resistance=5.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=57.14 liquidity=7962341.0 spike=0.31
- ROTO.CA: score=21.17 buy_ready=True sector_rank=5 price=44.02 support=38.0 resistance=46.71 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:08 AM market time freshness=DELAYED_CURRENT RSI=58.75 liquidity=2774721.5 spike=0.13
- RREI.CA: score=23.52 buy_ready=False sector_rank=5 price=4.72 support=3.34 resistance=4.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:17 AM market time freshness=DELAYED_CURRENT RSI=82.91 liquidity=45516172.0 spike=1.06
- RTVC.CA: score=15.3 buy_ready=False sector_rank=5 price=3.87 support=3.55 resistance=4.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=52.17 liquidity=900751.88 spike=0.2
- RUBX.CA: score=17.82 buy_ready=False sector_rank=5 price=13.0 support=11.07 resistance=14.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=50.28 liquidity=5424532.5 spike=0.08
- SAUD.CA: score=18.28 buy_ready=True sector_rank=8 price=22.3 support=20.0 resistance=22.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=57.75 liquidity=1879689.63 spike=0.2
- SCEM.CA: score=24.4 buy_ready=False sector_rank=3 price=85.0 support=60.14 resistance=87.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=87.72 liquidity=33875860.0 spike=0.49
- SCFM.CA: score=18.29 buy_ready=True sector_rank=5 price=275.25 support=230.0 resistance=325.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=60.71 liquidity=1888492.0 spike=0.09
- SCTS.CA: score=14.86 buy_ready=False sector_rank=7 price=612.28 support=540.0 resistance=649.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=44.86 liquidity=459623.84 spike=0.07
- SDTI.CA: score=23.4 buy_ready=False sector_rank=5 price=56.53 support=45.55 resistance=58.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=85.44 liquidity=12474922.0 spike=0.98
- SEIG.CA: score=14.76 buy_ready=False sector_rank=5 price=247.8 support=183.0 resistance=285.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=59.26 liquidity=362463.13 spike=0.02
- SIPC.CA: score=21.4 buy_ready=False sector_rank=5 price=4.02 support=3.25 resistance=4.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:17 AM market time freshness=DELAYED_CURRENT RSI=75.26 liquidity=11079891.0 spike=0.48
- SKPC.CA: score=14.8 buy_ready=False sector_rank=17 price=15.96 support=14.8 resistance=16.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:13 AM market time freshness=DELAYED_CURRENT RSI=49.88 liquidity=5501324.5 spike=0.16
- SMFR.CA: score=15.7 buy_ready=True sector_rank=5 price=235.14 support=189.3 resistance=277.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:13 AM market time freshness=DELAYED_CURRENT RSI=66.44 liquidity=1300704.75 spike=0.06
- SNFC.CA: score=10.45 buy_ready=False sector_rank=5 price=11.16 support=11.04 resistance=12.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=44.54 liquidity=1045037.25 spike=0.09
- SPIN.CA: score=23.4 buy_ready=False sector_rank=2 price=16.19 support=14.0 resistance=17.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=77.36 liquidity=13956204.0 spike=0.6
- SPMD.CA: score=26.4 buy_ready=False sector_rank=5 price=0.47 support=0.41 resistance=0.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:17 AM market time freshness=DELAYED_CURRENT RSI=74.24 liquidity=15545822.0 spike=0.6
- SUGR.CA: score=9.37 buy_ready=False sector_rank=19 price=46.89 support=45.31 resistance=47.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=46.03 liquidity=554635.0 spike=0.1
- SVCE.CA: score=18.66 buy_ready=False sector_rank=5 price=9.28 support=8.8 resistance=10.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:17 AM market time freshness=DELAYED_CURRENT RSI=44.85 liquidity=6261587.5 spike=0.12
- SWDY.CA: score=19.66 buy_ready=False sector_rank=4 price=94.83 support=84.3 resistance=97.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=70.73 liquidity=5262720.5 spike=0.25
- TALM.CA: score=14.4 buy_ready=False sector_rank=7 price=18.5 support=16.35 resistance=19.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=156735616.0 spike=9.39
- TMGH.CA: score=26.4 buy_ready=True sector_rank=6 price=99.78 support=92.1 resistance=103.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=54.91 liquidity=53835404.0 spike=0.15
- TRTO.CA: score=10.4 buy_ready=False sector_rank=5 price=0.03 support=0.03 resistance=0.03 source=Yahoo Finance as_of=2026-07-27T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=170.0 spike=0.15
- UEFM.CA: score=14.99 buy_ready=False sector_rank=5 price=542.85 support=462.0 resistance=625.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:07 AM market time freshness=DELAYED_CURRENT RSI=68.07 liquidity=593245.75 spike=0.14
- UEGC.CA: score=21.4 buy_ready=False sector_rank=5 price=2.3 support=1.33 resistance=2.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:17 AM market time freshness=DELAYED_CURRENT RSI=80.0 liquidity=21335062.0 spike=0.42
- UNIP.CA: score=9.4 buy_ready=False sector_rank=5 price=0.38 support=0.38 resistance=0.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:17 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=22213582.0 spike=0.89
- UNIT.CA: score=14.96 buy_ready=False sector_rank=6 price=18.03 support=12.0 resistance=21.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=53.41 liquidity=558712.13 spike=0.02
- WCDF.CA: score=17.1 buy_ready=False sector_rank=5 price=577.47 support=504.0 resistance=634.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=64.97 liquidity=697795.25 spike=0.28
- WKOL.CA: score=17.36 buy_ready=False sector_rank=5 price=311.06 support=273.1 resistance=340.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:17 AM market time freshness=DELAYED_CURRENT RSI=43.6 liquidity=958375.5 spike=0.09
- ZEOT.CA: score=20.27 buy_ready=False sector_rank=5 price=12.1 support=10.6 resistance=12.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:17 AM market time freshness=DELAYED_CURRENT RSI=71.56 liquidity=5867603.5 spike=0.18
- ZMID.CA: score=24.4 buy_ready=False sector_rank=6 price=7.5 support=6.19 resistance=7.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=70.62 liquidity=36544548.0 spike=0.15

## Backtesting Lite
- MPCO.CA: 180d return=9.04%, max drawdown=-20.56%, MA20>MA50 days last20=20, as_of=2026-07-27T21:00:00+00:00
- ATQA.CA: 180d return=-1.65%, max drawdown=-22.5%, MA20>MA50 days last20=1, as_of=2026-07-27T21:00:00+00:00
- ARCC.CA: 180d return=38.6%, max drawdown=-12.39%, MA20>MA50 days last20=6, as_of=2026-07-27T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- MPCO.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=574 sources=3 expected=Mansoura Poultry summary=Mansoura Poultry’s consolidated net profits drop in 2025; revenues near EGP 857m; Mansoura Poultry’s stock rebounds from key support level; Mansoura Poultry stock witnesses clear emergence of buying power
  - Mansoura Poultry’s consolidated net profits drop in 2025; revenues near EGP 857m: https://english.mubasher.info/news/4596342/Mansoura-Poultry-s-consolidated-net-profits-drop-in-2025-revenues-near-EGP-857m/
  - Mansoura Poultry’s stock rebounds from key support level: https://english.mubasher.info/news/4554482/Mansoura-Poultry-s-stock-rebounds-from-key-support-level/
  - Mansoura Poultry stock witnesses clear emergence of buying power: https://english.mubasher.info/news/4539119/Mansoura-Poultry-stock-witnesses-clear-emergence-of-buying-power/
- ATQA.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Misr National Steel Ataqa summary=Evidence rejected for ATQA.CA: source text did not clearly match ATQA.CA / Misr National Steel Ataqa.
- ARCC.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=574 sources=3 expected=Arabian Cement Company summary=Arabian Cement to pay out EGP 2bn dividends for 2025; Arabian Cement’s EGM approves nearly EGP 8m capital cut; Arabian Cement’s consolidated profits near EGP 3.6bn in 2025
  - Arabian Cement to pay out EGP 2bn dividends for 2025: https://english.mubasher.info/news/4587912/Arabian-Cement-to-pay-out-EGP-2bn-dividends-for-2025/
  - Arabian Cement’s EGM approves nearly EGP 8m capital cut: https://english.mubasher.info/news/4583762/Arabian-Cement-s-EGM-approves-nearly-EGP-8m-capital-cut/
  - Arabian Cement’s consolidated profits near EGP 3.6bn in 2025: https://english.mubasher.info/news/4562679/Arabian-Cement-s-consolidated-profits-near-EGP-3-6bn-in-2025/
- COMI.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Commercial International Bank Egypt summary=Evidence rejected for COMI.CA: source text did not clearly match COMI.CA / Commercial International Bank Egypt.
- PHAR.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Egyptian International Pharmaceutical Industries summary=Evidence rejected for PHAR.CA: source text did not clearly match PHAR.CA / Egyptian International Pharmaceutical Industries.
- ORWE.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=574 sources=3 expected=Oriental Weavers summary=Oriental Weavers to disburse EGP 1.5/shr dividends for 2025; Oriental Weavers’ consolidated profits cross EGP 2.2bn in 2025; Oriental Weavers generates EGP 12.5bn consolidated sales in H1-25
  - Oriental Weavers to disburse EGP 1.5/shr dividends for 2025: https://english.mubasher.info/news/4590236/Oriental-Weavers-to-disburse-EGP-1-5-shr-dividends-for-2025/
  - Oriental Weavers’ consolidated profits cross EGP 2.2bn in 2025: https://english.mubasher.info/news/4562972/Oriental-Weavers-consolidated-profits-cross-EGP-2-2bn-in-2025/
  - Oriental Weavers generates EGP 12.5bn consolidated sales in H1-25: https://english.mubasher.info/news/4487417/Oriental-Weavers-generates-EGP-12-5bn-consolidated-sales-in-H1-25/
- ORHD.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Orascom Development Egypt summary=Evidence rejected for ORHD.CA: source text did not clearly match ORHD.CA / Orascom Development Egypt.
- ADIB.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Abu Dhabi Islamic Bank Egypt summary=ADIB Egypt’s consolidated profits leap to EGP 3.6bn in Q1-26; ADIB Egypt stock approaches breakout above EGP 41; ADIB Egypt’s stock holds uptrend despite corrections
  - ADIB Egypt’s consolidated profits leap to EGP 3.6bn in Q1-26: https://english.mubasher.info/news/4607278/ADIB-Egypt-s-consolidated-profits-leap-to-EGP-3-6bn-in-Q1-26/
  - ADIB Egypt stock approaches breakout above EGP 41: https://english.mubasher.info/news/4591391/ADIB-Egypt-stock-approaches-breakout-above-EGP-41/
  - ADIB Egypt’s stock holds uptrend despite corrections: https://english.mubasher.info/news/4562331/ADIB-Egypt-s-stock-holds-uptrend-despite-corrections/

## Warnings
- Evidence for MPCO.CA matches the company but appears old; latest detected date is 2025-01-01.
- Gemini batch evidence failed: Server disconnected without sending a response.
- Evidence rejected for ATQA.CA: source text did not clearly match ATQA.CA / Misr National Steel Ataqa.
- Evidence for ARCC.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for COMI.CA: source text did not clearly match COMI.CA / Commercial International Bank Egypt.
- Evidence rejected for PHAR.CA: source text did not clearly match PHAR.CA / Egyptian International Pharmaceutical Industries.
- Evidence for ORWE.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for ORHD.CA: source text did not clearly match ORHD.CA / Orascom Development Egypt.
- Evidence for ADIB.CA matches the company but no source/report date was detected.
