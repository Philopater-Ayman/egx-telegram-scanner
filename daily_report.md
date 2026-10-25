# Telegram-First EGX Scanner Report

Scan phase: Post-close tomorrow tickets
Generated UTC: 2026-10-25T16:40:18.507815+00:00
Generated Cairo: 2026-10-25 19:40
Run timing: target 15:30 Cairo | generated Cairo 2026-10-25 19:40 | cron 30 12 * * 0-4
Trigger: scheduled cron=30 12 * * 0-4 mapped to post_close; Cairo now 2026-10-25 19:37

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 4
- Tradeable price/liquidity tickers: 49/186
- Top sector: Telecommunications

## Market Context
- Market trend: Bearish
- Source: Mubasher EGX market page (delayed public data)
- As of: Sunday, October 25
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 20.0% / above MA50 13.33%
- EGX70 regime: BEARISH / above MA20 0.0% / above MA50 16.67%
- Sector breadth: 4.76%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- CCAP.CA: liquidity=439987424.0 spike=0.83 score=10.84
- ETEL.CA: liquidity=399861184.0 spike=1.68 score=10.45
- COMI.CA: liquidity=227167344.0 spike=0.5 score=15.45
- TMGH.CA: liquidity=213575696.0 spike=0.82 score=15.49
- BTFH.CA: liquidity=179320704.0 spike=1.84 score=6.27

## AI Narrative
- Provider: OpenRouter ERROR
- Model: openai/gpt-oss-120b:free
- Summary: OpenRouter narrative failed; local scanner summary used.

## Top Liquidity Spikes
- EOSB.CA: spike=12.4 liquidity=443913.56 outlook=CONSTRUCTIVE score=61.42 buy_ready=False
- ELNA.CA: spike=11.15 liquidity=3093643.5 outlook=BULLISH_WATCH score=90.42 buy_ready=False
- SCTS.CA: spike=9.34 liquidity=18323180.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- CPCI.CA: spike=2.56 liquidity=11860184.0 outlook=BULLISH_WATCH score=70.42 buy_ready=False
- ADIB.CA: spike=2.39 liquidity=172919088.0 outlook=WEAK_OR_RISKY score=29.13 buy_ready=False

## Sector Leaderboard
- #1 Telecommunications: score=5.22 5d=1.25% 20d=0.17% aboveMA50=50.0%
- #2 Basic Resources & Chemicals: score=2.75 5d=0.0% 20d=0.0% aboveMA50=20.0%
- #3 Investment Holding: score=2.09 5d=0.0% 20d=0.0% aboveMA50=33.33%
- #4 Energy & Petrochemicals: score=2.08 5d=0.0% 20d=0.0% aboveMA50=33.33%
- #5 Industrial Goods & Construction: score=1.5 5d=0.0% 20d=0.0% aboveMA50=0.0%
- #6 Non-bank Financial Services: score=1.47 5d=0.0% 20d=0.0% aboveMA50=0.0%
- #7 General / Verified EGX Expansion: score=1.42 5d=0.0% 20d=0.0% aboveMA50=4.95%
- #8 Food, Beverages & Tobacco: score=1.39 5d=0.0% 20d=0.0% aboveMA50=0.0%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- MFPC.CA: BULLISH_WATCH score=93.75 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=No major short-term scanner risk flags.
- ELNA.CA: BULLISH_WATCH score=90.42 liquidity=TRADEABLE sector=IMPROVING risk=No major short-term scanner risk flags.
- ABUK.CA: BULLISH_WATCH score=87.75 liquidity=TRADEABLE sector=LEADING risk=No major short-term scanner risk flags.
- SDTI.CA: BULLISH_WATCH score=76.42 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=below MA20
- CPCI.CA: BULLISH_WATCH score=70.42 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=below MA20
- AMOC.CA: CONSTRUCTIVE score=65.08 liquidity=TRADEABLE sector=IMPROVING risk=below MA20
- EOSB.CA: CONSTRUCTIVE score=61.42 liquidity=THIN sector=IMPROVING risk=liquidity below minimum
- BINV.CA: NEUTRAL score=48.09 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; below MA20; overheated RSI
- EAST.CA: NEUTRAL score=45.39 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; below MA50; sector is not leading
- EGSA.CA: NEUTRAL score=44.22 liquidity=THIN sector=LEADING risk=liquidity below minimum; liquidity is cooling; momentum is extended; close to resistance

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- EKHO.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ARVA.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- GTWL.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=1.03 buy_ready=False sector_rank=7 price=193.56 support=192.0 resistance=223.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=6458457.0 spike=0.67
- ABUK.CA: score=24.58 buy_ready=False sector_rank=2 price=90.32 support=80.5 resistance=95.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=58.15 liquidity=95404672.0 spike=1.24
- ACAMD.CA: score=15.57 buy_ready=False sector_rank=7 price=1.92 support=1.87 resistance=2.16 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=48.84 liquidity=39082140.0 spike=0.83
- ACGC.CA: score=4.11 buy_ready=False sector_rank=16 price=12.36 support=12.5 resistance=14.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=27.91 liquidity=4805362.0 spike=0.43
- ADCI.CA: score=-4.03 buy_ready=False sector_rank=7 price=232.36 support=230.0 resistance=254.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=1404770.25 spike=0.88
- ADIB.CA: score=12.23 buy_ready=False sector_rank=12 price=45.99 support=43.45 resistance=51.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=33.8 liquidity=172919088.0 spike=2.39
- ADPC.CA: score=5.71 buy_ready=False sector_rank=7 price=2.64 support=2.53 resistance=2.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=16843660.0 spike=1.57
- AFDI.CA: score=-2.28 buy_ready=False sector_rank=7 price=38.13 support=38.01 resistance=43.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=3149060.0 spike=0.7
- AFMC.CA: score=0.55 buy_ready=False sector_rank=7 price=100.93 support=98.0 resistance=116.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=5977129.5 spike=0.33
- AJWA.CA: score=4.57 buy_ready=False sector_rank=7 price=201.29 support=191.0 resistance=221.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=32111608.0 spike=0.91
- ALCN.CA: score=14.28 buy_ready=False sector_rank=17 price=31.99 support=30.19 resistance=36.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=43.79 liquidity=21788760.0 spike=0.98
- ALUM.CA: score=-0.67 buy_ready=False sector_rank=7 price=16.37 support=16.1 resistance=20.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=4464986.0 spike=1.15
- AMER.CA: score=4.49 buy_ready=False sector_rank=10 price=3.42 support=3.4 resistance=4.06 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=30325522.0 spike=0.58
- AMES.CA: score=4.57 buy_ready=False sector_rank=7 price=29.21 support=29.0 resistance=33.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=26685590.0 spike=0.44
- AMIA.CA: score=4.57 buy_ready=False sector_rank=7 price=16.0 support=15.33 resistance=17.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=12599071.0 spike=0.76
- AMOC.CA: score=17.83 buy_ready=False sector_rank=4 price=13.02 support=12.18 resistance=14.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=41.72 liquidity=111901848.0 spike=0.88
- APSW.CA: score=4.0 buy_ready=False sector_rank=7 price=7.47 support=7.61 resistance=8.92 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:09 PM market time freshness=DELAYED_CURRENT RSI=36.02 liquidity=431389.13 spike=0.74
- ARAB.CA: score=4.49 buy_ready=False sector_rank=10 price=0.21 support=0.2 resistance=0.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=89598544.0 spike=0.82
- ARCC.CA: score=4.36 buy_ready=False sector_rank=15 price=59.8 support=58.12 resistance=65.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=30329642.0 spike=0.7
- AREH.CA: score=3.37 buy_ready=False sector_rank=7 price=0.97 support=0.94 resistance=1.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=8645311.0 spike=1.08
- ASCM.CA: score=4.05 buy_ready=False sector_rank=7 price=40.04 support=40.0 resistance=46.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=9483198.0 spike=1.0
- ASPI.CA: score=4.57 buy_ready=False sector_rank=7 price=0.27 support=0.27 resistance=0.31 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=16106036.0 spike=0.78
- ATLC.CA: score=2.11 buy_ready=False sector_rank=6 price=4.12 support=4.06 resistance=4.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=7523835.0 spike=0.99
- ATQA.CA: score=7.1 buy_ready=False sector_rank=2 price=8.86 support=8.43 resistance=10.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=35864800.0 spike=0.63
- AXPH.CA: score=3.57 buy_ready=False sector_rank=7 price=1172.99 support=1135.0 resistance=1260.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=8303287.0 spike=1.35
- BINV.CA: score=13.28 buy_ready=False sector_rank=3 price=57.46 support=52.11 resistance=65.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:08 PM market time freshness=DELAYED_CURRENT RSI=37.96 liquidity=4441112.0 spike=0.31
- BIOC.CA: score=4.57 buy_ready=False sector_rank=7 price=218.14 support=213.0 resistance=261.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=22149838.0 spike=0.2
- BTFH.CA: score=6.27 buy_ready=False sector_rank=6 price=2.13 support=2.05 resistance=2.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=179320704.0 spike=1.84
- CAED.CA: score=0.83 buy_ready=False sector_rank=7 price=70.79 support=70.0 resistance=85.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=6263281.0 spike=0.76
- CANA.CA: score=2.74 buy_ready=False sector_rank=12 price=39.92 support=39.24 resistance=42.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=8292934.0 spike=0.46
- CCAP.CA: score=10.84 buy_ready=False sector_rank=3 price=6.21 support=5.87 resistance=7.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=34.29 liquidity=439987424.0 spike=0.83
- CCRS.CA: score=0.69 buy_ready=False sector_rank=7 price=1.56 support=1.54 resistance=1.92 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=6118802.5 spike=0.9
- CEFM.CA: score=-4.34 buy_ready=False sector_rank=7 price=111.06 support=103.05 resistance=125.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=1087038.5 spike=0.52
- CERA.CA: score=4.57 buy_ready=False sector_rank=7 price=1.01 support=1.01 resistance=1.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=89310376.0 spike=0.71
- CFGH.CA: score=-5.13 buy_ready=False sector_rank=7 price=0.1 support=0.1 resistance=0.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=6460.51 spike=1.15
- CICH.CA: score=-3.15 buy_ready=False sector_rank=6 price=10.24 support=10.15 resistance=10.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=2258857.25 spike=0.98
- CIEB.CA: score=1.77 buy_ready=False sector_rank=12 price=21.41 support=21.4 resistance=22.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=7318167.0 spike=0.81
- CIRA.CA: score=4.41 buy_ready=False sector_rank=14 price=33.26 support=32.01 resistance=36.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=12176322.0 spike=0.69
- CLHO.CA: score=8.54 buy_ready=False sector_rank=9 price=13.28 support=13.0 resistance=16.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=15.19 liquidity=36056376.0 spike=0.99
- CNFN.CA: score=2.79 buy_ready=False sector_rank=6 price=3.53 support=3.5 resistance=4.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=8204556.5 spike=0.86
- COMI.CA: score=15.45 buy_ready=False sector_rank=12 price=122.01 support=120.0 resistance=130.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=43.17 liquidity=227167344.0 spike=0.5
- COPR.CA: score=4.57 buy_ready=False sector_rank=7 price=0.36 support=0.33 resistance=0.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=13364380.0 spike=0.79
- COSG.CA: score=4.67 buy_ready=False sector_rank=7 price=1.15 support=1.11 resistance=1.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=12659583.0 spike=1.05
- CPCI.CA: score=20.69 buy_ready=False sector_rank=7 price=579.75 support=502.25 resistance=619.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=47.27 liquidity=11860184.0 spike=2.56
- CSAG.CA: score=3.66 buy_ready=False sector_rank=17 price=30.32 support=30.1 resistance=34.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=8775476.0 spike=1.3
- DAPH.CA: score=4.57 buy_ready=False sector_rank=7 price=66.12 support=65.2 resistance=80.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=19786598.0 spike=0.47
- DEIN.CA: score=7.57 buy_ready=False sector_rank=7 price=10.35 support=10.35 resistance=12.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 09:54 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=37.26 spike=0.01
- DOMT.CA: score=-3.19 buy_ready=False sector_rank=8 price=20.47 support=20.27 resistance=22.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=2258518.5 spike=0.64
- DSCW.CA: score=4.65 buy_ready=False sector_rank=7 price=1.4 support=1.23 resistance=1.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=16883232.0 spike=1.04
- DTPP.CA: score=4.57 buy_ready=False sector_rank=7 price=42.02 support=41.81 resistance=51.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=29242752.0 spike=0.67
- EALR.CA: score=-2.88 buy_ready=False sector_rank=7 price=243.16 support=240.0 resistance=283.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=2556349.75 spike=0.74
- EASB.CA: score=-2.34 buy_ready=False sector_rank=7 price=5.21 support=5.03 resistance=6.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=3089164.75 spike=0.63
- EAST.CA: score=17.56 buy_ready=False sector_rank=8 price=29.99 support=27.01 resistance=32.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=57.0 liquidity=29515014.0 spike=0.67
- EBSC.CA: score=-0.53 buy_ready=False sector_rank=7 price=1.27 support=1.25 resistance=1.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=3486983.25 spike=1.71
- ECAP.CA: score=-2.85 buy_ready=False sector_rank=7 price=25.5 support=25.0 resistance=27.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=2580181.0 spike=0.69
- EDFM.CA: score=0.14 buy_ready=False sector_rank=7 price=375.69 support=335.2 resistance=425.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=34.92 liquidity=568979.19 spike=0.51
- EEII.CA: score=0.17 buy_ready=False sector_rank=7 price=1.52 support=1.5 resistance=1.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=5599654.5 spike=0.77
- EFIC.CA: score=7.1 buy_ready=False sector_rank=2 price=130.02 support=121.0 resistance=149.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=24420784.0 spike=0.83
- EFID.CA: score=4.56 buy_ready=False sector_rank=8 price=16.32 support=16.3 resistance=18.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=19469496.0 spike=0.45
- EFIH.CA: score=12.4 buy_ready=False sector_rank=20 price=20.82 support=20.2 resistance=25.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=37.5 liquidity=89487328.0 spike=1.41
- EGAL.CA: score=11.3 buy_ready=False sector_rank=2 price=291.68 support=275.0 resistance=362.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=28.15 liquidity=98272416.0 spike=1.1
- EGAS.CA: score=-0.18 buy_ready=False sector_rank=4 price=45.23 support=43.55 resistance=49.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=4983272.5 spike=0.7
- EGBE.CA: score=4.53 buy_ready=False sector_rank=12 price=0.48 support=0.5 resistance=0.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=35.14 liquidity=75501.77 spike=0.57
- EGCH.CA: score=7.1 buy_ready=False sector_rank=2 price=10.28 support=10.0 resistance=11.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=58483432.0 spike=0.83
- EGSA.CA: score=16.09 buy_ready=False sector_rank=1 price=9.03 support=8.75 resistance=9.09 source=Yahoo Finance as_of=2026-10-21T21:00:00+00:00 freshness=FRESH RSI=66.07 liquidity=3332.07 spike=0.57
- EGTS.CA: score=-0.62 buy_ready=False sector_rank=10 price=10.76 support=10.71 resistance=12.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=4887978.0 spike=0.19
- EHDR.CA: score=5.81 buy_ready=False sector_rank=7 price=1.84 support=1.8 resistance=2.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=16681744.0 spike=1.62
- ELEC.CA: score=3.77 buy_ready=False sector_rank=19 price=1.43 support=1.36 resistance=1.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=55259644.0 spike=1.1
- ELKA.CA: score=4.57 buy_ready=False sector_rank=7 price=1.24 support=1.23 resistance=1.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=11135251.0 spike=0.85
- ELNA.CA: score=21.66 buy_ready=False sector_rank=7 price=38.82 support=33.46 resistance=36.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=3093643.5 spike=11.15
- ELSH.CA: score=4.57 buy_ready=False sector_rank=7 price=8.71 support=8.6 resistance=10.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=17115798.0 spike=0.85
- ELWA.CA: score=8.83 buy_ready=False sector_rank=7 price=1.65 support=1.43 resistance=1.7 source=Yahoo Finance as_of=2026-10-21T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=261084.45 spike=0.72
- EMFD.CA: score=9.49 buy_ready=False sector_rank=10 price=11.54 support=11.2 resistance=13.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=26.2 liquidity=21331872.0 spike=0.35
- ENGC.CA: score=1.6 buy_ready=False sector_rank=7 price=28.16 support=28.12 resistance=31.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:10 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=7034984.5 spike=0.62
- EOSB.CA: score=17.01 buy_ready=False sector_rank=7 price=1.64 support=1.57 resistance=1.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=443913.56 spike=12.4
- EPCO.CA: score=-2.6 buy_ready=False sector_rank=7 price=7.26 support=7.0 resistance=8.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=2836126.25 spike=0.67
- EPPK.CA: score=-5.01 buy_ready=False sector_rank=7 price=10.29 support=10.29 resistance=10.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=8 September 01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=419183.72 spike=0.28
- ETEL.CA: score=10.45 buy_ready=False sector_rank=1 price=125.87 support=121.01 resistance=132.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=399861184.0 spike=1.68
- ETRS.CA: score=5.37 buy_ready=False sector_rank=7 price=9.59 support=9.51 resistance=10.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=14316720.0 spike=1.4
- EXPA.CA: score=4.45 buy_ready=False sector_rank=12 price=13.01 support=12.43 resistance=14.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=12107244.0 spike=0.31
- FAIT.CA: score=-1.93 buy_ready=False sector_rank=12 price=40.58 support=40.0 resistance=43.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=3377129.25 spike=1.12
- FAITA.CA: score=6.73 buy_ready=False sector_rank=12 price=0.98 support=0.98 resistance=1.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=57.84 liquidity=56507.8 spike=1.61
- FERC.CA: score=2.62 buy_ready=False sector_rank=2 price=56.1 support=53.57 resistance=63.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=4681800.5 spike=1.42
- FWRY.CA: score=11.64 buy_ready=False sector_rank=20 price=17.09 support=17.33 resistance=19.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=36.15 liquidity=115534296.0 spike=1.03
- GBCO.CA: score=7.36 buy_ready=False sector_rank=21 price=23.43 support=24.6 resistance=32.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=23.98 liquidity=166146640.0 spike=1.48
- GDWA.CA: score=4.57 buy_ready=False sector_rank=7 price=0.49 support=0.48 resistance=0.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=12348918.0 spike=0.78
- GGCC.CA: score=4.38 buy_ready=False sector_rank=7 price=0.51 support=0.5 resistance=0.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=9816796.0 spike=0.62
- GIHD.CA: score=4.57 buy_ready=False sector_rank=7 price=35.56 support=34.83 resistance=44.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=10830279.0 spike=0.57
- GMCI.CA: score=5.63 buy_ready=False sector_rank=7 price=1.54 support=1.47 resistance=1.77 source=Yahoo Finance as_of=2026-10-21T21:00:00+00:00 freshness=FRESH RSI=45.16 liquidity=59006.64 spike=0.18
- GRCA.CA: score=-2.96 buy_ready=False sector_rank=7 price=25.74 support=24.0 resistance=28.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=2471048.0 spike=0.46
- GSSC.CA: score=-4.76 buy_ready=False sector_rank=7 price=235.53 support=222.22 resistance=259.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=670999.63 spike=0.51
- HDBK.CA: score=6.71 buy_ready=False sector_rank=12 price=103.66 support=83.01 resistance=104.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=43183912.0 spike=2.13
- HELI.CA: score=6.11 buy_ready=False sector_rank=10 price=6.12 support=5.96 resistance=6.71 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=118616928.0 spike=1.81
- HRHO.CA: score=13.59 buy_ready=False sector_rank=6 price=23.99 support=22.81 resistance=27.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=51.87 liquidity=46131004.0 spike=0.36
- ICID.CA: score=3.36 buy_ready=False sector_rank=7 price=16.2 support=16.0 resistance=20.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=31.13 liquidity=3796548.5 spike=0.52
- IDRE.CA: score=3.69 buy_ready=False sector_rank=7 price=31.83 support=31.58 resistance=39.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=8259141.0 spike=1.43
- IFAP.CA: score=-1.49 buy_ready=False sector_rank=13 price=16.14 support=15.51 resistance=17.82 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=4078719.25 spike=0.74
- INFI.CA: score=4.57 buy_ready=False sector_rank=7 price=100.51 support=99.0 resistance=121.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=18873454.0 spike=0.9
- IRON.CA: score=16.1 buy_ready=False sector_rank=2 price=24.59 support=24.25 resistance=32.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=47.35 liquidity=10238054.0 spike=0.96
- ISMA.CA: score=-0.06 buy_ready=False sector_rank=7 price=16.31 support=16.3 resistance=20.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=5367769.0 spike=0.76
- ISMQ.CA: score=7.7 buy_ready=False sector_rank=2 price=6.17 support=6.0 resistance=7.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=22479536.0 spike=1.3
- ISPH.CA: score=5.54 buy_ready=False sector_rank=9 price=9.23 support=9.14 resistance=10.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=70260752.0 spike=1.5
- JUFO.CA: score=4.56 buy_ready=False sector_rank=8 price=21.08 support=21.01 resistance=23.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=11152959.0 spike=0.62
- KABO.CA: score=4.31 buy_ready=False sector_rank=16 price=6.17 support=6.02 resistance=7.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=11240457.0 spike=0.52
- KWIN.CA: score=-2.82 buy_ready=False sector_rank=7 price=49.38 support=48.5 resistance=60.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=2609399.5 spike=0.48
- KZPC.CA: score=0.24 buy_ready=False sector_rank=7 price=12.16 support=12.0 resistance=13.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=5667588.5 spike=0.67
- LCSW.CA: score=4.11 buy_ready=False sector_rank=15 price=31.54 support=28.0 resistance=33.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=9756325.0 spike=0.48
- LUTS.CA: score=4.65 buy_ready=False sector_rank=7 price=0.51 support=0.51 resistance=0.62 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=56118272.0 spike=1.04
- MAAL.CA: score=1.28 buy_ready=False sector_rank=7 price=5.26 support=5.26 resistance=6.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=6716020.5 spike=0.31
- MASR.CA: score=4.95 buy_ready=False sector_rank=7 price=5.9 support=5.6 resistance=6.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=58336264.0 spike=1.19
- MBSC.CA: score=4.36 buy_ready=False sector_rank=15 price=278.21 support=262.0 resistance=316.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=45752884.0 spike=0.48
- MCQE.CA: score=4.36 buy_ready=False sector_rank=15 price=146.25 support=145.05 resistance=164.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=52089064.0 spike=0.83
- MCRO.CA: score=4.57 buy_ready=False sector_rank=7 price=1.09 support=1.07 resistance=1.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=36743268.0 spike=0.78
- MENA.CA: score=-4.08 buy_ready=False sector_rank=10 price=5.59 support=5.58 resistance=5.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=1425947.75 spike=0.7
- MEPA.CA: score=0.59 buy_ready=False sector_rank=7 price=1.21 support=1.2 resistance=1.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=6024582.0 spike=0.83
- MFPC.CA: score=23.82 buy_ready=False sector_rank=2 price=46.24 support=40.66 resistance=48.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=49.02 liquidity=87665752.0 spike=1.86
- MFSC.CA: score=-3.64 buy_ready=False sector_rank=7 price=34.48 support=33.05 resistance=38.16 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=1793997.25 spike=0.77
- MHOT.CA: score=-3.74 buy_ready=False sector_rank=18 price=13.47 support=13.0 resistance=14.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=2182439.0 spike=0.13
- MICH.CA: score=1.05 buy_ready=False sector_rank=7 price=37.94 support=37.35 resistance=42.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=6484741.0 spike=0.76
- MILS.CA: score=5.51 buy_ready=False sector_rank=7 price=106.4 support=106.4 resistance=133.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=10941356.0 spike=1.47
- MIPH.CA: score=-4.25 buy_ready=False sector_rank=9 price=683.5 support=610.0 resistance=745.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=1205336.63 spike=0.29
- MOED.CA: score=5.95 buy_ready=False sector_rank=7 price=0.43 support=0.42 resistance=0.53 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=21855148.0 spike=1.69
- MOIL.CA: score=-0.0 buy_ready=False sector_rank=4 price=0.64 support=0.63 resistance=0.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=28.16 liquidity=165647.8 spike=0.72
- MOIN.CA: score=-1.74 buy_ready=False sector_rank=7 price=26.33 support=25.88 resistance=30.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=3690392.75 spike=0.37
- MOSC.CA: score=-4.31 buy_ready=False sector_rank=7 price=231.22 support=226.38 resistance=249.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=1123349.88 spike=0.33
- MPCI.CA: score=4.57 buy_ready=False sector_rank=7 price=251.65 support=239.0 resistance=295.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=45541764.0 spike=0.46
- MPCO.CA: score=4.43 buy_ready=False sector_rank=13 price=1.75 support=1.55 resistance=1.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=69085152.0 spike=0.7
- MPRC.CA: score=4.73 buy_ready=False sector_rank=7 price=28.04 support=27.1 resistance=33.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=17316336.0 spike=1.08
- MTIE.CA: score=2.4 buy_ready=False sector_rank=21 price=6.23 support=6.11 resistance=7.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=14202425.0 spike=0.71
- NAHO.CA: score=6.9 buy_ready=False sector_rank=7 price=0.13 support=0.12 resistance=0.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=33991.46 spike=2.15
- NCCW.CA: score=4.57 buy_ready=False sector_rank=7 price=4.29 support=4.21 resistance=5.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=13427574.0 spike=0.49
- NEDA.CA: score=1.74 buy_ready=False sector_rank=7 price=2.6 support=2.47 resistance=2.75 source=Yahoo Finance as_of=2026-10-21T21:00:00+00:00 freshness=FRESH RSI=0.0 liquidity=175562.39 spike=0.69
- NHPS.CA: score=0.24 buy_ready=False sector_rank=7 price=51.66 support=50.06 resistance=60.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=5675436.0 spike=0.57
- NINH.CA: score=1.82 buy_ready=False sector_rank=7 price=12.97 support=12.36 resistance=14.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=7256296.0 spike=0.65
- NIPH.CA: score=4.54 buy_ready=False sector_rank=9 price=228.22 support=220.0 resistance=266.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=98516824.0 spike=0.83
- OBRI.CA: score=4.57 buy_ready=False sector_rank=7 price=20.0 support=19.8 resistance=24.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=12358024.0 spike=0.85
- OCDI.CA: score=16.95 buy_ready=False sector_rank=10 price=23.72 support=22.6 resistance=28.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=38.56 liquidity=45709648.0 spike=1.23
- OCPH.CA: score=-0.86 buy_ready=False sector_rank=7 price=151.41 support=147.96 resistance=183.03 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=3892127.75 spike=1.34
- ODIN.CA: score=1.0 buy_ready=False sector_rank=7 price=1.85 support=1.8 resistance=2.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=6370403.0 spike=1.03
- OFH.CA: score=4.57 buy_ready=False sector_rank=7 price=0.65 support=0.63 resistance=0.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=18161872.0 spike=0.28
- OIH.CA: score=5.84 buy_ready=False sector_rank=3 price=1.65 support=1.64 resistance=1.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=49742752.0 spike=0.73
- OLFI.CA: score=7.89 buy_ready=False sector_rank=8 price=19.0 support=19.4 resistance=22.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=20.32 liquidity=9338280.0 spike=0.63
- ORAS.CA: score=4.6 buy_ready=False sector_rank=5 price=809.98 support=780.0 resistance=840.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=176169312.0 spike=1.0
- ORHD.CA: score=4.71 buy_ready=False sector_rank=10 price=9.3 support=8.5 resistance=9.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=134931024.0 spike=1.11
- ORWE.CA: score=4.31 buy_ready=False sector_rank=16 price=23.71 support=23.31 resistance=25.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=20882316.0 spike=0.5
- PHAR.CA: score=4.54 buy_ready=False sector_rank=9 price=94.52 support=91.61 resistance=101.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=46414952.0 spike=0.77
- PHDC.CA: score=15.49 buy_ready=False sector_rank=10 price=12.0 support=12.2 resistance=13.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=35.81 liquidity=89055272.0 spike=0.89
- PHTV.CA: score=-2.35 buy_ready=False sector_rank=7 price=306.01 support=305.0 resistance=326.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:09 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=1677593.63 spike=1.7
- POUL.CA: score=16.66 buy_ready=False sector_rank=8 price=9.45 support=9.12 resistance=38.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=37.4 liquidity=83023664.0 spike=1.55
- PRCL.CA: score=3.82 buy_ready=False sector_rank=15 price=17.53 support=17.25 resistance=21.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=9467286.0 spike=0.92
- PRDC.CA: score=4.49 buy_ready=False sector_rank=10 price=5.71 support=5.45 resistance=6.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=12017635.0 spike=0.33
- PRMH.CA: score=-3.62 buy_ready=False sector_rank=7 price=1.77 support=1.7 resistance=1.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=1812734.88 spike=0.57
- RACC.CA: score=-0.82 buy_ready=False sector_rank=7 price=7.32 support=7.13 resistance=8.16 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=4608421.0 spike=0.69
- RAKT.CA: score=9.86 buy_ready=False sector_rank=7 price=23.06 support=20.26 resistance=25.08 source=Yahoo Finance as_of=2026-10-21T21:00:00+00:00 freshness=FRESH RSI=66.11 liquidity=292631.39 spike=0.74
- RAYA.CA: score=4.49 buy_ready=False sector_rank=11 price=5.29 support=5.02 resistance=5.62 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=23942582.0 spike=0.82
- RMDA.CA: score=14.62 buy_ready=False sector_rank=9 price=4.95 support=4.8 resistance=5.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=35.1 liquidity=27866948.0 spike=1.04
- ROTO.CA: score=5.25 buy_ready=False sector_rank=7 price=26.69 support=25.0 resistance=31.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=11508482.0 spike=1.34
- RREI.CA: score=2.04 buy_ready=False sector_rank=7 price=2.44 support=2.42 resistance=3.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=7376367.5 spike=1.05
- RTVC.CA: score=-2.21 buy_ready=False sector_rank=7 price=3.04 support=3.04 resistance=3.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:45 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=2924114.0 spike=1.15
- RUBX.CA: score=4.57 buy_ready=False sector_rank=7 price=12.5 support=12.5 resistance=15.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=90292800.0 spike=0.97
- SAUD.CA: score=7.52 buy_ready=False sector_rank=12 price=20.04 support=20.2 resistance=24.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=31.68 liquidity=9071621.0 spike=0.7
- SCEM.CA: score=4.36 buy_ready=False sector_rank=15 price=76.36 support=75.11 resistance=83.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=23651188.0 spike=0.39
- SCFM.CA: score=-2.03 buy_ready=False sector_rank=7 price=186.74 support=182.0 resistance=222.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=2485544.75 spike=1.46
- SCTS.CA: score=9.41 buy_ready=False sector_rank=14 price=434.3 support=410.0 resistance=555.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=18323180.0 spike=9.34
- SDTI.CA: score=18.59 buy_ready=False sector_rank=7 price=81.83 support=76.1 resistance=94.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=43.63 liquidity=41534488.0 spike=1.51
- SEIG.CA: score=-3.7 buy_ready=False sector_rank=7 price=149.57 support=142.0 resistance=174.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=1734320.0 spike=0.85
- SIPC.CA: score=4.57 buy_ready=False sector_rank=7 price=4.04 support=4.04 resistance=4.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=34639856.0 spike=0.61
- SKPC.CA: score=11.1 buy_ready=False sector_rank=2 price=14.47 support=14.4 resistance=17.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=33.65 liquidity=38040592.0 spike=0.55
- SMFR.CA: score=-2.92 buy_ready=False sector_rank=7 price=175.5 support=173.0 resistance=197.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=2512142.75 spike=0.81
- SNFC.CA: score=9.86 buy_ready=False sector_rank=7 price=10.75 support=10.8 resistance=11.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=38.15 liquidity=6288872.5 spike=0.75
- SPIN.CA: score=-1.11 buy_ready=False sector_rank=16 price=13.15 support=12.9 resistance=14.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=4584043.0 spike=0.87
- SPMD.CA: score=1.12 buy_ready=False sector_rank=7 price=0.31 support=0.31 resistance=0.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=6551748.5 spike=0.54
- SUGR.CA: score=0.82 buy_ready=False sector_rank=8 price=51.0 support=50.6 resistance=54.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=6259138.5 spike=0.67
- SVCE.CA: score=4.57 buy_ready=False sector_rank=7 price=7.69 support=7.01 resistance=8.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=39172912.0 spike=0.56
- SWDY.CA: score=8.57 buy_ready=False sector_rank=19 price=101.73 support=101.5 resistance=124.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=28.2 liquidity=49062604.0 spike=0.75
- TALM.CA: score=9.41 buy_ready=False sector_rank=14 price=18.47 support=18.28 resistance=23.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=28.47 liquidity=19641908.0 spike=0.68
- TMGH.CA: score=15.49 buy_ready=False sector_rank=10 price=82.89 support=80.01 resistance=93.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=48.39 liquidity=213575696.0 spike=0.82
- TRTO.CA: score=0.34 buy_ready=False sector_rank=7 price=0.06 support=0.05 resistance=0.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=78.95 liquidity=9037.14 spike=1.38
- UEFM.CA: score=-4.59 buy_ready=False sector_rank=7 price=440.55 support=430.0 resistance=481.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=844174.69 spike=0.29
- UEGC.CA: score=4.57 buy_ready=False sector_rank=7 price=1.25 support=1.21 resistance=1.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=28553720.0 spike=0.63
- UNIP.CA: score=2.04 buy_ready=False sector_rank=7 price=0.26 support=0.26 resistance=0.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=7470099.5 spike=0.91
- UNIT.CA: score=-2.04 buy_ready=False sector_rank=10 price=15.5 support=15.06 resistance=16.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=3471111.5 spike=0.91
- WCDF.CA: score=-0.68 buy_ready=False sector_rank=7 price=477.22 support=432.5 resistance=686.53 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=17.19 liquidity=754735.13 spike=0.28
- WKOL.CA: score=0.83 buy_ready=False sector_rank=7 price=243.35 support=240.91 resistance=275.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=6264593.0 spike=0.85
- ZEOT.CA: score=1.79 buy_ready=False sector_rank=7 price=9.04 support=9.01 resistance=11.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=7221154.5 spike=0.92
- ZMID.CA: score=4.49 buy_ready=False sector_rank=10 price=6.13 support=6.01 resistance=6.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=54622764.0 spike=0.73

## Backtesting Lite
- ABUK.CA: 180d return=62.36%, max drawdown=-26.86%, MA20>MA50 days last20=20, as_of=2026-10-21T21:00:00+00:00
- MFPC.CA: 180d return=51.02%, max drawdown=-26.33%, MA20>MA50 days last20=20, as_of=2026-10-21T21:00:00+00:00
- ELNA.CA: 180d return=-1.83%, max drawdown=-15.86%, MA20>MA50 days last20=0, as_of=2026-10-21T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- ABUK.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Abu Qir Fertilizers summary=Abu Qir Fertilizers generates EGP 5.6bn net profits in Q1-26 unaudited results; Abu Qir Fertilizers&#39; board approves $5.6m coated urea project; Abu Qir Fertilizers&#39; profits exceed EGP 5.1bn in H1-25/26
  - Abu Qir Fertilizers generates EGP 5.6bn net profits in Q1-26 unaudited results: https://english.mubasher.info/news/4604919/Abu-Qir-Fertilizers-generates-EGP-5-6bn-net-profits-in-Q1-26-unaudited-results/
  - Abu Qir Fertilizers&#39; board approves $5.6m coated urea project: https://english.mubasher.info/news/4585599/Abu-Qir-Fertilizers-board-approves-5-6m-coated-urea-project/
  - Abu Qir Fertilizers&#39; profits exceed EGP 5.1bn in H1-25/26: https://english.mubasher.info/news/4554415/Abu-Qir-Fertilizers-profits-exceed-EGP-5-1bn-in-H1-25-26/
- MFPC.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Misr Fertilizers Production summary=Evidence rejected for MFPC.CA: source text did not clearly match MFPC.CA / Misr Fertilizers Production.
- ELNA.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=El Nasr Manufacturing Agricultural Crops S.A.E summary=Consortium offers to acquire controlling stake in El Nasr for Agricultural Crops; El Nasr for Agricultural Crops to sell Sohag factory land for EGP 650m; EGX halts trading on El Nasr for Manufacturing Agricultural Crops
  - Consortium offers to acquire controlling stake in El Nasr for Agricultural Crops: https://english.mubasher.info/news/3749421/Consortium-offers-to-acquire-controlling-stake-in-El-Nasr-for-Agricultural-Crops/
  - El Nasr for Agricultural Crops to sell Sohag factory land for EGP 650m: https://english.mubasher.info/news/3685533/El-Nasr-for-Agricultural-Crops-to-sell-Sohag-factory-land-for-EGP-650m/
  - EGX halts trading on El Nasr for Manufacturing Agricultural Crops: https://english.mubasher.info/news/3489525/EGX-halts-trading-on-El-Nasr-for-Manufacturing-Agricultural-Crops/
- CPCI.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Kahira Pharmaceuticals & Chemical Industries Company summary=Kahira Pharmaceuticals&#39; net profits up 22.5% in H1-21/22; Kahira Pharmaceuticals sees EGP 9m block trading deal; Adel Taha Abdel Wahab named Chairman of Kahira Pharmaceuticals
  - Kahira Pharmaceuticals&#39; net profits up 22.5% in H1-21/22: https://english.mubasher.info/news/3910780/Kahira-Pharmaceuticals-net-profits-up-22-5-in-H1-21-22/
  - Kahira Pharmaceuticals sees EGP 9m block trading deal: https://english.mubasher.info/news/3903033/Kahira-Pharmaceuticals-sees-EGP-9m-block-trading-deal/
  - Adel Taha Abdel Wahab named Chairman of Kahira Pharmaceuticals: https://english.mubasher.info/news/3816375/Adel-Taha-Abdel-Wahab-named-Chairman-of-Kahira-Pharmaceuticals/
- SDTI.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=SHARM DREAMS Co. for Touristic Investment S.A.E summary=Sharm Dreams stock maintains strong uptrend - Analysis; Sharm Dreams stock is experiencing sideways movement amid anticipation of next trend – Analysis; Sharm Dreams stock hits historic level halting driving buying force
  - Sharm Dreams stock maintains strong uptrend - Analysis: https://english.mubasher.info/news/4577977/Sharm-Dreams-stock-maintains-strong-uptrend-Analysis/
  - Sharm Dreams stock is experiencing sideways movement amid anticipation of next trend – Analysis: https://english.mubasher.info/news/4547831/Sharm-Dreams-stock-is-experiencing-sideways-movement-amid-anticipation-of-next-trend-Analysis/
  - Sharm Dreams stock hits historic level halting driving buying force: https://english.mubasher.info/news/4529096/Sharm-Dreams-stock-hits-historic-level-halting-driving-buying-force/
- AMOC.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Alexandria Mineral Oils summary=AMOC achieves EGP 10.5bn consolidated sales in Q1-26; AMOC studies potential project with Germany’s SULZER; AMOC to pay out EGP 0.4/shr dividends for H2-25
  - AMOC achieves EGP 10.5bn consolidated sales in Q1-26: https://english.mubasher.info/news/4604903/AMOC-achieves-EGP-10-5bn-consolidated-sales-in-Q1-26/
  - AMOC studies potential project with Germany’s SULZER: https://english.mubasher.info/news/4586853/AMOC-studies-potential-project-with-Germany-s-SULZER/
  - AMOC to pay out EGP 0.4/shr dividends for H2-25: https://english.mubasher.info/news/4586775/AMOC-to-pay-out-EGP-0-4-shr-dividends-for-H2-25/
- EAST.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Eastern Company summary=Evidence rejected for EAST.CA: source text did not clearly match EAST.CA / Eastern Company.
- EOSB.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=El Orouba Securities Brokerage summary=El Orouba Brokerage turns profitable in Q4; El Orouba Securities suffers 598,000 losses in Q3; El Orouba Securities H1 losses down 7%
  - El Orouba Brokerage turns profitable in Q4: https://english.mubasher.info/news/3067539/El-Orouba-Brokerage-turns-profitable-in-Q4/
  - El Orouba Securities suffers 598,000 losses in Q3: https://english.mubasher.info/news/3016624/El-Orouba-Securities-suffers-598-000-losses-in-Q3/
  - El Orouba Securities H1 losses down 7%: https://english.mubasher.info/news/2984110/El-Orouba-Securities-H1-losses-down-7-/

## Warnings
- OpenRouter API error: 404
- Evidence for ABUK.CA matches the company but no source/report date was detected.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence rejected for MFPC.CA: source text did not clearly match MFPC.CA / Misr Fertilizers Production.
- Evidence for ELNA.CA matches the company but no source/report date was detected.
- Evidence for CPCI.CA matches the company but no source/report date was detected.
- Evidence for SDTI.CA matches the company but no source/report date was detected.
- Evidence for AMOC.CA matches the company but no source/report date was detected.
- Evidence rejected for EAST.CA: source text did not clearly match EAST.CA / Eastern Company.
- Evidence for EOSB.CA matches the company but no source/report date was detected.
