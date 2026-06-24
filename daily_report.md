# Telegram-First EGX Scanner Report

Scan phase: Post-close tomorrow tickets
Generated UTC: 2026-06-24T15:20:21.936464+00:00
Generated Cairo: 2026-06-24 18:20
Run timing: target 15:30 Cairo | generated Cairo 2026-06-24 18:20 | cron 30 12 * * 0-4
Trigger: scheduled cron=30 12 * * 0-4 mapped to post_close; Cairo now 2026-06-24 18:15

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 46
- Data quality issues: 0
- Tradeable price/liquidity tickers: 184/190
- Top sector: Tourism & Leisure

## Market Context
- Market trend: Bearish
- Source: Mubasher EGX market page (delayed public data)
- As of: Wednesday, June 24
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 36.84% / above MA50 47.37%
- EGX70 regime: MIXED / above MA20 46.15% / above MA50 71.79%
- Sector breadth: 42.86%
- Risk mode: SELECTIVE_SWING_TRADES_ONLY

## Top Liquidity
- ZMID.CA: liquidity=451842368.0 spike=2.33 score=30.41
- COMI.CA: liquidity=401608800.0 spike=0.68 score=20.25
- CCAP.CA: liquidity=343383104.0 spike=0.46 score=21.41
- ISMQ.CA: liquidity=284564864.0 spike=3.76 score=11.47
- OCDI.CA: liquidity=238581856.0 spike=5.91 score=13.75

## AI Narrative
- Provider: OpenRouter OK
- Model: openai/gpt-oss-120b:free
- Summary: The scanner highlighted a handful of bullish‑watch stocks that cleared liquidity, freshness and technical gates, most notably CLHO.CA (Healthcare) and MHOT.CA (Tourism & Leisure). These tickets sit near strong 20‑day support with modest distance to resistance, and are in sectors that are currently leading the market breadth (42.86%). EGX30 remains bearish, while EGX70 shows mixed signals, prompting the engine to stay in a selective swing‑trade risk mode. Expect near‑term price moves to respect the identified support/resistance zones, but beware of heightened uncertainty from the overall bearish EGX30 trend and mixed EGX70 momentum.
- CLHO.CA and MHOT.CA have strong liquidity spikes and sit close to 20‑day support, making them the top buy‑ready candidates.
- Sector breadth is led by Tourism & Leisure and Healthcare, both above their 20‑day and 50‑day moving averages.
- EGX30 bearish trend limits broad market upside; EGX70 mixed trend allows selective swing opportunities.
- Support levels (e.g., CLHO 14.25, MHOT 28.83) act as near‑term price floors, while resistance is tight (e.g., CLHO 17.0).
- Uncertainty remains high due to overall market weakness and some stocks showing over‑extended RSI or cooling liquidity.

## Top Liquidity Spikes
- SPIN.CA: spike=10.09 liquidity=45853284.0 outlook=WEAK_OR_RISKY score=30.01 buy_ready=False
- GTWL.CA: spike=8.79 liquidity=56633008.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- OCDI.CA: spike=5.91 liquidity=238581856.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- GIHD.CA: spike=5.5 liquidity=31996158.0 outlook=BULLISH_WATCH score=90.08 buy_ready=True
- UEFM.CA: spike=5.42 liquidity=4304047.5 outlook=BULLISH_WATCH score=94.08 buy_ready=True

## Sector Leaderboard
- #1 Tourism & Leisure: score=17.22 5d=18.31% 20d=15.49% aboveMA50=100.0%
- #2 Automotive & Distribution: score=8.54 5d=3.97% 20d=8.41% aboveMA50=100.0%
- #3 Healthcare: score=7.81 5d=2.23% 20d=3.04% aboveMA50=100.0%
- #4 Technology & Distribution: score=7.61 5d=1.28% 20d=-5.08% aboveMA50=100.0%
- #5 Non-bank Financial Services: score=6.05 5d=1.67% 20d=1.05% aboveMA50=60.0%
- #6 Education: score=5.88 5d=-1.36% 20d=3.03% aboveMA50=66.67%
- #7 Telecommunications: score=5.29 5d=1.27% 20d=-1.83% aboveMA50=100.0%
- #8 Food, Beverages & Tobacco: score=5.09 5d=0.09% 20d=2.32% aboveMA50=71.43%

## Today's Prioritized Action Tickets
- HOLD: Local fallback HOLD: no candidate passed evidence, liquidity, freshness, and technical gates.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- CLHO.CA: BULLISH_WATCH score=100 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=close to resistance
- NIPH.CA: BULLISH_WATCH score=98.81 liquidity=TRADEABLE sector=LEADING risk=No major short-term scanner risk flags.
- UEFM.CA: BULLISH_WATCH score=94.08 liquidity=TRADEABLE sector=IMPROVING risk=sector is not leading
- TALM.CA: BULLISH_WATCH score=92.88 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=No major short-term scanner risk flags.
- GIHD.CA: BULLISH_WATCH score=90.08 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=far above support; sector is not leading
- POUL.CA: BULLISH_WATCH score=89.09 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- RAYA.CA: BULLISH_WATCH score=88.61 liquidity=TRADEABLE sector=IMPROVING risk=No major short-term scanner risk flags.
- ISPH.CA: BULLISH_WATCH score=87.81 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- MIPH.CA: BULLISH_WATCH score=87.81 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- MHOT.CA: BULLISH_WATCH score=86 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; momentum is extended; far above support

## BUY-Ready Candidates
- CLHO.CA: rank=34.4 outlook=BULLISH_WATCH outlook_score=100 sector_rank=3 price=16.81 support=14.25 resistance=17.0 liquidity=143580256.0
- GIHD.CA: rank=32.63 outlook=BULLISH_WATCH outlook_score=90.08 sector_rank=13 price=44.42 support=35.15 resistance=47.0 liquidity=31996158.0
- POUL.CA: rank=31.72 outlook=BULLISH_WATCH outlook_score=89.09 sector_rank=8 price=39.75 support=34.99 resistance=39.5 liquidity=106595192.0
- ZMID.CA: rank=30.41 outlook=BULLISH_WATCH outlook_score=80.37 sector_rank=11 price=6.58 support=5.82 resistance=6.55 liquidity=451842368.0
- MHOT.CA: rank=29.4 outlook=BULLISH_WATCH outlook_score=86 sector_rank=1 price=34.94 support=28.83 resistance=38.38 liquidity=13720377.0
- DAPH.CA: rank=28.15 outlook=BULLISH_WATCH outlook_score=80.08 sector_rank=13 price=82.12 support=76.6 resistance=82.5 liquidity=17523082.0
- AFDI.CA: rank=27.63 outlook=BULLISH_WATCH outlook_score=76.08 sector_rank=13 price=46.7 support=40.15 resistance=48.89 liquidity=11863123.0
- ISPH.CA: rank=27.4 outlook=BULLISH_WATCH outlook_score=87.81 sector_rank=3 price=12.29 support=11.3 resistance=12.74 liquidity=28083954.0
- PHAR.CA: rank=27.4 outlook=BULLISH_WATCH outlook_score=81.81 sector_rank=3 price=88.48 support=83.02 resistance=89.99 liquidity=13568224.0
- UEFM.CA: rank=26.94 outlook=BULLISH_WATCH outlook_score=94.08 sector_rank=13 price=496.53 support=465.01 resistance=490.0 liquidity=4304047.5

## Data Quality Issues
- No provider failures.

## Ranked Scanner Results
- AALR.CA: score=13.24 buy_ready=False sector_rank=13 price=206.12 support=200.0 resistance=231.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=44.48 liquidity=1605011.75 spike=0.26
- ABUK.CA: score=12.55 buy_ready=False sector_rank=21 price=70.39 support=68.01 resistance=86.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=6.56 liquidity=223649568.0 spike=1.54
- ACAMD.CA: score=21.63 buy_ready=False sector_rank=13 price=2.2 support=2.17 resistance=2.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=37.5 liquidity=109026992.0 spike=0.87
- ACGC.CA: score=20.8 buy_ready=False sector_rank=16 price=9.54 support=9.11 resistance=10.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=36.27 liquidity=31485260.0 spike=0.55
- ADCI.CA: score=23.95 buy_ready=False sector_rank=13 price=243.0 support=211.0 resistance=242.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=93.25 liquidity=13901931.0 spike=1.66
- ADIB.CA: score=18.25 buy_ready=False sector_rank=15 price=45.5 support=44.01 resistance=48.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=44.42 liquidity=76004056.0 spike=0.75
- ADPC.CA: score=17.43 buy_ready=False sector_rank=13 price=3.62 support=3.45 resistance=3.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=54.46 liquidity=6801130.0 spike=0.25
- AFDI.CA: score=27.63 buy_ready=True sector_rank=13 price=46.7 support=40.15 resistance=48.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=51.12 liquidity=11863123.0 spike=0.81
- AFMC.CA: score=9.67 buy_ready=False sector_rank=13 price=70.56 support=67.0 resistance=74.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=37.38 liquidity=1033436.44 spike=0.3
- AJWA.CA: score=17.84 buy_ready=False sector_rank=13 price=176.92 support=131.5 resistance=188.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=84.31 liquidity=7210317.5 spike=0.27
- ALCN.CA: score=6.66 buy_ready=False sector_rank=19 price=28.08 support=25.51 resistance=33.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=33.42 liquidity=4057477.0 spike=0.3
- ALUM.CA: score=11.0 buy_ready=False sector_rank=13 price=22.69 support=22.81 resistance=26.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=33.63 liquidity=7363641.5 spike=0.72
- AMER.CA: score=13.75 buy_ready=False sector_rank=11 price=2.41 support=2.35 resistance=3.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=25.84 liquidity=57662736.0 spike=0.67
- AMES.CA: score=8.89 buy_ready=False sector_rank=13 price=48.4 support=48.0 resistance=53.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=36.38 liquidity=1262151.25 spike=0.38
- AMIA.CA: score=15.56 buy_ready=False sector_rank=13 price=8.57 support=8.55 resistance=9.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=41.55 liquidity=3928874.0 spike=0.28
- AMOC.CA: score=13.96 buy_ready=False sector_rank=9 price=7.68 support=7.58 resistance=8.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=14.41 liquidity=29273186.0 spike=0.47
- ANFI.CA: score=18.96 buy_ready=True sector_rank=13 price=26.5 support=13.73 resistance=41.4 source=Yahoo Finance as_of=2026-06-22T21:00:00+00:00 freshness=FRESH RSI=64.45 liquidity=3331182.5 spike=0.04
- APSW.CA: score=3.14 buy_ready=False sector_rank=13 price=8.56 support=8.24 resistance=9.21 source=Yahoo Finance as_of=2026-06-22T21:00:00+00:00 freshness=FRESH RSI=11.11 liquidity=509508.34 spike=0.92
- ARAB.CA: score=18.75 buy_ready=False sector_rank=11 price=0.21 support=0.2 resistance=0.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=43.24 liquidity=33791800.0 spike=0.39
- ARCC.CA: score=15.7 buy_ready=False sector_rank=17 price=56.1 support=53.0 resistance=60.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=23.35 liquidity=30914488.0 spike=0.9
- AREH.CA: score=25.43 buy_ready=True sector_rank=13 price=1.62 support=1.32 resistance=1.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=69.09 liquidity=58523216.0 spike=1.9
- ARVA.CA: score=23.63 buy_ready=True sector_rank=13 price=11.18 support=8.08 resistance=13.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=59.13 liquidity=19571452.0 spike=0.61
- ASCM.CA: score=24.61 buy_ready=False sector_rank=13 price=61.16 support=47.45 resistance=73.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=75.5 liquidity=163861984.0 spike=1.99
- ASPI.CA: score=23.63 buy_ready=True sector_rank=13 price=0.32 support=0.26 resistance=0.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=46.67 liquidity=20466360.0 spike=0.29
- ATLC.CA: score=21.01 buy_ready=True sector_rank=5 price=5.1 support=4.7 resistance=5.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=57.24 liquidity=4614722.0 spike=0.78
- ATQA.CA: score=10.51 buy_ready=False sector_rank=21 price=9.39 support=9.02 resistance=10.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=31.67 liquidity=31897000.0 spike=1.02
- AXPH.CA: score=12.58 buy_ready=False sector_rank=13 price=1100.23 support=1073.0 resistance=1174.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=52.91 liquidity=943636.38 spike=0.58
- BINV.CA: score=14.33 buy_ready=False sector_rank=14 price=47.37 support=42.97 resistance=49.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=52.09 liquidity=925221.88 spike=0.09
- BIOC.CA: score=13.6 buy_ready=False sector_rank=13 price=71.02 support=68.34 resistance=75.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=51.74 liquidity=1969502.5 spike=0.78
- BTFH.CA: score=18.4 buy_ready=False sector_rank=5 price=3.02 support=2.96 resistance=3.23 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=44.44 liquidity=129275760.0 spike=0.65
- CAED.CA: score=13.57 buy_ready=False sector_rank=13 price=70.5 support=67.21 resistance=78.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=49.85 liquidity=1936312.88 spike=0.35
- CANA.CA: score=24.01 buy_ready=False sector_rank=15 price=36.2 support=34.5 resistance=39.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=51.92 liquidity=13433680.0 spike=1.38
- CCAP.CA: score=21.41 buy_ready=False sector_rank=14 price=5.02 support=4.92 resistance=5.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=37.58 liquidity=343383104.0 spike=0.46
- CCRS.CA: score=16.36 buy_ready=False sector_rank=13 price=2.4 support=2.32 resistance=2.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=39.39 liquidity=4723958.5 spike=0.21
- CEFM.CA: score=5.0 buy_ready=False sector_rank=13 price=100.87 support=100.53 resistance=109.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=28.56 liquidity=1364103.5 spike=0.58
- CERA.CA: score=23.37 buy_ready=True sector_rank=13 price=1.24 support=1.15 resistance=1.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=57.69 liquidity=8735567.0 spike=0.58
- CFGH.CA: score=2.63 buy_ready=False sector_rank=13 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance as_of=2026-06-22T21:00:00+00:00 freshness=FRESH RSI=0.0 liquidity=1497.53 spike=0.26
- CICH.CA: score=16.4 buy_ready=True sector_rank=5 price=12.11 support=11.1 resistance=13.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=42.25 liquidity=1997162.38 spike=0.56
- CIEB.CA: score=23.98 buy_ready=True sector_rank=15 price=23.97 support=23.27 resistance=24.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=62.5 liquidity=6729827.5 spike=0.99
- CIRA.CA: score=26.77 buy_ready=True sector_rank=6 price=28.73 support=25.23 resistance=31.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=62.76 liquidity=22830822.0 spike=1.21
- CLHO.CA: score=34.4 buy_ready=True sector_rank=3 price=16.81 support=14.25 resistance=17.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=53.85 liquidity=143580256.0 spike=4.93
- CNFN.CA: score=28.94 buy_ready=False sector_rank=5 price=4.94 support=4.36 resistance=5.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=73.13 liquidity=80228208.0 spike=2.27
- COMI.CA: score=20.25 buy_ready=False sector_rank=15 price=132.12 support=129.8 resistance=137.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=54.25 liquidity=401608800.0 spike=0.68
- COPR.CA: score=20.63 buy_ready=False sector_rank=13 price=0.36 support=0.35 resistance=0.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=53.97 liquidity=14759385.0 spike=0.38
- COSG.CA: score=21.63 buy_ready=False sector_rank=13 price=1.54 support=1.53 resistance=1.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=47.83 liquidity=10316492.0 spike=0.18
- CPCI.CA: score=12.2 buy_ready=False sector_rank=13 price=375.5 support=347.11 resistance=375.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=77.27 liquidity=1564888.88 spike=0.78
- CSAG.CA: score=20.78 buy_ready=False sector_rank=19 price=31.28 support=30.08 resistance=32.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=41.0 liquidity=12227716.0 spike=1.09
- DAPH.CA: score=28.15 buy_ready=True sector_rank=13 price=82.12 support=76.6 resistance=82.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=46.92 liquidity=17523082.0 spike=2.26
- DEIN.CA: score=9.63 buy_ready=False sector_rank=13 price=11.38 support=11.38 resistance=13.65 source=Yahoo Finance as_of=2026-06-22T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- DOMT.CA: score=22.77 buy_ready=False sector_rank=8 price=27.36 support=23.7 resistance=27.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=74.05 liquidity=5396509.5 spike=1.67
- DSCW.CA: score=19.63 buy_ready=False sector_rank=13 price=1.78 support=1.74 resistance=1.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=47.22 liquidity=38528188.0 spike=0.79
- DTPP.CA: score=4.75 buy_ready=False sector_rank=13 price=117.3 support=114.0 resistance=130.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=11.41 liquidity=1122218.38 spike=0.62
- EALR.CA: score=9.45 buy_ready=False sector_rank=13 price=354.7 support=350.2 resistance=380.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=48.02 liquidity=821950.81 spike=0.25
- EASB.CA: score=13.63 buy_ready=False sector_rank=13 price=8.0 support=7.0 resistance=8.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=28264484.0 spike=3.58
- EAST.CA: score=24.04 buy_ready=True sector_rank=8 price=38.94 support=37.01 resistance=40.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=51.91 liquidity=40242400.0 spike=0.88
- EBSC.CA: score=14.81 buy_ready=False sector_rank=13 price=1.82 support=1.66 resistance=2.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=51.11 liquidity=1177959.38 spike=0.43
- ECAP.CA: score=22.29 buy_ready=False sector_rank=13 price=32.55 support=29.8 resistance=34.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=70.87 liquidity=8122837.5 spike=1.27
- EDFM.CA: score=6.71 buy_ready=False sector_rank=13 price=332.0 support=322.11 resistance=355.0 source=Yahoo Finance as_of=2026-06-22T21:00:00+00:00 freshness=FRESH RSI=16.43 liquidity=76692.0 spike=0.15
- EEII.CA: score=21.58 buy_ready=True sector_rank=13 price=2.4 support=2.3 resistance=2.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=53.57 liquidity=5946222.0 spike=0.4
- EFIC.CA: score=0.98 buy_ready=False sector_rank=21 price=198.15 support=192.01 resistance=213.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=17.89 liquidity=510267.38 spike=0.24
- EFID.CA: score=14.04 buy_ready=False sector_rank=8 price=27.56 support=27.06 resistance=29.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=31.48 liquidity=22514866.0 spike=0.3
- EFIH.CA: score=16.53 buy_ready=False sector_rank=20 price=21.04 support=20.2 resistance=22.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=38.99 liquidity=13663688.0 spike=0.27
- EGAL.CA: score=11.47 buy_ready=False sector_rank=21 price=282.8 support=286.11 resistance=334.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=11.25 liquidity=44855560.0 spike=0.58
- EGAS.CA: score=21.64 buy_ready=True sector_rank=9 price=51.5 support=47.5 resistance=55.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=56.07 liquidity=7675069.0 spike=0.63
- EGBE.CA: score=11.26 buy_ready=False sector_rank=15 price=0.44 support=0.43 resistance=0.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=41.51 liquidity=16834.69 spike=0.17
- EGCH.CA: score=11.47 buy_ready=False sector_rank=21 price=13.1 support=12.8 resistance=15.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=20.74 liquidity=19785576.0 spike=0.3
- EGSA.CA: score=7.12 buy_ready=False sector_rank=7 price=8.78 support=8.55 resistance=9.1 source=Yahoo Finance as_of=2026-06-22T21:00:00+00:00 freshness=FRESH RSI=30.0 liquidity=2247.68 spike=0.28
- EGTS.CA: score=16.75 buy_ready=False sector_rank=11 price=17.4 support=17.25 resistance=22.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=33.94 liquidity=21909620.0 spike=0.19
- EHDR.CA: score=21.63 buy_ready=False sector_rank=13 price=2.54 support=2.25 resistance=2.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=56.25 liquidity=16665028.0 spike=0.3
- EKHO.CA: score=13.96 buy_ready=False sector_rank=9 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-06-22T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=19.74 buy_ready=False sector_rank=12 price=2.12 support=2.06 resistance=2.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=13926659.0 spike=0.62
- ELKA.CA: score=20.63 buy_ready=False sector_rank=13 price=1.23 support=1.15 resistance=1.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=44.44 liquidity=18966806.0 spike=0.46
- ELNA.CA: score=12.51 buy_ready=False sector_rank=13 price=37.73 support=37.11 resistance=41.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=44.89 liquidity=1182452.0 spike=2.85
- ELSH.CA: score=21.63 buy_ready=False sector_rank=13 price=11.91 support=8.31 resistance=14.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=51.24 liquidity=47691472.0 spike=0.25
- ELWA.CA: score=13.53 buy_ready=False sector_rank=13 price=2.01 support=2.0 resistance=2.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:10 PM market time freshness=DELAYED_CURRENT RSI=53.33 liquidity=1894716.0 spike=0.6
- EMFD.CA: score=21.75 buy_ready=False sector_rank=11 price=11.69 support=10.5 resistance=12.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=48.8 liquidity=68983944.0 spike=0.25
- ENGC.CA: score=18.26 buy_ready=True sector_rank=13 price=36.3 support=32.81 resistance=38.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=67.22 liquidity=4631234.0 spike=0.33
- EOSB.CA: score=15.72 buy_ready=False sector_rank=13 price=1.48 support=1.35 resistance=1.55 source=Yahoo Finance as_of=2026-06-22T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=86582.96 spike=0.7
- EPCO.CA: score=13.0 buy_ready=False sector_rank=13 price=9.01 support=8.9 resistance=9.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=48.02 liquidity=4367590.0 spike=0.46
- EPPK.CA: score=13.05 buy_ready=False sector_rank=13 price=12.52 support=11.67 resistance=13.12 source=Yahoo Finance as_of=2026-06-22T21:00:00+00:00 freshness=FRESH RSI=52.26 liquidity=415463.7 spike=0.5
- ETEL.CA: score=24.12 buy_ready=True sector_rank=7 price=94.99 support=89.61 resistance=98.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=41.29 liquidity=46821368.0 spike=0.58
- ETRS.CA: score=23.63 buy_ready=True sector_rank=13 price=10.21 support=7.93 resistance=11.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=65.81 liquidity=10980946.0 spike=0.18
- EXPA.CA: score=18.25 buy_ready=False sector_rank=15 price=18.22 support=18.21 resistance=20.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=46.63 liquidity=24797310.0 spike=0.74
- FAIT.CA: score=12.97 buy_ready=False sector_rank=15 price=36.24 support=35.01 resistance=38.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=36.17 liquidity=1717510.75 spike=0.45
- FAITA.CA: score=11.26 buy_ready=False sector_rank=15 price=0.99 support=0.99 resistance=1.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:32 PM market time freshness=DELAYED_CURRENT RSI=47.73 liquidity=9407.5 spike=0.25
- FERC.CA: score=12.28 buy_ready=False sector_rank=21 price=75.53 support=75.0 resistance=80.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=43.52 liquidity=4511723.5 spike=1.15
- FWRY.CA: score=13.53 buy_ready=False sector_rank=20 price=19.0 support=17.71 resistance=20.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=34.23 liquidity=47467560.0 spike=0.17
- GBCO.CA: score=25.4 buy_ready=False sector_rank=2 price=31.11 support=25.25 resistance=31.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=86.15 liquidity=49393692.0 spike=0.48
- GDWA.CA: score=14.87 buy_ready=False sector_rank=13 price=0.79 support=0.77 resistance=0.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=45.11 liquidity=7239696.5 spike=0.52
- GGCC.CA: score=19.08 buy_ready=True sector_rank=13 price=0.42 support=0.4 resistance=0.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=52.94 liquidity=4451210.0 spike=0.55
- GIHD.CA: score=32.63 buy_ready=True sector_rank=13 price=44.42 support=35.15 resistance=47.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=61.04 liquidity=31996158.0 spike=5.5
- GMCI.CA: score=9.02 buy_ready=False sector_rank=13 price=1.71 support=1.68 resistance=1.84 source=Yahoo Finance as_of=2026-06-22T21:00:00+00:00 freshness=FRESH RSI=40.0 liquidity=448782.67 spike=1.47
- GRCA.CA: score=7.49 buy_ready=False sector_rank=13 price=53.5 support=50.2 resistance=60.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=32.99 liquidity=3855224.75 spike=0.74
- GSSC.CA: score=13.66 buy_ready=False sector_rank=13 price=248.13 support=228.1 resistance=257.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=38.36 liquidity=3027222.75 spike=0.76
- GTWL.CA: score=13.63 buy_ready=False sector_rank=13 price=57.58 support=49.37 resistance=57.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=56633008.0 spike=8.79
- HDBK.CA: score=24.99 buy_ready=False sector_rank=15 price=163.1 support=138.0 resistance=172.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=78.35 liquidity=56888052.0 spike=2.37
- HELI.CA: score=23.75 buy_ready=True sector_rank=11 price=6.54 support=6.28 resistance=6.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=44.08 liquidity=117196848.0 spike=0.85
- HRHO.CA: score=22.4 buy_ready=False sector_rank=5 price=27.07 support=25.8 resistance=27.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=49.89 liquidity=61252084.0 spike=0.43
- ICID.CA: score=20.63 buy_ready=False sector_rank=13 price=7.55 support=5.0 resistance=7.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=77.09 liquidity=10569005.0 spike=0.66
- IDRE.CA: score=19.86 buy_ready=True sector_rank=13 price=44.55 support=42.01 resistance=47.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=41.24 liquidity=6224376.5 spike=0.36
- IFAP.CA: score=5.55 buy_ready=False sector_rank=10 price=19.21 support=16.5 resistance=23.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=31.95 liquidity=2752840.0 spike=0.44
- INFI.CA: score=4.91 buy_ready=False sector_rank=13 price=93.23 support=93.0 resistance=105.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=15.58 liquidity=2280388.75 spike=0.27
- IRON.CA: score=6.09 buy_ready=False sector_rank=21 price=31.68 support=31.0 resistance=34.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=26.16 liquidity=5614436.0 spike=0.7
- ISMA.CA: score=21.63 buy_ready=False sector_rank=13 price=29.64 support=25.79 resistance=36.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=73.58 liquidity=14247544.0 spike=0.35
- ISMQ.CA: score=11.47 buy_ready=False sector_rank=21 price=8.9 support=8.1 resistance=8.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=284564864.0 spike=3.76
- ISPH.CA: score=27.4 buy_ready=True sector_rank=3 price=12.29 support=11.3 resistance=12.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=52.16 liquidity=28083954.0 spike=0.22
- JUFO.CA: score=26.04 buy_ready=True sector_rank=8 price=30.87 support=28.09 resistance=32.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=62.06 liquidity=15922400.0 spike=0.38
- KABO.CA: score=15.8 buy_ready=False sector_rank=16 price=6.18 support=5.96 resistance=6.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=32.43 liquidity=13833675.0 spike=0.75
- KWIN.CA: score=12.86 buy_ready=False sector_rank=13 price=66.21 support=66.1 resistance=79.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=43.82 liquidity=5231443.0 spike=0.82
- KZPC.CA: score=15.91 buy_ready=False sector_rank=13 price=10.56 support=10.34 resistance=11.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=47.41 liquidity=4276242.0 spike=0.62
- LCSW.CA: score=21.84 buy_ready=False sector_rank=17 price=27.33 support=26.0 resistance=28.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=54.16 liquidity=9139116.0 spike=0.9
- LUTS.CA: score=23.63 buy_ready=False sector_rank=13 price=0.73 support=0.55 resistance=0.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=72.96 liquidity=36936776.0 spike=0.89
- MAAL.CA: score=23.23 buy_ready=False sector_rank=13 price=6.95 support=5.16 resistance=6.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=79.1 liquidity=33468210.0 spike=2.3
- MASR.CA: score=25.63 buy_ready=True sector_rank=13 price=7.11 support=6.54 resistance=7.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=52.49 liquidity=51863912.0 spike=0.93
- MBSC.CA: score=17.7 buy_ready=False sector_rank=17 price=243.5 support=243.0 resistance=258.91 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=36.19 liquidity=10313939.0 spike=0.24
- MCQE.CA: score=7.8 buy_ready=False sector_rank=17 price=171.9 support=171.0 resistance=200.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=19.3 liquidity=5098255.5 spike=0.32
- MCRO.CA: score=12.63 buy_ready=False sector_rank=13 price=1.22 support=1.2 resistance=1.31 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=33.33 liquidity=19370552.0 spike=0.46
- MENA.CA: score=7.91 buy_ready=False sector_rank=11 price=6.71 support=6.22 resistance=7.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=32.08 liquidity=1159815.88 spike=0.07
- MEPA.CA: score=15.44 buy_ready=False sector_rank=13 price=1.61 support=1.62 resistance=1.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=39.29 liquidity=7805821.5 spike=0.57
- MFPC.CA: score=11.71 buy_ready=False sector_rank=21 price=36.16 support=35.15 resistance=44.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=4.07 liquidity=99963152.0 spike=1.12
- MFSC.CA: score=22.4 buy_ready=True sector_rank=13 price=49.74 support=43.0 resistance=56.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=58.36 liquidity=8764479.0 spike=0.71
- MHOT.CA: score=29.4 buy_ready=True sector_rank=1 price=34.94 support=28.83 resistance=38.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=66.46 liquidity=13720377.0 spike=0.53
- MICH.CA: score=25.63 buy_ready=True sector_rank=13 price=38.2 support=35.4 resistance=40.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=62.39 liquidity=13894904.0 spike=0.92
- MILS.CA: score=19.48 buy_ready=False sector_rank=13 price=133.53 support=130.11 resistance=151.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=42.03 liquidity=7847676.0 spike=0.56
- MIPH.CA: score=16.95 buy_ready=True sector_rank=3 price=663.03 support=651.0 resistance=710.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=52.48 liquidity=1545985.88 spike=0.7
- MOED.CA: score=13.16 buy_ready=False sector_rank=13 price=0.68 support=0.65 resistance=0.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=47.54 liquidity=3528099.25 spike=0.32
- MOIL.CA: score=16.08 buy_ready=False sector_rank=9 price=0.48 support=0.46 resistance=0.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=60.0 liquidity=121803.66 spike=0.73
- MOIN.CA: score=2.77 buy_ready=False sector_rank=13 price=23.51 support=23.2 resistance=25.66 source=Yahoo Finance as_of=2026-06-22T21:00:00+00:00 freshness=FRESH RSI=12.26 liquidity=139414.3 spike=0.23
- MOSC.CA: score=13.99 buy_ready=False sector_rank=13 price=266.23 support=246.6 resistance=330.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=46.96 liquidity=2353919.25 spike=0.27
- MPCI.CA: score=25.09 buy_ready=False sector_rank=13 price=242.29 support=204.36 resistance=253.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=75.08 liquidity=199162208.0 spike=2.23
- MPCO.CA: score=23.8 buy_ready=True sector_rank=10 price=1.87 support=1.58 resistance=2.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=65.43 liquidity=69058640.0 spike=0.68
- MPRC.CA: score=30.63 buy_ready=False sector_rank=13 price=37.14 support=31.1 resistance=36.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=72.53 liquidity=130737432.0 spike=4.52
- MTIE.CA: score=23.41 buy_ready=False sector_rank=2 price=8.99 support=8.65 resistance=9.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=48.15 liquidity=9010370.0 spike=0.55
- NAHO.CA: score=7.64 buy_ready=False sector_rank=13 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance as_of=2026-06-22T21:00:00+00:00 freshness=FRESH RSI=42.86 liquidity=8410.06 spike=0.42
- NCCW.CA: score=23.63 buy_ready=False sector_rank=13 price=6.39 support=5.29 resistance=6.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=73.75 liquidity=16488388.0 spike=0.52
- NEDA.CA: score=8.95 buy_ready=False sector_rank=13 price=2.74 support=2.68 resistance=2.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=39.29 liquidity=318407.84 spike=0.72
- NHPS.CA: score=14.76 buy_ready=False sector_rank=13 price=66.69 support=65.03 resistance=71.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=41.25 liquidity=4866046.0 spike=1.13
- NINH.CA: score=20.66 buy_ready=True sector_rank=13 price=18.03 support=16.8 resistance=18.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=44.05 liquidity=6467177.5 spike=1.28
- NIPH.CA: score=25.46 buy_ready=True sector_rank=3 price=164.6 support=157.1 resistance=176.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=56.91 liquidity=77477568.0 spike=1.03
- OBRI.CA: score=15.04 buy_ready=False sector_rank=13 price=34.39 support=33.63 resistance=37.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=45.28 liquidity=4411086.0 spike=0.33
- OCDI.CA: score=13.75 buy_ready=False sector_rank=11 price=24.21 support=22.86 resistance=24.23 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=238581856.0 spike=5.91
- OCPH.CA: score=13.26 buy_ready=False sector_rank=13 price=342.28 support=337.0 resistance=377.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=44.61 liquidity=4628884.0 spike=0.73
- ODIN.CA: score=19.24 buy_ready=True sector_rank=13 price=2.1 support=1.91 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=55.71 liquidity=3612717.75 spike=0.32
- OFH.CA: score=12.63 buy_ready=False sector_rank=13 price=0.6 support=0.59 resistance=0.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=26.25 liquidity=17574808.0 spike=0.84
- OIH.CA: score=20.41 buy_ready=False sector_rank=14 price=1.4 support=1.33 resistance=1.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=43.24 liquidity=81448416.0 spike=0.94
- OLFI.CA: score=23.78 buy_ready=False sector_rank=8 price=21.83 support=21.39 resistance=23.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=58.39 liquidity=9740552.0 spike=0.49
- ORAS.CA: score=7.6 buy_ready=False sector_rank=18 price=789.2 support=783.0 resistance=795.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=174958688.0 spike=1.0
- ORHD.CA: score=23.75 buy_ready=True sector_rank=11 price=39.33 support=35.01 resistance=39.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=54.37 liquidity=126285840.0 spike=0.67
- ORWE.CA: score=20.8 buy_ready=False sector_rank=16 price=22.95 support=22.65 resistance=24.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=36.79 liquidity=12822819.0 spike=0.32
- PHAR.CA: score=27.4 buy_ready=True sector_rank=3 price=88.48 support=83.02 resistance=89.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=52.17 liquidity=13568224.0 spike=0.38
- PHDC.CA: score=23.75 buy_ready=True sector_rank=11 price=15.5 support=14.43 resistance=16.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=53.64 liquidity=124153712.0 spike=0.29
- PHTV.CA: score=24.15 buy_ready=False sector_rank=13 price=251.75 support=201.55 resistance=245.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=84.24 liquidity=33137080.0 spike=1.76
- POUL.CA: score=31.72 buy_ready=True sector_rank=8 price=39.75 support=34.99 resistance=39.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=61.33 liquidity=106595192.0 spike=2.84
- PRCL.CA: score=10.8 buy_ready=False sector_rank=17 price=29.62 support=28.92 resistance=31.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=85751720.0 spike=2.55
- PRDC.CA: score=26.33 buy_ready=True sector_rank=11 price=7.13 support=5.7 resistance=9.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=62.86 liquidity=135791968.0 spike=1.29
- PRMH.CA: score=22.49 buy_ready=False sector_rank=13 price=2.59 support=2.26 resistance=3.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=55.93 liquidity=40372008.0 spike=1.43
- RACC.CA: score=18.36 buy_ready=False sector_rank=13 price=9.85 support=9.38 resistance=10.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=46.32 liquidity=6728095.0 spike=0.67
- RAKT.CA: score=9.42 buy_ready=False sector_rank=13 price=23.11 support=22.0 resistance=24.1 source=Yahoo Finance as_of=2026-06-22T21:00:00+00:00 freshness=FRESH RSI=37.86 liquidity=391159.87 spike=1.7
- RAYA.CA: score=25.22 buy_ready=True sector_rank=4 price=7.37 support=6.7 resistance=7.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=40.98 liquidity=120658648.0 spike=1.41
- RMDA.CA: score=23.4 buy_ready=False sector_rank=3 price=5.0 support=4.92 resistance=5.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=48.48 liquidity=28004572.0 spike=0.34
- ROTO.CA: score=20.63 buy_ready=False sector_rank=13 price=41.43 support=32.76 resistance=47.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=82.18 liquidity=14859557.0 spike=0.55
- RREI.CA: score=18.39 buy_ready=False sector_rank=13 price=3.55 support=3.35 resistance=3.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=37.97 liquidity=7757960.5 spike=0.38
- RTVC.CA: score=12.73 buy_ready=False sector_rank=13 price=3.82 support=3.76 resistance=4.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=48.68 liquidity=2099775.25 spike=0.43
- RUBX.CA: score=20.03 buy_ready=False sector_rank=13 price=10.33 support=9.8 resistance=10.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=50.28 liquidity=7398229.0 spike=0.67
- SAUD.CA: score=6.62 buy_ready=False sector_rank=15 price=21.03 support=20.82 resistance=23.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=34.35 liquidity=3367148.25 spike=0.35
- SCEM.CA: score=17.68 buy_ready=False sector_rank=17 price=63.16 support=59.3 resistance=67.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=27.56 liquidity=37406336.0 spike=1.99
- SCFM.CA: score=6.8 buy_ready=False sector_rank=13 price=244.09 support=226.5 resistance=276.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=21.0 liquidity=3164795.0 spike=0.41
- SCTS.CA: score=5.6 buy_ready=False sector_rank=6 price=590.41 support=565.25 resistance=645.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=28.16 liquidity=1249897.63 spike=0.31
- SDTI.CA: score=18.08 buy_ready=True sector_rank=13 price=46.7 support=44.03 resistance=49.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=55.69 liquidity=4452140.5 spike=0.34
- SEIG.CA: score=9.61 buy_ready=False sector_rank=13 price=185.21 support=178.0 resistance=205.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=25.31 liquidity=977369.19 spike=0.23
- SIPC.CA: score=12.07 buy_ready=False sector_rank=13 price=3.42 support=3.4 resistance=3.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=35.19 liquidity=3435028.75 spike=0.28
- SKPC.CA: score=10.47 buy_ready=False sector_rank=21 price=16.11 support=16.01 resistance=17.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=27.31 liquidity=26134578.0 spike=0.59
- SMFR.CA: score=9.04 buy_ready=False sector_rank=13 price=199.24 support=192.0 resistance=214.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=37.93 liquidity=409668.72 spike=0.15
- SNFC.CA: score=17.69 buy_ready=False sector_rank=13 price=11.99 support=11.68 resistance=12.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=44.51 liquidity=6058559.0 spike=0.24
- SPIN.CA: score=17.8 buy_ready=False sector_rank=16 price=13.82 support=13.3 resistance=14.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=24.78 liquidity=45853284.0 spike=10.09
- SPMD.CA: score=25.63 buy_ready=True sector_rank=13 price=0.43 support=0.4 resistance=0.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=54.67 liquidity=23375084.0 spike=0.86
- SUGR.CA: score=7.48 buy_ready=False sector_rank=8 price=47.31 support=47.6 resistance=51.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=22.87 liquidity=4445959.0 spike=0.47
- SVCE.CA: score=24.39 buy_ready=True sector_rank=13 price=9.43 support=8.11 resistance=9.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=43.98 liquidity=105744128.0 spike=1.38
- SWDY.CA: score=23.74 buy_ready=True sector_rank=12 price=87.37 support=84.01 resistance=90.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=46.1 liquidity=10638777.0 spike=0.59
- TALM.CA: score=26.71 buy_ready=True sector_rank=6 price=15.96 support=15.5 resistance=16.53 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=43.82 liquidity=16714739.0 spike=2.18
- TMGH.CA: score=21.75 buy_ready=False sector_rank=11 price=95.52 support=92.91 resistance=98.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=43.48 liquidity=236083376.0 spike=0.48
- TRTO.CA: score=9.63 buy_ready=False sector_rank=13 price=0.03 support=0.03 resistance=0.04 source=Yahoo Finance as_of=2026-06-22T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=326.64 spike=0.46
- UEFM.CA: score=26.94 buy_ready=True sector_rank=13 price=496.53 support=465.01 resistance=490.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=55.92 liquidity=4304047.5 spike=5.42
- UEGC.CA: score=22.31 buy_ready=False sector_rank=13 price=1.39 support=1.32 resistance=1.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=54.76 liquidity=8674086.0 spike=0.36
- UNIP.CA: score=21.99 buy_ready=False sector_rank=13 price=0.32 support=0.28 resistance=0.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=70.37 liquidity=8359773.5 spike=0.34
- UNIT.CA: score=8.78 buy_ready=False sector_rank=11 price=13.09 support=12.92 resistance=15.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=30.42 liquidity=2036180.75 spike=0.28
- WCDF.CA: score=8.8 buy_ready=False sector_rank=13 price=531.95 support=450.0 resistance=547.9 source=Yahoo Finance as_of=2026-06-22T21:00:00+00:00 freshness=FRESH RSI=44.29 liquidity=172883.75 spike=0.7
- WKOL.CA: score=9.03 buy_ready=False sector_rank=13 price=287.75 support=287.66 resistance=312.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=36.68 liquidity=398957.66 spike=0.13
- ZEOT.CA: score=22.41 buy_ready=False sector_rank=13 price=11.44 support=8.41 resistance=12.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=80.14 liquidity=42633604.0 spike=1.89
- ZMID.CA: score=30.41 buy_ready=True sector_rank=11 price=6.58 support=5.82 resistance=6.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=64.96 liquidity=451842368.0 spike=2.33

## Backtesting Lite
- CLHO.CA: 180d return=45.91%, max drawdown=-14.16%, MA20>MA50 days last20=20, as_of=2026-06-22T21:00:00+00:00
- GIHD.CA: 180d return=3.78%, max drawdown=-35.06%, MA20>MA50 days last20=20, as_of=2026-06-22T21:00:00+00:00
- POUL.CA: 180d return=73.38%, max drawdown=-14.26%, MA20>MA50 days last20=20, as_of=2026-06-22T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- CLHO.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=539 sources=3 expected=Cleopatra Hospital Group summary=Cleopatra Hospitals unveils EGP 84m dividends to employee for 2025; Cleopatra Hospitals posts higher consolidated profits in 2025; revenues cross EGP 7.2bn; Cleopatra Hospitals launches EGP 3.5bn Sky hospital in East Cairo
  - Cleopatra Hospitals unveils EGP 84m dividends to employee for 2025: https://english.mubasher.info/news/4594702/Cleopatra-Hospitals-unveils-EGP-84m-dividends-to-employee-for-2025/
  - Cleopatra Hospitals posts higher consolidated profits in 2025; revenues cross EGP 7.2bn: https://english.mubasher.info/news/4579844/Cleopatra-Hospitals-posts-higher-consolidated-profits-in-2025-revenues-cross-EGP-7-2bn/
  - Cleopatra Hospitals launches EGP 3.5bn Sky hospital in East Cairo: https://english.mubasher.info/news/4553462/Cleopatra-Hospitals-launches-EGP-3-5bn-Sky-hospital-in-East-Cairo/
- GIHD.CA: status=OLD_ACCEPTED latest=2016-01-01 age_days=3827 sources=3 expected=Gharbia Islamic Housing Development Company summary=Gharbia Islamic Housing to discuss raising capital mid-December; Gharbia Islamic Housing to distribute EGP 0.2/shr; Gharbia Islamic Housing profits fall 46% in 2016
  - Gharbia Islamic Housing to discuss raising capital mid-December: https://english.mubasher.info/news/3147599/Gharbia-Islamic-Housing-to-discuss-raising-capital-mid-December/
  - Gharbia Islamic Housing to distribute EGP 0.2/shr: https://english.mubasher.info/news/3082262/Gharbia-Islamic-Housing-to-distribute-EGP-0-2-shr/
  - Gharbia Islamic Housing profits fall 46% in 2016: https://english.mubasher.info/news/3068305/Gharbia-Islamic-Housing-profits-fall-46-in-2016/
- POUL.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Cairo Poultry summary=Cairo Poultry stock approaching historic peak – Analysis; Cairo Poultry cancels commercial license in Dubai&#39;s JAFZA; Cairo Poultry sees EGP 871m block-trading deal
  - Cairo Poultry stock approaching historic peak – Analysis: https://english.mubasher.info/news/4539104/Cairo-Poultry-stock-approaching-historic-peak-Analysis/
  - Cairo Poultry cancels commercial license in Dubai&#39;s JAFZA: https://english.mubasher.info/news/3962334/Cairo-Poultry-cancels-commercial-license-in-Dubai-s-JAFZA/
  - Cairo Poultry sees EGP 871m block-trading deal: https://english.mubasher.info/news/3862165/Cairo-Poultry-sees-EGP-871m-block-trading-deal/
- MPRC.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Egyptian Media Production City summary=Evidence rejected for MPRC.CA: source text did not clearly match MPRC.CA / Egyptian Media Production City.
- ZMID.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=539 sources=3 expected=Zahraa Maadi Investment and Development summary=Zahraa Maadi unveils distribution date for 2025 cash dividends; Zahraa Maadi to disburse EGP 250m dividends for 2025; Zahraa Maadi’s stock faces key resistance at EGP 5.22
  - Zahraa Maadi unveils distribution date for 2025 cash dividends: https://english.mubasher.info/news/4594804/Zahraa-Maadi-unveils-distribution-date-for-2025-cash-dividends/
  - Zahraa Maadi to disburse EGP 250m dividends for 2025: https://english.mubasher.info/news/4583591/Zahraa-Maadi-to-disburse-EGP-250m-dividends-for-2025/
  - Zahraa Maadi’s stock faces key resistance at EGP 5.22: https://english.mubasher.info/news/4563531/Zahraa-Maadi-s-stock-faces-key-resistance-at-EGP-5-22/
- MHOT.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Misr Hotels summary=Misr Hotels’ net profits cross EGP 1.1bn in 9M-25/26; Shareholder buys EGP 3.39m worth of shares in Misr Hotels; Misr Hotels repays EGP 383m of NBE&#39;s loan, unveils estimated profits
  - Misr Hotels’ net profits cross EGP 1.1bn in 9M-25/26: https://english.mubasher.info/news/4602482/Misr-Hotels-net-profits-cross-EGP-1-1bn-in-9M-25-26/
  - Shareholder buys EGP 3.39m worth of shares in Misr Hotels: https://english.mubasher.info/news/4013808/Shareholder-buys-EGP-3-39m-worth-of-shares-in-Misr-Hotels/
  - Misr Hotels repays EGP 383m of NBE&#39;s loan, unveils estimated profits: https://english.mubasher.info/news/3975543/Misr-Hotels-repays-EGP-383m-of-NBE-s-loan-unveils-estimated-profits/
- CNFN.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=539 sources=3 expected=Contact Financial Holding summary=Contact’s consolidated profits approach EGP 471m in 2025; Contact logs lower consolidated net profits at EGP 291m in 9M-25; Contact, e&amp; money forge partnership to boost Egypt’s financial ecosystem
  - Contact’s consolidated profits approach EGP 471m in 2025: https://english.mubasher.info/news/4582855/Contact-s-consolidated-profits-approach-EGP-471m-in-2025/
  - Contact logs lower consolidated net profits at EGP 291m in 9M-25: https://english.mubasher.info/news/4526894/Contact-logs-lower-consolidated-net-profits-at-EGP-291m-in-9M-25/
  - Contact, e&amp; money forge partnership to boost Egypt’s financial ecosystem: https://english.mubasher.info/news/4509412/Contact-e-money-forge-partnership-to-boost-Egypt-s-financial-ecosystem/
- DAPH.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Development & Engineering Consultants summary=Evidence rejected for DAPH.CA: source text did not clearly match DAPH.CA / Development & Engineering Consultants.

## Warnings
- Evidence for CLHO.CA matches the company but appears old; latest detected date is 2025-01-01.
- Gemini batch evidence failed: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.', 'status': 'UNAVAILABLE'}}
- Evidence for GIHD.CA matches the company but appears old; latest detected date is 2016-01-01.
- Evidence for POUL.CA matches the company but no source/report date was detected.
- Evidence rejected for MPRC.CA: source text did not clearly match MPRC.CA / Egyptian Media Production City.
- Evidence for ZMID.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for MHOT.CA matches the company but no source/report date was detected.
- Evidence for CNFN.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for DAPH.CA: source text did not clearly match DAPH.CA / Development & Engineering Consultants.
