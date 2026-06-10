# Telegram-First EGX Scanner Report

Scan phase: Open liquidity confirmation
Generated UTC: 2026-06-10T10:24:19.629055+00:00
Generated Cairo: 2026-06-10 13:24
Run timing: target 09:15 Cairo | generated Cairo 2026-06-10 13:24 | cron 15 6 * * 0-4
Trigger: scheduled cron=15 6 * * 0-4 mapped to open_confirm; Cairo now 2026-06-10 13:20

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 0
- Tradeable price/liquidity tickers: 186/190
- Top sector: Real Estate

## Market Context
- Market trend: Bearish
- Source: Mubasher EGX market page (delayed public data)
- As of: Wednesday, June 10
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 10.0% / above MA50 65.0%
- EGX70 regime: MIXED / above MA20 62.5% / above MA50 82.5%
- Sector breadth: 23.81%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- CCAP.CA: liquidity=619584192.0 spike=0.73 score=22.35
- COMI.CA: liquidity=409607520.0 spike=0.61 score=18.17
- ELSH.CA: liquidity=384490976.0 spike=2.92 score=9.96
- ORAS.CA: liquidity=364709152.0 spike=1.0 score=4.6
- FWRY.CA: liquidity=279144960.0 spike=0.93 score=13.2

## AI Narrative
- Provider: OpenRouter OK
- Model: openai/gpt-oss-120b:free
- Summary: The local scanner stays on HOLD because EGX30 is in a bearish regime and sector breadth is weak (23.8%). EGX70 shows mixed signals but still negative 5‑day returns, so risk mode is DEFENSIVE_NO_NEW_BUY. Even top‑ranked Real Estate tickets (ZMID.CA, MENA.CA, ARAB.CA) show cooling liquidity or are far from support, limiting short‑term upside.
- EGX30 bearish, only 10% above MA20; EGX70 mixed, 62.5% above MA20 – market risk remains high.
- Real Estate leads sector breadth but liquidity is cooling; ZMID.CA faces resistance at 5.22 EGP.
- No tickets are buy‑ready; outlooks are bullish watch but support distances (5‑10%) and RSI levels suggest caution.
- Defensive risk mode blocks new entries until breadth improves and liquidity stabilises.

## Top Liquidity Spikes
- MICH.CA: spike=8.95 liquidity=79981536.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- EDFM.CA: spike=4.9 liquidity=2972828.22 outlook=CONSTRUCTIVE score=58.3 buy_ready=False
- ANFI.CA: spike=4.65 liquidity=134592218.23 outlook=CONSTRUCTIVE score=68.3 buy_ready=False
- ELNA.CA: spike=3.31 liquidity=1188965.25 outlook=BULLISH_WATCH score=70.3 buy_ready=False
- CFGH.CA: spike=3.23 liquidity=16747.74 outlook=WEAK_OR_RISKY score=0 buy_ready=False

## Sector Leaderboard
- #1 Real Estate: score=7.5 5d=-2.39% 20d=10.02% aboveMA50=100.0%
- #2 Tourism & Leisure: score=6.95 5d=-5.99% 20d=14.85% aboveMA50=100.0%
- #3 Investment Holding: score=5.87 5d=-3.11% 20d=14.08% aboveMA50=66.67%
- #4 Textiles: score=5.86 5d=-0.81% 20d=5.88% aboveMA50=75.0%
- #5 Automotive & Distribution: score=5.84 5d=2.17% 20d=-2.47% aboveMA50=100.0%
- #6 Agriculture & Food Production: score=5.52 5d=4.84% 20d=1.04% aboveMA50=50.0%
- #7 General / Verified EGX Expansion: score=5.3 5d=1.15% 20d=0.61% aboveMA50=81.73%
- #8 Food, Beverages & Tobacco: score=5.17 5d=-0.66% 20d=1.51% aboveMA50=85.71%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- ARAB.CA: BULLISH_WATCH score=100 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=No major short-term scanner risk flags.
- KZPC.CA: BULLISH_WATCH score=98.3 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=No major short-term scanner risk flags.
- KWIN.CA: BULLISH_WATCH score=98.3 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=No major short-term scanner risk flags.
- HELI.CA: BULLISH_WATCH score=92.5 liquidity=TRADEABLE sector=LEADING risk=No major short-term scanner risk flags.
- MASR.CA: BULLISH_WATCH score=92.3 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=No major short-term scanner risk flags.
- ALUM.CA: BULLISH_WATCH score=89.3 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- ZMID.CA: BULLISH_WATCH score=87.5 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; momentum is extended
- AMER.CA: BULLISH_WATCH score=87.5 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- ACAMD.CA: BULLISH_WATCH score=86.3 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=No major short-term scanner risk flags.
- ADCI.CA: BULLISH_WATCH score=86.3 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- No provider failures.

## Ranked Scanner Results
- AALR.CA: score=14.27 buy_ready=False sector_rank=7 price=216.98 support=195.1 resistance=233.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:55 AM market time freshness=DELAYED_CURRENT RSI=77.66 liquidity=6152212.0 spike=0.55
- ABUK.CA: score=9.86 buy_ready=False sector_rank=18 price=80.34 support=81.2 resistance=90.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=19.35 liquidity=43510668.0 spike=0.36
- ACAMD.CA: score=24.16 buy_ready=False sector_rank=7 price=2.37 support=2.1 resistance=2.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=59.65 liquidity=178198896.0 spike=1.52
- ACGC.CA: score=21.34 buy_ready=False sector_rank=4 price=9.78 support=8.51 resistance=10.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=52.21 liquidity=20870190.0 spike=0.36
- ADCI.CA: score=23.74 buy_ready=False sector_rank=7 price=227.08 support=202.22 resistance=225.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=66.05 liquidity=13933243.0 spike=2.31
- ADIB.CA: score=18.17 buy_ready=False sector_rank=16 price=46.03 support=45.3 resistance=50.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=44.08 liquidity=37327644.0 spike=0.24
- ADPC.CA: score=5.5 buy_ready=False sector_rank=7 price=3.67 support=3.54 resistance=4.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:55 AM market time freshness=DELAYED_CURRENT RSI=24.74 liquidity=4375524.0 spike=0.18
- AFDI.CA: score=17.49 buy_ready=False sector_rank=7 price=44.18 support=40.0 resistance=46.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=61.36 liquidity=6369769.0 spike=0.35
- AFMC.CA: score=10.59 buy_ready=False sector_rank=7 price=71.95 support=69.33 resistance=80.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:55 AM market time freshness=DELAYED_CURRENT RSI=41.89 liquidity=1471572.63 spike=0.16
- AJWA.CA: score=20.12 buy_ready=False sector_rank=7 price=150.0 support=130.01 resistance=154.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=84.58 liquidity=12139160.0 spike=0.71
- ALCN.CA: score=14.93 buy_ready=False sector_rank=17 price=28.97 support=28.4 resistance=30.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=40.99 liquidity=10867509.0 spike=0.51
- ALUM.CA: score=20.87 buy_ready=False sector_rank=7 price=25.1 support=22.66 resistance=26.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:55 AM market time freshness=DELAYED_CURRENT RSI=57.44 liquidity=5750127.0 spike=0.27
- AMER.CA: score=24.4 buy_ready=False sector_rank=1 price=2.77 support=2.4 resistance=3.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT RSI=59.34 liquidity=35118080.0 spike=0.31
- AMES.CA: score=7.33 buy_ready=False sector_rank=7 price=50.44 support=48.0 resistance=57.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=18.46 liquidity=3214663.25 spike=0.55
- AMIA.CA: score=16.19 buy_ready=False sector_rank=7 price=9.06 support=8.54 resistance=10.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=64.0 liquidity=5074884.0 spike=0.18
- AMOC.CA: score=10.48 buy_ready=False sector_rank=13 price=8.24 support=8.1 resistance=9.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=30.36 liquidity=20552144.0 spike=0.25
- ANFI.CA: score=25.12 buy_ready=False sector_rank=7 price=18.62 support=13.5 resistance=18.62 source=Yahoo Finance as_of=2026-06-08T21:00:00+00:00 freshness=FRESH RSI=79.32 liquidity=134592218.23 spike=4.65
- APSW.CA: score=3.51 buy_ready=False sector_rank=7 price=8.9 support=8.62 resistance=9.38 source=Yahoo Finance as_of=2026-06-08T21:00:00+00:00 freshness=FRESH RSI=34.21 liquidity=391929.28 spike=0.46
- ARAB.CA: score=25.48 buy_ready=False sector_rank=1 price=0.21 support=0.19 resistance=0.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:55 AM market time freshness=DELAYED_CURRENT RSI=51.72 liquidity=118336912.0 spike=1.54
- ARCC.CA: score=18.58 buy_ready=False sector_rank=12 price=56.73 support=53.35 resistance=60.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:55 AM market time freshness=DELAYED_CURRENT RSI=66.67 liquidity=18473726.0 spike=0.43
- AREH.CA: score=19.09 buy_ready=False sector_rank=7 price=1.5 support=1.27 resistance=1.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT RSI=80.65 liquidity=8973357.0 spike=0.32
- ARVA.CA: score=19.49 buy_ready=False sector_rank=7 price=11.17 support=7.71 resistance=11.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT RSI=74.61 liquidity=8369809.5 spike=0.34
- ASCM.CA: score=18.12 buy_ready=False sector_rank=7 price=57.0 support=47.3 resistance=59.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:55 AM market time freshness=DELAYED_CURRENT RSI=75.73 liquidity=54206136.0 spike=0.8
- ASPI.CA: score=23.12 buy_ready=False sector_rank=7 price=0.34 support=0.25 resistance=0.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:55 AM market time freshness=DELAYED_CURRENT RSI=60.57 liquidity=34005792.0 spike=0.54
- ATLC.CA: score=10.44 buy_ready=False sector_rank=19 price=5.02 support=4.71 resistance=5.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=66.04 liquidity=755087.25 spike=0.12
- ATQA.CA: score=21.86 buy_ready=False sector_rank=18 price=9.92 support=9.41 resistance=10.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:55 AM market time freshness=DELAYED_CURRENT RSI=60.0 liquidity=13264492.0 spike=0.33
- AXPH.CA: score=11.48 buy_ready=False sector_rank=7 price=1146.04 support=1100.12 resistance=1239.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=51.16 liquidity=362778.94 spike=0.06
- BINV.CA: score=13.74 buy_ready=False sector_rank=3 price=46.42 support=40.8 resistance=49.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:46 AM market time freshness=DELAYED_CURRENT RSI=71.75 liquidity=1392931.88 spike=0.12
- BIOC.CA: score=11.97 buy_ready=False sector_rank=7 price=71.08 support=70.0 resistance=79.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT RSI=53.57 liquidity=2845081.75 spike=0.44
- BTFH.CA: score=17.69 buy_ready=False sector_rank=19 price=3.11 support=3.03 resistance=3.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:55 AM market time freshness=DELAYED_CURRENT RSI=47.27 liquidity=50725632.0 spike=0.21
- CAED.CA: score=5.58 buy_ready=False sector_rank=7 price=71.44 support=70.41 resistance=89.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:47 AM market time freshness=DELAYED_CURRENT RSI=34.62 liquidity=1464320.88 spike=0.1
- CANA.CA: score=15.04 buy_ready=False sector_rank=16 price=37.31 support=34.01 resistance=39.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:55 AM market time freshness=DELAYED_CURRENT RSI=65.43 liquidity=4867221.5 spike=0.34
- CCAP.CA: score=22.35 buy_ready=False sector_rank=3 price=5.47 support=4.68 resistance=5.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=56.52 liquidity=619584192.0 spike=0.73
- CCRS.CA: score=15.59 buy_ready=False sector_rank=7 price=2.46 support=2.1 resistance=2.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:55 AM market time freshness=DELAYED_CURRENT RSI=55.71 liquidity=4470025.0 spike=0.16
- CEFM.CA: score=4.65 buy_ready=False sector_rank=7 price=105.24 support=103.07 resistance=119.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=30.19 liquidity=534810.5 spike=0.11
- CERA.CA: score=18.67 buy_ready=False sector_rank=7 price=1.2 support=1.13 resistance=1.23 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=53.85 liquidity=4549977.0 spike=0.3
- CFGH.CA: score=4.6 buy_ready=False sector_rank=7 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=0.0 liquidity=16747.74 spike=3.23
- CICH.CA: score=3.53 buy_ready=False sector_rank=19 price=11.81 support=11.71 resistance=13.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=24.14 liquidity=844111.38 spike=0.18
- CIEB.CA: score=7.52 buy_ready=False sector_rank=16 price=23.51 support=23.31 resistance=24.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=37.39 liquidity=2350535.75 spike=0.23
- CIRA.CA: score=13.55 buy_ready=False sector_rank=14 price=26.25 support=23.23 resistance=28.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=37.54 liquidity=5114463.5 spike=0.18
- CLHO.CA: score=9.87 buy_ready=False sector_rank=9 price=14.81 support=14.83 resistance=16.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:55 AM market time freshness=DELAYED_CURRENT RSI=30.36 liquidity=6062376.0 spike=0.17
- CNFN.CA: score=10.64 buy_ready=False sector_rank=19 price=4.58 support=4.47 resistance=4.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:47 AM market time freshness=DELAYED_CURRENT RSI=35.94 liquidity=3954743.25 spike=0.23
- COMI.CA: score=18.17 buy_ready=False sector_rank=16 price=132.5 support=129.8 resistance=144.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=48.51 liquidity=409607520.0 spike=0.61
- COPR.CA: score=6.48 buy_ready=False sector_rank=7 price=0.38 support=0.36 resistance=0.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=45486180.0 spike=1.18
- COSG.CA: score=23.36 buy_ready=False sector_rank=7 price=1.69 support=1.46 resistance=1.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:55 AM market time freshness=DELAYED_CURRENT RSI=64.71 liquidity=68383952.0 spike=1.12
- CPCI.CA: score=7.77 buy_ready=False sector_rank=7 price=365.01 support=340.01 resistance=370.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:55 AM market time freshness=DELAYED_CURRENT RSI=82.12 liquidity=1654626.5 spike=0.37
- CSAG.CA: score=17.14 buy_ready=False sector_rank=17 price=31.61 support=30.4 resistance=32.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=54.85 liquidity=7212332.0 spike=0.39
- DAPH.CA: score=3.53 buy_ready=False sector_rank=7 price=80.71 support=79.25 resistance=96.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT RSI=27.1 liquidity=2407690.5 spike=0.08
- DEIN.CA: score=7.12 buy_ready=False sector_rank=7 price=11.38 support=11.38 resistance=13.65 source=Yahoo Finance as_of=2026-06-08T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- DOMT.CA: score=5.03 buy_ready=False sector_rank=8 price=24.74 support=24.24 resistance=26.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=29.8 liquidity=3243057.75 spike=1.36
- DSCW.CA: score=17.12 buy_ready=False sector_rank=7 price=1.81 support=1.71 resistance=1.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=45.16 liquidity=10159833.0 spike=0.17
- DTPP.CA: score=5.22 buy_ready=False sector_rank=7 price=122.21 support=123.0 resistance=139.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=27.06 liquidity=1100154.25 spike=0.29
- EALR.CA: score=13.11 buy_ready=False sector_rank=7 price=362.22 support=346.01 resistance=392.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=48.06 liquidity=1990270.5 spike=0.21
- EASB.CA: score=9.9 buy_ready=False sector_rank=7 price=4.99 support=4.61 resistance=5.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=72.58 liquidity=780475.69 spike=0.62
- EAST.CA: score=14.48 buy_ready=False sector_rank=8 price=39.18 support=37.01 resistance=39.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:55 AM market time freshness=DELAYED_CURRENT RSI=60.28 liquidity=1416341.5 spike=0.02
- EBSC.CA: score=13.98 buy_ready=False sector_rank=7 price=1.82 support=1.64 resistance=2.09 source=Yahoo Finance as_of=2026-06-08T21:00:00+00:00 freshness=FRESH RSI=62.79 liquidity=862683.66 spike=0.35
- ECAP.CA: score=16.82 buy_ready=False sector_rank=7 price=32.16 support=28.7 resistance=32.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=88.3 liquidity=6321802.5 spike=1.19
- EDFM.CA: score=17.09 buy_ready=False sector_rank=7 price=333.09 support=320.2 resistance=355.0 source=Yahoo Finance as_of=2026-06-08T21:00:00+00:00 freshness=FRESH RSI=38.06 liquidity=2972828.22 spike=4.9
- EEII.CA: score=23.12 buy_ready=False sector_rank=7 price=2.49 support=2.27 resistance=2.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:55 AM market time freshness=DELAYED_CURRENT RSI=56.1 liquidity=11069062.0 spike=0.56
- EFIC.CA: score=0.49 buy_ready=False sector_rank=18 price=204.92 support=203.01 resistance=219.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=7.01 liquidity=629483.25 spike=0.16
- EFID.CA: score=19.07 buy_ready=False sector_rank=8 price=27.88 support=27.49 resistance=29.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:55 AM market time freshness=DELAYED_CURRENT RSI=51.57 liquidity=17471704.0 spike=0.23
- EFIH.CA: score=14.83 buy_ready=False sector_rank=21 price=21.06 support=21.0 resistance=22.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=44.32 liquidity=8634995.0 spike=0.13
- EGAL.CA: score=17.86 buy_ready=False sector_rank=18 price=316.46 support=304.0 resistance=344.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:55 AM market time freshness=DELAYED_CURRENT RSI=38.47 liquidity=35993056.0 spike=0.33
- EGAS.CA: score=14.61 buy_ready=False sector_rank=13 price=49.91 support=46.51 resistance=51.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:55 AM market time freshness=DELAYED_CURRENT RSI=42.63 liquidity=4123929.75 spike=0.31
- EGBE.CA: score=8.24 buy_ready=False sector_rank=16 price=0.44 support=0.44 resistance=0.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=42.52 liquidity=68564.97 spike=0.49
- EGCH.CA: score=21.86 buy_ready=False sector_rank=18 price=14.5 support=12.95 resistance=15.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:55 AM market time freshness=DELAYED_CURRENT RSI=57.7 liquidity=10935922.0 spike=0.09
- EGSA.CA: score=8.07 buy_ready=False sector_rank=15 price=8.73 support=8.3 resistance=9.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=67.78 liquidity=27979.15 spike=1.86
- EGTS.CA: score=24.4 buy_ready=False sector_rank=1 price=19.06 support=12.9 resistance=22.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:55 AM market time freshness=DELAYED_CURRENT RSI=47.4 liquidity=70352904.0 spike=0.61
- EHDR.CA: score=20.12 buy_ready=False sector_rank=7 price=2.77 support=2.25 resistance=2.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=85.33 liquidity=33944444.0 spike=0.67
- EKHO.CA: score=10.48 buy_ready=False sector_rank=13 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-06-08T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=18.15 buy_ready=False sector_rank=10 price=2.16 support=2.06 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT RSI=54.17 liquidity=6349169.0 spike=0.23
- ELKA.CA: score=20.32 buy_ready=False sector_rank=7 price=1.3 support=1.12 resistance=1.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=66.67 liquidity=45842648.0 spike=1.1
- ELNA.CA: score=16.93 buy_ready=False sector_rank=7 price=41.41 support=37.11 resistance=42.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=38.94 liquidity=1188965.25 spike=3.31
- ELSH.CA: score=9.96 buy_ready=False sector_rank=7 price=14.61 support=13.03 resistance=14.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=384490976.0 spike=2.92
- ELWA.CA: score=11.7 buy_ready=False sector_rank=7 price=2.12 support=1.79 resistance=2.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=91.67 liquidity=1577907.5 spike=0.52
- EMFD.CA: score=21.4 buy_ready=False sector_rank=1 price=11.9 support=9.83 resistance=12.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=75.07 liquidity=164128832.0 spike=0.68
- ENGC.CA: score=21.82 buy_ready=False sector_rank=7 price=35.2 support=32.31 resistance=35.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=70.72 liquidity=17664938.0 spike=1.35
- EOSB.CA: score=11.51 buy_ready=False sector_rank=7 price=1.42 support=1.34 resistance=1.54 source=Yahoo Finance as_of=2026-06-08T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=253701.45 spike=2.07
- EPCO.CA: score=15.61 buy_ready=False sector_rank=7 price=9.34 support=8.56 resistance=9.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:55 AM market time freshness=DELAYED_CURRENT RSI=55.31 liquidity=2493530.25 spike=0.2
- EPPK.CA: score=6.54 buy_ready=False sector_rank=7 price=12.25 support=11.67 resistance=13.6 source=Yahoo Finance as_of=2026-06-08T21:00:00+00:00 freshness=FRESH RSI=47.1 liquidity=416512.25 spike=0.39
- ETEL.CA: score=18.32 buy_ready=False sector_rank=15 price=93.64 support=92.17 resistance=99.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:55 AM market time freshness=DELAYED_CURRENT RSI=41.38 liquidity=23159714.0 spike=0.21
- ETRS.CA: score=21.32 buy_ready=False sector_rank=7 price=9.57 support=7.37 resistance=9.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=75.0 liquidity=61270956.0 spike=1.1
- EXPA.CA: score=20.17 buy_ready=False sector_rank=16 price=18.84 support=18.34 resistance=20.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:55 AM market time freshness=DELAYED_CURRENT RSI=48.93 liquidity=15828597.0 spike=0.4
- FAIT.CA: score=3.86 buy_ready=False sector_rank=16 price=36.63 support=34.11 resistance=38.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:44 AM market time freshness=DELAYED_CURRENT RSI=32.88 liquidity=691793.19 spike=0.11
- FAITA.CA: score=8.18 buy_ready=False sector_rank=16 price=0.99 support=0.98 resistance=1.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=58.82 liquidity=13934.01 spike=0.31
- FERC.CA: score=5.89 buy_ready=False sector_rank=18 price=77.37 support=76.5 resistance=83.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=36.33 liquidity=1030618.44 spike=0.17
- FWRY.CA: score=13.2 buy_ready=False sector_rank=21 price=18.6 support=18.32 resistance=21.16 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=40.53 liquidity=279144960.0 spike=0.93
- GBCO.CA: score=21.34 buy_ready=False sector_rank=5 price=28.3 support=25.25 resistance=29.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=65.27 liquidity=124194208.0 spike=1.0
- GDWA.CA: score=20.59 buy_ready=False sector_rank=7 price=0.81 support=0.77 resistance=0.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=64.71 liquidity=8470300.0 spike=0.9
- GGCC.CA: score=17.63 buy_ready=False sector_rank=7 price=0.43 support=0.39 resistance=0.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=66.67 liquidity=7410810.5 spike=1.05
- GIHD.CA: score=14.13 buy_ready=False sector_rank=7 price=41.63 support=39.1 resistance=44.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=50.23 liquidity=1009890.94 spike=0.19
- GMCI.CA: score=9.17 buy_ready=False sector_rank=7 price=1.74 support=1.67 resistance=1.84 source=Yahoo Finance as_of=2026-06-08T21:00:00+00:00 freshness=FRESH RSI=56.67 liquidity=428001.72 spike=1.31
- GRCA.CA: score=1.92 buy_ready=False sector_rank=7 price=54.57 support=53.16 resistance=60.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=26.97 liquidity=799869.06 spike=0.09
- GSSC.CA: score=4.46 buy_ready=False sector_rank=7 price=251.27 support=228.1 resistance=272.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=9.47 liquidity=3336759.25 spike=0.45
- GTWL.CA: score=15.88 buy_ready=False sector_rank=7 price=49.08 support=45.47 resistance=59.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=28.28 liquidity=13043007.0 spike=1.88
- HDBK.CA: score=10.37 buy_ready=False sector_rank=16 price=140.44 support=138.75 resistance=149.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=44.01 liquidity=5197813.5 spike=0.34
- HELI.CA: score=24.4 buy_ready=False sector_rank=1 price=6.65 support=6.28 resistance=6.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT RSI=56.55 liquidity=135584528.0 spike=0.81
- HRHO.CA: score=13.69 buy_ready=False sector_rank=19 price=26.59 support=26.05 resistance=29.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:55 AM market time freshness=DELAYED_CURRENT RSI=47.48 liquidity=47226584.0 spike=0.25
- ICID.CA: score=20.12 buy_ready=False sector_rank=7 price=6.81 support=4.5 resistance=6.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=90.23 liquidity=13389478.0 spike=0.93
- IDRE.CA: score=13.87 buy_ready=False sector_rank=7 price=43.66 support=39.8 resistance=49.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=53.64 liquidity=4754390.5 spike=0.14
- IFAP.CA: score=7.52 buy_ready=False sector_rank=6 price=19.39 support=16.5 resistance=23.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=37.74 liquidity=2316517.25 spike=0.18
- INFI.CA: score=11.15 buy_ready=False sector_rank=7 price=100.69 support=99.51 resistance=112.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=52.53 liquidity=3025456.5 spike=0.19
- IRON.CA: score=10.21 buy_ready=False sector_rank=18 price=32.56 support=31.83 resistance=35.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=36.2 liquidity=4350617.5 spike=0.55
- ISMA.CA: score=20.12 buy_ready=False sector_rank=7 price=29.69 support=20.66 resistance=30.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=92.96 liquidity=10758071.0 spike=0.21
- ISMQ.CA: score=24.06 buy_ready=False sector_rank=18 price=8.25 support=7.27 resistance=8.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=67.86 liquidity=107060328.0 spike=2.1
- ISPH.CA: score=22.81 buy_ready=False sector_rank=9 price=12.32 support=11.12 resistance=12.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:55 AM market time freshness=DELAYED_CURRENT RSI=63.98 liquidity=34261324.0 spike=0.22
- JUFO.CA: score=20.07 buy_ready=False sector_rank=8 price=30.15 support=26.51 resistance=30.82 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:55 AM market time freshness=DELAYED_CURRENT RSI=75.46 liquidity=13591435.0 spike=0.28
- KABO.CA: score=21.34 buy_ready=False sector_rank=4 price=6.36 support=5.92 resistance=6.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT RSI=72.34 liquidity=12440935.0 spike=0.62
- KWIN.CA: score=24.46 buy_ready=False sector_rank=7 price=73.03 support=69.0 resistance=80.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT RSI=58.39 liquidity=10377440.0 spike=2.67
- KZPC.CA: score=24.94 buy_ready=False sector_rank=7 price=10.88 support=10.3 resistance=11.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=48.59 liquidity=33581980.0 spike=2.91
- LCSW.CA: score=10.78 buy_ready=False sector_rank=12 price=27.18 support=26.16 resistance=29.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT RSI=53.42 liquidity=2202406.25 spike=0.14
- LUTS.CA: score=24.54 buy_ready=False sector_rank=7 price=0.66 support=0.54 resistance=0.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=68.55 liquidity=44543916.0 spike=2.71
- MAAL.CA: score=23.76 buy_ready=False sector_rank=7 price=6.11 support=4.44 resistance=6.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=8644112.0 spike=0.68
- MASR.CA: score=24.32 buy_ready=False sector_rank=7 price=7.11 support=6.63 resistance=7.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=52.34 liquidity=150702656.0 spike=2.6
- MBSC.CA: score=20.58 buy_ready=False sector_rank=12 price=275.0 support=261.52 resistance=295.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=37.97 liquidity=17696974.0 spike=0.36
- MCQE.CA: score=15.58 buy_ready=False sector_rank=12 price=183.0 support=185.59 resistance=201.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=44.13 liquidity=14424044.0 spike=0.75
- MCRO.CA: score=20.12 buy_ready=False sector_rank=7 price=1.26 support=1.21 resistance=1.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=57.89 liquidity=16677856.0 spike=0.19
- MENA.CA: score=26.08 buy_ready=False sector_rank=1 price=7.07 support=5.8 resistance=7.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=51.75 liquidity=9676442.0 spike=0.6
- MEPA.CA: score=14.09 buy_ready=False sector_rank=7 price=1.71 support=1.63 resistance=1.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=2972317.0 spike=0.16
- MFPC.CA: score=9.86 buy_ready=False sector_rank=18 price=42.01 support=42.01 resistance=46.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:55 AM market time freshness=DELAYED_CURRENT RSI=28.62 liquidity=28149568.0 spike=0.33
- MFSC.CA: score=7.3 buy_ready=False sector_rank=7 price=45.4 support=40.62 resistance=65.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT RSI=12.81 liquidity=3182667.0 spike=0.21
- MHOT.CA: score=18.56 buy_ready=False sector_rank=2 price=30.69 support=26.3 resistance=34.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT RSI=62.18 liquidity=5158943.0 spike=0.25
- MICH.CA: score=11.12 buy_ready=False sector_rank=7 price=38.97 support=36.7 resistance=40.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=79981536.0 spike=8.95
- MILS.CA: score=14.09 buy_ready=False sector_rank=7 price=143.51 support=127.01 resistance=153.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=70.06 liquidity=2965481.25 spike=0.13
- MIPH.CA: score=10.92 buy_ready=False sector_rank=9 price=658.83 support=640.0 resistance=729.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=39.51 liquidity=2111803.25 spike=0.66
- MOED.CA: score=4.95 buy_ready=False sector_rank=7 price=0.69 support=0.68 resistance=0.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=26.04 liquidity=4834088.0 spike=0.37
- MOIL.CA: score=14.5 buy_ready=False sector_rank=13 price=0.48 support=0.44 resistance=0.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:16 AM market time freshness=DELAYED_CURRENT RSI=64.71 liquidity=19952.96 spike=0.11
- MOIN.CA: score=8.68 buy_ready=False sector_rank=7 price=25.16 support=24.02 resistance=26.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=67.2 liquidity=555380.19 spike=0.28
- MOSC.CA: score=5.27 buy_ready=False sector_rank=7 price=261.0 support=264.0 resistance=320.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=19.23 liquidity=1148377.0 spike=0.09
- MPCI.CA: score=23.12 buy_ready=False sector_rank=7 price=227.05 support=193.8 resistance=238.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=68.96 liquidity=41103856.0 spike=0.46
- MPCO.CA: score=21.21 buy_ready=False sector_rank=6 price=1.78 support=1.54 resistance=1.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:55 AM market time freshness=DELAYED_CURRENT RSI=70.83 liquidity=23277186.0 spike=0.32
- MPRC.CA: score=23.12 buy_ready=False sector_rank=7 price=33.11 support=30.61 resistance=34.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT RSI=62.93 liquidity=14190391.0 spike=0.65
- MTIE.CA: score=15.32 buy_ready=False sector_rank=5 price=9.05 support=8.71 resistance=9.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:55 AM market time freshness=DELAYED_CURRENT RSI=48.87 liquidity=5987878.5 spike=0.29
- NAHO.CA: score=5.13 buy_ready=False sector_rank=7 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:45 AM market time freshness=DELAYED_CURRENT RSI=44.44 liquidity=14441.6 spike=0.39
- NCCW.CA: score=20.24 buy_ready=False sector_rank=7 price=6.65 support=5.13 resistance=6.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=82.23 liquidity=26238062.0 spike=1.06
- NEDA.CA: score=11.25 buy_ready=False sector_rank=7 price=2.8 support=2.65 resistance=2.87 source=Yahoo Finance as_of=2026-06-08T21:00:00+00:00 freshness=FRESH RSI=60.0 liquidity=132372.8 spike=0.27
- NHPS.CA: score=9.48 buy_ready=False sector_rank=7 price=69.43 support=67.53 resistance=73.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:55 AM market time freshness=DELAYED_CURRENT RSI=46.68 liquidity=1360014.13 spike=0.13
- NINH.CA: score=5.59 buy_ready=False sector_rank=7 price=17.59 support=17.53 resistance=20.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=26.42 liquidity=1468600.5 spike=0.15
- NIPH.CA: score=18.81 buy_ready=False sector_rank=9 price=164.17 support=155.1 resistance=186.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=57.17 liquidity=37929692.0 spike=0.33
- OBRI.CA: score=22.4 buy_ready=False sector_rank=7 price=36.7 support=33.63 resistance=39.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=48.8 liquidity=24280482.0 spike=2.14
- OCDI.CA: score=22.4 buy_ready=False sector_rank=1 price=21.39 support=20.19 resistance=23.67 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=51.38 liquidity=14469206.0 spike=0.34
- OCPH.CA: score=12.01 buy_ready=False sector_rank=7 price=358.61 support=350.0 resistance=409.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT RSI=48.02 liquidity=2887509.5 spike=0.3
- ODIN.CA: score=17.66 buy_ready=False sector_rank=7 price=2.14 support=1.89 resistance=2.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:55 AM market time freshness=DELAYED_CURRENT RSI=79.07 liquidity=7541837.5 spike=0.71
- OFH.CA: score=18.12 buy_ready=False sector_rank=7 price=0.61 support=0.6 resistance=0.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT RSI=51.11 liquidity=12878894.0 spike=0.58
- OIH.CA: score=12.35 buy_ready=False sector_rank=3 price=1.39 support=1.35 resistance=1.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:55 AM market time freshness=DELAYED_CURRENT RSI=27.59 liquidity=22858398.0 spike=0.2
- OLFI.CA: score=21.07 buy_ready=False sector_rank=8 price=21.89 support=21.0 resistance=22.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:55 AM market time freshness=DELAYED_CURRENT RSI=61.66 liquidity=18932670.0 spike=0.91
- ORAS.CA: score=4.6 buy_ready=False sector_rank=20 price=750.62 support=722.0 resistance=763.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=364709152.0 spike=1.0
- ORHD.CA: score=24.4 buy_ready=False sector_rank=1 price=37.71 support=32.9 resistance=39.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=62.47 liquidity=177970560.0 spike=0.87
- ORWE.CA: score=21.34 buy_ready=False sector_rank=4 price=23.64 support=21.6 resistance=24.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:55 AM market time freshness=DELAYED_CURRENT RSI=72.17 liquidity=14641922.0 spike=0.32
- PHAR.CA: score=13.48 buy_ready=False sector_rank=9 price=86.39 support=83.96 resistance=92.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:46 AM market time freshness=DELAYED_CURRENT RSI=46.88 liquidity=4664829.5 spike=0.14
- PHDC.CA: score=22.4 buy_ready=False sector_rank=1 price=15.07 support=13.01 resistance=16.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=66.12 liquidity=85593992.0 spike=0.21
- PHTV.CA: score=11.81 buy_ready=False sector_rank=7 price=207.36 support=203.25 resistance=233.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=56.33 liquidity=2688607.0 spike=0.18
- POUL.CA: score=17.52 buy_ready=False sector_rank=8 price=37.07 support=34.8 resistance=39.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:55 AM market time freshness=DELAYED_CURRENT RSI=56.22 liquidity=6449461.5 spike=0.14
- PRCL.CA: score=19.01 buy_ready=False sector_rank=12 price=25.29 support=21.01 resistance=28.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT RSI=62.27 liquidity=6436018.0 spike=0.18
- PRDC.CA: score=21.4 buy_ready=False sector_rank=1 price=6.27 support=5.3 resistance=6.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:55 AM market time freshness=DELAYED_CURRENT RSI=76.3 liquidity=15799972.0 spike=0.8
- PRMH.CA: score=15.82 buy_ready=False sector_rank=7 price=2.71 support=2.17 resistance=2.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=77.53 liquidity=7703504.5 spike=0.51
- RACC.CA: score=11.22 buy_ready=False sector_rank=7 price=9.87 support=9.56 resistance=12.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=47.73 liquidity=2095279.88 spike=0.11
- RAKT.CA: score=7.49 buy_ready=False sector_rank=7 price=23.24 support=22.1 resistance=25.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT RSI=54.9 liquidity=307903.81 spike=1.03
- RAYA.CA: score=18.61 buy_ready=False sector_rank=11 price=7.38 support=6.94 resistance=8.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=51.57 liquidity=47416012.0 spike=0.42
- RMDA.CA: score=22.81 buy_ready=False sector_rank=9 price=5.18 support=4.95 resistance=5.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:55 AM market time freshness=DELAYED_CURRENT RSI=63.41 liquidity=17037796.0 spike=0.16
- ROTO.CA: score=17.7 buy_ready=False sector_rank=7 price=34.94 support=32.66 resistance=36.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=71.72 liquidity=4582371.5 spike=0.35
- RREI.CA: score=16.56 buy_ready=False sector_rank=7 price=3.52 support=3.32 resistance=3.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT RSI=52.17 liquidity=7436870.0 spike=0.32
- RTVC.CA: score=16.55 buy_ready=False sector_rank=7 price=4.0 support=3.75 resistance=4.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:55 AM market time freshness=DELAYED_CURRENT RSI=57.81 liquidity=3427720.75 spike=0.51
- RUBX.CA: score=9.02 buy_ready=False sector_rank=7 price=10.43 support=9.8 resistance=11.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:55 AM market time freshness=DELAYED_CURRENT RSI=32.96 liquidity=4897077.5 spike=0.33
- SAUD.CA: score=12.19 buy_ready=False sector_rank=16 price=21.79 support=21.8 resistance=24.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT RSI=41.58 liquidity=7021432.0 spike=0.51
- SCEM.CA: score=18.58 buy_ready=False sector_rank=12 price=63.4 support=62.5 resistance=72.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:55 AM market time freshness=DELAYED_CURRENT RSI=38.89 liquidity=26028592.0 spike=0.66
- SCFM.CA: score=6.9 buy_ready=False sector_rank=7 price=258.8 support=255.7 resistance=315.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=30.8 liquidity=2776763.75 spike=0.13
- SCTS.CA: score=4.97 buy_ready=False sector_rank=14 price=622.53 support=590.01 resistance=690.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:55 AM market time freshness=DELAYED_CURRENT RSI=33.16 liquidity=1529056.63 spike=0.14
- SDTI.CA: score=15.34 buy_ready=False sector_rank=7 price=47.52 support=43.4 resistance=47.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=68.43 liquidity=2223065.75 spike=0.11
- SEIG.CA: score=13.92 buy_ready=False sector_rank=7 price=188.07 support=173.35 resistance=205.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT RSI=57.11 liquidity=796954.38 spike=0.15
- SIPC.CA: score=18.38 buy_ready=False sector_rank=7 price=3.64 support=3.4 resistance=3.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:55 AM market time freshness=DELAYED_CURRENT RSI=55.56 liquidity=5259475.0 spike=0.34
- SKPC.CA: score=13.86 buy_ready=False sector_rank=18 price=17.19 support=16.8 resistance=18.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:55 AM market time freshness=DELAYED_CURRENT RSI=40.27 liquidity=12936621.0 spike=0.19
- SMFR.CA: score=11.52 buy_ready=False sector_rank=7 price=204.78 support=203.51 resistance=224.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:45 AM market time freshness=DELAYED_CURRENT RSI=35.22 liquidity=2402559.25 spike=0.4
- SNFC.CA: score=19.03 buy_ready=False sector_rank=7 price=12.11 support=11.66 resistance=12.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:55 AM market time freshness=DELAYED_CURRENT RSI=41.28 liquidity=9912979.0 spike=0.37
- SPIN.CA: score=2.82 buy_ready=False sector_rank=4 price=14.08 support=13.69 resistance=15.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:04 AM market time freshness=DELAYED_CURRENT RSI=23.93 liquidity=1476336.0 spike=0.3
- SPMD.CA: score=18.59 buy_ready=False sector_rank=7 price=0.42 support=0.38 resistance=0.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:58 AM market time freshness=DELAYED_CURRENT RSI=58.42 liquidity=7471019.5 spike=0.3
- SUGR.CA: score=16.95 buy_ready=False sector_rank=8 price=49.9 support=48.0 resistance=52.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=42.71 liquidity=5877192.5 spike=0.37
- SVCE.CA: score=14.12 buy_ready=False sector_rank=7 price=8.62 support=8.33 resistance=9.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:58 AM market time freshness=DELAYED_CURRENT RSI=28.71 liquidity=13572068.0 spike=0.12
- SWDY.CA: score=16.03 buy_ready=False sector_rank=10 price=87.41 support=85.25 resistance=90.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT RSI=54.88 liquidity=7231291.5 spike=0.21
- TALM.CA: score=15.77 buy_ready=False sector_rank=14 price=15.93 support=15.12 resistance=17.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=48.64 liquidity=3330704.75 spike=0.25
- TMGH.CA: score=17.4 buy_ready=False sector_rank=1 price=95.89 support=91.87 resistance=101.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:55 AM market time freshness=DELAYED_CURRENT RSI=34.65 liquidity=163009376.0 spike=0.33
- TRTO.CA: score=7.12 buy_ready=False sector_rank=7 price=0.03 support=0.03 resistance=0.04 source=Yahoo Finance as_of=2026-06-08T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=189.24 spike=0.4
- UEFM.CA: score=0.72 buy_ready=False sector_rank=7 price=473.74 support=455.6 resistance=504.97 source=Yahoo Finance as_of=2026-06-08T21:00:00+00:00 freshness=FRESH RSI=33.63 liquidity=604018.49 spike=0.72
- UEGC.CA: score=21.7 buy_ready=False sector_rank=7 price=1.47 support=1.3 resistance=1.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT RSI=72.0 liquidity=33048112.0 spike=1.29
- UNIP.CA: score=24.62 buy_ready=False sector_rank=7 price=0.33 support=0.28 resistance=0.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=72.13 liquidity=44822876.0 spike=2.75
- UNIT.CA: score=21.96 buy_ready=False sector_rank=1 price=14.46 support=11.28 resistance=15.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT RSI=56.32 liquidity=7561845.0 spike=0.71
- WCDF.CA: score=4.24 buy_ready=False sector_rank=7 price=539.17 support=535.0 resistance=558.89 source=Yahoo Finance as_of=2026-06-08T21:00:00+00:00 freshness=FRESH RSI=25.38 liquidity=124548.27 spike=0.42
- WKOL.CA: score=13.37 buy_ready=False sector_rank=7 price=301.02 support=290.0 resistance=324.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=48.9 liquidity=2253881.75 spike=0.36
- ZEOT.CA: score=14.44 buy_ready=False sector_rank=7 price=9.18 support=8.43 resistance=9.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=59.86 liquidity=1316867.63 spike=0.19
- ZMID.CA: score=28.4 buy_ready=False sector_rank=1 price=6.39 support=5.77 resistance=6.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=63.11 liquidity=112833352.0 spike=0.5

## Backtesting Lite
- ZMID.CA: 180d return=62.61%, max drawdown=-19.84%, MA20>MA50 days last20=20, as_of=2026-06-08T21:00:00+00:00
- MENA.CA: 180d return=49.12%, max drawdown=-23.9%, MA20>MA50 days last20=20, as_of=2026-06-08T21:00:00+00:00
- ARAB.CA: 180d return=12.09%, max drawdown=-38.02%, MA20>MA50 days last20=20, as_of=2026-06-08T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- ZMID.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=525 sources=3 expected=Zahraa Maadi Investment and Development summary=Zahraa Maadi unveils distribution date for 2025 cash dividends; Zahraa Maadi to disburse EGP 250m dividends for 2025; Zahraa Maadi’s stock faces key resistance at EGP 5.22
  - Zahraa Maadi unveils distribution date for 2025 cash dividends: https://english.mubasher.info/news/4594804/Zahraa-Maadi-unveils-distribution-date-for-2025-cash-dividends/
  - Zahraa Maadi to disburse EGP 250m dividends for 2025: https://english.mubasher.info/news/4583591/Zahraa-Maadi-to-disburse-EGP-250m-dividends-for-2025/
  - Zahraa Maadi’s stock faces key resistance at EGP 5.22: https://english.mubasher.info/news/4563531/Zahraa-Maadi-s-stock-faces-key-resistance-at-EGP-5-22/
- MENA.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Mena Touristic and Real Estate Investment summary=Mena stock tests key resistance level on back of buying power; Bahraini Lamar acquires Kuwaiti Mawared’s stake in Egypt-based Mena; Mena Touristic losses up 19.2% in Q1-20
  - Mena stock tests key resistance level on back of buying power: https://english.mubasher.info/news/4531390/Mena-stock-tests-key-resistance-level-on-back-of-buying-power/
  - Bahraini Lamar acquires Kuwaiti Mawared’s stake in Egypt-based Mena: https://english.mubasher.info/news/3963376/Bahraini-Lamar-acquires-Kuwaiti-Mawared-s-stake-in-Egypt-based-Mena/
  - Mena Touristic losses up 19.2% in Q1-20: https://english.mubasher.info/news/3654698/Mena-Touristic-losses-up-19-2-in-Q1-20/
- ARAB.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Arab Developers Holding summary=Arab Developers Holding unveils EGP 1bn expansion plans to improve financial efficiency; FRA gives initial approval for Arab Developers’ rights issue; Arab Developers stock stabilizes after correction
  - Arab Developers Holding unveils EGP 1bn expansion plans to improve financial efficiency: https://english.mubasher.info/news/4601724/Arab-Developers-Holding-unveils-EGP-1bn-expansion-plans-to-improve-financial-efficiency/
  - FRA gives initial approval for Arab Developers’ rights issue: https://english.mubasher.info/news/4582627/FRA-gives-initial-approval-for-Arab-Developers-rights-issue/
  - Arab Developers stock stabilizes after correction: https://english.mubasher.info/news/4564643/Arab-Developers-stock-stabilizes-after-correction/
- ANFI.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Tycoon Holding Company For Financial Investments summary=Evidence rejected for ANFI.CA: source text did not clearly match ANFI.CA / Tycoon Holding Company For Financial Investments.
- KZPC.CA: status=OLD_ACCEPTED latest=2024-01-01 age_days=891 sources=3 expected=Kafr El Zayat For Pesticides & Chemicals Co.(S.A.E) summary=Kafr El Zayat to set up fund with EGP 5m capital; Kafr El Zayat Pesticides targets EGP 1.73bn sales in 2024; Kafr El Zayat Pesticides’ EGM approves stock split, capital hike
  - Kafr El Zayat to set up fund with EGP 5m capital: https://english.mubasher.info/news/4201137/Kafr-El-Zayat-to-set-up-fund-with-EGP-5m-capital/
  - Kafr El Zayat Pesticides targets EGP 1.73bn sales in 2024: https://english.mubasher.info/news/4200526/Kafr-El-Zayat-Pesticides-targets-EGP-1-73bn-sales-in-2024/
  - Kafr El Zayat Pesticides’ EGM approves stock split, capital hike: https://english.mubasher.info/news/4052937/Kafr-El-Zayat-Pesticides-EGM-approves-stock-split-capital-hike/
- UNIP.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Universal For Paper and Packaging Materials summary=Evidence rejected for UNIP.CA: source text did not clearly match UNIP.CA / Universal For Paper and Packaging Materials.
- LUTS.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Lotus Agri Capital summary=Evidence rejected for LUTS.CA: source text did not clearly match LUTS.CA / Lotus Agri Capital.
- KWIN.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=El Kahera El Watania Investment summary=ADIB Egypt&#39;s Cairo National unveils equity reduction transaction worth over EGP 3m; El Kahera El Watania to buy stake in Assiut for Agricultural Development; Tycoon Holding acquires 85% of Alexandria National Investment
  - ADIB Egypt&#39;s Cairo National unveils equity reduction transaction worth over EGP 3m: https://english.mubasher.info/news/4546852/ADIB-Egypt-s-Cairo-National-unveils-equity-reduction-transaction-worth-over-EGP-3m/
  - El Kahera El Watania to buy stake in Assiut for Agricultural Development: https://english.mubasher.info/news/4009433/El-Kahera-El-Watania-to-buy-stake-in-Assiut-for-Agricultural-Development/
  - Tycoon Holding acquires 85% of Alexandria National Investment: https://english.mubasher.info/news/3844623/Tycoon-Holding-acquires-85-of-Alexandria-National-Investment/

## Warnings
- Evidence for ZMID.CA matches the company but appears old; latest detected date is 2025-01-01.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence for MENA.CA matches the company but no source/report date was detected.
- Evidence for ARAB.CA matches the company but no source/report date was detected.
- Mubasher stock-page evidence failed for ANFI.CA: 404 Client Error: Not Found for url: https://english.mubasher.info/markets/EGX/stocks/ANFI
- No Yahoo or Mubasher evidence found for ANFI.CA.
- Evidence rejected for ANFI.CA: source text did not clearly match ANFI.CA / Tycoon Holding Company For Financial Investments.
- Evidence for KZPC.CA matches the company but appears old; latest detected date is 2024-01-01.
- Evidence rejected for UNIP.CA: source text did not clearly match UNIP.CA / Universal For Paper and Packaging Materials.
- Mubasher stock page returned no evidence titles for LUTS.CA.
- No Yahoo or Mubasher evidence found for LUTS.CA.
- Evidence rejected for LUTS.CA: source text did not clearly match LUTS.CA / Lotus Agri Capital.
- Evidence for KWIN.CA matches the company but no source/report date was detected.
