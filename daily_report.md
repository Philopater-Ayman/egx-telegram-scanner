# Telegram-First EGX Scanner Report

Scan phase: Intraday liquidity update
Generated UTC: 2026-08-25T08:38:34.280678+00:00
Generated Cairo: 2026-08-25 11:38
Run timing: target 11:00 Cairo | generated Cairo 2026-08-25 11:38 | cron 0 8 * * 0-4
Trigger: scheduled cron=0 8 * * 0-4 mapped to intraday; Cairo now 2026-08-25 11:34

## Control Center
- Action tickets: 3 prioritized signal(s)
- BUY-ready candidates: 57
- Data quality issues: 1
- Tradeable price/liquidity tickers: 164/189
- Top sector: Textiles

## Market Context
- Market trend: Bullish
- Source: Mubasher EGX market page (delayed public data)
- As of: Tuesday, August 25
- Freshness: DELAYED
- EGX30 regime: BULLISH / above MA20 77.78% / above MA50 77.78%
- EGX70 regime: MIXED / above MA20 60.53% / above MA50 78.95%
- Sector breadth: 42.86%
- Risk mode: SELECTIVE_SWING_TRADES_ONLY

## Top Liquidity
- COMI.CA: liquidity=270185920.0 spike=0.59 score=24.4
- ORAS.CA: liquidity=216614368.0 spike=1.0 score=7.6
- GTWL.CA: liquidity=184652640.0 spike=1.0 score=8.76
- CCRS.CA: liquidity=163146624.0 spike=10.23 score=13.76
- LUTS.CA: liquidity=149902752.0 spike=0.93 score=8.76

## AI Narrative
- Provider: OpenRouter OK
- Model: nvidia/nemotron-3-super-120b-a12b:free
- Summary: Scanner flagged EFIH.CA, FWRY.CA and CLHO.CA as BUY SETUPs because each shows price above its MA20/MA50, adequate liquidity, defined support/resistance and a BULLISH_WATCH outlook, though confidence is low and liquidity is cooling.

## Top Liquidity Spikes
- CCRS.CA: spike=10.23 liquidity=163146624.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- CFGH.CA: spike=3.83 liquidity=58682.31 outlook=WEAK_OR_RISKY score=25.4 buy_ready=False
- TRTO.CA: spike=2.83 liquidity=31244.54 outlook=NEUTRAL score=49.4 buy_ready=False
- AFDI.CA: spike=2.28 liquidity=57132376.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- ALUM.CA: spike=2.12 liquidity=42668716.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False

## Sector Leaderboard
- #1 Textiles: score=10.94 5d=1.79% 20d=20.36% aboveMA50=100.0%
- #2 Healthcare: score=9.07 5d=-2.3% 20d=18.92% aboveMA50=100.0%
- #3 Transportation & Logistics: score=8.95 5d=-1.1% 20d=16.27% aboveMA50=100.0%
- #4 Education: score=8.43 5d=0.13% 20d=15.22% aboveMA50=100.0%
- #5 Investment Holding: score=8.37 5d=2.73% 20d=4.52% aboveMA50=100.0%
- #6 Agriculture & Food Production: score=8.1 5d=1.4% 20d=14.66% aboveMA50=100.0%
- #7 Banking & Financials: score=7.66 5d=0.29% 20d=9.27% aboveMA50=90.0%
- #8 Fintech & Payments: score=7.64 5d=1.41% 20d=3.41% aboveMA50=100.0%

## Today's Prioritized Action Tickets
- Priority #1: BUY EFIH.CA
  - Entry: 23.76 | Take profit: 25.27 | Stop loss: 23.27
  - Confidence: LOW | score=26.4 | outlook=BULLISH_WATCH 78.64
  - Reason: BUY SETUP: EFIH.CA has aligned current price data, liquidity above threshold, price above MA20/MA50, RSI 61.6, support 22.15, resistance 25.4, and evidence sources. Macro trend is Bullish; market regime is SELECTIVE_SWING_TRADES_ONLY; verify price action in Thndr before treating it as a swing entry.
- Priority #2: BUY FWRY.CA
  - Entry: 19.1 | Take profit: 19.9 | Stop loss: 18.7
  - Confidence: LOW | score=26.4 | outlook=BULLISH_WATCH 72.64
  - Reason: BUY SETUP: FWRY.CA has aligned current price data, liquidity above threshold, price above MA20/MA50, RSI 56.34, support 18.69, resistance 19.81, and evidence sources. Macro trend is Bullish; market regime is SELECTIVE_SWING_TRADES_ONLY; verify price action in Thndr before treating it as a swing entry.
- Priority #3: BUY CLHO.CA
  - Entry: 17.42 | Take profit: 19.62 | Stop loss: 17.04
  - Confidence: LOW | score=26.4 | outlook=BULLISH_WATCH 73.07
  - Reason: BUY SETUP: CLHO.CA has aligned current price data, liquidity above threshold, price above MA20/MA50, RSI 37.94, support 16.0, resistance 19.72, and evidence sources. Macro trend is Bullish; market regime is SELECTIVE_SWING_TRADES_ONLY; verify price action in Thndr before treating it as a swing entry.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- UNIT.CA: BULLISH_WATCH score=92.72 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- EBSC.CA: BULLISH_WATCH score=92.4 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- ALCN.CA: BULLISH_WATCH score=86.95 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; momentum is extended
- RMDA.CA: BULLISH_WATCH score=85.07 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; far above support
- KABO.CA: BULLISH_WATCH score=82 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; momentum is extended
- PHAR.CA: BULLISH_WATCH score=79.07 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; far above support; high short-term volatility
- EFIH.CA: BULLISH_WATCH score=78.64 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; sector is not leading
- SPIN.CA: BULLISH_WATCH score=78 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; momentum is extended; far above support
- PRDC.CA: BULLISH_WATCH score=77.72 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; sector is not leading
- SCTS.CA: BULLISH_WATCH score=76.43 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; momentum is extended

## BUY-Ready Candidates
- EFIH.CA: rank=26.4 outlook=BULLISH_WATCH outlook_score=78.64 sector_rank=8 price=23.76 support=22.15 resistance=25.4 liquidity=20627796.0
- FWRY.CA: rank=26.4 outlook=BULLISH_WATCH outlook_score=72.64 sector_rank=8 price=19.1 support=18.69 resistance=19.81 liquidity=41931160.0
- CLHO.CA: rank=26.4 outlook=BULLISH_WATCH outlook_score=73.07 sector_rank=2 price=17.42 support=16.0 resistance=19.72 liquidity=15486549.0
- PHAR.CA: rank=26.4 outlook=BULLISH_WATCH outlook_score=79.07 sector_rank=2 price=133.36 support=92.1 resistance=178.99 liquidity=48913372.0
- TALM.CA: rank=25.91 outlook=BULLISH_WATCH outlook_score=74.43 sector_rank=4 price=19.0 support=15.7 resistance=20.49 liquidity=9513583.0
- EBSC.CA: rank=25.54 outlook=BULLISH_WATCH outlook_score=92.4 sector_rank=13 price=1.95 support=1.85 resistance=2.06 liquidity=10221409.0
- CPCI.CA: rank=25.46 outlook=BULLISH_WATCH outlook_score=74.4 sector_rank=13 price=551.38 support=440.01 resistance=644.0 liquidity=14781395.17
- UNIT.CA: rank=25.23 outlook=BULLISH_WATCH outlook_score=92.72 sector_rank=12 price=19.21 support=17.32 resistance=23.0 liquidity=19272316.32
- RMDA.CA: rank=24.61 outlook=BULLISH_WATCH outlook_score=85.07 sector_rank=2 price=6.12 support=5.08 resistance=7.39 liquidity=8205500.0
- COMI.CA: rank=24.4 outlook=BULLISH_WATCH outlook_score=71.66 sector_rank=7 price=140.48 support=135.35 resistance=142.88 liquidity=270185920.0

## Data Quality Issues
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=21.46 buy_ready=True sector_rank=13 price=328.02 support=236.15 resistance=375.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:20 AM market time freshness=DELAYED_CURRENT RSI=63.58 liquidity=5695756.5 spike=0.09
- ABUK.CA: score=23.89 buy_ready=False sector_rank=11 price=76.51 support=70.6 resistance=80.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=73.7 liquidity=14106415.0 spike=0.13
- ACAMD.CA: score=13.76 buy_ready=False sector_rank=13 price=2.03 support=2.05 resistance=2.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:21 AM market time freshness=DELAYED_CURRENT RSI=24.98 liquidity=23182112.0 spike=0.41
- ACGC.CA: score=23.71 buy_ready=False sector_rank=1 price=13.77 support=10.12 resistance=13.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=79.02 liquidity=7305235.5 spike=0.16
- ADCI.CA: score=15.08 buy_ready=True sector_rank=13 price=294.73 support=245.0 resistance=389.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:17 AM market time freshness=DELAYED_CURRENT RSI=46.79 liquidity=1321736.13 spike=0.06
- ADIB.CA: score=19.38 buy_ready=True sector_rank=7 price=54.05 support=49.01 resistance=55.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=64.5 liquidity=4977747.5 spike=0.05
- ADPC.CA: score=17.17 buy_ready=False sector_rank=13 price=3.92 support=3.81 resistance=4.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:20 AM market time freshness=DELAYED_CURRENT RSI=55.88 liquidity=5407909.0 spike=0.1
- AFDI.CA: score=11.32 buy_ready=False sector_rank=13 price=60.45 support=58.11 resistance=65.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:21 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=57132376.0 spike=2.28
- AFMC.CA: score=21.76 buy_ready=True sector_rank=13 price=234.3 support=102.11 resistance=300.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:20 AM market time freshness=DELAYED_CURRENT RSI=68.82 liquidity=13530514.0 spike=0.08
- AJWA.CA: score=19.53 buy_ready=False sector_rank=13 price=183.01 support=182.0 resistance=210.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:20 AM market time freshness=DELAYED_CURRENT RSI=50.45 liquidity=7766941.0 spike=0.16
- ALCN.CA: score=19.46 buy_ready=True sector_rank=3 price=30.91 support=28.8 resistance=32.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=64.04 liquidity=2055694.63 spike=0.08
- ALUM.CA: score=11.0 buy_ready=False sector_rank=13 price=30.13 support=29.5 resistance=30.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:21 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=42668716.0 spike=2.12
- AMER.CA: score=23.89 buy_ready=True sector_rank=12 price=5.95 support=4.22 resistance=8.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:20 AM market time freshness=DELAYED_CURRENT RSI=59.78 liquidity=16426959.0 spike=0.17
- AMES.CA: score=20.76 buy_ready=False sector_rank=13 price=152.52 support=110.54 resistance=173.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:21 AM market time freshness=DELAYED_CURRENT RSI=76.07 liquidity=36505160.0 spike=0.5
- AMIA.CA: score=22.76 buy_ready=False sector_rank=13 price=19.16 support=10.27 resistance=19.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:21 AM market time freshness=DELAYED_CURRENT RSI=96.11 liquidity=16792518.0 spike=0.44
- AMOC.CA: score=21.4 buy_ready=False sector_rank=9 price=10.87 support=8.23 resistance=12.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:20 AM market time freshness=DELAYED_CURRENT RSI=77.51 liquidity=32736346.0 spike=0.24
- APSW.CA: score=8.15 buy_ready=False sector_rank=13 price=8.6 support=8.6 resistance=9.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:18 AM market time freshness=DELAYED_CURRENT RSI=44.07 liquidity=392859.5 spike=0.22
- ARAB.CA: score=23.89 buy_ready=True sector_rank=12 price=0.25 support=0.23 resistance=0.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:20 AM market time freshness=DELAYED_CURRENT RSI=56.76 liquidity=51167696.0 spike=0.63
- ARCC.CA: score=8.14 buy_ready=False sector_rank=15 price=77.96 support=75.98 resistance=78.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:20 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=41073708.0 spike=0.43
- AREH.CA: score=12.32 buy_ready=False sector_rank=13 price=1.49 support=1.38 resistance=1.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:20 AM market time freshness=DELAYED_CURRENT RSI=42.5 liquidity=3556951.5 spike=0.11
- ARVA.CA: score=8.76 buy_ready=False sector_rank=13 price=14.99 support=14.45 resistance=14.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=16 August 01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=30473338.0 spike=0.56
- ASCM.CA: score=14.86 buy_ready=False sector_rank=13 price=63.25 support=61.0 resistance=69.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:20 AM market time freshness=DELAYED_CURRENT RSI=33.24 liquidity=8096218.5 spike=0.14
- ASPI.CA: score=22.83 buy_ready=True sector_rank=13 price=0.52 support=0.39 resistance=0.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=69.88 liquidity=9067180.0 spike=0.22
- ATLC.CA: score=15.02 buy_ready=True sector_rank=16 price=5.5 support=5.0 resistance=5.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:17 AM market time freshness=DELAYED_CURRENT RSI=60.63 liquidity=2264601.75 spike=0.12
- ATQA.CA: score=20.89 buy_ready=False sector_rank=11 price=11.12 support=9.66 resistance=11.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:20 AM market time freshness=DELAYED_CURRENT RSI=78.37 liquidity=12084206.0 spike=0.15
- AXPH.CA: score=18.93 buy_ready=False sector_rank=13 price=1526.24 support=1121.56 resistance=1630.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:20 AM market time freshness=DELAYED_CURRENT RSI=74.33 liquidity=3173074.5 spike=0.4
- BINV.CA: score=16.04 buy_ready=True sector_rank=5 price=49.0 support=46.01 resistance=50.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=38.86 liquidity=1638199.13 spike=0.25
- BIOC.CA: score=23.76 buy_ready=True sector_rank=13 price=470.11 support=119.32 resistance=563.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:21 AM market time freshness=DELAYED_CURRENT RSI=63.88 liquidity=32452546.0 spike=0.13
- BTFH.CA: score=16.75 buy_ready=False sector_rank=16 price=2.96 support=2.98 resistance=3.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:20 AM market time freshness=DELAYED_CURRENT RSI=35.0 liquidity=22846850.0 spike=0.11
- CAED.CA: score=20.76 buy_ready=False sector_rank=13 price=162.32 support=118.01 resistance=185.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:20 AM market time freshness=DELAYED_CURRENT RSI=86.84 liquidity=22544758.0 spike=0.42
- CANA.CA: score=13.63 buy_ready=False sector_rank=7 price=42.22 support=36.5 resistance=43.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:18 AM market time freshness=DELAYED_CURRENT RSI=75.78 liquidity=2231067.0 spike=0.11
- CCAP.CA: score=23.4 buy_ready=False sector_rank=5 price=5.75 support=5.14 resistance=5.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:20 AM market time freshness=DELAYED_CURRENT RSI=78.35 liquidity=91386432.0 spike=0.14
- CCRS.CA: score=13.76 buy_ready=False sector_rank=13 price=3.05 support=2.88 resistance=3.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:21 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=163146624.0 spike=10.23
- CEFM.CA: score=15.81 buy_ready=True sector_rank=13 price=148.3 support=121.4 resistance=168.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=69.01 liquidity=2054324.0 spike=0.06
- CERA.CA: score=10.31 buy_ready=False sector_rank=13 price=1.29 support=1.23 resistance=1.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=55.0 liquidity=1548501.62 spike=0.1
- CFGH.CA: score=17.82 buy_ready=False sector_rank=13 price=0.12 support=0.1 resistance=0.12 source=Yahoo Finance as_of=2026-08-22T21:00:00+00:00 freshness=FRESH RSI=83.33 liquidity=58682.31 spike=3.83
- CICH.CA: score=7.45 buy_ready=False sector_rank=16 price=12.4 support=11.92 resistance=13.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:20 AM market time freshness=DELAYED_CURRENT RSI=30.5 liquidity=1693412.75 spike=0.24
- CIEB.CA: score=16.52 buy_ready=True sector_rank=7 price=25.0 support=23.75 resistance=25.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:18 AM market time freshness=DELAYED_CURRENT RSI=66.67 liquidity=2123586.75 spike=0.16
- CIRA.CA: score=13.96 buy_ready=False sector_rank=4 price=35.99 support=31.8 resistance=40.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=51.39 liquidity=1564955.63 spike=0.03
- CLHO.CA: score=26.4 buy_ready=True sector_rank=2 price=17.42 support=16.0 resistance=19.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:20 AM market time freshness=DELAYED_CURRENT RSI=37.94 liquidity=15486549.0 spike=0.26
- CNFN.CA: score=14.2 buy_ready=False sector_rank=16 price=4.83 support=4.68 resistance=5.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:20 AM market time freshness=DELAYED_CURRENT RSI=54.1 liquidity=3443900.0 spike=0.17
- COMI.CA: score=24.4 buy_ready=True sector_rank=7 price=140.48 support=135.35 resistance=142.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=40.98 liquidity=270185920.0 spike=0.59
- COPR.CA: score=22.76 buy_ready=False sector_rank=13 price=0.55 support=0.39 resistance=0.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:21 AM market time freshness=DELAYED_CURRENT RSI=79.04 liquidity=42754780.0 spike=0.51
- COSG.CA: score=25.76 buy_ready=False sector_rank=13 price=1.88 support=1.6 resistance=1.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:20 AM market time freshness=DELAYED_CURRENT RSI=71.79 liquidity=25199720.0 spike=0.48
- CPCI.CA: score=25.46 buy_ready=True sector_rank=13 price=551.38 support=440.01 resistance=644.0 source=Yahoo Finance as_of=2026-08-22T21:00:00+00:00 freshness=FRESH RSI=66.57 liquidity=14781395.17 spike=1.85
- CSAG.CA: score=14.82 buy_ready=False sector_rank=3 price=40.4 support=31.35 resistance=43.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=76.6 liquidity=2416292.75 spike=0.1
- DAPH.CA: score=19.22 buy_ready=True sector_rank=13 price=113.86 support=92.1 resistance=147.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:20 AM market time freshness=DELAYED_CURRENT RSI=63.87 liquidity=5458960.5 spike=0.12
- DEIN.CA: score=-1.24 buy_ready=False sector_rank=13 price=11.38 support=13.65 resistance=13.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 June 12:11 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=40.95 spike=0.01
- DOMT.CA: score=14.17 buy_ready=False sector_rank=17 price=28.04 support=26.01 resistance=32.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=51.01 liquidity=3467456.25 spike=0.23
- DSCW.CA: score=16.53 buy_ready=False sector_rank=13 price=1.89 support=1.89 resistance=2.21 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:21 AM market time freshness=DELAYED_CURRENT RSI=40.82 liquidity=7770278.5 spike=0.09
- DTPP.CA: score=18.05 buy_ready=False sector_rank=13 price=294.81 support=235.59 resistance=340.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:20 AM market time freshness=DELAYED_CURRENT RSI=71.59 liquidity=6285032.5 spike=0.12
- EALR.CA: score=18.51 buy_ready=True sector_rank=13 price=406.84 support=363.0 resistance=471.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:21 AM market time freshness=DELAYED_CURRENT RSI=55.18 liquidity=2749101.25 spike=0.06
- EASB.CA: score=16.69 buy_ready=True sector_rank=13 price=7.41 support=6.71 resistance=8.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:20 AM market time freshness=DELAYED_CURRENT RSI=50.59 liquidity=2927623.75 spike=0.32
- EAST.CA: score=14.57 buy_ready=False sector_rank=17 price=35.51 support=36.0 resistance=37.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=49.67 liquidity=5862757.0 spike=0.1
- EBSC.CA: score=25.54 buy_ready=True sector_rank=13 price=1.95 support=1.85 resistance=2.06 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:21 AM market time freshness=DELAYED_CURRENT RSI=45.83 liquidity=10221409.0 spike=1.89
- ECAP.CA: score=10.74 buy_ready=False sector_rank=13 price=34.5 support=33.51 resistance=36.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:21 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=24643772.0 spike=1.99
- EDFM.CA: score=14.16 buy_ready=False sector_rank=13 price=407.25 support=352.0 resistance=425.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=59.2 liquidity=403605.19 spike=0.12
- EEII.CA: score=23.61 buy_ready=True sector_rank=13 price=2.96 support=2.54 resistance=3.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:21 AM market time freshness=DELAYED_CURRENT RSI=56.39 liquidity=7853060.0 spike=0.31
- EFIC.CA: score=22.89 buy_ready=False sector_rank=11 price=203.82 support=184.0 resistance=260.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:20 AM market time freshness=DELAYED_CURRENT RSI=64.82 liquidity=12228006.0 spike=0.27
- EFID.CA: score=12.15 buy_ready=False sector_rank=17 price=32.07 support=26.64 resistance=34.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:20 AM market time freshness=DELAYED_CURRENT RSI=84.76 liquidity=2446216.5 spike=0.03
- EFIH.CA: score=26.4 buy_ready=True sector_rank=8 price=23.76 support=22.15 resistance=25.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=61.6 liquidity=20627796.0 spike=0.17
- EGAL.CA: score=9.33 buy_ready=False sector_rank=11 price=355.0 support=345.0 resistance=355.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=126721592.0 spike=1.22
- EGAS.CA: score=15.61 buy_ready=True sector_rank=9 price=58.15 support=50.0 resistance=67.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=45.91 liquidity=1210879.88 spike=0.05
- EGBE.CA: score=12.54 buy_ready=False sector_rank=7 price=0.55 support=0.47 resistance=0.57 source=Yahoo Finance as_of=2026-08-22T21:00:00+00:00 freshness=FRESH RSI=66.14 liquidity=139420.27 spike=0.76
- EGCH.CA: score=20.3 buy_ready=False sector_rank=11 price=13.8 support=12.69 resistance=14.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=41.24 liquidity=8413064.0 spike=0.07
- EGSA.CA: score=4.09 buy_ready=False sector_rank=10 price=8.69 support=8.65 resistance=9.0 source=Yahoo Finance as_of=2026-08-22T21:00:00+00:00 freshness=FRESH RSI=20.0 liquidity=1738.0 spike=0.15
- EGTS.CA: score=9.99 buy_ready=False sector_rank=12 price=17.02 support=16.17 resistance=20.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=47.95 liquidity=1097421.63 spike=0.03
- EHDR.CA: score=17.29 buy_ready=True sector_rank=13 price=2.94 support=2.71 resistance=3.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:18 AM market time freshness=DELAYED_CURRENT RSI=63.41 liquidity=3530071.0 spike=0.09
- EKHO.CA: score=10.4 buy_ready=False sector_rank=9 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-08-22T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=10.66 buy_ready=False sector_rank=19 price=2.09 support=2.06 resistance=2.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:20 AM market time freshness=DELAYED_CURRENT RSI=31.58 liquidity=14176482.0 spike=0.25
- ELKA.CA: score=14.84 buy_ready=False sector_rank=13 price=1.73 support=1.69 resistance=2.06 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:21 AM market time freshness=DELAYED_CURRENT RSI=55.56 liquidity=3077138.25 spike=0.05
- ELNA.CA: score=9.01 buy_ready=False sector_rank=13 price=37.01 support=36.1 resistance=39.37 source=Yahoo Finance as_of=2026-08-22T21:00:00+00:00 freshness=FRESH RSI=44.41 liquidity=531019.46 spike=1.36
- ELSH.CA: score=10.74 buy_ready=False sector_rank=13 price=13.23 support=13.14 resistance=15.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:17 AM market time freshness=DELAYED_CURRENT RSI=37.58 liquidity=1981558.5 spike=0.03
- ELWA.CA: score=-0.21 buy_ready=False sector_rank=13 price=1.95 support=1.92 resistance=1.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:20 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=1032989.69 spike=0.59
- EMFD.CA: score=23.89 buy_ready=True sector_rank=12 price=12.25 support=11.08 resistance=12.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=66.67 liquidity=47737852.0 spike=0.68
- ENGC.CA: score=16.33 buy_ready=False sector_rank=13 price=46.2 support=40.11 resistance=54.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=61.43 liquidity=4573129.5 spike=0.16
- EOSB.CA: score=15.78 buy_ready=False sector_rank=13 price=1.55 support=1.53 resistance=1.62 source=Yahoo Finance as_of=2026-08-22T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=15500.0 spike=0.37
- EPCO.CA: score=14.38 buy_ready=False sector_rank=13 price=10.94 support=10.32 resistance=13.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:18 AM market time freshness=DELAYED_CURRENT RSI=49.62 liquidity=2617064.0 spike=0.11
- EPPK.CA: score=5.46 buy_ready=False sector_rank=13 price=12.58 support=12.3 resistance=15.93 source=Yahoo Finance as_of=2026-08-22T21:00:00+00:00 freshness=FRESH RSI=22.0 liquidity=883417.91 spike=1.41
- ETEL.CA: score=24.09 buy_ready=True sector_rank=10 price=116.84 support=102.51 resistance=120.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:20 AM market time freshness=DELAYED_CURRENT RSI=69.75 liquidity=10672652.0 spike=0.08
- ETRS.CA: score=15.38 buy_ready=True sector_rank=13 price=10.88 support=10.21 resistance=11.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:20 AM market time freshness=DELAYED_CURRENT RSI=66.28 liquidity=1618888.0 spike=0.05
- EXPA.CA: score=22.4 buy_ready=False sector_rank=7 price=20.2 support=19.6 resistance=21.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:20 AM market time freshness=DELAYED_CURRENT RSI=41.61 liquidity=14261108.0 spike=0.37
- FAIT.CA: score=14.18 buy_ready=False sector_rank=7 price=42.08 support=36.1 resistance=43.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:13 AM market time freshness=DELAYED_CURRENT RSI=75.23 liquidity=775039.81 spike=0.17
- FAITA.CA: score=14.42 buy_ready=False sector_rank=7 price=0.99 support=0.96 resistance=1.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:01 AM market time freshness=DELAYED_CURRENT RSI=69.49 liquidity=21627.3 spike=0.43
- FERC.CA: score=19.02 buy_ready=True sector_rank=11 price=80.09 support=75.01 resistance=87.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:20 AM market time freshness=DELAYED_CURRENT RSI=55.64 liquidity=5129151.0 spike=0.26
- FWRY.CA: score=26.4 buy_ready=True sector_rank=8 price=19.1 support=18.69 resistance=19.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=56.34 liquidity=41931160.0 spike=0.36
- GBCO.CA: score=15.4 buy_ready=False sector_rank=21 price=28.68 support=29.31 resistance=33.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:20 AM market time freshness=DELAYED_CURRENT RSI=35.11 liquidity=37099128.0 spike=0.8
- GDWA.CA: score=9.21 buy_ready=False sector_rank=13 price=0.78 support=0.78 resistance=0.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:21 AM market time freshness=DELAYED_CURRENT RSI=32.81 liquidity=6449656.5 spike=0.07
- GGCC.CA: score=14.01 buy_ready=False sector_rank=13 price=0.92 support=0.81 resistance=1.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:21 AM market time freshness=DELAYED_CURRENT RSI=52.91 liquidity=2250973.5 spike=0.05
- GIHD.CA: score=23.02 buy_ready=True sector_rank=13 price=63.98 support=56.51 resistance=76.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:21 AM market time freshness=DELAYED_CURRENT RSI=56.94 liquidity=9258934.0 spike=0.23
- GMCI.CA: score=4.32 buy_ready=False sector_rank=13 price=1.9 support=1.88 resistance=2.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=22.22 liquidity=562984.0 spike=0.98
- GRCA.CA: score=9.34 buy_ready=False sector_rank=13 price=80.39 support=76.8 resistance=81.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:21 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=45858652.0 spike=1.29
- GSSC.CA: score=17.22 buy_ready=True sector_rank=13 price=290.92 support=265.01 resistance=301.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:21 AM market time freshness=DELAYED_CURRENT RSI=49.27 liquidity=3464577.25 spike=0.19
- GTWL.CA: score=8.76 buy_ready=False sector_rank=13 price=203.0 support=201.3 resistance=219.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:21 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=184652640.0 spike=1.0
- HDBK.CA: score=16.32 buy_ready=False sector_rank=7 price=91.97 support=80.8 resistance=93.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:18 AM market time freshness=DELAYED_CURRENT RSI=78.97 liquidity=8920825.0 spike=0.22
- HELI.CA: score=16.89 buy_ready=False sector_rank=12 price=7.45 support=7.5 resistance=8.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=25.19 liquidity=28936150.0 spike=0.18
- HRHO.CA: score=16.75 buy_ready=False sector_rank=16 price=25.91 support=25.95 resistance=28.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=44.14 liquidity=54168076.0 spike=0.57
- ICID.CA: score=17.1 buy_ready=False sector_rank=13 price=17.17 support=7.85 resistance=18.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:20 AM market time freshness=DELAYED_CURRENT RSI=99.08 liquidity=4341690.0 spike=0.18
- IDRE.CA: score=15.45 buy_ready=True sector_rank=13 price=52.97 support=46.04 resistance=58.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT RSI=64.36 liquidity=1688647.5 spike=0.06
- IFAP.CA: score=13.63 buy_ready=False sector_rank=6 price=20.63 support=19.0 resistance=22.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:18 AM market time freshness=DELAYED_CURRENT RSI=58.05 liquidity=1229408.13 spike=0.04
- INFI.CA: score=8.76 buy_ready=False sector_rank=13 price=166.67 support=163.0 resistance=168.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:20 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=14884528.0 spike=0.24
- IRON.CA: score=11.59 buy_ready=False sector_rank=11 price=30.68 support=30.14 resistance=34.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=48.87 liquidity=3703442.5 spike=0.33
- ISMA.CA: score=13.5 buy_ready=False sector_rank=13 price=35.0 support=29.5 resistance=36.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:20 AM market time freshness=DELAYED_CURRENT RSI=80.26 liquidity=2743077.25 spike=0.09
- ISMQ.CA: score=13.84 buy_ready=False sector_rank=11 price=9.13 support=8.96 resistance=9.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:20 AM market time freshness=DELAYED_CURRENT RSI=54.95 liquidity=4947822.0 spike=0.09
- ISPH.CA: score=21.92 buy_ready=True sector_rank=2 price=13.1 support=11.3 resistance=16.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:20 AM market time freshness=DELAYED_CURRENT RSI=35.78 liquidity=5521016.5 spike=0.03
- JUFO.CA: score=9.47 buy_ready=False sector_rank=17 price=26.94 support=22.78 resistance=29.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:18 AM market time freshness=DELAYED_CURRENT RSI=81.44 liquidity=3767442.0 spike=0.06
- KABO.CA: score=21.67 buy_ready=True sector_rank=1 price=9.02 support=7.75 resistance=9.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=67.9 liquidity=4270368.5 spike=0.1
- KWIN.CA: score=8.76 buy_ready=False sector_rank=13 price=111.2 support=101.01 resistance=111.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=38267476.0 spike=0.7
- KZPC.CA: score=20.76 buy_ready=False sector_rank=13 price=13.4 support=8.42 resistance=16.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:21 AM market time freshness=DELAYED_CURRENT RSI=83.65 liquidity=24982880.0 spike=0.57
- LCSW.CA: score=16.17 buy_ready=True sector_rank=15 price=34.71 support=30.2 resistance=37.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:20 AM market time freshness=DELAYED_CURRENT RSI=38.58 liquidity=3027891.25 spike=0.07
- LUTS.CA: score=8.76 buy_ready=False sector_rank=13 price=1.43 support=1.39 resistance=1.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:22 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=149902752.0 spike=0.93
- MAAL.CA: score=21.0 buy_ready=True sector_rank=13 price=9.19 support=8.32 resistance=9.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:22 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=7235585.5 spike=0.6
- MASR.CA: score=18.76 buy_ready=False sector_rank=13 price=7.59 support=7.45 resistance=8.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:21 AM market time freshness=DELAYED_CURRENT RSI=40.82 liquidity=16236679.0 spike=0.24
- MBSC.CA: score=8.03 buy_ready=False sector_rank=15 price=385.34 support=380.01 resistance=389.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=9891070.0 spike=0.13
- MCQE.CA: score=8.14 buy_ready=False sector_rank=15 price=235.0 support=230.04 resistance=239.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:20 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=16710855.0 spike=0.33
- MCRO.CA: score=17.46 buy_ready=False sector_rank=13 price=1.52 support=1.44 resistance=1.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:21 AM market time freshness=DELAYED_CURRENT RSI=46.15 liquidity=5697517.0 spike=0.03
- MENA.CA: score=12.22 buy_ready=False sector_rank=12 price=7.01 support=6.82 resistance=7.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=329404.06 spike=0.05
- MEPA.CA: score=13.42 buy_ready=False sector_rank=13 price=1.82 support=1.78 resistance=2.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:22 AM market time freshness=DELAYED_CURRENT RSI=41.46 liquidity=1657486.5 spike=0.03
- MFPC.CA: score=20.89 buy_ready=False sector_rank=11 price=40.11 support=35.37 resistance=41.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=77.31 liquidity=16426568.0 spike=0.2
- MFSC.CA: score=13.2 buy_ready=False sector_rank=13 price=49.51 support=46.02 resistance=65.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:21 AM market time freshness=DELAYED_CURRENT RSI=39.14 liquidity=1444556.25 spike=0.13
- MHOT.CA: score=12.42 buy_ready=False sector_rank=14 price=18.11 support=16.2 resistance=21.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:13 AM market time freshness=DELAYED_CURRENT RSI=59.4 liquidity=669881.63 spike=0.04
- MICH.CA: score=23.76 buy_ready=True sector_rank=13 price=51.81 support=39.01 resistance=53.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:21 AM market time freshness=DELAYED_CURRENT RSI=63.13 liquidity=31553202.0 spike=0.74
- MILS.CA: score=23.76 buy_ready=True sector_rank=13 price=224.99 support=167.0 resistance=248.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:21 AM market time freshness=DELAYED_CURRENT RSI=65.95 liquidity=29107976.0 spike=0.35
- MIPH.CA: score=20.1 buy_ready=True sector_rank=2 price=794.08 support=722.7 resistance=828.36 source=Yahoo Finance as_of=2026-08-22T21:00:00+00:00 freshness=FRESH RSI=39.31 liquidity=3699618.8 spike=0.94
- MOED.CA: score=20.76 buy_ready=False sector_rank=13 price=0.81 support=0.65 resistance=0.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:22 AM market time freshness=DELAYED_CURRENT RSI=81.07 liquidity=36200700.0 spike=0.42
- MOIL.CA: score=18.95 buy_ready=False sector_rank=9 price=0.68 support=0.61 resistance=0.69 source=Yahoo Finance as_of=2026-08-22T21:00:00+00:00 freshness=FRESH RSI=54.64 liquidity=871802.57 spike=1.84
- MOIN.CA: score=13.48 buy_ready=True sector_rank=13 price=34.72 support=23.11 resistance=40.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:20 AM market time freshness=DELAYED_CURRENT RSI=69.79 liquidity=1716630.38 spike=0.06
- MOSC.CA: score=13.2 buy_ready=False sector_rank=13 price=336.29 support=282.0 resistance=380.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=77.62 liquidity=2442402.0 spike=0.17
- MPCI.CA: score=25.76 buy_ready=False sector_rank=13 price=415.84 support=281.05 resistance=460.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:20 AM market time freshness=DELAYED_CURRENT RSI=70.55 liquidity=44136904.0 spike=0.27
- MPCO.CA: score=23.4 buy_ready=False sector_rank=6 price=2.25 support=1.84 resistance=2.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=75.64 liquidity=13739613.0 spike=0.11
- MPRC.CA: score=17.75 buy_ready=False sector_rank=13 price=42.92 support=39.5 resistance=52.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:21 AM market time freshness=DELAYED_CURRENT RSI=42.42 liquidity=5991844.5 spike=0.22
- MTIE.CA: score=15.4 buy_ready=False sector_rank=21 price=8.71 support=8.01 resistance=10.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:20 AM market time freshness=DELAYED_CURRENT RSI=35.67 liquidity=14609988.0 spike=0.25
- NAHO.CA: score=10.8 buy_ready=False sector_rank=13 price=0.14 support=0.1 resistance=0.16 source=Yahoo Finance as_of=2026-08-22T21:00:00+00:00 freshness=FRESH RSI=90.38 liquidity=36038.01 spike=0.45
- NCCW.CA: score=10.98 buy_ready=False sector_rank=13 price=5.98 support=5.59 resistance=7.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:21 AM market time freshness=DELAYED_CURRENT RSI=54.1 liquidity=2220770.75 spike=0.07
- NEDA.CA: score=16.47 buy_ready=False sector_rank=13 price=2.79 support=2.7 resistance=2.97 source=Yahoo Finance as_of=2026-08-22T21:00:00+00:00 freshness=FRESH RSI=55.56 liquidity=708623.72 spike=0.9
- NHPS.CA: score=9.9 buy_ready=False sector_rank=13 price=95.96 support=91.71 resistance=98.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:21 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=67929160.0 spike=1.57
- NINH.CA: score=18.76 buy_ready=False sector_rank=13 price=23.21 support=21.22 resistance=25.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:22 AM market time freshness=DELAYED_CURRENT RSI=17.84 liquidity=28699980.0 spike=0.85
- NIPH.CA: score=24.4 buy_ready=True sector_rank=2 price=384.16 support=209.0 resistance=450.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:20 AM market time freshness=DELAYED_CURRENT RSI=65.73 liquidity=51408048.0 spike=0.16
- OBRI.CA: score=12.5 buy_ready=False sector_rank=13 price=32.12 support=31.61 resistance=35.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:22 AM market time freshness=DELAYED_CURRENT RSI=59.37 liquidity=2741994.5 spike=0.08
- OCDI.CA: score=21.89 buy_ready=True sector_rank=12 price=32.75 support=27.08 resistance=36.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:17 AM market time freshness=DELAYED_CURRENT RSI=67.61 liquidity=49543204.0 spike=0.36
- OCPH.CA: score=12.77 buy_ready=False sector_rank=13 price=262.93 support=225.0 resistance=483.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:22 AM market time freshness=DELAYED_CURRENT RSI=55.77 liquidity=2008424.63 spike=0.08
- ODIN.CA: score=8.76 buy_ready=False sector_rank=13 price=3.27 support=3.13 resistance=3.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:21 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=34563336.0 spike=0.82
- OFH.CA: score=22.76 buy_ready=False sector_rank=13 price=0.97 support=0.69 resistance=0.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:22 AM market time freshness=DELAYED_CURRENT RSI=91.73 liquidity=35771828.0 spike=0.47
- OIH.CA: score=21.4 buy_ready=False sector_rank=5 price=1.94 support=1.43 resistance=1.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=85.45 liquidity=35612196.0 spike=0.28
- OLFI.CA: score=12.69 buy_ready=False sector_rank=17 price=23.58 support=22.25 resistance=26.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:18 AM market time freshness=DELAYED_CURRENT RSI=53.52 liquidity=1985897.25 spike=0.03
- ORAS.CA: score=7.6 buy_ready=False sector_rank=18 price=807.46 support=781.02 resistance=812.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=216614368.0 spike=1.0
- ORHD.CA: score=23.89 buy_ready=True sector_rank=12 price=41.87 support=38.0 resistance=44.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=64.2 liquidity=10882737.0 spike=0.07
- ORWE.CA: score=23.85 buy_ready=False sector_rank=1 price=26.43 support=22.55 resistance=27.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:18 AM market time freshness=DELAYED_CURRENT RSI=74.75 liquidity=8447735.0 spike=0.11
- PHAR.CA: score=26.4 buy_ready=True sector_rank=2 price=133.36 support=92.1 resistance=178.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=42.5 liquidity=48913372.0 spike=0.11
- PHDC.CA: score=18.89 buy_ready=False sector_rank=12 price=14.75 support=14.32 resistance=16.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=56.41 liquidity=29039726.0 spike=0.12
- PHTV.CA: score=14.25 buy_ready=False sector_rank=13 price=355.69 support=311.11 resistance=447.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:21 AM market time freshness=DELAYED_CURRENT RSI=61.37 liquidity=492058.56 spike=0.18
- POUL.CA: score=9.42 buy_ready=False sector_rank=17 price=37.56 support=36.5 resistance=40.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=55.38 liquidity=1718523.63 spike=0.06
- PRCL.CA: score=12.31 buy_ready=False sector_rank=15 price=34.21 support=32.0 resistance=37.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:20 AM market time freshness=DELAYED_CURRENT RSI=39.88 liquidity=1171886.13 spike=0.04
- PRDC.CA: score=19.61 buy_ready=True sector_rank=12 price=9.49 support=8.7 resistance=9.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=50.22 liquidity=3718769.75 spike=0.06
- PRMH.CA: score=15.72 buy_ready=False sector_rank=13 price=2.47 support=2.35 resistance=2.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:22 AM market time freshness=DELAYED_CURRENT RSI=30.38 liquidity=24041580.0 spike=1.98
- RACC.CA: score=12.86 buy_ready=False sector_rank=13 price=9.83 support=9.8 resistance=10.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:22 AM market time freshness=DELAYED_CURRENT RSI=45.92 liquidity=4096745.0 spike=0.21
- RAKT.CA: score=2.95 buy_ready=False sector_rank=13 price=22.25 support=21.65 resistance=24.0 source=Yahoo Finance as_of=2026-08-22T21:00:00+00:00 freshness=FRESH RSI=9.2 liquidity=194843.25 spike=0.7
- RAYA.CA: score=5.55 buy_ready=False sector_rank=20 price=7.04 support=6.95 resistance=7.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=25.53 liquidity=4069798.5 spike=0.05
- RMDA.CA: score=24.61 buy_ready=True sector_rank=2 price=6.12 support=5.08 resistance=7.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=51.32 liquidity=8205500.0 spike=0.07
- ROTO.CA: score=23.69 buy_ready=True sector_rank=13 price=46.99 support=41.85 resistance=52.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=52.93 liquidity=9931850.0 spike=0.4
- RREI.CA: score=14.77 buy_ready=False sector_rank=13 price=4.54 support=3.85 resistance=5.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:21 AM market time freshness=DELAYED_CURRENT RSI=50.3 liquidity=3014316.25 spike=0.04
- RTVC.CA: score=5.46 buy_ready=False sector_rank=13 price=4.28 support=4.12 resistance=4.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:21 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=6700438.0 spike=0.91
- RUBX.CA: score=6.47 buy_ready=False sector_rank=13 price=13.23 support=13.15 resistance=13.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:20 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=7705166.0 spike=0.39
- SAUD.CA: score=12.62 buy_ready=False sector_rank=7 price=23.73 support=21.4 resistance=24.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=87.22 liquidity=1223046.25 spike=0.05
- SCEM.CA: score=23.14 buy_ready=True sector_rank=15 price=98.25 support=76.75 resistance=113.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:20 AM market time freshness=DELAYED_CURRENT RSI=65.03 liquidity=37636692.0 spike=0.18
- SCFM.CA: score=15.62 buy_ready=True sector_rank=13 price=286.11 support=271.51 resistance=319.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:21 AM market time freshness=DELAYED_CURRENT RSI=52.04 liquidity=1857145.5 spike=0.08
- SCTS.CA: score=19.28 buy_ready=True sector_rank=4 price=637.44 support=603.13 resistance=685.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:18 AM market time freshness=DELAYED_CURRENT RSI=68.46 liquidity=4876878.0 spike=0.52
- SDTI.CA: score=16.45 buy_ready=True sector_rank=13 price=70.61 support=51.75 resistance=75.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=66.82 liquidity=4685311.0 spike=0.15
- SEIG.CA: score=12.1 buy_ready=False sector_rank=13 price=264.14 support=242.1 resistance=295.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=40.99 liquidity=335463.66 spike=0.03
- SIPC.CA: score=18.51 buy_ready=True sector_rank=13 price=4.96 support=3.8 resistance=5.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:20 AM market time freshness=DELAYED_CURRENT RSI=51.98 liquidity=4752447.5 spike=0.08
- SKPC.CA: score=16.98 buy_ready=False sector_rank=11 price=17.41 support=15.61 resistance=18.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=77.7 liquidity=6092016.0 spike=0.09
- SMFR.CA: score=15.5 buy_ready=False sector_rank=13 price=267.34 support=228.88 resistance=309.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:21 AM market time freshness=DELAYED_CURRENT RSI=71.76 liquidity=3740251.0 spike=0.14
- SNFC.CA: score=18.51 buy_ready=False sector_rank=13 price=10.7 support=10.6 resistance=11.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:09 AM market time freshness=DELAYED_CURRENT RSI=46.31 liquidity=7751883.5 spike=0.64
- SPIN.CA: score=19.72 buy_ready=True sector_rank=1 price=18.98 support=15.05 resistance=21.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:18 AM market time freshness=DELAYED_CURRENT RSI=69.33 liquidity=2319863.25 spike=0.05
- SPMD.CA: score=7.94 buy_ready=False sector_rank=13 price=0.46 support=0.44 resistance=0.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:21 AM market time freshness=DELAYED_CURRENT RSI=31.15 liquidity=1182495.62 spike=0.04
- SUGR.CA: score=9.14 buy_ready=False sector_rank=17 price=59.35 support=58.4 resistance=60.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:20 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=40855624.0 spike=1.72
- SVCE.CA: score=8.76 buy_ready=False sector_rank=13 price=11.07 support=10.81 resistance=11.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:22 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=26476394.0 spike=0.27
- SWDY.CA: score=6.66 buy_ready=False sector_rank=19 price=127.0 support=126.0 resistance=128.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=11809181.0 spike=0.13
- TALM.CA: score=25.91 buy_ready=True sector_rank=4 price=19.0 support=15.7 resistance=20.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=55.95 liquidity=9513583.0 spike=0.22
- TMGH.CA: score=21.89 buy_ready=False sector_rank=12 price=97.49 support=95.2 resistance=100.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=51.94 liquidity=16884430.0 spike=0.06
- TRTO.CA: score=21.45 buy_ready=False sector_rank=13 price=0.05 support=0.03 resistance=0.05 source=Yahoo Finance as_of=2026-08-22T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=31244.54 spike=2.83
- UEFM.CA: score=14.41 buy_ready=False sector_rank=13 price=553.46 support=531.0 resistance=594.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:20 AM market time freshness=DELAYED_CURRENT RSI=52.6 liquidity=647326.5 spike=0.14
- UEGC.CA: score=2.67 buy_ready=False sector_rank=13 price=2.08 support=2.06 resistance=2.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:22 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=3914829.75 spike=0.11
- UNIP.CA: score=17.5 buy_ready=False sector_rank=13 price=0.38 support=0.35 resistance=0.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:22 AM market time freshness=DELAYED_CURRENT RSI=47.71 liquidity=5737306.0 spike=0.15
- UNIT.CA: score=25.23 buy_ready=True sector_rank=12 price=19.21 support=17.32 resistance=23.0 source=Yahoo Finance as_of=2026-08-22T21:00:00+00:00 freshness=FRESH RSI=57.67 liquidity=19272316.32 spike=1.67
- WCDF.CA: score=13.16 buy_ready=False sector_rank=13 price=645.12 support=571.0 resistance=700.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:17 AM market time freshness=DELAYED_CURRENT RSI=77.81 liquidity=403606.88 spike=0.09
- WKOL.CA: score=17.71 buy_ready=True sector_rank=13 price=350.07 support=310.0 resistance=390.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:22 AM market time freshness=DELAYED_CURRENT RSI=60.26 liquidity=1947123.25 spike=0.06
- ZEOT.CA: score=15.48 buy_ready=True sector_rank=13 price=13.9 support=11.59 resistance=14.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:20 AM market time freshness=DELAYED_CURRENT RSI=66.07 liquidity=1723130.63 spike=0.07
- ZMID.CA: score=22.89 buy_ready=False sector_rank=12 price=8.01 support=7.06 resistance=8.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:20 AM market time freshness=DELAYED_CURRENT RSI=80.0 liquidity=20230328.0 spike=0.08

## Backtesting Lite
- EFIH.CA: 180d return=44.31%, max drawdown=-22.68%, MA20>MA50 days last20=20, as_of=2026-08-22T21:00:00+00:00
- FWRY.CA: 180d return=19.63%, max drawdown=-18.89%, MA20>MA50 days last20=13, as_of=2026-08-22T21:00:00+00:00
- CLHO.CA: 180d return=42.82%, max drawdown=-12.5%, MA20>MA50 days last20=20, as_of=2026-08-22T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- EFIH.CA: status=RECENT_ACCEPTED latest=2026-03-31 age_days=147 sources=3 expected=E-Finance For Digital and Financial Investments summary=E-Finance For Digital and Financial Investments (EFIH.CA) has shown strong financial performance in 2025 with significant revenue and earnings growth. The company has also been active in acquisitions and has released recent quarterly earnings reports and board decisions.
  - Second quarter 2026 earnings released: EPS: ج.م0.21 (vs ج.م0.10 in 2Q 2025) - Reported Earnings • Aug 14: https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF1hkTmKmfKZQLeNBcIwHe57L19bBGUuP2oYkKdGvixAFT4bdu1ALJV2x9K0TNMP7IWDPdI_pPUikBB1mmFC1GO7NFAJn6szTVpe4sSBeHA4eW4yT7gqecex00a_qbvPQ==
  - E-finance for Digital and Financial Investments S.A.E. (CASE:EFIH) agreed to acquire Tamweely Microfinance Company for $91.3 million. - Aug. 11: https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHJ2cAu86S8f59nPgcrqIfy6thjUMZQYHanYCNUhPtKHsJzsKvUqGh4O2r0ZOxKnpEk34Ttvr9fSlE9u4ddXoh2I_huPlpsikvjbqCMw-4NGjkCZQjyDMidrgc-WOmQOK5nGI1J7yqa5lBXFVxGeEGQAHt3fe78ByqTlR9MvHl92IgsRe3DkBxzfg==
  - E-finance for Digital and Financial Investments S.A.E. Reports Earnings Results for the First Quarter Ended March 31, 2026. - May. 12: https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHJ2cAu86S8f59nPgcrqIfy6thjUMZQYHanYCNUhPtKHsJzsKvUqGh4O2r0ZOxKnpEk34Ttvr9fSlE9u4ddXoh2I_huPlpsikvjbqCMw-4NGjkCZQjyDMidrgc-WOmQOK5nGI1J7yqa5lBXFVxGeEGQAHt3fe78ByqTlR9MvHl92IgsRe3DkBxzfg==
- FWRY.CA: status=RECENT_ACCEPTED latest=2026-01-01 age_days=236 sources=3 expected=Fawry For Banking Technology and Electronic Payments summary=Fawry For Banking Technology and Electronic Payments (FWRY.CA) has demonstrated strong financial growth in 2025 and has been actively involved in new financing, strategic partnerships, and plans for a microinsurance subsidiary. The company also saw a price target increase in June 2026.
  - Fawry records EGP 2.4bn consolidated revenues in Q1-26 - Company News: https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGUDdaumrS3cVFZe3MgWNV0sRwjt20pNVheCTgHsnfwsZKc9d2m-nGD4Ie3KPDuvPMlIQF8ePOTK71gt1Vm-6mbuxYUAi41HzEZpXfsBBbgn6XEXvwCam7jAm6QxgDSSIyLNCJwLHz2XIcOIUKxxLz-
  - EBRD grants Fawry MSME EGP 250m facility to accelerate youth-led SME projects - Companies Investments: https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGUDdaumrS3cVFZe3MgWNV0sRwjt20pNVheCTgHsnfwsZKc9d2m-nGD4Ie3KPDuvPMlIQF8ePOTK71gt1Vm-6mbuxYUAi41HzEZpXfsBBbgn6XEXvwCam7jAm6QxgDSSIyLNCJwLHz2XIcOIUKxxLz-
  - Fawry to launch microinsurance subsidiary to boost Egypt's financial inclusion - Companies Investments: https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGUDdaumrS3cVFZe3MgWNV0sRwjt20pNVheCTgHsnfwsZKc9d2m-nGD4Ie3KPDuvPMlIQF8ePOTK71gt1Vm-6mbuxYUAi41HzEZpXfsBBbgn6XEXvwCam7jAm6QxgDSSIyLNCJwLHz2XIcOIUKxxLz-
- CLHO.CA: status=RECENT_ACCEPTED latest=2026-01-01 age_days=236 sources=3 expected=Cleopatra Hospital Group summary=Cleopatra Hospital Group (CLHO.CA) has released recent quarterly and annual investor presentations and earnings. The company also received a price target increase in June 2026 and had a board decision approved by the FRA in July 2026.
  - Investors Presentation Q1 2026 - 2026: https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEY0CgAwL-PpZ6GX0-aVWLXf9i21FcHiwY1-mkdTHmoYU1cf1KcC4pnXibkQ4glj1sscALx0mVrbg59ZKlclQ9xaoupZfgtteVDcgIbiOCL0MlXLGq96DPEcO1GUeJyIae9qOK2w9P4h47x
  - First quarter 2026 earnings released: EPS: ج.م0.08 (vs ج.م0.14 in 1Q 2025) - Reported Earnings • Jun 08: https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGi2QKqKimOTzNMBpnNJonjGbe28oYXaGCdR3w8ZmBwYpv3J6ntgVNy-DqE36aTjiuvXZ-ZQ7MoliDRlHraDKOHpCM55sPvG884BRb8Ke2pIn7DnGagRTvdIoPI7suUVw==
  - Price target increased by 19% to ج.م17.35. Up from ج.م14.57, the current price target is an average from 4 analysts. - Price Target Changed • Jun 26: https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGi2QKqKimOTzNMBpnNJonjGbe28oYXaGCdR3w8ZmBwYpv3J6ntgVNy-DqE36aTjiuvXZ-ZQ7MoliDRlHraDKOHpCM55sPvG884BRb8Ke2pIn7DnGagRTvdIoPI7suUVw==
- PHAR.CA: status=RECENT_ACCEPTED latest=2026-01-01 age_days=236 sources=3 expected=Egyptian International Pharmaceutical Industries summary=Egyptian International Pharmaceutical Industries (PHAR.CA) is a pharmaceutical company with strong fundamentals, including export revenue and a solid domestic market position. Recent evidence includes a disclosure form release and current stock price information.
  - Egyptian International Pharmaceuticals (EIPICO) (PHAR.CA) - Release Concerning a Disclosure Form - Source: MIST: https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEwrXGXJhfEKv0uVyidUA76rrgvkaWut20nFUvFu_r_-qcw5w_p8bCibX0HCWxrQRliwEf9c8lVI7xEZKVAV2RqPj6vwbx1I_5ai9tzu6dFEPf0lNFII5KxfnCPLWPFpaYqpYd6LXdqInJoIoLey364uaWokmBeJcA2DHhfHoLiZFni2xIF45QCc93nsV3RKoECUjjpiEAAhM0SHMl2mq9GtnNXE9lBjfF5sYHCjaex3LE=
  - Close Price(19/07/2026), 90.880.: https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFVrEMOz2uvA9FR1qPrjqo2KH23ichdbIzMm3EM3XWV3nRec2zQrx17d95vbaFzIlWxe3NB2FRRaR4iUT0b7uOTW6z9UIjfIoumb5PzKzhy4w4y8aZXKudHLbn34bR71-RahfDRJEWnVMkp6gSZB6EDEx57nGs=
  - PHAR: Strong Fundamentals, Healthy Cooling-Off 📊 PHAR: Strong Fundamentals, Healthy Cooling-Off 📈 🏛️ Fundamentals: PHAR has strong fundamentals, supported by its export USD revenue, EIPICO 3 biologicals project, and strong domestic market position.: https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGlhWe0PLLymaIJP1yyT1KLhZFm3Oc40Is6h3eVmPO9bJKawJjTx0zs2zXsj5XyLtp6YzH-Dkp2bp-gtKDepd1RRKOG10OfXZxuJjFjJvny9ouGnczNpMTq33A4VI6ylh5Vna4DeJRg
- TALM.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Talim Management Services summary=Evidence rejected for TALM.CA: source text did not clearly match TALM.CA / Talim Management Services.
- COSG.CA: status=RECENT_ACCEPTED latest=2026-08-23 age_days=2 sources=3 expected=Cairo Oil & Soap Company summary=Cairo Oil & Soap Company (COSG.CA) has reported recent financial performance, including revenue and losses for the last 12 months, and a positive stock price change over the last 52 weeks. The company has also issued several market announcements related to its board and shareholder structure.
  - In the last 12 months, EGX:COSG had revenue of EGP 802.09 million and -62.23 million in losses. Loss per share was -0.10. - (August 23 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGds8mPWQapJSfDwRbdLxeYeb2NzC63S0TLpE__LYcoNiJMPO31zAMTW16BYARExx0MzSZckv0BKbY5wo14y9x13LYVbAgzne4Kt4nYsoxP1jP2o600VThSotuWrcyBTXkQkAgUurYdXw7cULGtTg==
  - The stock price has increased by +9.91% in the last 52 weeks. - (August 23 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGds8mPWQapJSfDwRbdLxeYeb2NzC63S0TLpE__LYcoNiJMPO31zAMTW16BYARExx0MzSZckv0BKbY5wo14y9x13LYVbAgzne4Kt4nYsoxP1jP2o600VThSotuWrcyBTXkQkAgUurYdXw7cULGtTg==
  - Cairo Oils & Soap (COSG.CA) - Disclosure Form for the BoD & the Shareholders' Structure. - 7 July 02:33 PM: https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHFNEqo2zyVAIKJ0DX0NnPfFWwSGkL9MCAUkF8X2B4T8MxGI0Cl44E05xXhqQpxDinn6Yr1rnR_7PQ5QVOPTNUVjyj0Ut2_y26vrvfpM436Oh2Cq-a1tWHCOLiPsdJE4EyEiU6-ge-Q1fvxBdM58bmk
- MPCI.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=601 sources=3 expected=Memphis Pharmaceuticals & Chemical Industries summary=Memphis Pharmaceuticals & Chemical Industries (MPCI.CA) has shown substantial growth in revenue and earnings in fiscal year 2025. The company has also released recent quarterly earnings and announced a board approval for an authorized capital increase.
  - In fiscal year 2025, EGX:MPCI's revenue was 1.51 billion, an increase of 72.93% compared to the previous year's 871.91 million. Earnings were 505.28 million, an increase of 163.91%.: https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH9H9OO10TpSL8tXxYwL11HObFG7k9Uza_ryDCUGeQypSl9PcXsojkHCw4R5w1UaTUKWc2Z1b1fa2pa9uCbne1R1ZmoRXo8BmPF2Y9N-rHQA4CiXDy9Mmy7UaOxoOHXGffwZMY=
  - Memphis Pharmaceuticals and Chemical Industries sees FY2026/27 profit EGP 496 mln. - 11/05 RE: https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHBrAPO41ZImj3HQjOjJ0yNd8aeNGvD5tccvdrcwCCR80mEzMO9eNrfV8AlcznQ8EcVofsAAve5pfPC1NCPby_P--eYUR2e2TNaahfPu8R3HWaN--UYc7EcNDhxdE920a0wXTWcCLdRdI7nSwPPixy2lbu5X_fy5_sPqWTp8aaxWQiBq32mq-Q==
  - Memphis Pharmaceuticals and Chemical Industries 9-month net profit EGP 388.8 million. - 03/05 RE: https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHBrAPO41ZImj3HQjOjJ0yNd8aeNGvD5tccvdrcwCCR80mEzMO9eNrfV8AlcznQ8EcVofsAAve5pfPC1NCPby_P--eYUR2e2TNaahfPu8R3HWaN--UYc7EcNDhxdE920a0wXTWcCLdRdI7nSwPPixy2lbu5X_fy5_sPqWTp8aaxWQiBq32mq-Q==
- EBSC.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Osool ESB Securities Brokerage summary=Evidence rejected for EBSC.CA: source text did not clearly match EBSC.CA / Osool ESB Securities Brokerage.

## Warnings
- Evidence rejected for TALM.CA: source text did not clearly match TALM.CA / Talim Management Services.
- Evidence for MPCI.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for EBSC.CA: source text did not clearly match EBSC.CA / Osool ESB Securities Brokerage.
