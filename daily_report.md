# Telegram-First EGX Scanner Report

Scan phase: Post-close tomorrow tickets
Generated UTC: 2026-06-08T16:37:51.007372+00:00
Generated Cairo: 2026-06-08 19:37
Run timing: target 15:30 Cairo | generated Cairo 2026-06-08 19:37 | cron 30 12 * * 0-4
Trigger: scheduled cron=30 12 * * 0-4 mapped to post_close; Cairo now 2026-06-08 19:33

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 63
- Data quality issues: 0
- Tradeable price/liquidity tickers: 184/190
- Top sector: Technology & Distribution

## Market Context
- Market trend: Bearish
- Source: Mubasher EGX market page (delayed public data)
- As of: Monday, June 08
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 10.0% / above MA50 70.0%
- EGX70 regime: CONSTRUCTIVE / above MA20 51.28% / above MA50 84.62%
- Sector breadth: 61.9%
- Risk mode: SELECTIVE_SMALL_MID_SWINGS

## Top Liquidity
- RMDA.CA: liquidity=1053935232.0 spike=18.77 score=31.4
- CCAP.CA: liquidity=956173760.0 spike=1.12 score=30.64
- COMI.CA: liquidity=724858304.0 spike=1.11 score=19.02
- EFID.CA: liquidity=602547904.0 spike=12.54 score=24.16
- ELSH.CA: liquidity=529396576.0 spike=5.85 score=14.32

## AI Narrative
- Provider: OpenRouter OK
- Model: openai/gpt-oss-120b:free
- Summary: The scanner found no ticket meeting all evidence, liquidity, freshness, and technical gates, so the default action is HOLD. EGX30 remains bearish with weak breadth, while EGX70 shows a constructive trend and broader sector support. Risk mode is set to SELECTIVE_SMALL_MID_SWINGS, focusing on limited‑size, short‑term opportunities amid mixed market signals.
- EGX30: 10% above MA20, 70% above MA50, median 5‑day return –0.75%; bearish regime limits upside risk.
- EGX70: 51% above MA20, 85% above MA50, median 5‑day return +0.91%; constructive regime permits selective swings.
- Sector breadth 61.9% with Technology & Distribution, Investment Holding, Tourism & Leisure leading.
- Top scanner rows (RMDA, ECAP, CCAP, etc.) show bullish outlooks but lack confirmed evidence, so they stay on hold.
- Uncertainty remains high: liquidity spikes and RSI levels vary, and market regime shift could change risk exposure in the next 1‑3 days.

## Top Liquidity Spikes
- RMDA.CA: spike=18.77 liquidity=1053935232.0 outlook=BULLISH_WATCH score=96.1 buy_ready=True
- EFID.CA: spike=12.54 liquidity=602547904.0 outlook=NEUTRAL score=47.41 buy_ready=False
- ELSH.CA: spike=5.85 liquidity=529396576.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- LUTS.CA: spike=3.97 liquidity=53786864.0 outlook=BULLISH_WATCH score=73.79 buy_ready=False
- ECAP.CA: spike=3.38 liquidity=16700049.0 outlook=BULLISH_WATCH score=81.79 buy_ready=True

## Sector Leaderboard
- #1 Technology & Distribution: score=11.83 5d=3.21% 20d=18.4% aboveMA50=100.0%
- #2 Investment Holding: score=10.76 5d=6.55% 20d=12.31% aboveMA50=66.67%
- #3 Tourism & Leisure: score=9.89 5d=0.75% 20d=14.57% aboveMA50=100.0%
- #4 Healthcare: score=9.1 5d=3.62% 20d=7.32% aboveMA50=100.0%
- #5 Real Estate: score=8.04 5d=1.26% 20d=11.28% aboveMA50=84.62%
- #6 Textiles: score=7.34 5d=1.5% 20d=6.29% aboveMA50=75.0%
- #7 Agriculture & Food Production: score=6.39 5d=4.46% 20d=0.38% aboveMA50=50.0%
- #8 General / Verified EGX Expansion: score=5.79 5d=2.1% 20d=0.93% aboveMA50=81.73%

## Today's Prioritized Action Tickets
- HOLD: Local fallback HOLD: no candidate passed evidence, liquidity, freshness, and technical gates.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- RMDA.CA: BULLISH_WATCH score=96.1 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended
- MPRC.CA: BULLISH_WATCH score=95.79 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- ZMID.CA: BULLISH_WATCH score=95.04 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=No major short-term scanner risk flags.
- CCAP.CA: BULLISH_WATCH score=93 liquidity=TRADEABLE sector=LEADING risk=far above support
- NIPH.CA: BULLISH_WATCH score=90.1 liquidity=TRADEABLE sector=IMPROVING risk=No major short-term scanner risk flags.
- RAYA.CA: BULLISH_WATCH score=90 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; momentum is extended
- MHOT.CA: BULLISH_WATCH score=89.89 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- AREH.CA: BULLISH_WATCH score=87.79 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended; sector is not leading
- AJWA.CA: BULLISH_WATCH score=87.79 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- BINV.CA: BULLISH_WATCH score=87 liquidity=TRADEABLE sector=LEADING risk=momentum is extended

## BUY-Ready Candidates
- RMDA.CA: rank=31.4 outlook=BULLISH_WATCH outlook_score=96.1 sector_rank=4 price=5.24 support=4.78 resistance=5.19 liquidity=1053935232.0
- ECAP.CA: rank=31.08 outlook=BULLISH_WATCH outlook_score=81.79 sector_rank=8 price=31.11 support=28.7 resistance=31.5 liquidity=16700049.0
- CCAP.CA: rank=30.64 outlook=BULLISH_WATCH outlook_score=93 sector_rank=2 price=5.6 support=4.55 resistance=5.72 liquidity=956173760.0
- MPRC.CA: rank=29.84 outlook=BULLISH_WATCH outlook_score=95.79 sector_rank=8 price=33.56 support=30.61 resistance=34.55 liquidity=35699504.0
- RAYA.CA: rank=29.4 outlook=BULLISH_WATCH outlook_score=90 sector_rank=1 price=7.45 support=6.6 resistance=8.0 liquidity=69999072.0
- NCCW.CA: rank=28.6 outlook=BULLISH_WATCH outlook_score=77.79 sector_rank=8 price=6.22 support=5.13 resistance=6.5 liquidity=42720952.0
- AREH.CA: rank=28.52 outlook=BULLISH_WATCH outlook_score=87.79 sector_rank=8 price=1.48 support=1.27 resistance=1.57 liquidity=53063516.0
- MPCO.CA: rank=27.9 outlook=BULLISH_WATCH outlook_score=85.39 sector_rank=7 price=1.78 support=1.54 resistance=1.93 liquidity=111873864.0
- GDWA.CA: rank=27.74 outlook=BULLISH_WATCH outlook_score=72.79 sector_rank=8 price=0.82 support=0.77 resistance=0.83 liquidity=13121701.0
- JUFO.CA: rank=27.54 outlook=BULLISH_WATCH outlook_score=81.41 sector_rank=10 price=30.1 support=26.51 resistance=29.98 liquidity=76470752.0

## Data Quality Issues
- No provider failures.

## Ranked Scanner Results
- AALR.CA: score=16.43 buy_ready=True sector_rank=8 price=211.65 support=195.1 resistance=233.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=48.5 liquidity=2118624.0 spike=0.15
- ABUK.CA: score=13.03 buy_ready=False sector_rank=17 price=81.92 support=81.2 resistance=90.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=26.31 liquidity=89988936.0 spike=0.69
- ACAMD.CA: score=26.6 buy_ready=True sector_rank=8 price=2.29 support=1.96 resistance=2.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=64.81 liquidity=133482416.0 spike=1.14
- ACGC.CA: score=24.4 buy_ready=True sector_rank=6 price=9.69 support=8.3 resistance=10.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=61.04 liquidity=47779580.0 spike=0.87
- ADCI.CA: score=17.95 buy_ready=True sector_rank=8 price=215.04 support=202.22 resistance=225.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=56.57 liquidity=3637684.75 spike=0.52
- ADIB.CA: score=21.8 buy_ready=False sector_rank=13 price=46.25 support=44.45 resistance=50.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=54.16 liquidity=61398484.0 spike=0.37
- ADPC.CA: score=17.83 buy_ready=False sector_rank=8 price=3.67 support=3.54 resistance=4.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=37.72 liquidity=8518491.0 spike=0.35
- AFDI.CA: score=22.46 buy_ready=True sector_rank=8 price=43.79 support=37.54 resistance=46.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=65.21 liquidity=8140690.5 spike=0.45
- AFMC.CA: score=15.52 buy_ready=False sector_rank=8 price=72.8 support=69.33 resistance=80.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=37.49 liquidity=3208083.25 spike=0.24
- AJWA.CA: score=25.78 buy_ready=True sector_rank=8 price=135.0 support=130.01 resistance=139.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:09 PM market time freshness=DELAYED_CURRENT RSI=50.49 liquidity=17730854.0 spike=1.73
- ALCN.CA: score=17.98 buy_ready=False sector_rank=18 price=28.81 support=28.4 resistance=30.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=48.74 liquidity=11267697.0 spike=0.46
- ALUM.CA: score=24.71 buy_ready=True sector_rank=8 price=25.21 support=22.5 resistance=26.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=56.55 liquidity=6395757.0 spike=0.29
- AMER.CA: score=24.4 buy_ready=True sector_rank=5 price=2.74 support=2.3 resistance=3.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=51.9 liquidity=66026556.0 spike=0.51
- AMES.CA: score=8.91 buy_ready=False sector_rank=8 price=50.63 support=48.0 resistance=57.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=29.19 liquidity=1594079.0 spike=0.17
- AMIA.CA: score=19.45 buy_ready=True sector_rank=8 price=8.99 support=8.25 resistance=10.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=55.56 liquidity=5129881.5 spike=0.16
- AMOC.CA: score=17.37 buy_ready=False sector_rank=9 price=8.3 support=8.12 resistance=9.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=21.05 liquidity=90094736.0 spike=1.05
- ANFI.CA: score=12.95 buy_ready=False sector_rank=8 price=14.05 support=13.5 resistance=15.55 source=Yahoo Finance as_of=2026-06-03T21:00:00+00:00 freshness=FRESH RSI=24.73 liquidity=5638883.28 spike=0.28
- APSW.CA: score=11.96 buy_ready=False sector_rank=8 price=8.9 support=8.62 resistance=9.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=43.64 liquidity=639410.56 spike=0.57
- ARAB.CA: score=20.4 buy_ready=False sector_rank=5 price=0.2 support=0.19 resistance=0.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=57.69 liquidity=62072020.0 spike=0.81
- ARCC.CA: score=23.98 buy_ready=True sector_rank=12 price=57.82 support=53.35 resistance=60.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=68.08 liquidity=26896934.0 spike=0.61
- AREH.CA: score=28.52 buy_ready=True sector_rank=8 price=1.48 support=1.27 resistance=1.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=67.74 liquidity=53063516.0 spike=2.1
- ARVA.CA: score=23.84 buy_ready=False sector_rank=8 price=11.37 support=7.71 resistance=11.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=75.37 liquidity=31788592.0 spike=1.26
- ASCM.CA: score=24.32 buy_ready=False sector_rank=8 price=55.17 support=44.75 resistance=59.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=73.58 liquidity=41424792.0 spike=0.64
- ASPI.CA: score=10.48 buy_ready=False sector_rank=8 price=0.34 support=0.34 resistance=0.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=84535928.0 spike=1.58
- ATLC.CA: score=17.14 buy_ready=True sector_rank=16 price=5.02 support=4.71 resistance=5.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=47.3 liquidity=3968074.75 spike=0.49
- ATQA.CA: score=24.03 buy_ready=True sector_rank=17 price=9.82 support=9.41 resistance=10.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=47.77 liquidity=21247940.0 spike=0.44
- AXPH.CA: score=12.87 buy_ready=False sector_rank=8 price=1142.08 support=985.0 resistance=1239.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=20.12 liquidity=3551952.5 spike=0.62
- BINV.CA: score=26.62 buy_ready=True sector_rank=2 price=46.0 support=40.5 resistance=49.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=66.86 liquidity=14469145.0 spike=1.11
- BIOC.CA: score=18.42 buy_ready=True sector_rank=8 price=73.58 support=70.0 resistance=79.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=47.22 liquidity=4099275.25 spike=0.55
- BTFH.CA: score=15.17 buy_ready=False sector_rank=16 price=3.04 support=3.03 resistance=3.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=31.37 liquidity=129029000.0 spike=0.52
- CAED.CA: score=9.84 buy_ready=False sector_rank=8 price=71.26 support=66.56 resistance=89.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=26.71 liquidity=2520967.25 spike=0.17
- CANA.CA: score=27.34 buy_ready=True sector_rank=13 price=38.08 support=33.15 resistance=38.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=63.1 liquidity=25147458.0 spike=1.77
- CCAP.CA: score=30.64 buy_ready=True sector_rank=2 price=5.6 support=4.55 resistance=5.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=54.55 liquidity=956173760.0 spike=1.12
- CCRS.CA: score=9.32 buy_ready=False sector_rank=8 price=2.46 support=2.45 resistance=2.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=20926650.0 spike=0.76
- CEFM.CA: score=8.56 buy_ready=False sector_rank=8 price=106.58 support=103.07 resistance=119.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=25.15 liquidity=1245029.25 spike=0.18
- CERA.CA: score=27.18 buy_ready=True sector_rank=8 price=1.2 support=1.13 resistance=1.23 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=46.67 liquidity=40801044.0 spike=2.93
- CFGH.CA: score=3.32 buy_ready=False sector_rank=8 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance as_of=2026-06-06T21:00:00+00:00 freshness=FRESH RSI=0.0 liquidity=2804.02 spike=0.7
- CICH.CA: score=13.42 buy_ready=False sector_rank=16 price=12.1 support=11.01 resistance=13.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=43.24 liquidity=2248342.5 spike=0.49
- CIEB.CA: score=15.56 buy_ready=False sector_rank=13 price=23.54 support=23.31 resistance=24.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=3756678.5 spike=0.32
- CIRA.CA: score=19.8 buy_ready=False sector_rank=14 price=26.19 support=21.0 resistance=28.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=56.48 liquidity=8249773.5 spike=0.29
- CLHO.CA: score=22.4 buy_ready=False sector_rank=4 price=15.2 support=14.58 resistance=16.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=43.06 liquidity=25219514.0 spike=0.68
- CNFN.CA: score=22.99 buy_ready=False sector_rank=16 price=4.6 support=4.47 resistance=4.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=37.7 liquidity=39086532.0 spike=2.41
- COMI.CA: score=19.02 buy_ready=False sector_rank=13 price=130.1 support=131.3 resistance=144.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=48.15 liquidity=724858304.0 spike=1.11
- COPR.CA: score=23.32 buy_ready=True sector_rank=8 price=0.36 support=0.31 resistance=0.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=66.67 liquidity=18064114.0 spike=0.46
- COSG.CA: score=26.36 buy_ready=True sector_rank=8 price=1.64 support=1.45 resistance=1.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=58.97 liquidity=59851216.0 spike=1.02
- CPCI.CA: score=16.98 buy_ready=False sector_rank=8 price=364.82 support=340.01 resistance=374.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=72.04 liquidity=2662899.75 spike=0.36
- CSAG.CA: score=22.98 buy_ready=False sector_rank=18 price=31.22 support=30.4 resistance=32.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=53.77 liquidity=11945372.0 spike=0.61
- DAPH.CA: score=12.53 buy_ready=False sector_rank=8 price=80.85 support=79.25 resistance=96.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=16.14 liquidity=5212809.0 spike=0.16
- DEIN.CA: score=10.32 buy_ready=False sector_rank=8 price=11.38 support=11.38 resistance=13.65 source=Yahoo Finance as_of=2026-06-06T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- DOMT.CA: score=4.95 buy_ready=False sector_rank=10 price=24.47 support=24.45 resistance=26.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=22.14 liquidity=790895.19 spike=0.33
- DSCW.CA: score=20.32 buy_ready=False sector_rank=8 price=1.81 support=1.71 resistance=1.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=44.83 liquidity=20869180.0 spike=0.32
- DTPP.CA: score=8.25 buy_ready=False sector_rank=8 price=124.05 support=121.0 resistance=139.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=27.48 liquidity=935830.69 spike=0.17
- EALR.CA: score=14.05 buy_ready=False sector_rank=8 price=352.93 support=346.01 resistance=392.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=36.82 liquidity=1736380.38 spike=0.14
- EASB.CA: score=15.46 buy_ready=True sector_rank=8 price=5.06 support=4.61 resistance=5.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=55.71 liquidity=1141829.13 spike=0.7
- EAST.CA: score=26.98 buy_ready=True sector_rank=10 price=39.85 support=37.01 resistance=39.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=53.99 liquidity=98541120.0 spike=1.41
- EBSC.CA: score=17.44 buy_ready=True sector_rank=8 price=1.84 support=1.64 resistance=2.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=63.64 liquidity=1123310.88 spike=0.37
- ECAP.CA: score=31.08 buy_ready=True sector_rank=8 price=31.11 support=28.7 resistance=31.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=59.45 liquidity=16700049.0 spike=3.38
- EDFM.CA: score=13.32 buy_ready=False sector_rank=8 price=333.99 support=320.2 resistance=349.0 source=Yahoo Finance as_of=2026-06-06T21:00:00+00:00 freshness=FRESH RSI=39.0 liquidity=667979.98 spike=1.17
- EEII.CA: score=26.8 buy_ready=True sector_rank=8 price=2.44 support=2.27 resistance=2.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=35.0 liquidity=39564460.0 spike=2.24
- EFIC.CA: score=5.01 buy_ready=False sector_rank=17 price=204.1 support=195.25 resistance=219.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=6.17 liquidity=2977785.0 spike=0.67
- EFID.CA: score=24.16 buy_ready=False sector_rank=10 price=28.39 support=27.49 resistance=29.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=76.47 liquidity=602547904.0 spike=12.54
- EFIH.CA: score=19.78 buy_ready=False sector_rank=21 price=21.07 support=21.3 resistance=22.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=49.84 liquidity=51399028.0 spike=0.8
- EGAL.CA: score=21.03 buy_ready=False sector_rank=17 price=319.71 support=303.05 resistance=344.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=54.23 liquidity=48703520.0 spike=0.43
- EGAS.CA: score=16.37 buy_ready=True sector_rank=9 price=49.76 support=46.51 resistance=51.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=68.15 liquidity=4093902.0 spike=0.28
- EGBE.CA: score=6.9 buy_ready=False sector_rank=13 price=0.45 support=0.41 resistance=0.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=23.54 liquidity=97953.0 spike=0.65
- EGCH.CA: score=25.03 buy_ready=True sector_rank=17 price=14.6 support=11.95 resistance=15.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=49.0 liquidity=58531792.0 spike=0.49
- EGSA.CA: score=9.14 buy_ready=False sector_rank=11 price=8.89 support=8.3 resistance=9.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:33 PM market time freshness=DELAYED_CURRENT RSI=84.34 liquidity=15330.06 spike=0.95
- EGTS.CA: score=22.4 buy_ready=False sector_rank=5 price=17.67 support=12.9 resistance=22.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=54.78 liquidity=57188644.0 spike=0.52
- EHDR.CA: score=21.58 buy_ready=False sector_rank=8 price=2.68 support=2.25 resistance=2.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=75.71 liquidity=59534404.0 spike=1.13
- EKHO.CA: score=14.27 buy_ready=False sector_rank=9 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-06-06T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=19.19 buy_ready=False sector_rank=15 price=2.14 support=2.06 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=47.83 liquidity=19668976.0 spike=0.66
- ELKA.CA: score=25.32 buy_ready=True sector_rank=8 price=1.26 support=1.12 resistance=1.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=62.5 liquidity=39283356.0 spike=0.93
- ELNA.CA: score=7.64 buy_ready=False sector_rank=8 price=39.54 support=37.11 resistance=42.79 source=Yahoo Finance as_of=2026-06-06T21:00:00+00:00 freshness=FRESH RSI=31.33 liquidity=323002.27 spike=1.0
- ELSH.CA: score=14.32 buy_ready=False sector_rank=8 price=13.5 support=11.15 resistance=13.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=529396576.0 spike=5.85
- ELWA.CA: score=17.66 buy_ready=False sector_rank=8 price=2.13 support=1.79 resistance=2.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=84.62 liquidity=4947720.5 spike=1.7
- EMFD.CA: score=27.04 buy_ready=False sector_rank=5 price=12.09 support=9.83 resistance=12.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=71.51 liquidity=300904032.0 spike=1.32
- ENGC.CA: score=26.94 buy_ready=True sector_rank=8 price=34.2 support=32.31 resistance=35.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=42.02 liquidity=15754680.0 spike=1.31
- EOSB.CA: score=14.85 buy_ready=False sector_rank=8 price=1.42 support=1.34 resistance=1.54 source=Yahoo Finance as_of=2026-06-06T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=253515.43 spike=2.14
- EPCO.CA: score=19.32 buy_ready=False sector_rank=8 price=9.09 support=8.56 resistance=9.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=46.78 liquidity=5005989.0 spike=0.4
- EPPK.CA: score=8.46 buy_ready=False sector_rank=8 price=12.5 support=11.67 resistance=13.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=32.88 liquidity=1522483.25 spike=1.31
- ETEL.CA: score=22.12 buy_ready=False sector_rank=11 price=94.46 support=93.01 resistance=101.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=50.71 liquidity=65286200.0 spike=0.59
- ETRS.CA: score=24.72 buy_ready=False sector_rank=8 price=8.91 support=7.37 resistance=9.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=73.88 liquidity=59852780.0 spike=1.2
- EXPA.CA: score=24.18 buy_ready=False sector_rank=13 price=19.14 support=18.34 resistance=20.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=72.8 liquidity=54011248.0 spike=1.19
- FAIT.CA: score=15.55 buy_ready=True sector_rank=13 price=37.3 support=33.57 resistance=38.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=46.42 liquidity=1751522.5 spike=0.24
- FAITA.CA: score=11.81 buy_ready=False sector_rank=13 price=0.99 support=0.98 resistance=1.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=57.14 liquidity=10019.24 spike=0.19
- FERC.CA: score=4.4 buy_ready=False sector_rank=17 price=77.41 support=76.5 resistance=83.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=27.01 liquidity=1366362.13 spike=0.2
- FWRY.CA: score=17.36 buy_ready=False sector_rank=21 price=18.39 support=18.6 resistance=21.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=37.14 liquidity=372303232.0 spike=1.29
- GBCO.CA: score=15.84 buy_ready=False sector_rank=19 price=26.6 support=25.25 resistance=29.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=31.56 liquidity=87602152.0 spike=0.75
- GDWA.CA: score=27.74 buy_ready=True sector_rank=8 price=0.82 support=0.77 resistance=0.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=61.11 liquidity=13121701.0 spike=1.21
- GGCC.CA: score=24.58 buy_ready=False sector_rank=8 price=0.42 support=0.39 resistance=0.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=70.37 liquidity=8604227.0 spike=1.33
- GIHD.CA: score=18.47 buy_ready=True sector_rank=8 price=41.6 support=39.1 resistance=44.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=46.01 liquidity=2151187.5 spike=0.37
- GMCI.CA: score=16.63 buy_ready=False sector_rank=8 price=1.78 support=1.67 resistance=1.84 source=Yahoo Finance as_of=2026-06-06T21:00:00+00:00 freshness=FRESH RSI=60.71 liquidity=317931.13 spike=0.89
- GRCA.CA: score=7.32 buy_ready=False sector_rank=8 price=54.49 support=53.36 resistance=60.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:08 PM market time freshness=DELAYED_CURRENT RSI=30.73 liquidity=3008424.75 spike=0.31
- GSSC.CA: score=7.38 buy_ready=False sector_rank=8 price=248.92 support=228.1 resistance=272.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=4.44 liquidity=3068461.25 spike=0.31
- GTWL.CA: score=9.2 buy_ready=False sector_rank=8 price=45.8 support=46.3 resistance=59.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=10.97 liquidity=4881280.0 spike=0.44
- HDBK.CA: score=22.9 buy_ready=False sector_rank=13 price=143.02 support=140.0 resistance=150.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=43.81 liquidity=25471244.0 spike=1.55
- HELI.CA: score=22.4 buy_ready=False sector_rank=5 price=6.39 support=6.28 resistance=6.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=56.02 liquidity=62840080.0 spike=0.37
- HRHO.CA: score=17.17 buy_ready=False sector_rank=16 price=26.4 support=26.16 resistance=30.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=36.17 liquidity=173497504.0 spike=0.83
- ICID.CA: score=22.59 buy_ready=False sector_rank=8 price=6.12 support=4.4 resistance=6.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=78.54 liquidity=9271017.0 spike=0.75
- IDRE.CA: score=22.32 buy_ready=False sector_rank=8 price=44.0 support=39.72 resistance=49.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=47.94 liquidity=11856058.0 spike=0.35
- IFAP.CA: score=8.21 buy_ready=False sector_rank=7 price=19.34 support=16.5 resistance=23.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=31.0 liquidity=4806117.5 spike=0.29
- INFI.CA: score=16.81 buy_ready=False sector_rank=8 price=100.25 support=99.51 resistance=112.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=37.06 liquidity=5495299.0 spike=0.32
- IRON.CA: score=12.35 buy_ready=False sector_rank=17 price=32.52 support=31.83 resistance=35.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=51.17 liquidity=3315529.25 spike=0.39
- ISMA.CA: score=23.58 buy_ready=False sector_rank=8 price=28.8 support=19.8 resistance=29.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=98.97 liquidity=54333632.0 spike=1.13
- ISMQ.CA: score=25.03 buy_ready=True sector_rank=17 price=7.74 support=7.27 resistance=8.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=51.72 liquidity=31375760.0 spike=0.61
- ISPH.CA: score=28.04 buy_ready=False sector_rank=4 price=12.44 support=11.12 resistance=12.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=74.25 liquidity=259398640.0 spike=1.82
- JUFO.CA: score=27.54 buy_ready=True sector_rank=10 price=30.1 support=26.51 resistance=29.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=54.12 liquidity=76470752.0 spike=1.69
- KABO.CA: score=26.4 buy_ready=True sector_rank=6 price=6.29 support=5.92 resistance=6.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=64.89 liquidity=10637835.0 spike=0.54
- KWIN.CA: score=13.74 buy_ready=False sector_rank=8 price=71.91 support=69.0 resistance=81.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=43.56 liquidity=1427921.0 spike=0.34
- KZPC.CA: score=16.83 buy_ready=False sector_rank=8 price=10.52 support=10.3 resistance=11.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=42.66 liquidity=4515571.0 spike=0.38
- LCSW.CA: score=21.98 buy_ready=False sector_rank=12 price=26.96 support=26.16 resistance=29.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=36.2 liquidity=12163651.0 spike=0.7
- LUTS.CA: score=28.32 buy_ready=False sector_rank=8 price=0.64 support=0.54 resistance=0.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=78.81 liquidity=53786864.0 spike=3.97
- MAAL.CA: score=23.8 buy_ready=False sector_rank=8 price=5.95 support=4.44 resistance=6.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=97.28 liquidity=14052629.0 spike=1.24
- MASR.CA: score=22.32 buy_ready=False sector_rank=8 price=6.9 support=6.46 resistance=7.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=39.29 liquidity=21039632.0 spike=0.34
- MBSC.CA: score=24.7 buy_ready=True sector_rank=12 price=276.35 support=259.63 resistance=295.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=55.46 liquidity=64670620.0 spike=1.36
- MCQE.CA: score=21.98 buy_ready=False sector_rank=12 price=189.96 support=188.01 resistance=201.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=58.89 liquidity=17530058.0 spike=0.9
- MCRO.CA: score=23.32 buy_ready=False sector_rank=8 price=1.26 support=1.21 resistance=1.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=54.55 liquidity=68439496.0 spike=0.73
- MENA.CA: score=25.57 buy_ready=True sector_rank=5 price=6.74 support=5.76 resistance=7.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=61.37 liquidity=9170942.0 spike=0.56
- MEPA.CA: score=21.03 buy_ready=False sector_rank=8 price=1.71 support=1.63 resistance=1.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=43.33 liquidity=8714360.0 spike=0.37
- MFPC.CA: score=16.03 buy_ready=False sector_rank=17 price=42.59 support=42.3 resistance=46.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=21.93 liquidity=67279064.0 spike=0.65
- MFSC.CA: score=10.7 buy_ready=False sector_rank=8 price=47.48 support=33.0 resistance=65.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=30.21 liquidity=3387161.0 spike=0.23
- MHOT.CA: score=26.21 buy_ready=True sector_rank=3 price=30.67 support=26.3 resistance=34.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=60.77 liquidity=8813933.0 spike=0.45
- MICH.CA: score=23.67 buy_ready=True sector_rank=8 price=36.96 support=35.01 resistance=38.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=49.24 liquidity=7354302.5 spike=0.82
- MILS.CA: score=24.84 buy_ready=True sector_rank=8 price=140.73 support=127.01 resistance=153.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=52.36 liquidity=8521199.0 spike=0.31
- MIPH.CA: score=10.89 buy_ready=False sector_rank=4 price=669.69 support=640.0 resistance=729.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=27.24 liquidity=1491877.0 spike=0.34
- MOED.CA: score=9.43 buy_ready=False sector_rank=8 price=0.69 support=0.68 resistance=0.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=16.5 liquidity=6116487.5 spike=0.45
- MOIL.CA: score=16.38 buy_ready=False sector_rank=9 price=0.48 support=0.44 resistance=0.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=52.11 liquidity=110688.77 spike=0.55
- MOIN.CA: score=14.74 buy_ready=True sector_rank=8 price=24.99 support=23.13 resistance=26.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=53.71 liquidity=1427506.75 spike=0.57
- MOSC.CA: score=10.54 buy_ready=False sector_rank=8 price=268.0 support=268.0 resistance=329.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=17.07 liquidity=3227661.5 spike=0.16
- MPCI.CA: score=26.32 buy_ready=True sector_rank=8 price=226.14 support=187.01 resistance=224.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=63.07 liquidity=75799008.0 spike=0.77
- MPCO.CA: score=27.9 buy_ready=True sector_rank=7 price=1.78 support=1.54 resistance=1.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=63.83 liquidity=111873864.0 spike=1.75
- MPRC.CA: score=29.84 buy_ready=True sector_rank=8 price=33.56 support=30.61 resistance=34.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=60.71 liquidity=35699504.0 spike=1.76
- MTIE.CA: score=19.69 buy_ready=False sector_rank=19 price=9.02 support=8.71 resistance=9.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=42.75 liquidity=8854916.0 spike=0.35
- NAHO.CA: score=3.35 buy_ready=False sector_rank=8 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:55 PM market time freshness=DELAYED_CURRENT RSI=33.33 liquidity=32070.31 spike=0.86
- NCCW.CA: score=28.6 buy_ready=True sector_rank=8 price=6.22 support=5.13 resistance=6.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=67.37 liquidity=42720952.0 spike=2.14
- NEDA.CA: score=16.64 buy_ready=False sector_rank=8 price=2.8 support=2.65 resistance=2.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=55.56 liquidity=326062.69 spike=0.37
- NHPS.CA: score=12.35 buy_ready=False sector_rank=8 price=68.43 support=67.53 resistance=73.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=38.38 liquidity=1034804.38 spike=0.09
- NINH.CA: score=15.12 buy_ready=False sector_rank=8 price=17.85 support=17.53 resistance=20.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=47.16 liquidity=2805428.25 spike=0.2
- NIPH.CA: score=24.4 buy_ready=True sector_rank=4 price=170.0 support=155.1 resistance=186.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=59.65 liquidity=112767776.0 spike=0.9
- OBRI.CA: score=11.65 buy_ready=False sector_rank=8 price=34.31 support=34.2 resistance=39.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=26.33 liquidity=7337342.0 spike=0.6
- OCDI.CA: score=19.4 buy_ready=False sector_rank=5 price=20.79 support=20.19 resistance=23.67 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=44.4 liquidity=16838730.0 spike=0.38
- OCPH.CA: score=9.92 buy_ready=False sector_rank=8 price=357.69 support=350.0 resistance=409.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=20.34 liquidity=2601371.75 spike=0.19
- ODIN.CA: score=21.6 buy_ready=True sector_rank=8 price=2.05 support=1.89 resistance=2.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=65.62 liquidity=7285295.5 spike=0.72
- OFH.CA: score=25.38 buy_ready=True sector_rank=8 price=0.63 support=0.6 resistance=0.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=43.4 liquidity=9066465.0 spike=0.4
- OIH.CA: score=16.8 buy_ready=False sector_rank=2 price=1.41 support=1.35 resistance=1.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=12.5 liquidity=156191616.0 spike=1.2
- OLFI.CA: score=22.16 buy_ready=False sector_rank=10 price=21.73 support=21.0 resistance=22.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=43.78 liquidity=14632009.0 spike=0.67
- ORAS.CA: score=7.6 buy_ready=False sector_rank=20 price=718.01 support=710.01 resistance=730.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=165497472.0 spike=1.0
- ORHD.CA: score=22.4 buy_ready=True sector_rank=5 price=36.58 support=32.9 resistance=39.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=68.84 liquidity=168647312.0 spike=0.82
- ORWE.CA: score=21.4 buy_ready=False sector_rank=6 price=23.62 support=21.6 resistance=24.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=76.41 liquidity=36805568.0 spike=0.77
- PHAR.CA: score=19.72 buy_ready=False sector_rank=4 price=86.6 support=83.96 resistance=92.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=37.37 liquidity=7322141.5 spike=0.2
- PHDC.CA: score=24.4 buy_ready=True sector_rank=5 price=14.8 support=13.01 resistance=16.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=64.65 liquidity=300274496.0 spike=0.7
- PHTV.CA: score=15.91 buy_ready=False sector_rank=8 price=205.13 support=201.5 resistance=233.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=44.25 liquidity=3594322.75 spike=0.23
- POUL.CA: score=24.16 buy_ready=True sector_rank=10 price=36.88 support=34.06 resistance=39.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=60.39 liquidity=12554174.0 spike=0.25
- PRCL.CA: score=13.62 buy_ready=False sector_rank=12 price=26.23 support=24.26 resistance=28.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=107079088.0 spike=3.32
- PRDC.CA: score=24.4 buy_ready=True sector_rank=5 price=6.08 support=5.2 resistance=6.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=69.29 liquidity=12076066.0 spike=0.6
- PRMH.CA: score=22.52 buy_ready=False sector_rank=8 price=2.82 support=2.17 resistance=2.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=76.04 liquidity=24587362.0 spike=1.6
- RACC.CA: score=16.86 buy_ready=False sector_rank=8 price=9.84 support=9.56 resistance=12.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=57.05 liquidity=4547141.0 spike=0.14
- RAKT.CA: score=7.43 buy_ready=False sector_rank=8 price=23.79 support=22.1 resistance=25.0 source=Yahoo Finance as_of=2026-06-06T21:00:00+00:00 freshness=FRESH RSI=34.57 liquidity=113287.98 spike=0.44
- RAYA.CA: score=29.4 buy_ready=True sector_rank=1 price=7.45 support=6.6 resistance=8.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=62.76 liquidity=69999072.0 spike=0.58
- RMDA.CA: score=31.4 buy_ready=True sector_rank=4 price=5.24 support=4.78 resistance=5.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=62.85 liquidity=1053935232.0 spike=18.77
- ROTO.CA: score=22.64 buy_ready=True sector_rank=8 price=33.89 support=32.66 resistance=36.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=43.85 liquidity=8320576.0 spike=0.64
- RREI.CA: score=26.32 buy_ready=True sector_rank=8 price=3.57 support=3.32 resistance=3.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=49.44 liquidity=17682696.0 spike=0.75
- RTVC.CA: score=10.52 buy_ready=False sector_rank=8 price=3.99 support=3.77 resistance=3.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=10208296.0 spike=1.6
- RUBX.CA: score=16.32 buy_ready=False sector_rank=8 price=10.23 support=9.8 resistance=11.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=31.69 liquidity=10606694.0 spike=0.67
- SAUD.CA: score=19.1 buy_ready=False sector_rank=13 price=22.23 support=21.8 resistance=25.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=47.0 liquidity=7300927.0 spike=0.5
- SCEM.CA: score=19.7 buy_ready=False sector_rank=12 price=63.5 support=62.07 resistance=72.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=42.14 liquidity=7724471.5 spike=0.18
- SCFM.CA: score=10.69 buy_ready=False sector_rank=8 price=258.54 support=255.7 resistance=315.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=22.13 liquidity=3378850.5 spike=0.12
- SCTS.CA: score=10.26 buy_ready=False sector_rank=14 price=614.35 support=590.01 resistance=709.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=14.59 liquidity=3709912.0 spike=0.33
- SDTI.CA: score=19.06 buy_ready=True sector_rank=8 price=45.93 support=43.4 resistance=46.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=55.97 liquidity=4743270.0 spike=0.24
- SEIG.CA: score=17.77 buy_ready=True sector_rank=8 price=186.72 support=173.35 resistance=205.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=53.14 liquidity=1455058.75 spike=0.24
- SIPC.CA: score=26.32 buy_ready=True sector_rank=8 price=3.63 support=3.4 resistance=3.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=53.06 liquidity=13837966.0 spike=0.9
- SKPC.CA: score=12.03 buy_ready=False sector_rank=17 price=17.17 support=16.8 resistance=18.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=27.72 liquidity=68225560.0 spike=0.92
- SMFR.CA: score=10.11 buy_ready=False sector_rank=8 price=206.04 support=203.51 resistance=224.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=29.94 liquidity=2792379.0 spike=0.23
- SNFC.CA: score=22.32 buy_ready=False sector_rank=8 price=12.09 support=11.66 resistance=12.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=45.45 liquidity=13304299.0 spike=0.48
- SPIN.CA: score=11.13 buy_ready=False sector_rank=6 price=14.1 support=13.69 resistance=15.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=40.88 liquidity=1730602.63 spike=0.35
- SPMD.CA: score=27.16 buy_ready=True sector_rank=8 price=0.42 support=0.38 resistance=0.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=66.96 liquidity=33993392.0 spike=1.42
- SUGR.CA: score=19.61 buy_ready=False sector_rank=10 price=49.22 support=48.0 resistance=52.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=36.46 liquidity=5442366.0 spike=0.33
- SVCE.CA: score=22.32 buy_ready=False sector_rank=8 price=8.68 support=7.98 resistance=9.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=42.27 liquidity=60069376.0 spike=0.43
- SWDY.CA: score=21.19 buy_ready=False sector_rank=15 price=87.2 support=85.25 resistance=91.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=55.17 liquidity=16498053.0 spike=0.46
- TALM.CA: score=15.86 buy_ready=False sector_rank=14 price=15.9 support=15.12 resistance=17.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=40.94 liquidity=4316822.0 spike=0.33
- TMGH.CA: score=22.4 buy_ready=False sector_rank=5 price=96.48 support=91.87 resistance=101.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=57.55 liquidity=268021488.0 spike=0.49
- TRTO.CA: score=10.32 buy_ready=False sector_rank=8 price=0.03 support=0.03 resistance=0.04 source=Yahoo Finance as_of=2026-06-06T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- UEFM.CA: score=3.69 buy_ready=False sector_rank=8 price=474.08 support=455.6 resistance=508.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:09 PM market time freshness=DELAYED_CURRENT RSI=30.99 liquidity=377875.19 spike=0.22
- UEGC.CA: score=27.92 buy_ready=False sector_rank=8 price=1.44 support=1.3 resistance=1.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=75.0 liquidity=43930372.0 spike=1.8
- UNIP.CA: score=22.42 buy_ready=False sector_rank=8 price=0.32 support=0.28 resistance=0.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=78.46 liquidity=16238167.0 spike=1.05
- UNIT.CA: score=26.52 buy_ready=True sector_rank=5 price=14.15 support=10.83 resistance=15.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=62.8 liquidity=10664645.0 spike=1.06
- WCDF.CA: score=7.69 buy_ready=False sector_rank=8 price=539.17 support=535.0 resistance=559.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=15.04 liquidity=370845.44 spike=0.49
- WKOL.CA: score=5.85 buy_ready=False sector_rank=8 price=292.31 support=290.0 resistance=339.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=30.88 liquidity=1530177.88 spike=0.2
- ZEOT.CA: score=19.7 buy_ready=True sector_rank=8 price=9.16 support=8.43 resistance=9.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=55.41 liquidity=3382228.5 spike=0.4
- ZMID.CA: score=26.26 buy_ready=True sector_rank=5 price=6.28 support=5.77 resistance=6.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=40.0 liquidity=381908864.0 spike=1.93

## Backtesting Lite
- RMDA.CA: 180d return=26.65%, max drawdown=-31.33%, MA20>MA50 days last20=20, as_of=2026-06-06T21:00:00+00:00
- ECAP.CA: 180d return=7.11%, max drawdown=-28.16%, MA20>MA50 days last20=20, as_of=2026-06-06T21:00:00+00:00
- CCAP.CA: 180d return=120.08%, max drawdown=-25.0%, MA20>MA50 days last20=20, as_of=2026-06-06T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- RMDA.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Tenth of Ramadan Pharmaceutical Industries summary=Evidence rejected for RMDA.CA: source text did not clearly match RMDA.CA / Tenth of Ramadan Pharmaceutical Industries.
- ECAP.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Al Ezz Ceramics & Porcelain Co. summary=Evidence rejected for ECAP.CA: source text did not clearly match ECAP.CA / Al Ezz Ceramics & Porcelain Co..
- CCAP.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Qalaa Holdings summary=Evidence rejected for CCAP.CA: source text did not clearly match CCAP.CA / Qalaa Holdings.
- MPRC.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Egyptian Media Production City summary=Evidence rejected for MPRC.CA: source text did not clearly match MPRC.CA / Egyptian Media Production City.
- RAYA.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=523 sources=3 expected=Raya Holding summary=Raya stock maintains bullish momentum above EGP 9; Aman Holding, MSMEDA partner to inject EGP 300m into SMEs across Egypt; Raya Holding’s consolidated profits surge in 2025; revenues hit EGP 63.8bn
  - Raya stock maintains bullish momentum above EGP 9: https://english.mubasher.info/news/4601857/Raya-stock-maintains-bullish-momentum-above-EGP-9/
  - Aman Holding, MSMEDA partner to inject EGP 300m into SMEs across Egypt: https://english.mubasher.info/news/4577815/Aman-Holding-MSMEDA-partner-to-inject-EGP-300m-into-SMEs-across-Egypt/
  - Raya Holding’s consolidated profits surge in 2025; revenues hit EGP 63.8bn: https://english.mubasher.info/news/4564195/Raya-Holding-s-consolidated-profits-surge-in-2025-revenues-hit-EGP-63-8bn/
- NCCW.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Nasr Company for Civil Works summary=Nasr for Civil Works unveils EGP 150m capital increase; Arabia Investments, Nasr Company for Civil Works unveil capital hike; Nasr Company for Civil Works’ consortium signs EUR 46m agreement with Uganda
  - Nasr for Civil Works unveils EGP 150m capital increase: https://english.mubasher.info/news/4550493/Nasr-for-Civil-Works-unveils-EGP-150m-capital-increase/
  - Arabia Investments, Nasr Company for Civil Works unveil capital hike: https://english.mubasher.info/news/4284206/Arabia-Investments-Nasr-Company-for-Civil-Works-unveil-capital-hike/
  - Nasr Company for Civil Works’ consortium signs EUR 46m agreement with Uganda: https://english.mubasher.info/news/4249759/Nasr-Company-for-Civil-Works-consortium-signs-EUR-46m-agreement-with-Uganda/
- AREH.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Real Estate Egyptian Consortium S.A.E summary=Real Estate Egyptian Consortium’s net profits approach EGP 2m in 9M-25; Shareholder ups stake in Real Estate Egyptian; Target for Real Estate Investment cuts stake in Real Estate Egyptian
  - Real Estate Egyptian Consortium’s net profits approach EGP 2m in 9M-25: https://english.mubasher.info/news/4528467/Real-Estate-Egyptian-Consortium-s-net-profits-approach-EGP-2m-in-9M-25/
  - Shareholder ups stake in Real Estate Egyptian: https://english.mubasher.info/news/4026301/Shareholder-ups-stake-in-Real-Estate-Egyptian/
  - Target for Real Estate Investment cuts stake in Real Estate Egyptian: https://english.mubasher.info/news/4010821/Target-for-Real-Estate-Investment-cuts-stake-in-Real-Estate-Egyptian/
- LUTS.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Lotus Agri Capital summary=Evidence rejected for LUTS.CA: source text did not clearly match LUTS.CA / Lotus Agri Capital.

## Warnings
- Evidence rejected for RMDA.CA: source text did not clearly match RMDA.CA / Tenth of Ramadan Pharmaceutical Industries.
- Gemini batch evidence failed: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.', 'status': 'UNAVAILABLE'}}
- Evidence rejected for ECAP.CA: source text did not clearly match ECAP.CA / Al Ezz Ceramics & Porcelain Co..
- Evidence rejected for CCAP.CA: source text did not clearly match CCAP.CA / Qalaa Holdings.
- Evidence rejected for MPRC.CA: source text did not clearly match MPRC.CA / Egyptian Media Production City.
- Evidence for RAYA.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for NCCW.CA matches the company but no source/report date was detected.
- Evidence for AREH.CA matches the company but no source/report date was detected.
- Mubasher stock page returned no evidence titles for LUTS.CA.
- No Yahoo or Mubasher evidence found for LUTS.CA.
- Evidence rejected for LUTS.CA: source text did not clearly match LUTS.CA / Lotus Agri Capital.
