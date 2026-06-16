# Telegram-First EGX Scanner Report

Scan phase: Open liquidity confirmation
Generated UTC: 2026-06-16T11:36:15.647760+00:00
Generated Cairo: 2026-06-16 14:36
Run timing: target 09:15 Cairo | generated Cairo 2026-06-16 14:36 | cron 15 6 * * 0-4
Trigger: scheduled cron=15 6 * * 0-4 mapped to open_confirm; Cairo now 2026-06-16 14:32

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 0
- Tradeable price/liquidity tickers: 179/190
- Top sector: Automotive & Distribution

## Market Context
- Market trend: Bearish
- Source: Mubasher EGX market page (delayed public data)
- As of: Tuesday, June 16
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 40.0% / above MA50 50.0%
- EGX70 regime: MIXED / above MA20 47.37% / above MA50 73.68%
- Sector breadth: 28.57%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- CCAP.CA: liquidity=679041408.0 spike=0.79 score=17.46
- PHDC.CA: liquidity=587560704.0 spike=1.43 score=25.26
- TMGH.CA: liquidity=456631904.0 spike=1.0 score=20.4
- COMI.CA: liquidity=450561248.0 spike=0.71 score=19.95
- HRHO.CA: liquidity=420805440.0 spike=3.02 score=23.82

## AI Narrative
- Provider: OpenRouter OK
- Model: openai/gpt-oss-120b:free
- Summary: The local scanner flags a defensive market regime – EGX30 is bearish and EGX70 mixed, with sector breadth only 28.57% and risk mode set to DEFENSIVE_NO_NEW_BUY. Consequently all tickets are marked HOLD despite bullish watch outlooks. Liquidity spikes and proximity to resistance/support are noted, but weak breadth and bearish trends limit new entries for the next 1‑3 days.
- EGX30 bearish, EGX70 mixed → overall risk mode defensive, no new buys allowed.
- Sector breadth low (28.57%); only Automotive, Agriculture & Food, and Real Estate show relative strength.
- Top tickets (MTIE, HDBK, MPCO, etc.) show strong liquidity spikes but sit near resistance or have overbought RSI.
- Support levels are 5‑27% away; resistance within 1‑2% suggests limited upside in the short term.
- Uncertainty remains high as market breadth could shift, but current regime favors holding positions only.

## Top Liquidity Spikes
- ZEOT.CA: spike=30.85 liquidity=196665104.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- EASB.CA: spike=9.83 liquidity=29006738.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- CERA.CA: spike=5.27 liquidity=69372832.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- HDBK.CA: spike=4.2 liquidity=59049372.0 outlook=BULLISH_WATCH score=93.88 buy_ready=False
- ANFI.CA: spike=3.88 liquidity=202227615.0 outlook=CONSTRUCTIVE score=61.32 buy_ready=False

## Sector Leaderboard
- #1 Automotive & Distribution: score=11.44 5d=4.94% 20d=1.99% aboveMA50=100.0%
- #2 Agriculture & Food Production: score=10.42 5d=6.94% 20d=7.82% aboveMA50=50.0%
- #3 Real Estate: score=6.53 5d=0.0% 20d=7.32% aboveMA50=76.92%
- #4 Education: score=5.2 5d=1.38% 20d=-1.41% aboveMA50=100.0%
- #5 Food, Beverages & Tobacco: score=5.15 5d=0.13% 20d=2.66% aboveMA50=85.71%
- #6 Banking & Financials: score=4.88 5d=0.06% 20d=0.77% aboveMA50=70.0%
- #7 General / Verified EGX Expansion: score=4.32 5d=-0.33% 20d=-0.86% aboveMA50=70.19%
- #8 Tourism & Leisure: score=4.15 5d=-3.06% 20d=9.1% aboveMA50=100.0%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- MTIE.CA: BULLISH_WATCH score=100 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=close to resistance
- RREI.CA: BULLISH_WATCH score=97.32 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=No major short-term scanner risk flags.
- HDBK.CA: BULLISH_WATCH score=93.88 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=close to resistance
- PHTV.CA: BULLISH_WATCH score=93.32 liquidity=TRADEABLE sector=IMPROVING risk=No major short-term scanner risk flags.
- MOSC.CA: BULLISH_WATCH score=91.32 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=No major short-term scanner risk flags.
- PHDC.CA: BULLISH_WATCH score=89.53 liquidity=TRADEABLE sector=LEADING risk=far above support
- ORHD.CA: BULLISH_WATCH score=86.53 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- UNIT.CA: BULLISH_WATCH score=86.53 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- MENA.CA: BULLISH_WATCH score=86.53 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- GDWA.CA: BULLISH_WATCH score=86.32 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=No major short-term scanner risk flags.

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- No provider failures.

## Ranked Scanner Results
- AALR.CA: score=12.91 buy_ready=False sector_rank=7 price=205.78 support=195.1 resistance=231.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=53.35 liquidity=2178464.25 spike=0.31
- ABUK.CA: score=9.14 buy_ready=False sector_rank=21 price=71.71 support=72.2 resistance=90.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=4.53 liquidity=141062016.0 spike=1.05
- ACAMD.CA: score=20.73 buy_ready=False sector_rank=7 price=2.36 support=2.14 resistance=2.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=58.46 liquidity=91972992.0 spike=0.71
- ACGC.CA: score=12.21 buy_ready=False sector_rank=9 price=9.45 support=8.95 resistance=10.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=34.36 liquidity=8907088.0 spike=0.15
- ADCI.CA: score=18.03 buy_ready=False sector_rank=7 price=227.1 support=202.22 resistance=230.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=68.48 liquidity=8763726.0 spike=1.27
- ADIB.CA: score=20.95 buy_ready=False sector_rank=6 price=47.63 support=44.01 resistance=48.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=48.4 liquidity=68575040.0 spike=0.55
- ADPC.CA: score=15.73 buy_ready=False sector_rank=7 price=3.6 support=3.45 resistance=4.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=45.76 liquidity=10910743.0 spike=0.43
- AFDI.CA: score=16.17 buy_ready=False sector_rank=7 price=42.8 support=40.15 resistance=46.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=55.48 liquidity=5443557.5 spike=0.33
- AFMC.CA: score=9.56 buy_ready=False sector_rank=7 price=71.23 support=67.0 resistance=77.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=47.13 liquidity=833926.0 spike=0.14
- AJWA.CA: score=8.63 buy_ready=False sector_rank=7 price=181.0 support=172.98 resistance=188.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=58474916.0 spike=2.45
- ALCN.CA: score=12.5 buy_ready=False sector_rank=15 price=28.61 support=25.51 resistance=33.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=41.08 liquidity=7649520.0 spike=0.49
- ALUM.CA: score=14.18 buy_ready=False sector_rank=7 price=23.08 support=23.05 resistance=26.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=53.51 liquidity=5451780.0 spike=0.32
- AMER.CA: score=7.72 buy_ready=False sector_rank=3 price=2.49 support=2.47 resistance=2.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=123964464.0 spike=1.16
- AMES.CA: score=3.12 buy_ready=False sector_rank=7 price=48.9 support=48.0 resistance=55.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=29.88 liquidity=391923.09 spike=0.09
- AMIA.CA: score=20.73 buy_ready=False sector_rank=7 price=9.18 support=8.54 resistance=9.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=70.87 liquidity=10960644.0 spike=0.61
- AMOC.CA: score=10.28 buy_ready=False sector_rank=10 price=7.85 support=7.71 resistance=9.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=29.36 liquidity=29253350.0 spike=0.39
- ANFI.CA: score=24.73 buy_ready=False sector_rank=7 price=28.75 support=13.73 resistance=28.75 source=Yahoo Finance as_of=2026-06-14T21:00:00+00:00 freshness=FRESH RSI=96.86 liquidity=202227615.0 spike=3.88
- APSW.CA: score=3.0 buy_ready=False sector_rank=7 price=8.53 support=8.24 resistance=9.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=31.58 liquidity=1734798.5 spike=1.77
- ARAB.CA: score=25.02 buy_ready=False sector_rank=3 price=0.22 support=0.19 resistance=0.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=69.44 liquidity=114685952.0 spike=1.31
- ARCC.CA: score=18.26 buy_ready=False sector_rank=11 price=56.05 support=53.35 resistance=60.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=53.41 liquidity=23911138.0 spike=0.65
- AREH.CA: score=19.73 buy_ready=False sector_rank=7 price=1.58 support=1.27 resistance=1.62 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=87.18 liquidity=25566024.0 spike=0.88
- ARVA.CA: score=18.77 buy_ready=False sector_rank=7 price=11.27 support=7.71 resistance=13.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=79.19 liquidity=43019852.0 spike=1.52
- ASCM.CA: score=19.73 buy_ready=False sector_rank=7 price=59.0 support=47.3 resistance=64.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=80.71 liquidity=40577396.0 spike=0.58
- ASPI.CA: score=22.73 buy_ready=False sector_rank=7 price=0.31 support=0.25 resistance=0.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=61.57 liquidity=26618008.0 spike=0.4
- ATLC.CA: score=17.38 buy_ready=False sector_rank=16 price=5.16 support=4.7 resistance=5.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=67.29 liquidity=5348554.5 spike=1.13
- ATQA.CA: score=19.44 buy_ready=False sector_rank=21 price=9.7 support=9.02 resistance=10.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=49.1 liquidity=60280940.0 spike=1.7
- AXPH.CA: score=10.44 buy_ready=False sector_rank=7 price=1081.84 support=1111.0 resistance=1175.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=45.47 liquidity=1714305.13 spike=0.76
- BINV.CA: score=18.0 buy_ready=False sector_rank=19 price=47.25 support=40.8 resistance=49.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=66.54 liquidity=8540421.0 spike=0.8
- BIOC.CA: score=11.54 buy_ready=False sector_rank=7 price=71.82 support=68.34 resistance=75.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=45.0 liquidity=2809520.25 spike=0.78
- BTFH.CA: score=13.78 buy_ready=False sector_rank=16 price=3.0 support=2.96 resistance=3.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=45.59 liquidity=108248216.0 spike=0.52
- CAED.CA: score=9.97 buy_ready=False sector_rank=7 price=70.8 support=67.21 resistance=79.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=39.83 liquidity=1246551.63 spike=0.19
- CANA.CA: score=22.95 buy_ready=False sector_rank=6 price=37.22 support=34.07 resistance=39.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:09 PM market time freshness=DELAYED_CURRENT RSI=63.59 liquidity=12045348.0 spike=0.89
- CCAP.CA: score=17.46 buy_ready=False sector_rank=19 price=5.11 support=4.92 resistance=5.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=47.49 liquidity=679041408.0 spike=0.79
- CCRS.CA: score=20.85 buy_ready=False sector_rank=7 price=2.51 support=2.25 resistance=2.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=49.09 liquidity=24781168.0 spike=1.06
- CEFM.CA: score=10.54 buy_ready=False sector_rank=7 price=103.68 support=100.53 resistance=116.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=40.43 liquidity=1810362.38 spike=0.51
- CERA.CA: score=10.73 buy_ready=False sector_rank=7 price=1.29 support=1.17 resistance=1.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=69372832.0 spike=5.27
- CFGH.CA: score=-0.27 buy_ready=False sector_rank=7 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance as_of=2026-06-14T21:00:00+00:00 freshness=FRESH RSI=0.0 liquidity=4303.99 spike=0.7
- CICH.CA: score=1.33 buy_ready=False sector_rank=16 price=11.53 support=11.1 resistance=13.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=27.27 liquidity=1552479.25 spike=0.48
- CIEB.CA: score=13.66 buy_ready=False sector_rank=6 price=23.58 support=23.27 resistance=24.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=49.69 liquidity=5710884.5 spike=0.77
- CIRA.CA: score=15.15 buy_ready=False sector_rank=4 price=26.3 support=25.23 resistance=28.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=50.48 liquidity=6065684.5 spike=0.28
- CLHO.CA: score=17.56 buy_ready=False sector_rank=12 price=15.59 support=14.25 resistance=16.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=55.46 liquidity=7375807.5 spike=0.25
- CNFN.CA: score=10.78 buy_ready=False sector_rank=16 price=4.41 support=4.36 resistance=4.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=42.65 liquidity=7000365.0 spike=0.45
- COMI.CA: score=19.95 buy_ready=False sector_rank=6 price=133.2 support=129.8 resistance=136.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=56.11 liquidity=450561248.0 spike=0.71
- COPR.CA: score=19.73 buy_ready=False sector_rank=7 price=0.37 support=0.34 resistance=0.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=54.84 liquidity=39812236.0 spike=0.98
- COSG.CA: score=21.27 buy_ready=False sector_rank=7 price=1.61 support=1.49 resistance=1.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=55.81 liquidity=86856816.0 spike=1.27
- CPCI.CA: score=10.27 buy_ready=False sector_rank=7 price=362.52 support=345.0 resistance=368.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=71.12 liquidity=1537138.63 spike=0.66
- CSAG.CA: score=13.17 buy_ready=False sector_rank=15 price=31.22 support=30.08 resistance=32.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=51.0 liquidity=5320786.0 spike=0.39
- DAPH.CA: score=20.73 buy_ready=False sector_rank=7 price=81.26 support=76.6 resistance=89.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=41.06 liquidity=11262527.0 spike=0.42
- DEIN.CA: score=6.73 buy_ready=False sector_rank=7 price=11.38 support=11.38 resistance=13.65 source=Yahoo Finance as_of=2026-06-14T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- DOMT.CA: score=1.65 buy_ready=False sector_rank=5 price=24.47 support=23.7 resistance=26.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=27.27 liquidity=594415.75 spike=0.29
- DSCW.CA: score=19.19 buy_ready=False sector_rank=7 price=1.85 support=1.71 resistance=1.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=58.06 liquidity=63348316.0 spike=1.23
- DTPP.CA: score=1.7 buy_ready=False sector_rank=7 price=116.3 support=114.0 resistance=137.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=17.35 liquidity=972815.0 spike=0.48
- EALR.CA: score=13.22 buy_ready=False sector_rank=7 price=357.56 support=346.01 resistance=380.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=51.01 liquidity=2492238.5 spike=0.61
- EASB.CA: score=10.73 buy_ready=False sector_rank=7 price=7.33 support=5.9 resistance=7.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=29006738.0 spike=9.83
- EAST.CA: score=25.06 buy_ready=False sector_rank=5 price=39.0 support=37.01 resistance=39.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=63.42 liquidity=32234120.0 spike=0.47
- EBSC.CA: score=12.56 buy_ready=False sector_rank=7 price=1.9 support=1.64 resistance=2.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=70.37 liquidity=1831543.75 spike=0.66
- ECAP.CA: score=17.95 buy_ready=False sector_rank=7 price=32.56 support=28.7 resistance=32.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=81.33 liquidity=8780674.0 spike=1.72
- EDFM.CA: score=12.04 buy_ready=False sector_rank=7 price=331.68 support=320.2 resistance=355.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=56.83 liquidity=1270632.88 spike=2.02
- EEII.CA: score=20.73 buy_ready=False sector_rank=7 price=2.42 support=2.27 resistance=2.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=57.45 liquidity=10089831.0 spike=0.52
- EFIC.CA: score=-0.61 buy_ready=False sector_rank=21 price=204.02 support=192.01 resistance=219.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=25.91 liquidity=1346042.75 spike=0.38
- EFID.CA: score=19.06 buy_ready=False sector_rank=5 price=28.39 support=27.06 resistance=29.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=48.95 liquidity=32920384.0 spike=0.42
- EFIH.CA: score=14.5 buy_ready=False sector_rank=18 price=21.03 support=20.2 resistance=22.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=40.17 liquidity=26909366.0 spike=0.47
- EGAL.CA: score=9.04 buy_ready=False sector_rank=21 price=298.99 support=297.1 resistance=335.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=24.21 liquidity=34256852.0 spike=0.36
- EGAS.CA: score=14.05 buy_ready=False sector_rank=10 price=51.15 support=47.15 resistance=55.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=72.5 liquidity=3771289.25 spike=0.3
- EGBE.CA: score=9.01 buy_ready=False sector_rank=6 price=0.44 support=0.43 resistance=0.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=35.74 liquidity=56037.59 spike=0.48
- EGCH.CA: score=17.04 buy_ready=False sector_rank=21 price=13.79 support=12.9 resistance=15.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=43.18 liquidity=45136036.0 spike=0.46
- EGSA.CA: score=2.98 buy_ready=False sector_rank=14 price=8.78 support=8.3 resistance=9.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=21.87 liquidity=12908.61 spike=0.83
- EGTS.CA: score=20.4 buy_ready=False sector_rank=3 price=17.8 support=16.65 resistance=22.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=42.18 liquidity=52778644.0 spike=0.43
- EHDR.CA: score=20.73 buy_ready=False sector_rank=7 price=2.7 support=2.25 resistance=2.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=69.57 liquidity=29766946.0 spike=0.5
- EKHO.CA: score=10.28 buy_ready=False sector_rank=10 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-06-14T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=16.06 buy_ready=False sector_rank=13 price=2.14 support=2.06 resistance=2.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=48.15 liquidity=17767084.0 spike=0.68
- ELKA.CA: score=20.39 buy_ready=False sector_rank=7 price=1.31 support=1.12 resistance=1.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=65.79 liquidity=52665352.0 spike=1.33
- ELNA.CA: score=10.25 buy_ready=False sector_rank=7 price=39.45 support=37.11 resistance=41.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=39.76 liquidity=578597.13 spike=1.47
- ELSH.CA: score=6.51 buy_ready=False sector_rank=7 price=13.62 support=12.85 resistance=13.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=243234480.0 spike=1.39
- ELWA.CA: score=14.31 buy_ready=False sector_rank=7 price=2.03 support=1.79 resistance=2.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=60.61 liquidity=1581159.63 spike=0.49
- EMFD.CA: score=24.5 buy_ready=False sector_rank=3 price=12.38 support=9.83 resistance=12.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=70.0 liquidity=277003488.0 spike=1.05
- ENGC.CA: score=19.8 buy_ready=False sector_rank=7 price=35.8 support=32.31 resistance=36.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=73.25 liquidity=7067165.0 spike=0.5
- EOSB.CA: score=14.84 buy_ready=False sector_rank=7 price=1.48 support=1.34 resistance=1.55 source=Yahoo Finance as_of=2026-06-14T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=110727.68 spike=0.93
- EPCO.CA: score=25.73 buy_ready=False sector_rank=7 price=9.41 support=8.56 resistance=9.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=59.03 liquidity=39246164.0 spike=3.69
- EPPK.CA: score=8.45 buy_ready=False sector_rank=7 price=12.34 support=11.67 resistance=12.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=36.73 liquidity=723811.25 spike=0.64
- ETEL.CA: score=9.97 buy_ready=False sector_rank=14 price=92.65 support=89.61 resistance=98.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=32.31 liquidity=64865180.0 spike=0.79
- ETRS.CA: score=19.73 buy_ready=False sector_rank=7 price=10.0 support=7.37 resistance=10.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=78.63 liquidity=30513280.0 spike=0.47
- EXPA.CA: score=18.95 buy_ready=False sector_rank=6 price=18.66 support=18.31 resistance=20.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=47.04 liquidity=27059442.0 spike=0.76
- FAIT.CA: score=10.33 buy_ready=False sector_rank=6 price=37.21 support=35.01 resistance=38.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=50.81 liquidity=1377505.0 spike=0.24
- FAITA.CA: score=12.99 buy_ready=False sector_rank=6 price=0.99 support=0.98 resistance=1.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:37 PM market time freshness=DELAYED_CURRENT RSI=60.0 liquidity=36950.47 spike=0.83
- FERC.CA: score=2.21 buy_ready=False sector_rank=21 price=75.38 support=75.0 resistance=80.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=28.35 liquidity=4166436.0 spike=0.93
- FWRY.CA: score=9.5 buy_ready=False sector_rank=18 price=18.83 support=17.71 resistance=20.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=29.98 liquidity=215633952.0 spike=0.73
- GBCO.CA: score=26.4 buy_ready=False sector_rank=1 price=28.38 support=25.25 resistance=28.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=69.0 liquidity=42336780.0 spike=0.37
- GDWA.CA: score=20.75 buy_ready=False sector_rank=7 price=0.81 support=0.77 resistance=0.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=57.14 liquidity=20278764.0 spike=1.51
- GGCC.CA: score=13.86 buy_ready=False sector_rank=7 price=0.41 support=0.39 resistance=0.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=56.18 liquidity=6128260.5 spike=0.8
- GIHD.CA: score=12.85 buy_ready=False sector_rank=7 price=41.4 support=35.15 resistance=43.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=58.85 liquidity=2120084.5 spike=0.52
- GMCI.CA: score=12.02 buy_ready=False sector_rank=7 price=1.79 support=1.68 resistance=1.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=52.78 liquidity=555000.06 spike=1.37
- GRCA.CA: score=6.97 buy_ready=False sector_rank=7 price=53.35 support=50.2 resistance=60.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=35.59 liquidity=1245091.0 spike=0.18
- GSSC.CA: score=2.23 buy_ready=False sector_rank=7 price=247.54 support=228.1 resistance=268.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=22.42 liquidity=1499170.88 spike=0.28
- GTWL.CA: score=20.73 buy_ready=False sector_rank=7 price=48.39 support=45.47 resistance=56.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=37.94 liquidity=23765920.0 spike=3.52
- HDBK.CA: score=27.95 buy_ready=False sector_rank=6 price=148.0 support=138.0 resistance=148.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=56.68 liquidity=59049372.0 spike=4.2
- HELI.CA: score=20.4 buy_ready=False sector_rank=3 price=6.44 support=6.28 resistance=6.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=51.69 liquidity=115153424.0 spike=0.76
- HRHO.CA: score=23.82 buy_ready=False sector_rank=16 price=27.87 support=25.8 resistance=28.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=53.5 liquidity=420805440.0 spike=3.02
- ICID.CA: score=14.82 buy_ready=False sector_rank=7 price=7.17 support=4.5 resistance=7.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=85.77 liquidity=5093559.0 spike=0.31
- IDRE.CA: score=18.73 buy_ready=False sector_rank=7 price=43.54 support=41.01 resistance=47.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=40.08 liquidity=11650984.0 spike=0.36
- IFAP.CA: score=10.13 buy_ready=False sector_rank=2 price=19.37 support=16.5 resistance=23.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=37.96 liquidity=2730036.75 spike=0.33
- INFI.CA: score=5.14 buy_ready=False sector_rank=7 price=98.53 support=97.0 resistance=109.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=22.76 liquidity=2409984.75 spike=0.16
- IRON.CA: score=16.14 buy_ready=False sector_rank=21 price=32.56 support=31.3 resistance=35.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=40.46 liquidity=11808268.0 spike=1.55
- ISMA.CA: score=22.73 buy_ready=False sector_rank=7 price=30.15 support=23.4 resistance=31.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=83.61 liquidity=146232512.0 spike=3.77
- ISMQ.CA: score=20.32 buy_ready=False sector_rank=21 price=8.13 support=7.27 resistance=8.62 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=65.57 liquidity=113137408.0 spike=1.64
- ISPH.CA: score=20.18 buy_ready=False sector_rank=12 price=12.1 support=11.12 resistance=12.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=60.92 liquidity=41497568.0 spike=0.31
- JUFO.CA: score=23.06 buy_ready=False sector_rank=5 price=30.54 support=26.51 resistance=30.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=70.99 liquidity=21286428.0 spike=0.51
- KABO.CA: score=14.86 buy_ready=False sector_rank=9 price=6.23 support=5.92 resistance=6.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=6555883.0 spike=0.31
- KWIN.CA: score=18.27 buy_ready=False sector_rank=7 price=74.15 support=69.0 resistance=77.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=65.36 liquidity=5304087.0 spike=1.12
- KZPC.CA: score=12.51 buy_ready=False sector_rank=7 price=10.58 support=10.3 resistance=11.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=56.29 liquidity=1784035.63 spike=0.18
- LCSW.CA: score=9.46 buy_ready=False sector_rank=11 price=26.89 support=26.0 resistance=28.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=31.73 liquidity=6194893.5 spike=0.61
- LUTS.CA: score=20.85 buy_ready=False sector_rank=7 price=0.74 support=0.54 resistance=0.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=88.76 liquidity=51326676.0 spike=1.56
- MAAL.CA: score=7.17 buy_ready=False sector_rank=7 price=6.25 support=5.82 resistance=6.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=22089546.0 spike=1.72
- MASR.CA: score=21.07 buy_ready=False sector_rank=7 price=7.2 support=6.54 resistance=7.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=57.14 liquidity=66671480.0 spike=1.17
- MBSC.CA: score=20.26 buy_ready=False sector_rank=11 price=251.92 support=251.52 resistance=251.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=29754320.0 spike=1.0
- MCQE.CA: score=6.31 buy_ready=False sector_rank=11 price=176.75 support=174.0 resistance=201.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=26.9 liquidity=6049756.0 spike=0.35
- MCRO.CA: score=17.73 buy_ready=False sector_rank=7 price=1.24 support=1.2 resistance=1.31 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=47.62 liquidity=45721192.0 spike=0.89
- MENA.CA: score=14.21 buy_ready=False sector_rank=3 price=6.7 support=5.98 resistance=7.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=59.09 liquidity=1813221.5 spike=0.1
- MEPA.CA: score=15.29 buy_ready=False sector_rank=7 price=1.7 support=1.63 resistance=1.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=55.56 liquidity=6565186.5 spike=0.37
- MFPC.CA: score=9.04 buy_ready=False sector_rank=21 price=37.13 support=36.9 resistance=46.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=4.92 liquidity=77088096.0 spike=0.88
- MFSC.CA: score=5.83 buy_ready=False sector_rank=7 price=44.58 support=43.0 resistance=65.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=23.23 liquidity=2098527.25 spike=0.14
- MHOT.CA: score=16.6 buy_ready=False sector_rank=8 price=29.87 support=26.3 resistance=34.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=44.65 liquidity=7936807.5 spike=0.37
- MICH.CA: score=17.83 buy_ready=False sector_rank=7 price=37.79 support=35.05 resistance=40.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=65.46 liquidity=7106672.0 spike=0.49
- MILS.CA: score=18.73 buy_ready=False sector_rank=7 price=141.82 support=127.01 resistance=151.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=69.34 liquidity=13534356.0 spike=0.68
- MIPH.CA: score=11.98 buy_ready=False sector_rank=12 price=664.14 support=640.0 resistance=700.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:09 PM market time freshness=DELAYED_CURRENT RSI=55.66 liquidity=1802889.13 spike=0.64
- MOED.CA: score=17.37 buy_ready=False sector_rank=7 price=0.71 support=0.65 resistance=0.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=47.15 liquidity=16316894.0 spike=1.32
- MOIL.CA: score=8.32 buy_ready=False sector_rank=10 price=0.47 support=0.44 resistance=0.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=56.45 liquidity=36256.89 spike=0.22
- MOIN.CA: score=4.18 buy_ready=False sector_rank=7 price=24.34 support=24.1 resistance=26.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:08 PM market time freshness=DELAYED_CURRENT RSI=31.78 liquidity=1450905.63 spike=0.85
- MOSC.CA: score=25.39 buy_ready=False sector_rank=7 price=285.82 support=246.6 resistance=330.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=50.99 liquidity=29213778.0 spike=3.33
- MPCI.CA: score=20.79 buy_ready=False sector_rank=7 price=220.97 support=197.0 resistance=238.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=60.95 liquidity=82339904.0 spike=1.03
- MPCO.CA: score=27.4 buy_ready=False sector_rank=2 price=1.95 support=1.54 resistance=2.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=75.64 liquidity=342549952.0 spike=3.78
- MPRC.CA: score=18.73 buy_ready=False sector_rank=7 price=31.98 support=30.61 resistance=34.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=58.69 liquidity=12738283.0 spike=0.63
- MTIE.CA: score=29.4 buy_ready=False sector_rank=1 price=9.25 support=8.65 resistance=9.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=54.86 liquidity=70548184.0 spike=3.72
- NAHO.CA: score=4.76 buy_ready=False sector_rank=7 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance as_of=2026-06-14T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=33624.25 spike=1.0
- NCCW.CA: score=20.73 buy_ready=False sector_rank=7 price=6.27 support=5.13 resistance=6.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=73.64 liquidity=11451460.0 spike=0.41
- NEDA.CA: score=11.1 buy_ready=False sector_rank=7 price=2.81 support=2.65 resistance=2.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:52 PM market time freshness=DELAYED_CURRENT RSI=53.57 liquidity=376752.5 spike=0.74
- NHPS.CA: score=7.66 buy_ready=False sector_rank=7 price=68.07 support=65.03 resistance=72.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=42.54 liquidity=2928049.0 spike=0.62
- NINH.CA: score=10.54 buy_ready=False sector_rank=7 price=17.69 support=16.8 resistance=19.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=36.05 liquidity=1816454.25 spike=0.3
- NIPH.CA: score=18.18 buy_ready=False sector_rank=12 price=160.97 support=155.1 resistance=176.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=48.47 liquidity=50494200.0 spike=0.58
- OBRI.CA: score=18.29 buy_ready=False sector_rank=7 price=36.12 support=33.63 resistance=37.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=61.01 liquidity=8558929.0 spike=0.62
- OCDI.CA: score=17.4 buy_ready=False sector_rank=3 price=20.71 support=20.0 resistance=22.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=44.83 liquidity=14394806.0 spike=0.41
- OCPH.CA: score=6.0 buy_ready=False sector_rank=7 price=344.0 support=337.0 resistance=389.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=27.26 liquidity=2273658.0 spike=0.33
- ODIN.CA: score=22.13 buy_ready=False sector_rank=7 price=2.21 support=1.89 resistance=2.23 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=69.7 liquidity=17647592.0 spike=1.7
- OFH.CA: score=14.7 buy_ready=False sector_rank=7 price=0.62 support=0.59 resistance=0.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=54.78 liquidity=8971724.0 spike=0.39
- OIH.CA: score=9.46 buy_ready=False sector_rank=19 price=1.37 support=1.33 resistance=1.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=34.29 liquidity=13581725.0 spike=0.14
- OLFI.CA: score=21.2 buy_ready=False sector_rank=5 price=21.88 support=21.0 resistance=23.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=74.01 liquidity=21383068.0 spike=1.07
- ORAS.CA: score=4.6 buy_ready=False sector_rank=17 price=785.0 support=780.01 resistance=788.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=120380216.0 spike=1.0
- ORHD.CA: score=22.4 buy_ready=False sector_rank=3 price=37.2 support=33.09 resistance=39.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=48.15 liquidity=110538160.0 spike=0.59
- ORWE.CA: score=20.3 buy_ready=False sector_rank=9 price=23.18 support=21.6 resistance=24.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=56.23 liquidity=12493544.0 spike=0.29
- PHAR.CA: score=15.18 buy_ready=False sector_rank=12 price=84.0 support=83.02 resistance=89.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=48.01 liquidity=12765535.0 spike=0.42
- PHDC.CA: score=25.26 buy_ready=False sector_rank=3 price=15.81 support=13.01 resistance=16.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=59.77 liquidity=587560704.0 spike=1.43
- PHTV.CA: score=23.61 buy_ready=False sector_rank=7 price=221.5 support=201.55 resistance=233.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=61.46 liquidity=22966882.0 spike=1.44
- POUL.CA: score=19.06 buy_ready=False sector_rank=5 price=36.01 support=34.8 resistance=38.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=40.21 liquidity=29524666.0 spike=0.79
- PRCL.CA: score=20.26 buy_ready=False sector_rank=11 price=24.6 support=21.01 resistance=28.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=62.78 liquidity=21833476.0 spike=0.77
- PRDC.CA: score=9.7 buy_ready=False sector_rank=3 price=7.82 support=6.6 resistance=8.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=191600672.0 spike=2.15
- PRMH.CA: score=22.25 buy_ready=False sector_rank=7 price=2.87 support=2.19 resistance=2.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=68.89 liquidity=43292304.0 spike=1.76
- RACC.CA: score=7.67 buy_ready=False sector_rank=7 price=9.69 support=9.38 resistance=10.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=26.09 liquidity=3944285.75 spike=0.36
- RAKT.CA: score=6.51 buy_ready=False sector_rank=7 price=23.03 support=22.1 resistance=24.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=37.17 liquidity=517743.66 spike=1.63
- RAYA.CA: score=12.39 buy_ready=False sector_rank=20 price=6.98 support=6.7 resistance=7.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=32.09 liquidity=86506064.0 spike=0.9
- RMDA.CA: score=18.18 buy_ready=False sector_rank=12 price=5.09 support=4.92 resistance=5.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=53.61 liquidity=13207526.0 spike=0.15
- ROTO.CA: score=22.99 buy_ready=False sector_rank=7 price=35.54 support=32.66 resistance=35.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=63.99 liquidity=15199464.0 spike=1.13
- RREI.CA: score=22.41 buy_ready=False sector_rank=7 price=3.63 support=3.32 resistance=3.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=55.95 liquidity=39247916.0 spike=1.84
- RTVC.CA: score=14.78 buy_ready=False sector_rank=7 price=3.83 support=3.75 resistance=4.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=57.14 liquidity=6775079.5 spike=1.14
- RUBX.CA: score=10.55 buy_ready=False sector_rank=7 price=9.96 support=9.8 resistance=11.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=40.96 liquidity=5819146.5 spike=0.5
- SAUD.CA: score=11.32 buy_ready=False sector_rank=6 price=21.96 support=20.82 resistance=23.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=37.2 liquidity=5365095.5 spike=0.43
- SCEM.CA: score=18.26 buy_ready=False sector_rank=11 price=62.18 support=59.3 resistance=67.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=38.18 liquidity=20106452.0 spike=0.75
- SCFM.CA: score=7.77 buy_ready=False sector_rank=7 price=252.04 support=248.1 resistance=296.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=35.98 liquidity=2039905.5 spike=0.16
- SCTS.CA: score=7.93 buy_ready=False sector_rank=4 price=600.65 support=590.01 resistance=670.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=30.31 liquidity=3854715.0 spike=0.62
- SDTI.CA: score=16.35 buy_ready=False sector_rank=7 price=46.94 support=43.4 resistance=47.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=62.16 liquidity=3623679.0 spike=0.23
- SEIG.CA: score=12.22 buy_ready=False sector_rank=7 price=183.39 support=173.35 resistance=205.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=52.07 liquidity=1489143.75 spike=0.31
- SIPC.CA: score=16.17 buy_ready=False sector_rank=7 price=3.46 support=3.4 resistance=3.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=45.28 liquidity=15122035.0 spike=1.22
- SKPC.CA: score=13.04 buy_ready=False sector_rank=21 price=16.24 support=16.29 resistance=18.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=35.1 liquidity=19313822.0 spike=0.36
- SMFR.CA: score=9.62 buy_ready=False sector_rank=7 price=203.84 support=192.0 resistance=219.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:10 PM market time freshness=DELAYED_CURRENT RSI=43.26 liquidity=888619.44 spike=0.16
- SNFC.CA: score=13.98 buy_ready=False sector_rank=7 price=12.36 support=11.68 resistance=12.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=48.64 liquidity=5251659.5 spike=0.2
- SPIN.CA: score=1.7 buy_ready=False sector_rank=9 price=13.98 support=13.61 resistance=15.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=33.02 liquidity=1392024.5 spike=0.3
- SPMD.CA: score=18.73 buy_ready=False sector_rank=7 price=0.41 support=0.38 resistance=0.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=45.56 liquidity=12213444.0 spike=0.52
- SUGR.CA: score=11.14 buy_ready=False sector_rank=5 price=48.64 support=48.0 resistance=52.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=50.07 liquidity=3080752.75 spike=0.2
- SVCE.CA: score=18.73 buy_ready=False sector_rank=7 price=9.04 support=8.11 resistance=9.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=49.22 liquidity=82676088.0 spike=0.86
- SWDY.CA: score=13.38 buy_ready=False sector_rank=13 price=86.13 support=84.01 resistance=90.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=44.22 liquidity=5324819.0 spike=0.25
- TALM.CA: score=14.88 buy_ready=False sector_rank=4 price=16.28 support=15.12 resistance=16.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=75.86 liquidity=6796552.5 spike=0.81
- TMGH.CA: score=20.4 buy_ready=False sector_rank=3 price=95.0 support=91.87 resistance=101.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=47.36 liquidity=456631904.0 spike=1.0
- TRTO.CA: score=6.73 buy_ready=False sector_rank=7 price=0.03 support=0.03 resistance=0.04 source=Yahoo Finance as_of=2026-06-14T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=45.66 spike=0.05
- UEFM.CA: score=5.2 buy_ready=False sector_rank=7 price=472.2 support=455.6 resistance=500.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=49.25 liquidity=473098.34 spike=0.51
- UEGC.CA: score=22.73 buy_ready=False sector_rank=7 price=1.43 support=1.3 resistance=1.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=63.89 liquidity=17052080.0 spike=0.68
- UNIP.CA: score=10.73 buy_ready=False sector_rank=7 price=0.34 support=0.33 resistance=0.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=77937168.0 spike=3.83
- UNIT.CA: score=14.93 buy_ready=False sector_rank=3 price=13.64 support=12.07 resistance=15.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:10 PM market time freshness=DELAYED_CURRENT RSI=56.67 liquidity=2527978.25 spike=0.32
- WCDF.CA: score=-3.24 buy_ready=False sector_rank=7 price=537.53 support=530.11 resistance=544.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=467109.78 spike=1.28
- WKOL.CA: score=7.75 buy_ready=False sector_rank=7 price=289.05 support=289.5 resistance=312.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=46.28 liquidity=2023771.25 spike=0.52
- ZEOT.CA: score=10.73 buy_ready=False sector_rank=7 price=11.28 support=9.47 resistance=11.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=196665104.0 spike=30.85
- ZMID.CA: score=22.4 buy_ready=False sector_rank=3 price=6.17 support=5.77 resistance=6.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=62.77 liquidity=85010976.0 spike=0.37

## Backtesting Lite
- MTIE.CA: 180d return=40.27%, max drawdown=-20.49%, MA20>MA50 days last20=20, as_of=2026-06-14T21:00:00+00:00
- HDBK.CA: 180d return=134.98%, max drawdown=-12.66%, MA20>MA50 days last20=16, as_of=2026-06-14T21:00:00+00:00
- MPCO.CA: 180d return=-0.99%, max drawdown=-53.57%, MA20>MA50 days last20=20, as_of=2026-06-14T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- MTIE.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=MM Group For Industry and International Trade summary=Evidence rejected for MTIE.CA: source text did not clearly match MTIE.CA / MM Group For Industry and International Trade.
- HDBK.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Housing and Development Bank Egypt summary=Evidence rejected for HDBK.CA: source text did not clearly match HDBK.CA / Housing and Development Bank Egypt.
- MPCO.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=531 sources=3 expected=Mansoura Poultry summary=Mansoura Poultry’s consolidated net profits drop in 2025; revenues near EGP 857m; Mansoura Poultry’s stock rebounds from key support level; Mansoura Poultry stock witnesses clear emergence of buying power
  - Mansoura Poultry’s consolidated net profits drop in 2025; revenues near EGP 857m: https://english.mubasher.info/news/4596342/Mansoura-Poultry-s-consolidated-net-profits-drop-in-2025-revenues-near-EGP-857m/
  - Mansoura Poultry’s stock rebounds from key support level: https://english.mubasher.info/news/4554482/Mansoura-Poultry-s-stock-rebounds-from-key-support-level/
  - Mansoura Poultry stock witnesses clear emergence of buying power: https://english.mubasher.info/news/4539119/Mansoura-Poultry-stock-witnesses-clear-emergence-of-buying-power/
- GBCO.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=GB Corp summary=Evidence rejected for GBCO.CA: source text did not clearly match GBCO.CA / GB Corp.
- EPCO.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Egypt for Poultry summary=Evidence rejected for EPCO.CA: source text did not clearly match EPCO.CA / Egypt for Poultry.
- MOSC.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Misr Oils & Soap summary=Misr Oils and Soap not to pay dividends for FY20/21; Misr Oils and Soap&#39;s profit plunges 78% in FY20/21; Misr Oils and Soap swings to loss in 10 months
  - Misr Oils and Soap not to pay dividends for FY20/21: https://english.mubasher.info/news/3856493/Misr-Oils-and-Soap-not-to-pay-dividends-for-FY20-21/
  - Misr Oils and Soap&#39;s profit plunges 78% in FY20/21: https://english.mubasher.info/news/3851183/Misr-Oils-and-Soap-s-profit-plunges-78-in-FY20-21/
  - Misr Oils and Soap swings to loss in 10 months: https://english.mubasher.info/news/3811105/Misr-Oils-and-Soap-swings-to-loss-in-10-months/
- PHDC.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=531 sources=3 expected=Palm Hills Development summary=Palm Hills, UAE’s Miran to launch new development project in Ras Al Hikma; Palm Hills records 30% higher profits in 2025, unveils new project in UAE; Strong momentum pushes Palm Hills toward EGP 10.15
  - Palm Hills, UAE’s Miran to launch new development project in Ras Al Hikma: https://english.mubasher.info/news/4598123/Palm-Hills-UAE-s-Miran-to-launch-new-development-project-in-Ras-Al-Hikma/
  - Palm Hills records 30% higher profits in 2025, unveils new project in UAE: https://english.mubasher.info/news/4580548/Palm-Hills-records-30-higher-profits-in-2025-unveils-new-project-in-UAE/
  - Strong momentum pushes Palm Hills toward EGP 10.15: https://english.mubasher.info/news/4560871/Strong-momentum-pushes-Palm-Hills-toward-EGP-10-15/
- EAST.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Eastern Company summary=Evidence rejected for EAST.CA: source text did not clearly match EAST.CA / Eastern Company.

## Warnings
- Evidence rejected for MTIE.CA: source text did not clearly match MTIE.CA / MM Group For Industry and International Trade.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence rejected for HDBK.CA: source text did not clearly match HDBK.CA / Housing and Development Bank Egypt.
- Evidence for MPCO.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for GBCO.CA: source text did not clearly match GBCO.CA / GB Corp.
- Evidence rejected for EPCO.CA: source text did not clearly match EPCO.CA / Egypt for Poultry.
- Evidence for MOSC.CA matches the company but no source/report date was detected.
- Evidence for PHDC.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for EAST.CA: source text did not clearly match EAST.CA / Eastern Company.
