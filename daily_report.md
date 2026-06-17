# Telegram-First EGX Scanner Report

Scan phase: Open liquidity confirmation
Generated UTC: 2026-06-17T11:20:26.665876+00:00
Generated Cairo: 2026-06-17 14:20
Run timing: target 09:15 Cairo | generated Cairo 2026-06-17 14:20 | cron 15 6 * * 0-4
Trigger: scheduled cron=15 6 * * 0-4 mapped to open_confirm; Cairo now 2026-06-17 14:16

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 0
- Tradeable price/liquidity tickers: 182/190
- Top sector: Automotive & Distribution

## Market Context
- Market trend: Bullish
- Source: Mubasher EGX market page (delayed public data)
- As of: Wednesday, June 17
- Freshness: DELAYED
- EGX30 regime: MIXED / above MA20 50.0% / above MA50 60.0%
- EGX70 regime: MIXED / above MA20 53.85% / above MA50 79.49%
- Sector breadth: 14.29%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- TMGH.CA: liquidity=1090958848.0 spike=2.39 score=24.04
- COMI.CA: liquidity=685244416.0 spike=1.12 score=24.58
- PHDC.CA: liquidity=488932544.0 spike=1.18 score=21.62
- CCAP.CA: liquidity=448131104.0 spike=0.52 score=17.79
- ORAS.CA: liquidity=356046400.0 spike=1.0 score=4.6

## AI Narrative
- Provider: OpenRouter OK
- Model: openai/gpt-oss-120b:free
- Summary: The scanner flags a defensive market regime (EGX30 & EGX70 mixed, sector breadth ≈ 14 %) so new buys are blocked. Still, several stocks show bullish technical outlooks, solid liquidity spikes and support levels within 5‑15 % of current price, mainly in Automotive & Distribution and Banking & Financials.
- EGX30/EGX70 mixed trends, 5‑day returns negative → risk mode = DEFENSIVE_NO_NEW_BUY.
- Sector breadth weak (14 %); only Automotive & Distribution leads with 100 % above MA20/50.
- Top watches: MTIE.CA, HDBK.CA, SPMD.CA, MASR.CA, CANA.CA – bullish outlook, liquidity spikes, support 5‑16 % away.
- Liquidity spikes suggest accumulation, but resistance levels are near for HDBK.CA & HRHO.CA.
- Uncertainty remains due to overall market weakness and over‑bought RSI on ECAP.CA and ANFI.CA.

## Top Liquidity Spikes
- KWIN.CA: spike=30.17 liquidity=146769360.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- CICH.CA: spike=24.28 liquidity=77455376.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- ZEOT.CA: spike=14.95 liquidity=247653584.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- DOMT.CA: spike=12.85 liquidity=24773406.0 outlook=CONSTRUCTIVE score=66.68 buy_ready=False
- ECAP.CA: spike=10.45 liquidity=54172300.0 outlook=BULLISH_WATCH score=71.71 buy_ready=False

## Sector Leaderboard
- #1 Automotive & Distribution: score=9.15 5d=1.59% 20d=4.33% aboveMA50=100.0%
- #2 Agriculture & Food Production: score=6.75 5d=3.53% 20d=8.18% aboveMA50=50.0%
- #3 Banking & Financials: score=5.85 5d=0.21% 20d=1.05% aboveMA50=80.0%
- #4 Food, Beverages & Tobacco: score=5.68 5d=-0.85% 20d=1.9% aboveMA50=100.0%
- #5 Real Estate: score=5.64 5d=-1.03% 20d=2.03% aboveMA50=84.62%
- #6 Education: score=5.62 5d=-0.75% 20d=-1.72% aboveMA50=100.0%
- #7 General / Verified EGX Expansion: score=4.71 5d=-0.43% 20d=0.29% aboveMA50=70.19%
- #8 Non-bank Financial Services: score=4.68 5d=0.0% 20d=0.0% aboveMA50=60.0%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- MTIE.CA: BULLISH_WATCH score=100 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=No major short-term scanner risk flags.
- HDBK.CA: BULLISH_WATCH score=100 liquidity=TRADEABLE sector=LEADING risk=No major short-term scanner risk flags.
- CANA.CA: BULLISH_WATCH score=100 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=No major short-term scanner risk flags.
- MASR.CA: BULLISH_WATCH score=93.71 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=No major short-term scanner risk flags.
- TMGH.CA: BULLISH_WATCH score=92.64 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=No major short-term scanner risk flags.
- MOSC.CA: BULLISH_WATCH score=91.71 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=No major short-term scanner risk flags.
- COPR.CA: BULLISH_WATCH score=86.71 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended
- HELI.CA: BULLISH_WATCH score=86.64 liquidity=TRADEABLE sector=IMPROVING risk=No major short-term scanner risk flags.
- ADIB.CA: BULLISH_WATCH score=85.85 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- FAIT.CA: BULLISH_WATCH score=85.85 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- No provider failures.

## Ranked Scanner Results
- AALR.CA: score=12.93 buy_ready=False sector_rank=7 price=205.84 support=195.1 resistance=231.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=54.01 liquidity=2048879.88 spike=0.31
- ABUK.CA: score=9.06 buy_ready=False sector_rank=21 price=70.4 support=71.06 resistance=90.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=4.08 liquidity=168866608.0 spike=1.21
- ACAMD.CA: score=20.88 buy_ready=False sector_rank=7 price=2.38 support=2.14 resistance=2.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=61.97 liquidity=72335232.0 spike=0.58
- ACGC.CA: score=18.48 buy_ready=False sector_rank=11 price=9.53 support=9.02 resistance=10.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=37.43 liquidity=18355418.0 spike=0.32
- ADCI.CA: score=19.63 buy_ready=False sector_rank=7 price=227.12 support=205.1 resistance=230.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=68.7 liquidity=9850949.0 spike=1.45
- ADIB.CA: score=22.34 buy_ready=False sector_rank=3 price=47.08 support=44.01 resistance=48.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=50.93 liquidity=54047508.0 spike=0.49
- ADPC.CA: score=13.66 buy_ready=False sector_rank=7 price=3.65 support=3.45 resistance=4.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=7776869.5 spike=0.3
- AFDI.CA: score=11.95 buy_ready=False sector_rank=7 price=42.5 support=40.15 resistance=46.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=54.73 liquidity=3068594.0 spike=0.19
- AFMC.CA: score=9.66 buy_ready=False sector_rank=7 price=71.19 support=67.0 resistance=77.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:48 PM market time freshness=DELAYED_CURRENT RSI=46.63 liquidity=779532.06 spike=0.14
- AJWA.CA: score=22.42 buy_ready=False sector_rank=7 price=186.03 support=130.01 resistance=188.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=93.13 liquidity=58899424.0 spike=2.27
- ALCN.CA: score=12.58 buy_ready=False sector_rank=12 price=28.54 support=25.51 resistance=33.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=38.58 liquidity=7174271.5 spike=0.49
- ALUM.CA: score=13.88 buy_ready=False sector_rank=7 price=23.05 support=23.02 resistance=26.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=49.34 liquidity=4997546.5 spike=0.31
- AMER.CA: score=19.26 buy_ready=False sector_rank=5 price=2.52 support=2.47 resistance=3.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=36.79 liquidity=73014176.0 spike=0.72
- AMES.CA: score=4.38 buy_ready=False sector_rank=7 price=48.83 support=48.0 resistance=55.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=30.05 liquidity=1500691.25 spike=0.37
- AMIA.CA: score=18.88 buy_ready=False sector_rank=7 price=9.08 support=8.54 resistance=9.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=66.67 liquidity=15580329.0 spike=0.99
- AMOC.CA: score=10.65 buy_ready=False sector_rank=10 price=7.78 support=7.71 resistance=8.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=31.86 liquidity=20801128.0 spike=0.28
- ANFI.CA: score=24.88 buy_ready=False sector_rank=7 price=34.5 support=13.73 resistance=34.5 source=Yahoo Finance as_of=2026-06-15T21:00:00+00:00 freshness=FRESH RSI=97.65 liquidity=273902676.0 spike=4.23
- APSW.CA: score=4.22 buy_ready=False sector_rank=7 price=8.53 support=8.24 resistance=9.38 source=Yahoo Finance as_of=2026-06-15T21:00:00+00:00 freshness=FRESH RSI=28.92 liquidity=1735957.31 spike=2.3
- ARAB.CA: score=19.26 buy_ready=False sector_rank=5 price=0.21 support=0.19 resistance=0.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=67.57 liquidity=45552132.0 spike=0.53
- ARCC.CA: score=18.06 buy_ready=False sector_rank=16 price=55.96 support=53.6 resistance=60.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=50.97 liquidity=14292065.0 spike=0.39
- AREH.CA: score=18.18 buy_ready=False sector_rank=7 price=1.6 support=1.27 resistance=1.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=79.07 liquidity=32032644.0 spike=1.15
- ARVA.CA: score=21.88 buy_ready=False sector_rank=7 price=10.89 support=7.71 resistance=13.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=72.75 liquidity=45234116.0 spike=1.5
- ASCM.CA: score=20.88 buy_ready=False sector_rank=7 price=59.01 support=47.3 resistance=64.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=73.67 liquidity=43293400.0 spike=0.63
- ASPI.CA: score=20.88 buy_ready=False sector_rank=7 price=0.31 support=0.25 resistance=0.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=60.09 liquidity=23524300.0 spike=0.34
- ATLC.CA: score=16.03 buy_ready=False sector_rank=8 price=5.17 support=4.7 resistance=5.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=64.86 liquidity=3158619.75 spike=0.72
- ATQA.CA: score=12.64 buy_ready=False sector_rank=21 price=9.6 support=9.02 resistance=10.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=55.16 liquidity=18713506.0 spike=0.54
- AXPH.CA: score=4.74 buy_ready=False sector_rank=7 price=1107.03 support=1073.0 resistance=1174.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=28.66 liquidity=857677.0 spike=0.45
- BINV.CA: score=13.72 buy_ready=False sector_rank=18 price=47.33 support=40.8 resistance=49.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:00 PM market time freshness=DELAYED_CURRENT RSI=63.48 liquidity=1929251.25 spike=0.18
- BIOC.CA: score=9.39 buy_ready=False sector_rank=7 price=71.44 support=68.34 resistance=75.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=48.88 liquidity=504446.44 spike=0.18
- BTFH.CA: score=14.87 buy_ready=False sector_rank=8 price=2.99 support=2.96 resistance=3.23 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=43.66 liquidity=119492552.0 spike=0.57
- CAED.CA: score=22.7 buy_ready=False sector_rank=7 price=73.84 support=67.21 resistance=79.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=39.03 liquidity=10735767.0 spike=1.91
- CANA.CA: score=25.52 buy_ready=False sector_rank=3 price=37.77 support=34.07 resistance=39.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=58.62 liquidity=16617501.0 spike=1.59
- CCAP.CA: score=17.79 buy_ready=False sector_rank=18 price=5.02 support=4.92 resistance=5.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:00 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=448131104.0 spike=0.52
- CCRS.CA: score=20.88 buy_ready=False sector_rank=7 price=2.48 support=2.27 resistance=2.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:00 PM market time freshness=DELAYED_CURRENT RSI=58.21 liquidity=13355417.0 spike=0.56
- CEFM.CA: score=6.92 buy_ready=False sector_rank=7 price=102.07 support=100.53 resistance=115.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=41.26 liquidity=1037774.31 spike=0.29
- CERA.CA: score=23.88 buy_ready=False sector_rank=7 price=1.27 support=1.13 resistance=1.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:00 PM market time freshness=DELAYED_CURRENT RSI=79.17 liquidity=69279728.0 spike=4.11
- CFGH.CA: score=-0.11 buy_ready=False sector_rank=7 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=0.0 liquidity=6144.56 spike=0.95
- CICH.CA: score=10.87 buy_ready=False sector_rank=8 price=12.49 support=11.54 resistance=13.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=77455376.0 spike=24.28
- CIEB.CA: score=18.49 buy_ready=False sector_rank=3 price=23.83 support=23.27 resistance=24.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:00 PM market time freshness=DELAYED_CURRENT RSI=60.1 liquidity=5147363.0 spike=0.73
- CIRA.CA: score=21.25 buy_ready=False sector_rank=6 price=27.41 support=25.23 resistance=28.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=44.95 liquidity=13013778.0 spike=0.84
- CLHO.CA: score=20.21 buy_ready=False sector_rank=14 price=15.54 support=14.25 resistance=16.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=56.73 liquidity=22257336.0 spike=0.79
- CNFN.CA: score=20.21 buy_ready=False sector_rank=8 price=4.54 support=4.36 resistance=4.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=41.43 liquidity=17649804.0 spike=1.17
- COMI.CA: score=24.58 buy_ready=False sector_rank=3 price=136.25 support=129.8 resistance=136.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=51.28 liquidity=685244416.0 spike=1.12
- COPR.CA: score=21.38 buy_ready=False sector_rank=7 price=0.38 support=0.34 resistance=0.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=65.85 liquidity=73172976.0 spike=1.75
- COSG.CA: score=20.88 buy_ready=False sector_rank=7 price=1.6 support=1.49 resistance=1.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=59.57 liquidity=35513288.0 spike=0.51
- CPCI.CA: score=11.31 buy_ready=False sector_rank=7 price=366.69 support=345.01 resistance=368.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=71.29 liquidity=2307566.0 spike=1.06
- CSAG.CA: score=15.98 buy_ready=False sector_rank=12 price=31.52 support=30.08 resistance=32.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:00 PM market time freshness=DELAYED_CURRENT RSI=50.66 liquidity=5571469.5 spike=0.43
- DAPH.CA: score=14.96 buy_ready=False sector_rank=7 price=81.12 support=76.6 resistance=86.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=56.52 liquidity=7074429.0 spike=0.62
- DEIN.CA: score=6.88 buy_ready=False sector_rank=7 price=11.38 support=11.38 resistance=13.65 source=Yahoo Finance as_of=2026-06-15T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- DOMT.CA: score=21.27 buy_ready=False sector_rank=4 price=25.59 support=23.7 resistance=26.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:00 PM market time freshness=DELAYED_CURRENT RSI=30.71 liquidity=24773406.0 spike=12.85
- DSCW.CA: score=20.88 buy_ready=False sector_rank=7 price=1.85 support=1.71 resistance=1.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=64.86 liquidity=39221412.0 spike=0.74
- DTPP.CA: score=1.32 buy_ready=False sector_rank=7 price=116.53 support=114.0 resistance=137.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=16.62 liquidity=435693.41 spike=0.23
- EALR.CA: score=10.06 buy_ready=False sector_rank=7 price=355.95 support=346.01 resistance=380.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:00 PM market time freshness=DELAYED_CURRENT RSI=54.36 liquidity=1172837.63 spike=0.31
- EASB.CA: score=10.88 buy_ready=False sector_rank=7 price=8.43 support=7.33 resistance=8.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=44304976.0 spike=9.97
- EAST.CA: score=23.27 buy_ready=False sector_rank=4 price=39.2 support=37.01 resistance=40.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=56.27 liquidity=31292260.0 spike=0.46
- EBSC.CA: score=11.81 buy_ready=False sector_rank=7 price=1.91 support=1.64 resistance=2.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:55 PM market time freshness=DELAYED_CURRENT RSI=70.91 liquidity=930530.19 spike=0.34
- ECAP.CA: score=24.88 buy_ready=False sector_rank=7 price=33.99 support=28.7 resistance=32.62 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=86.18 liquidity=54172300.0 spike=10.45
- EDFM.CA: score=12.58 buy_ready=False sector_rank=7 price=331.68 support=320.2 resistance=355.0 source=Yahoo Finance as_of=2026-06-15T21:00:00+00:00 freshness=FRESH RSI=52.43 liquidity=1255408.77 spike=2.22
- EEII.CA: score=18.75 buy_ready=False sector_rank=7 price=2.43 support=2.27 resistance=2.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=61.54 liquidity=7861464.0 spike=0.44
- EFIC.CA: score=-1.97 buy_ready=False sector_rank=21 price=203.26 support=192.01 resistance=218.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:55 PM market time freshness=DELAYED_CURRENT RSI=23.12 liquidity=386268.22 spike=0.16
- EFID.CA: score=19.27 buy_ready=False sector_rank=4 price=28.26 support=27.06 resistance=29.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=43.58 liquidity=36072344.0 spike=0.49
- EFIH.CA: score=18.44 buy_ready=False sector_rank=17 price=21.49 support=20.2 resistance=22.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:00 PM market time freshness=DELAYED_CURRENT RSI=35.74 liquidity=66742684.0 spike=1.27
- EGAL.CA: score=8.64 buy_ready=False sector_rank=21 price=298.47 support=297.1 resistance=335.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=24.21 liquidity=26830244.0 spike=0.34
- EGAS.CA: score=15.62 buy_ready=False sector_rank=10 price=51.71 support=47.5 resistance=55.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=69.09 liquidity=4974911.0 spike=0.4
- EGBE.CA: score=10.37 buy_ready=False sector_rank=3 price=0.44 support=0.43 resistance=0.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:32 PM market time freshness=DELAYED_CURRENT RSI=44.02 liquidity=26481.14 spike=0.24
- EGCH.CA: score=16.64 buy_ready=False sector_rank=21 price=13.65 support=12.9 resistance=15.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=38939364.0 spike=0.42
- EGSA.CA: score=3.13 buy_ready=False sector_rank=15 price=8.78 support=8.44 resistance=9.19 source=Yahoo Finance as_of=2026-06-15T21:00:00+00:00 freshness=FRESH RSI=26.47 liquidity=12906.6 spike=0.93
- EGTS.CA: score=19.26 buy_ready=False sector_rank=5 price=18.3 support=17.25 resistance=22.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=41.85 liquidity=47760952.0 spike=0.38
- EHDR.CA: score=20.88 buy_ready=False sector_rank=7 price=2.7 support=2.25 resistance=2.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=68.97 liquidity=21007660.0 spike=0.36
- EKHO.CA: score=10.65 buy_ready=False sector_rank=10 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-06-15T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=16.26 buy_ready=False sector_rank=13 price=2.14 support=2.06 resistance=2.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=54.84 liquidity=11620270.0 spike=0.44
- ELKA.CA: score=21.88 buy_ready=False sector_rank=7 price=1.32 support=1.12 resistance=1.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=69.77 liquidity=38358204.0 spike=0.94
- ELNA.CA: score=13.22 buy_ready=False sector_rank=7 price=39.45 support=37.11 resistance=41.51 source=Yahoo Finance as_of=2026-06-15T21:00:00+00:00 freshness=FRESH RSI=50.98 liquidity=592144.51 spike=1.87
- ELSH.CA: score=17.88 buy_ready=False sector_rank=7 price=13.39 support=8.11 resistance=14.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=76.56 liquidity=144090288.0 spike=0.78
- ELWA.CA: score=9.45 buy_ready=False sector_rank=7 price=2.03 support=1.79 resistance=2.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:38 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=561670.63 spike=0.18
- EMFD.CA: score=23.66 buy_ready=False sector_rank=5 price=12.53 support=9.83 resistance=12.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=71.01 liquidity=331800096.0 spike=1.2
- ENGC.CA: score=24.02 buy_ready=False sector_rank=7 price=37.01 support=32.31 resistance=36.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=70.73 liquidity=35702464.0 spike=2.57
- EOSB.CA: score=16.81 buy_ready=False sector_rank=7 price=1.48 support=1.34 resistance=1.55 source=Yahoo Finance as_of=2026-06-15T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=229601.28 spike=1.85
- EPCO.CA: score=22.41 buy_ready=False sector_rank=7 price=9.31 support=8.56 resistance=9.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=62.42 liquidity=7527617.5 spike=0.69
- EPPK.CA: score=8.69 buy_ready=False sector_rank=7 price=12.42 support=11.67 resistance=12.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=47.1 liquidity=801604.38 spike=0.73
- ETEL.CA: score=10.12 buy_ready=False sector_rank=15 price=93.11 support=89.61 resistance=98.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=32.31 liquidity=67908048.0 spike=0.83
- ETRS.CA: score=17.88 buy_ready=False sector_rank=7 price=10.26 support=7.37 resistance=10.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=76.02 liquidity=47002472.0 spike=0.77
- EXPA.CA: score=20.5 buy_ready=False sector_rank=3 price=18.31 support=18.31 resistance=20.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=47.37 liquidity=37672480.0 spike=1.08
- FAIT.CA: score=14.87 buy_ready=False sector_rank=3 price=37.45 support=35.01 resistance=38.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=49.14 liquidity=2534459.5 spike=0.52
- FAITA.CA: score=10.67 buy_ready=False sector_rank=3 price=0.99 support=0.98 resistance=1.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=47.73 liquidity=52256.68 spike=1.14
- FERC.CA: score=0.67 buy_ready=False sector_rank=21 price=75.08 support=75.0 resistance=79.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=24.38 liquidity=3029258.0 spike=0.75
- FWRY.CA: score=9.9 buy_ready=False sector_rank=17 price=18.91 support=17.71 resistance=20.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=32.35 liquidity=138800832.0 spike=0.47
- GBCO.CA: score=24.4 buy_ready=False sector_rank=1 price=28.61 support=25.25 resistance=28.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=66.73 liquidity=66840152.0 spike=0.62
- GDWA.CA: score=21.88 buy_ready=False sector_rank=7 price=0.81 support=0.77 resistance=0.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=61.94 liquidity=12135147.0 spike=0.86
- GGCC.CA: score=14.64 buy_ready=False sector_rank=7 price=0.42 support=0.39 resistance=0.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=59.38 liquidity=4752157.0 spike=0.61
- GIHD.CA: score=12.49 buy_ready=False sector_rank=7 price=40.93 support=35.15 resistance=43.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=59.11 liquidity=1602815.38 spike=0.46
- GMCI.CA: score=13.4 buy_ready=False sector_rank=7 price=1.77 support=1.68 resistance=1.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:52 PM market time freshness=DELAYED_CURRENT RSI=54.05 liquidity=437283.09 spike=1.04
- GRCA.CA: score=4.67 buy_ready=False sector_rank=7 price=55.24 support=50.2 resistance=60.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=30.47 liquidity=3784065.5 spike=0.62
- GSSC.CA: score=3.7 buy_ready=False sector_rank=7 price=248.0 support=228.1 resistance=267.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=21.11 liquidity=2819507.5 spike=0.58
- GTWL.CA: score=15.13 buy_ready=False sector_rank=7 price=49.15 support=45.47 resistance=55.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=50.92 liquidity=4242551.5 spike=0.56
- HDBK.CA: score=26.5 buy_ready=False sector_rank=3 price=145.18 support=138.0 resistance=154.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=59.06 liquidity=17514798.0 spike=1.08
- HELI.CA: score=21.5 buy_ready=False sector_rank=5 price=6.52 support=6.28 resistance=6.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=50.83 liquidity=167360288.0 spike=1.12
- HRHO.CA: score=24.87 buy_ready=False sector_rank=8 price=27.63 support=25.8 resistance=27.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=61.13 liquidity=58670948.0 spike=0.39
- ICID.CA: score=16.75 buy_ready=False sector_rank=7 price=7.16 support=4.5 resistance=7.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=86.6 liquidity=6862534.0 spike=0.42
- IDRE.CA: score=20.88 buy_ready=False sector_rank=7 price=44.59 support=41.01 resistance=47.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=45.41 liquidity=16143056.0 spike=0.71
- IFAP.CA: score=9.44 buy_ready=False sector_rank=2 price=19.22 support=16.5 resistance=23.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=35.91 liquidity=2038667.75 spike=0.27
- INFI.CA: score=8.15 buy_ready=False sector_rank=7 price=96.99 support=97.0 resistance=109.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=24.9 liquidity=8263855.0 spike=0.84
- IRON.CA: score=10.14 buy_ready=False sector_rank=21 price=32.44 support=31.3 resistance=35.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:00 PM market time freshness=DELAYED_CURRENT RSI=50.32 liquidity=5504144.5 spike=0.69
- ISMA.CA: score=15.88 buy_ready=False sector_rank=7 price=29.84 support=23.6 resistance=36.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=80.54 liquidity=21454524.0 spike=0.5
- ISMQ.CA: score=20.64 buy_ready=False sector_rank=21 price=8.04 support=7.27 resistance=8.62 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=64.52 liquidity=68433656.0 spike=0.97
- ISPH.CA: score=20.21 buy_ready=False sector_rank=14 price=12.06 support=11.12 resistance=12.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=59.28 liquidity=30871846.0 spike=0.24
- JUFO.CA: score=21.27 buy_ready=False sector_rank=4 price=31.34 support=26.51 resistance=31.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=69.55 liquidity=24175112.0 spike=0.62
- KABO.CA: score=16.85 buy_ready=False sector_rank=11 price=6.2 support=5.94 resistance=6.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=49.49 liquidity=8376395.5 spike=0.43
- KWIN.CA: score=10.88 buy_ready=False sector_rank=7 price=79.01 support=73.1 resistance=88.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=146769360.0 spike=30.17
- KZPC.CA: score=13.11 buy_ready=False sector_rank=7 price=10.56 support=10.3 resistance=11.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:00 PM market time freshness=DELAYED_CURRENT RSI=57.42 liquidity=2223521.0 spike=0.25
- LCSW.CA: score=21.28 buy_ready=False sector_rank=16 price=27.89 support=26.0 resistance=28.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=42.74 liquidity=14075692.0 spike=1.61
- LUTS.CA: score=17.88 buy_ready=False sector_rank=7 price=0.73 support=0.54 resistance=0.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=83.88 liquidity=32385562.0 spike=0.93
- MAAL.CA: score=7.0 buy_ready=False sector_rank=7 price=6.65 support=6.28 resistance=6.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=21753052.0 spike=1.56
- MASR.CA: score=25.62 buy_ready=False sector_rank=7 price=7.6 support=6.54 resistance=7.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=61.24 liquidity=134703680.0 spike=2.37
- MBSC.CA: score=18.06 buy_ready=False sector_rank=16 price=252.92 support=247.43 resistance=273.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=48.2 liquidity=30674008.0 spike=0.69
- MCQE.CA: score=9.08 buy_ready=False sector_rank=16 price=176.86 support=174.0 resistance=201.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=25.31 liquidity=9021322.0 spike=0.55
- MCRO.CA: score=17.88 buy_ready=False sector_rank=7 price=1.24 support=1.2 resistance=1.31 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=47.62 liquidity=36406128.0 spike=0.76
- MENA.CA: score=21.26 buy_ready=False sector_rank=5 price=6.93 support=6.12 resistance=7.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:00 PM market time freshness=DELAYED_CURRENT RSI=58.21 liquidity=11836660.0 spike=0.69
- MEPA.CA: score=20.88 buy_ready=False sector_rank=7 price=1.72 support=1.63 resistance=1.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=55.56 liquidity=11620565.0 spike=0.68
- MFPC.CA: score=9.06 buy_ready=False sector_rank=21 price=36.69 support=36.9 resistance=45.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=4.77 liquidity=106268208.0 spike=1.21
- MFSC.CA: score=5.68 buy_ready=False sector_rank=7 price=44.18 support=43.0 resistance=63.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=21.46 liquidity=1798414.13 spike=0.14
- MHOT.CA: score=18.64 buy_ready=False sector_rank=9 price=30.1 support=26.3 resistance=34.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=45.59 liquidity=9895493.0 spike=0.45
- MICH.CA: score=18.54 buy_ready=False sector_rank=7 price=37.38 support=35.05 resistance=40.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=70.19 liquidity=5658518.5 spike=0.39
- MILS.CA: score=20.88 buy_ready=False sector_rank=7 price=139.41 support=127.01 resistance=151.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=62.27 liquidity=10125679.0 spike=0.51
- MIPH.CA: score=17.85 buy_ready=False sector_rank=14 price=688.96 support=640.0 resistance=697.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:00 PM market time freshness=DELAYED_CURRENT RSI=56.6 liquidity=5084432.0 spike=2.28
- MOED.CA: score=14.83 buy_ready=False sector_rank=7 price=0.7 support=0.65 resistance=0.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=46.03 liquidity=7950841.0 spike=0.63
- MOIL.CA: score=10.98 buy_ready=False sector_rank=10 price=0.48 support=0.44 resistance=0.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=55.56 liquidity=175644.56 spike=1.08
- MOIN.CA: score=0.78 buy_ready=False sector_rank=7 price=24.26 support=24.1 resistance=26.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=21.12 liquidity=896274.06 spike=0.52
- MOSC.CA: score=23.1 buy_ready=False sector_rank=7 price=281.01 support=246.6 resistance=330.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=53.26 liquidity=19626212.0 spike=2.11
- MPCI.CA: score=21.18 buy_ready=False sector_rank=7 price=223.37 support=197.0 resistance=238.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=62.21 liquidity=91017776.0 spike=1.15
- MPCO.CA: score=23.4 buy_ready=False sector_rank=2 price=1.96 support=1.54 resistance=2.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=71.08 liquidity=66466880.0 spike=0.67
- MPRC.CA: score=16.47 buy_ready=False sector_rank=7 price=31.98 support=30.61 resistance=34.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:00 PM market time freshness=DELAYED_CURRENT RSI=60.66 liquidity=7583775.0 spike=0.38
- MTIE.CA: score=27.54 buy_ready=False sector_rank=1 price=9.15 support=8.65 resistance=9.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=55.48 liquidity=28379012.0 spike=1.57
- NAHO.CA: score=4.88 buy_ready=False sector_rank=7 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance as_of=2026-06-15T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=669.5 spike=0.02
- NCCW.CA: score=20.88 buy_ready=False sector_rank=7 price=6.19 support=5.13 resistance=6.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=69.02 liquidity=16474486.0 spike=0.59
- NEDA.CA: score=11.25 buy_ready=False sector_rank=7 price=2.78 support=2.65 resistance=2.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=61.76 liquidity=366246.47 spike=0.74
- NHPS.CA: score=14.53 buy_ready=False sector_rank=7 price=69.03 support=65.03 resistance=72.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=45.56 liquidity=4589239.5 spike=1.03
- NINH.CA: score=9.9 buy_ready=False sector_rank=7 price=17.6 support=16.8 resistance=19.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=43.3 liquidity=1014093.69 spike=0.2
- NIPH.CA: score=18.21 buy_ready=False sector_rank=14 price=161.99 support=155.1 resistance=176.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=46.81 liquidity=19252538.0 spike=0.24
- OBRI.CA: score=18.57 buy_ready=False sector_rank=7 price=35.97 support=33.63 resistance=37.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=56.68 liquidity=8690119.0 spike=0.64
- OCDI.CA: score=18.26 buy_ready=False sector_rank=5 price=21.2 support=20.0 resistance=22.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=45.39 liquidity=22440620.0 spike=0.66
- OCPH.CA: score=13.46 buy_ready=False sector_rank=7 price=341.97 support=337.0 resistance=379.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=26.79 liquidity=8619360.0 spike=1.48
- ODIN.CA: score=19.23 buy_ready=False sector_rank=7 price=2.19 support=1.89 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:00 PM market time freshness=DELAYED_CURRENT RSI=71.43 liquidity=6342141.5 spike=0.58
- OFH.CA: score=15.88 buy_ready=False sector_rank=7 price=0.61 support=0.59 resistance=0.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=54.78 liquidity=12130013.0 spike=0.52
- OIH.CA: score=9.79 buy_ready=False sector_rank=18 price=1.38 support=1.33 resistance=1.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=34.29 liquidity=25912774.0 spike=0.29
- OLFI.CA: score=23.65 buy_ready=False sector_rank=4 price=22.1 support=21.0 resistance=23.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=61.21 liquidity=23601272.0 spike=1.19
- ORAS.CA: score=4.6 buy_ready=False sector_rank=19 price=794.05 support=785.01 resistance=799.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=356046400.0 spike=1.0
- ORHD.CA: score=21.26 buy_ready=False sector_rank=5 price=38.28 support=33.51 resistance=39.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=49.64 liquidity=123783144.0 spike=0.68
- ORWE.CA: score=20.48 buy_ready=False sector_rank=11 price=23.25 support=21.6 resistance=24.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=56.81 liquidity=21361016.0 spike=0.51
- PHAR.CA: score=8.97 buy_ready=False sector_rank=14 price=84.18 support=83.02 resistance=88.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:00 PM market time freshness=DELAYED_CURRENT RSI=47.88 liquidity=3764816.75 spike=0.13
- PHDC.CA: score=21.62 buy_ready=False sector_rank=5 price=16.15 support=13.4 resistance=16.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=56.98 liquidity=488932544.0 spike=1.18
- PHTV.CA: score=24.16 buy_ready=False sector_rank=7 price=220.0 support=201.55 resistance=233.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=63.1 liquidity=9277339.0 spike=0.55
- POUL.CA: score=20.11 buy_ready=False sector_rank=4 price=35.62 support=34.8 resistance=38.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=37.3 liquidity=51270920.0 spike=1.42
- PRCL.CA: score=20.2 buy_ready=False sector_rank=16 price=25.4 support=21.01 resistance=28.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=62.78 liquidity=30014704.0 spike=1.07
- PRDC.CA: score=7.7 buy_ready=False sector_rank=5 price=8.58 support=7.72 resistance=8.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=169424320.0 spike=1.72
- PRMH.CA: score=21.58 buy_ready=False sector_rank=7 price=2.79 support=2.21 resistance=3.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=70.63 liquidity=35684000.0 spike=1.35
- RACC.CA: score=6.75 buy_ready=False sector_rank=7 price=9.75 support=9.38 resistance=10.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=26.88 liquidity=2863322.0 spike=0.28
- RAKT.CA: score=7.38 buy_ready=False sector_rank=7 price=23.03 support=22.0 resistance=24.75 source=Yahoo Finance as_of=2026-06-15T21:00:00+00:00 freshness=FRESH RSI=48.94 liquidity=520846.5 spike=1.99
- RAYA.CA: score=12.22 buy_ready=False sector_rank=20 price=7.25 support=6.7 resistance=7.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=32.59 liquidity=71441616.0 spike=0.76
- RMDA.CA: score=18.21 buy_ready=False sector_rank=14 price=5.07 support=4.92 resistance=5.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=52.66 liquidity=18588758.0 spike=0.22
- ROTO.CA: score=10.88 buy_ready=False sector_rank=7 price=42.64 support=35.7 resistance=42.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=134374560.0 spike=9.94
- RREI.CA: score=20.88 buy_ready=False sector_rank=7 price=3.71 support=3.32 resistance=3.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=62.63 liquidity=19429000.0 spike=0.91
- RTVC.CA: score=10.05 buy_ready=False sector_rank=7 price=3.83 support=3.75 resistance=4.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=55.38 liquidity=4166415.75 spike=0.74
- RUBX.CA: score=8.05 buy_ready=False sector_rank=7 price=9.94 support=9.8 resistance=11.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:55 PM market time freshness=DELAYED_CURRENT RSI=44.32 liquidity=3168042.0 spike=0.28
- SAUD.CA: score=13.57 buy_ready=False sector_rank=3 price=22.19 support=20.82 resistance=23.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=36.8 liquidity=6230110.5 spike=0.57
- SCEM.CA: score=15.06 buy_ready=False sector_rank=16 price=61.92 support=59.3 resistance=67.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=38.76 liquidity=10600053.0 spike=0.49
- SCFM.CA: score=3.09 buy_ready=False sector_rank=7 price=250.17 support=248.1 resistance=296.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:00 PM market time freshness=DELAYED_CURRENT RSI=34.55 liquidity=2204787.5 spike=0.18
- SCTS.CA: score=6.62 buy_ready=False sector_rank=6 price=600.94 support=565.25 resistance=668.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:00 PM market time freshness=DELAYED_CURRENT RSI=28.2 liquidity=2370042.0 spike=0.45
- SDTI.CA: score=22.88 buy_ready=False sector_rank=7 price=48.01 support=43.4 resistance=47.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=62.01 liquidity=12307650.0 spike=0.84
- SEIG.CA: score=13.91 buy_ready=False sector_rank=7 price=183.14 support=173.35 resistance=205.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=54.17 liquidity=3028783.0 spike=0.64
- SIPC.CA: score=12.77 buy_ready=False sector_rank=7 price=3.5 support=3.4 resistance=3.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=44.44 liquidity=6888335.5 spike=0.54
- SKPC.CA: score=7.64 buy_ready=False sector_rank=21 price=16.1 support=16.16 resistance=17.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=33.46 liquidity=18971344.0 spike=0.36
- SMFR.CA: score=9.6 buy_ready=False sector_rank=7 price=203.74 support=192.0 resistance=218.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:55 PM market time freshness=DELAYED_CURRENT RSI=42.73 liquidity=718012.38 spike=0.17
- SNFC.CA: score=16.96 buy_ready=False sector_rank=7 price=12.1 support=11.68 resistance=12.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=47.98 liquidity=8079362.0 spike=0.31
- SPIN.CA: score=13.08 buy_ready=False sector_rank=11 price=14.0 support=13.3 resistance=15.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT RSI=31.53 liquidity=10537799.0 spike=2.3
- SPMD.CA: score=25.88 buy_ready=False sector_rank=7 price=0.44 support=0.39 resistance=0.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=52.43 liquidity=106849040.0 spike=4.52
- SUGR.CA: score=12.74 buy_ready=False sector_rank=4 price=48.66 support=48.0 resistance=51.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=50.74 liquidity=4472842.5 spike=0.3
- SVCE.CA: score=21.32 buy_ready=False sector_rank=7 price=9.4 support=8.11 resistance=9.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=46.67 liquidity=111766104.0 spike=1.22
- SWDY.CA: score=14.11 buy_ready=False sector_rank=13 price=86.71 support=84.01 resistance=90.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:00 PM market time freshness=DELAYED_CURRENT RSI=42.95 liquidity=5854334.5 spike=0.29
- TALM.CA: score=18.37 buy_ready=False sector_rank=6 price=16.0 support=15.12 resistance=16.53 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=77.6 liquidity=8081958.5 spike=1.02
- TMGH.CA: score=24.04 buy_ready=False sector_rank=5 price=97.25 support=92.91 resistance=101.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=48.52 liquidity=1090958848.0 spike=2.39
- TRTO.CA: score=6.88 buy_ready=False sector_rank=7 price=0.03 support=0.03 resistance=0.04 source=Yahoo Finance as_of=2026-06-15T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- UEFM.CA: score=10.22 buy_ready=False sector_rank=7 price=470.07 support=455.6 resistance=500.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=48.69 liquidity=1535967.88 spike=1.9
- UEGC.CA: score=20.46 buy_ready=False sector_rank=7 price=1.44 support=1.3 resistance=1.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=64.86 liquidity=7574910.5 spike=0.3
- UNIP.CA: score=19.88 buy_ready=False sector_rank=7 price=0.34 support=0.28 resistance=0.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=85.92 liquidity=19059318.0 spike=0.8
- UNIT.CA: score=13.6 buy_ready=False sector_rank=5 price=13.8 support=12.25 resistance=15.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=58.26 liquidity=2347655.75 spike=0.3
- WCDF.CA: score=6.23 buy_ready=False sector_rank=7 price=531.8 support=450.0 resistance=550.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:55 PM market time freshness=DELAYED_CURRENT RSI=45.74 liquidity=347167.63 spike=0.95
- WKOL.CA: score=8.2 buy_ready=False sector_rank=7 price=287.63 support=289.0 resistance=312.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:56 PM market time freshness=DELAYED_CURRENT RSI=44.38 liquidity=2318781.75 spike=0.68
- ZEOT.CA: score=10.88 buy_ready=False sector_rank=7 price=12.5 support=11.0 resistance=13.53 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=247653584.0 spike=14.95
- ZMID.CA: score=21.26 buy_ready=False sector_rank=5 price=6.23 support=5.77 resistance=6.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=62.77 liquidity=126525992.0 spike=0.6

## Backtesting Lite
- MTIE.CA: 180d return=40.36%, max drawdown=-20.49%, MA20>MA50 days last20=20, as_of=2026-06-15T21:00:00+00:00
- HDBK.CA: 180d return=134.47%, max drawdown=-12.66%, MA20>MA50 days last20=15, as_of=2026-06-15T21:00:00+00:00
- SPMD.CA: 180d return=29.81%, max drawdown=-15.63%, MA20>MA50 days last20=20, as_of=2026-06-15T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- MTIE.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=MM Group For Industry and International Trade summary=Evidence rejected for MTIE.CA: source text did not clearly match MTIE.CA / MM Group For Industry and International Trade.
- HDBK.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Housing and Development Bank Egypt summary=Evidence rejected for HDBK.CA: source text did not clearly match HDBK.CA / Housing and Development Bank Egypt.
- SPMD.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Speed Medical Co summary=Speed Medical’s stock reflects strong technical breakthrough; Speed Medical turns to losses in 9M-22; Shareholder ups stake in Speed Medical for EGP 3.5m
  - Speed Medical’s stock reflects strong technical breakthrough: https://english.mubasher.info/news/4546374/Speed-Medical-s-stock-reflects-strong-technical-breakthrough/
  - Speed Medical turns to losses in 9M-22: https://english.mubasher.info/news/4054471/Speed-Medical-turns-to-losses-in-9M-22/
  - Shareholder ups stake in Speed Medical for EGP 3.5m: https://english.mubasher.info/news/4049449/Shareholder-ups-stake-in-Speed-Medical-for-EGP-3-5m/
- MASR.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=532 sources=3 expected=Madinet Masr For Housing and Development summary=Madinet Masr to pay out EGP 0.15/shr for 2025 upon equityholders&#39; approval; Madinet Masr logs 24% higher consolidated profits in 2025; dividends recommended; Madinet Masr to distribute treasury stocks in first-ever move
  - Madinet Masr to pay out EGP 0.15/shr for 2025 upon equityholders&#39; approval: https://english.mubasher.info/news/4601386/Madinet-Masr-to-pay-out-EGP-0-15-shr-for-2025-upon-equityholders-approval/
  - Madinet Masr logs 24% higher consolidated profits in 2025; dividends recommended: https://english.mubasher.info/news/4578449/Madinet-Masr-logs-24-higher-consolidated-profits-in-2025-dividends-recommended/
  - Madinet Masr to distribute treasury stocks in first-ever move: https://english.mubasher.info/news/4577724/Madinet-Masr-to-distribute-treasury-stocks-in-first-ever-move/
- CANA.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=532 sources=3 expected=Suez Canal Bank summary=Suez Canal Bank delivers EGP 1.6bn profits in Q1-26; Suez Canal Bank unveils details for previous dividends payout; Suez Canal Bank to distribute EGP 5bn bonus shares for 2025
  - Suez Canal Bank delivers EGP 1.6bn profits in Q1-26: https://english.mubasher.info/news/4611255/Suez-Canal-Bank-delivers-EGP-1-6bn-profits-in-Q1-26/
  - Suez Canal Bank unveils details for previous dividends payout: https://english.mubasher.info/news/4586807/Suez-Canal-Bank-unveils-details-for-previous-dividends-payout/
  - Suez Canal Bank to distribute EGP 5bn bonus shares for 2025: https://english.mubasher.info/news/4581661/Suez-Canal-Bank-to-distribute-EGP-5bn-bonus-shares-for-2025/
- ECAP.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Al Ezz Ceramics & Porcelain Co. summary=Evidence rejected for ECAP.CA: source text did not clearly match ECAP.CA / Al Ezz Ceramics & Porcelain Co..
- ANFI.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Tycoon Holding Company For Financial Investments summary=Evidence rejected for ANFI.CA: source text did not clearly match ANFI.CA / Tycoon Holding Company For Financial Investments.
- HRHO.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=EFG Holding summary=Evidence rejected for HRHO.CA: source text did not clearly match HRHO.CA / EFG Holding.

## Warnings
- Evidence rejected for MTIE.CA: source text did not clearly match MTIE.CA / MM Group For Industry and International Trade.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence rejected for HDBK.CA: source text did not clearly match HDBK.CA / Housing and Development Bank Egypt.
- Evidence for SPMD.CA matches the company but no source/report date was detected.
- Evidence for MASR.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for CANA.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for ECAP.CA: source text did not clearly match ECAP.CA / Al Ezz Ceramics & Porcelain Co..
- Mubasher stock-page evidence failed for ANFI.CA: 404 Client Error: Not Found for url: https://english.mubasher.info/markets/EGX/stocks/ANFI
- No Yahoo or Mubasher evidence found for ANFI.CA.
- Evidence rejected for ANFI.CA: source text did not clearly match ANFI.CA / Tycoon Holding Company For Financial Investments.
- Evidence rejected for HRHO.CA: source text did not clearly match HRHO.CA / EFG Holding.
