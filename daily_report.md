# Telegram-First EGX Scanner Report

Scan phase: Pre-market risk check
Generated UTC: 2026-11-01T12:02:50.711315+00:00
Generated Cairo: 2026-11-01 14:02
Run timing: target 08:45 Cairo | generated Cairo 2026-11-01 14:02 | cron 45 5 * * 0-4
Trigger: scheduled cron=45 5 * * 0-4 mapped to pre_market; Cairo now 2026-11-01 14:00

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 5
- Tradeable price/liquidity tickers: 173/185
- Top sector: Tourism & Leisure

## Market Context
- Market trend: Bearish
- Source: Mubasher EGX market page (delayed public data)
- As of: Sunday, November 01
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 10.53% / above MA50 0.0%
- EGX70 regime: BEARISH / above MA20 8.11% / above MA50 5.41%
- Sector breadth: 0.0%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- AMOC.CA: liquidity=520581376.0 spike=3.91 score=24.22
- COMI.CA: liquidity=348198048.0 spike=0.68 score=14.78
- CCAP.CA: liquidity=286200864.0 spike=0.59 score=12.46
- TMGH.CA: liquidity=210827072.0 spike=0.82 score=12.3
- ORAS.CA: liquidity=147702512.0 spike=1.0 score=4.6

## AI Narrative
- Provider: OpenRouter ERROR
- Model: openai/gpt-oss-120b:free
- Summary: OpenRouter narrative failed; local scanner summary used.

## Top Liquidity Spikes
- MENA.CA: spike=12.39 liquidity=33222170.0 outlook=WEAK_OR_RISKY score=23 buy_ready=False
- SEIG.CA: spike=10.09 liquidity=24195224.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- AMOC.CA: spike=3.91 liquidity=520581376.0 outlook=BULLISH_WATCH score=81.54 buy_ready=False
- ELNA.CA: spike=3.3 liquidity=1724653.38 outlook=NEUTRAL score=48 buy_ready=False
- ISPH.CA: spike=2.79 liquidity=125323808.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False

## Sector Leaderboard
- #1 Tourism & Leisure: score=2.61 5d=4.37% 20d=-2.5% aboveMA50=0.0%
- #2 Building Materials: score=2.59 5d=-0.62% 20d=3.54% aboveMA50=16.67%
- #3 Banking & Financials: score=1.96 5d=0.09% 20d=-4.33% aboveMA50=20.0%
- #4 Fintech & Payments: score=1.61 5d=2.18% 20d=-1.99% aboveMA50=0.0%
- #5 Industrial Goods & Construction: score=1.5 5d=0.0% 20d=0.0% aboveMA50=0.0%
- #6 Healthcare: score=0.67 5d=0.85% 20d=-6.88% aboveMA50=0.0%
- #7 Energy & Petrochemicals: score=0.54 5d=-1.81% 20d=-7.8% aboveMA50=33.33%
- #8 Education: score=-0.06 5d=0.11% 20d=-5.72% aboveMA50=0.0%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- CANA.CA: BULLISH_WATCH score=96.96 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=far above support
- AMOC.CA: BULLISH_WATCH score=81.54 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=No major short-term scanner risk flags.
- LCSW.CA: BULLISH_WATCH score=80.59 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; far above support
- ADIB.CA: BULLISH_WATCH score=70.96 liquidity=TRADEABLE sector=LEADING risk=below MA50
- AJWA.CA: BULLISH_WATCH score=70 liquidity=TRADEABLE sector=LAGGING risk=sector is not leading
- CPCI.CA: CONSTRUCTIVE score=67 liquidity=TRADEABLE sector=LAGGING risk=liquidity is cooling; sector is not leading
- SCEM.CA: CONSTRUCTIVE score=65.59 liquidity=TRADEABLE sector=LEADING risk=below MA50
- SDTI.CA: CONSTRUCTIVE score=53 liquidity=TRADEABLE sector=LAGGING risk=liquidity is cooling; below MA20; sector is not leading
- ELNA.CA: NEUTRAL score=48 liquidity=TRADEABLE sector=LAGGING risk=overheated RSI; close to resistance; sector is not leading
- CIEB.CA: NEUTRAL score=47.96 liquidity=TRADEABLE sector=LEADING risk=below MA20; below MA50

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- EKHO.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ARVA.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- EDFM.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- GTWL.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=0.25 buy_ready=False sector_rank=16 price=215.43 support=171.02 resistance=275.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:44 PM market time freshness=DELAYED_CURRENT RSI=34.68 liquidity=2998598.5 spike=0.33
- ABUK.CA: score=13.19 buy_ready=False sector_rank=17 price=85.19 support=80.5 resistance=95.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:45 PM market time freshness=DELAYED_CURRENT RSI=51.35 liquidity=64737888.0 spike=0.77
- ACAMD.CA: score=12.25 buy_ready=False sector_rank=16 price=1.9 support=1.86 resistance=2.16 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:45 PM market time freshness=DELAYED_CURRENT RSI=44.44 liquidity=27555168.0 spike=0.63
- ACGC.CA: score=8.44 buy_ready=False sector_rank=12 price=13.06 support=11.6 resistance=14.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:45 PM market time freshness=DELAYED_CURRENT RSI=44.94 liquidity=4842044.0 spike=0.58
- ADCI.CA: score=13.58 buy_ready=False sector_rank=16 price=258.08 support=221.0 resistance=278.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:43 PM market time freshness=DELAYED_CURRENT RSI=51.17 liquidity=4809262.0 spike=2.76
- ADIB.CA: score=19.78 buy_ready=False sector_rank=3 price=47.32 support=43.16 resistance=50.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:44 PM market time freshness=DELAYED_CURRENT RSI=49.15 liquidity=64088356.0 spike=0.84
- ADPC.CA: score=3.77 buy_ready=False sector_rank=16 price=2.94 support=2.53 resistance=3.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:44 PM market time freshness=DELAYED_CURRENT RSI=35.22 liquidity=1519415.38 spike=0.16
- AFDI.CA: score=0.6 buy_ready=False sector_rank=16 price=43.0 support=34.8 resistance=54.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:43 PM market time freshness=DELAYED_CURRENT RSI=27.79 liquidity=2348846.25 spike=0.61
- AFMC.CA: score=13.69 buy_ready=False sector_rank=16 price=127.43 support=94.6 resistance=179.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:44 PM market time freshness=DELAYED_CURRENT RSI=36.49 liquidity=22849360.0 spike=1.22
- AJWA.CA: score=18.25 buy_ready=False sector_rank=16 price=206.5 support=179.0 resistance=229.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:45 PM market time freshness=DELAYED_CURRENT RSI=53.33 liquidity=28115284.0 spike=0.81
- ALCN.CA: score=8.07 buy_ready=False sector_rank=14 price=31.29 support=27.11 resistance=36.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:44 PM market time freshness=DELAYED_CURRENT RSI=43.01 liquidity=4726215.5 spike=0.25
- ALUM.CA: score=0.86 buy_ready=False sector_rank=16 price=18.38 support=16.02 resistance=25.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:45 PM market time freshness=DELAYED_CURRENT RSI=30.4 liquidity=3434819.25 spike=1.09
- AMER.CA: score=15.3 buy_ready=False sector_rank=15 price=4.24 support=3.21 resistance=5.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:45 PM market time freshness=DELAYED_CURRENT RSI=39.6 liquidity=19855486.0 spike=0.35
- AMES.CA: score=9.25 buy_ready=False sector_rank=16 price=32.44 support=28.0 resistance=51.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:46 PM market time freshness=DELAYED_CURRENT RSI=25.87 liquidity=17008544.0 spike=0.31
- AMIA.CA: score=7.63 buy_ready=False sector_rank=16 price=17.18 support=14.0 resistance=19.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:44 PM market time freshness=DELAYED_CURRENT RSI=38.11 liquidity=4385697.5 spike=0.28
- AMOC.CA: score=24.22 buy_ready=False sector_rank=7 price=14.32 support=12.55 resistance=14.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:45 PM market time freshness=DELAYED_CURRENT RSI=53.51 liquidity=520581376.0 spike=3.91
- APSW.CA: score=-2.43 buy_ready=False sector_rank=16 price=7.27 support=7.1 resistance=8.92 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=27.17 liquidity=321136.31 spike=0.52
- ARAB.CA: score=8.3 buy_ready=False sector_rank=15 price=0.23 support=0.2 resistance=0.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:45 PM market time freshness=DELAYED_CURRENT RSI=32.84 liquidity=69539616.0 spike=0.58
- ARCC.CA: score=17.04 buy_ready=False sector_rank=2 price=63.71 support=58.01 resistance=74.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:45 PM market time freshness=DELAYED_CURRENT RSI=35.86 liquidity=18827038.0 spike=0.43
- AREH.CA: score=0.96 buy_ready=False sector_rank=16 price=1.04 support=0.91 resistance=1.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:42 PM market time freshness=DELAYED_CURRENT RSI=34.55 liquidity=3715658.25 spike=0.47
- ASCM.CA: score=-0.2 buy_ready=False sector_rank=16 price=43.2 support=38.2 resistance=59.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:44 PM market time freshness=DELAYED_CURRENT RSI=27.14 liquidity=2549097.0 spike=0.31
- ASPI.CA: score=14.25 buy_ready=False sector_rank=16 price=0.29 support=0.27 resistance=0.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:46 PM market time freshness=DELAYED_CURRENT RSI=37.43 liquidity=10009773.0 spike=0.52
- ATLC.CA: score=4.15 buy_ready=False sector_rank=18 price=4.89 support=3.93 resistance=6.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:45 PM market time freshness=DELAYED_CURRENT RSI=35.32 liquidity=2184705.75 spike=0.3
- ATQA.CA: score=7.19 buy_ready=False sector_rank=17 price=8.97 support=8.25 resistance=12.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:46 PM market time freshness=DELAYED_CURRENT RSI=26.77 liquidity=20736682.0 spike=0.4
- AXPH.CA: score=10.4 buy_ready=False sector_rank=16 price=1338.27 support=1135.0 resistance=1550.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:43 PM market time freshness=DELAYED_CURRENT RSI=42.61 liquidity=5027376.5 spike=1.06
- BINV.CA: score=-0.84 buy_ready=False sector_rank=20 price=52.4 support=51.0 resistance=63.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:40 PM market time freshness=DELAYED_CURRENT RSI=31.17 liquidity=1698263.25 spike=0.14
- BIOC.CA: score=13.25 buy_ready=False sector_rank=16 price=280.97 support=212.05 resistance=380.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:45 PM market time freshness=DELAYED_CURRENT RSI=46.24 liquidity=49333004.0 spike=0.46
- BTFH.CA: score=11.97 buy_ready=False sector_rank=18 price=2.33 support=2.05 resistance=2.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:45 PM market time freshness=DELAYED_CURRENT RSI=36.51 liquidity=76862200.0 spike=0.67
- CAED.CA: score=4.04 buy_ready=False sector_rank=16 price=86.35 support=64.0 resistance=130.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:42 PM market time freshness=DELAYED_CURRENT RSI=34.07 liquidity=5793231.5 spike=0.61
- CANA.CA: score=26.92 buy_ready=False sector_rank=3 price=47.47 support=38.1 resistance=46.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:44 PM market time freshness=DELAYED_CURRENT RSI=58.17 liquidity=37418880.0 spike=2.07
- CCAP.CA: score=12.46 buy_ready=False sector_rank=20 price=5.97 support=5.8 resistance=6.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:45 PM market time freshness=DELAYED_CURRENT RSI=40.4 liquidity=286200864.0 spike=0.59
- CCRS.CA: score=2.97 buy_ready=False sector_rank=16 price=1.68 support=1.3 resistance=2.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:46 PM market time freshness=DELAYED_CURRENT RSI=28.23 liquidity=5725829.0 spike=0.86
- CEFM.CA: score=6.57 buy_ready=False sector_rank=16 price=113.5 support=97.79 resistance=140.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:43 PM market time freshness=DELAYED_CURRENT RSI=40.4 liquidity=2921016.5 spike=1.2
- CERA.CA: score=7.25 buy_ready=False sector_rank=16 price=1.04 support=0.93 resistance=1.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:46 PM market time freshness=DELAYED_CURRENT RSI=29.41 liquidity=38126088.0 spike=0.31
- CFGH.CA: score=-2.75 buy_ready=False sector_rank=16 price=0.1 support=0.1 resistance=0.12 source=Yahoo Finance as_of=2026-10-28T21:00:00+00:00 freshness=FRESH RSI=10.0 liquidity=0.0 spike=0.0
- CICH.CA: score=-1.86 buy_ready=False sector_rank=18 price=10.32 support=9.63 resistance=12.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:39 PM market time freshness=DELAYED_CURRENT RSI=32.64 liquidity=1176299.0 spike=0.67
- CIEB.CA: score=17.38 buy_ready=False sector_rank=3 price=22.81 support=21.35 resistance=24.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:44 PM market time freshness=DELAYED_CURRENT RSI=40.3 liquidity=10246016.0 spike=1.3
- CIRA.CA: score=13.98 buy_ready=False sector_rank=8 price=35.93 support=32.01 resistance=41.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:42 PM market time freshness=DELAYED_CURRENT RSI=43.83 liquidity=10924518.0 spike=0.69
- CLHO.CA: score=10.27 buy_ready=False sector_rank=6 price=13.14 support=12.51 resistance=16.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:45 PM market time freshness=DELAYED_CURRENT RSI=29.36 liquidity=23908690.0 spike=0.64
- CNFN.CA: score=4.38 buy_ready=False sector_rank=18 price=3.67 support=3.25 resistance=4.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:44 PM market time freshness=DELAYED_CURRENT RSI=38.5 liquidity=2415260.0 spike=0.26
- COMI.CA: score=14.78 buy_ready=False sector_rank=3 price=117.5 support=118.06 resistance=129.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:45 PM market time freshness=DELAYED_CURRENT RSI=45.51 liquidity=348198048.0 spike=0.68
- COPR.CA: score=5.91 buy_ready=False sector_rank=16 price=0.39 support=0.33 resistance=0.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:44 PM market time freshness=DELAYED_CURRENT RSI=31.47 liquidity=7660737.5 spike=0.48
- COSG.CA: score=2.74 buy_ready=False sector_rank=16 price=1.27 support=1.11 resistance=1.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:46 PM market time freshness=DELAYED_CURRENT RSI=33.33 liquidity=5491592.5 spike=0.52
- CPCI.CA: score=13.81 buy_ready=False sector_rank=16 price=602.68 support=502.25 resistance=620.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:45 PM market time freshness=DELAYED_CURRENT RSI=56.06 liquidity=3559897.25 spike=0.69
- CSAG.CA: score=7.28 buy_ready=False sector_rank=14 price=33.56 support=30.1 resistance=38.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:44 PM market time freshness=DELAYED_CURRENT RSI=39.67 liquidity=3937624.0 spike=0.6
- DAPH.CA: score=7.25 buy_ready=False sector_rank=16 price=81.01 support=65.2 resistance=114.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:44 PM market time freshness=DELAYED_CURRENT RSI=30.37 liquidity=11802071.0 spike=0.29
- DEIN.CA: score=6.25 buy_ready=False sector_rank=16 price=10.35 support=10.35 resistance=12.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=29 October 12:10 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=62.1 spike=0.02
- DOMT.CA: score=5.4 buy_ready=False sector_rank=9 price=22.85 support=20.27 resistance=25.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:45 PM market time freshness=DELAYED_CURRENT RSI=40.24 liquidity=468936.81 spike=0.16
- DSCW.CA: score=11.65 buy_ready=False sector_rank=16 price=1.48 support=1.23 resistance=1.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:45 PM market time freshness=DELAYED_CURRENT RSI=38.96 liquidity=7404960.5 spike=0.51
- DTPP.CA: score=4.79 buy_ready=False sector_rank=16 price=47.08 support=43.15 resistance=50.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:46 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=65235416.0 spike=1.77
- EALR.CA: score=-0.73 buy_ready=False sector_rank=16 price=258.29 support=236.01 resistance=355.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:44 PM market time freshness=DELAYED_CURRENT RSI=25.33 liquidity=2019845.38 spike=0.64
- EASB.CA: score=2.92 buy_ready=False sector_rank=16 price=6.05 support=5.03 resistance=8.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:41 PM market time freshness=DELAYED_CURRENT RSI=34.01 liquidity=4669447.5 spike=0.91
- EAST.CA: score=10.46 buy_ready=False sector_rank=9 price=31.56 support=27.01 resistance=32.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:42 PM market time freshness=DELAYED_CURRENT RSI=74.08 liquidity=3536046.0 spike=0.08
- EBSC.CA: score=5.76 buy_ready=False sector_rank=16 price=1.43 support=1.2 resistance=1.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:46 PM market time freshness=DELAYED_CURRENT RSI=36.0 liquidity=1508240.75 spike=0.6
- ECAP.CA: score=-1.31 buy_ready=False sector_rank=16 price=26.61 support=24.8 resistance=31.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:38 PM market time freshness=DELAYED_CURRENT RSI=31.17 liquidity=1438473.75 spike=0.44
- EEII.CA: score=3.77 buy_ready=False sector_rank=16 price=1.7 support=1.42 resistance=2.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:46 PM market time freshness=DELAYED_CURRENT RSI=26.37 liquidity=6526717.0 spike=0.98
- EFIC.CA: score=8.39 buy_ready=False sector_rank=17 price=137.26 support=121.0 resistance=178.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:45 PM market time freshness=DELAYED_CURRENT RSI=40.17 liquidity=6202841.5 spike=0.27
- EFID.CA: score=14.93 buy_ready=False sector_rank=9 price=17.8 support=16.01 resistance=19.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:45 PM market time freshness=DELAYED_CURRENT RSI=42.76 liquidity=19419840.0 spike=0.49
- EFIH.CA: score=14.64 buy_ready=False sector_rank=4 price=23.2 support=20.3 resistance=25.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:45 PM market time freshness=DELAYED_CURRENT RSI=41.27 liquidity=62595576.0 spike=0.96
- EGAL.CA: score=15.19 buy_ready=False sector_rank=17 price=302.95 support=275.0 resistance=359.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:45 PM market time freshness=DELAYED_CURRENT RSI=35.16 liquidity=34088976.0 spike=0.35
- EGAS.CA: score=-0.06 buy_ready=False sector_rank=7 price=46.7 support=43.0 resistance=58.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:44 PM market time freshness=DELAYED_CURRENT RSI=31.66 liquidity=1725659.75 spike=0.4
- EGBE.CA: score=8.12 buy_ready=False sector_rank=3 price=0.51 support=0.47 resistance=0.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=29 October 12:24 PM market time freshness=DELAYED_CURRENT RSI=37.38 liquidity=214553.1 spike=2.06
- EGCH.CA: score=7.19 buy_ready=False sector_rank=17 price=10.17 support=10.0 resistance=13.71 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:44 PM market time freshness=DELAYED_CURRENT RSI=25.61 liquidity=44468816.0 spike=0.81
- EGSA.CA: score=2.94 buy_ready=False sector_rank=19 price=8.81 support=8.75 resistance=9.09 source=Yahoo Finance as_of=2026-10-28T21:00:00+00:00 freshness=FRESH RSI=46.05 liquidity=4405.0 spike=0.89
- EGTS.CA: score=7.96 buy_ready=False sector_rank=15 price=12.28 support=10.19 resistance=17.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:45 PM market time freshness=DELAYED_CURRENT RSI=28.44 liquidity=26665096.0 spike=1.33
- EHDR.CA: score=0.46 buy_ready=False sector_rank=16 price=2.0 support=1.8 resistance=2.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:44 PM market time freshness=DELAYED_CURRENT RSI=34.37 liquidity=3208306.5 spike=0.35
- ELEC.CA: score=12.87 buy_ready=False sector_rank=10 price=1.5 support=1.34 resistance=1.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:46 PM market time freshness=DELAYED_CURRENT RSI=36.54 liquidity=20800120.0 spike=0.41
- ELKA.CA: score=12.25 buy_ready=False sector_rank=16 price=1.4 support=1.21 resistance=1.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:45 PM market time freshness=DELAYED_CURRENT RSI=44.71 liquidity=11312992.0 spike=0.84
- ELNA.CA: score=14.57 buy_ready=False sector_rank=16 price=39.66 support=33.46 resistance=39.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:34 PM market time freshness=DELAYED_CURRENT RSI=70.13 liquidity=1724653.38 spike=3.3
- ELSH.CA: score=9.17 buy_ready=False sector_rank=16 price=9.93 support=8.57 resistance=12.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:44 PM market time freshness=DELAYED_CURRENT RSI=35.8 liquidity=6923303.0 spike=0.38
- ELWA.CA: score=1.48 buy_ready=False sector_rank=16 price=1.5 support=1.43 resistance=1.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:46 PM market time freshness=DELAYED_CURRENT RSI=0.0 liquidity=489484.5 spike=1.87
- EMFD.CA: score=13.3 buy_ready=False sector_rank=15 price=11.8 support=10.6 resistance=13.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:44 PM market time freshness=DELAYED_CURRENT RSI=39.58 liquidity=18860894.0 spike=0.37
- ENGC.CA: score=12.0 buy_ready=False sector_rank=16 price=34.73 support=26.91 resistance=38.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:46 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=5753779.0 spike=0.56
- EOSB.CA: score=10.78 buy_ready=False sector_rank=16 price=1.61 support=1.56 resistance=1.72 source=Yahoo Finance as_of=2026-10-28T21:00:00+00:00 freshness=FRESH RSI=70.0 liquidity=170141.58 spike=2.18
- EPCO.CA: score=-0.97 buy_ready=False sector_rank=16 price=7.82 support=7.0 resistance=10.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:44 PM market time freshness=DELAYED_CURRENT RSI=33.4 liquidity=1783292.38 spike=0.42
- EPPK.CA: score=-6.33 buy_ready=False sector_rank=16 price=10.29 support=10.29 resistance=10.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=8 September 01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=419183.72 spike=0.28
- ETEL.CA: score=7.93 buy_ready=False sector_rank=19 price=118.02 support=115.0 resistance=156.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:45 PM market time freshness=DELAYED_CURRENT RSI=28.61 liquidity=104113792.0 spike=0.39
- ETRS.CA: score=12.52 buy_ready=False sector_rank=16 price=10.43 support=9.51 resistance=11.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:45 PM market time freshness=DELAYED_CURRENT RSI=46.99 liquidity=7269623.5 spike=0.55
- EXPA.CA: score=16.78 buy_ready=False sector_rank=3 price=14.16 support=12.0 resistance=16.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:44 PM market time freshness=DELAYED_CURRENT RSI=37.33 liquidity=29663534.0 spike=0.88
- FAIT.CA: score=6.76 buy_ready=False sector_rank=3 price=43.55 support=40.0 resistance=45.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:41 PM market time freshness=DELAYED_CURRENT RSI=45.78 liquidity=974801.38 spike=0.35
- FAITA.CA: score=12.79 buy_ready=False sector_rank=3 price=1.0 support=0.98 resistance=1.01 source=Yahoo Finance as_of=2026-10-28T21:00:00+00:00 freshness=FRESH RSI=54.46 liquidity=6663.33 spike=0.2
- FERC.CA: score=-1.53 buy_ready=False sector_rank=17 price=61.21 support=53.57 resistance=77.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:43 PM market time freshness=DELAYED_CURRENT RSI=33.29 liquidity=1283396.5 spike=0.36
- FWRY.CA: score=8.64 buy_ready=False sector_rank=4 price=16.49 support=16.45 resistance=19.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:45 PM market time freshness=DELAYED_CURRENT RSI=30.48 liquidity=70371656.0 spike=0.55
- GBCO.CA: score=3.63 buy_ready=False sector_rank=11 price=21.63 support=21.58 resistance=23.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:45 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=117883504.0 spike=1.01
- GDWA.CA: score=7.45 buy_ready=False sector_rank=16 price=0.55 support=0.48 resistance=0.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:44 PM market time freshness=DELAYED_CURRENT RSI=35.05 liquidity=5200977.0 spike=0.39
- GGCC.CA: score=3.49 buy_ready=False sector_rank=16 price=0.52 support=0.52 resistance=0.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:46 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=18985548.0 spike=1.12
- GIHD.CA: score=5.73 buy_ready=False sector_rank=16 price=43.81 support=41.0 resistance=44.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:46 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=29952708.0 spike=2.24
- GMCI.CA: score=-0.24 buy_ready=False sector_rank=16 price=1.41 support=1.41 resistance=1.77 source=Yahoo Finance as_of=2026-10-28T21:00:00+00:00 freshness=FRESH RSI=0.0 liquidity=507131.87 spike=2.0
- GRCA.CA: score=1.89 buy_ready=False sector_rank=16 price=26.2 support=22.57 resistance=39.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:44 PM market time freshness=DELAYED_CURRENT RSI=25.12 liquidity=2645881.5 spike=0.53
- GSSC.CA: score=3.06 buy_ready=False sector_rank=16 price=255.37 support=211.52 resistance=290.0 source=Yahoo Finance as_of=2026-10-28T21:00:00+00:00 freshness=FRESH RSI=38.74 liquidity=808501.4 spike=0.78
- HDBK.CA: score=14.78 buy_ready=False sector_rank=3 price=98.39 support=83.01 resistance=112.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:44 PM market time freshness=DELAYED_CURRENT RSI=39.53 liquidity=20242474.0 spike=0.9
- HELI.CA: score=13.3 buy_ready=False sector_rank=15 price=6.3 support=5.72 resistance=7.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:45 PM market time freshness=DELAYED_CURRENT RSI=38.7 liquidity=23542360.0 spike=0.35
- HRHO.CA: score=6.97 buy_ready=False sector_rank=18 price=23.17 support=22.8 resistance=27.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:44 PM market time freshness=DELAYED_CURRENT RSI=30.44 liquidity=22489136.0 spike=0.19
- ICID.CA: score=6.84 buy_ready=False sector_rank=16 price=17.41 support=14.26 resistance=20.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:37 PM market time freshness=DELAYED_CURRENT RSI=48.79 liquidity=3589306.75 spike=0.51
- IDRE.CA: score=5.13 buy_ready=False sector_rank=16 price=37.94 support=29.11 resistance=52.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:44 PM market time freshness=DELAYED_CURRENT RSI=32.11 liquidity=7261154.5 spike=1.31
- IFAP.CA: score=-0.87 buy_ready=False sector_rank=21 price=16.5 support=15.51 resistance=19.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:41 PM market time freshness=DELAYED_CURRENT RSI=27.02 liquidity=2732123.0 spike=0.58
- INFI.CA: score=10.27 buy_ready=False sector_rank=16 price=113.47 support=93.44 resistance=138.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:46 PM market time freshness=DELAYED_CURRENT RSI=43.84 liquidity=7020560.0 spike=0.34
- IRON.CA: score=3.66 buy_ready=False sector_rank=17 price=24.66 support=23.53 resistance=32.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:37 PM market time freshness=DELAYED_CURRENT RSI=31.07 liquidity=6473676.0 spike=0.61
- ISMA.CA: score=1.45 buy_ready=False sector_rank=16 price=18.85 support=14.11 resistance=27.06 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:47 PM market time freshness=DELAYED_CURRENT RSI=33.35 liquidity=4206150.5 spike=0.58
- ISMQ.CA: score=3.19 buy_ready=False sector_rank=17 price=7.04 support=6.55 resistance=7.06 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:46 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=11935165.0 spike=0.78
- ISPH.CA: score=7.85 buy_ready=False sector_rank=6 price=9.4 support=9.17 resistance=9.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:45 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=125323808.0 spike=2.79
- JUFO.CA: score=14.58 buy_ready=False sector_rank=9 price=22.28 support=21.01 resistance=26.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:45 PM market time freshness=DELAYED_CURRENT RSI=41.28 liquidity=9650616.0 spike=0.54
- KABO.CA: score=2.68 buy_ready=False sector_rank=12 price=6.53 support=5.58 resistance=9.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:44 PM market time freshness=DELAYED_CURRENT RSI=30.21 liquidity=5083984.0 spike=0.23
- KWIN.CA: score=3.27 buy_ready=False sector_rank=16 price=54.43 support=44.02 resistance=82.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:43 PM market time freshness=DELAYED_CURRENT RSI=28.75 liquidity=5582999.5 spike=1.22
- KZPC.CA: score=4.61 buy_ready=False sector_rank=16 price=12.69 support=11.56 resistance=13.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:44 PM market time freshness=DELAYED_CURRENT RSI=46.72 liquidity=1357014.0 spike=0.2
- LCSW.CA: score=25.12 buy_ready=False sector_rank=2 price=35.31 support=28.0 resistance=36.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:45 PM market time freshness=DELAYED_CURRENT RSI=56.98 liquidity=9088031.0 spike=0.35
- LUTS.CA: score=5.23 buy_ready=False sector_rank=16 price=0.72 support=0.64 resistance=0.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:47 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=107977400.0 spike=1.99
- MAAL.CA: score=8.55 buy_ready=False sector_rank=16 price=6.93 support=4.88 resistance=11.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:45 PM market time freshness=DELAYED_CURRENT RSI=27.26 liquidity=14906307.0 spike=1.15
- MASR.CA: score=13.25 buy_ready=False sector_rank=16 price=6.73 support=5.6 resistance=8.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:44 PM market time freshness=DELAYED_CURRENT RSI=40.29 liquidity=24538074.0 spike=0.49
- MBSC.CA: score=12.04 buy_ready=False sector_rank=2 price=299.47 support=262.0 resistance=414.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:45 PM market time freshness=DELAYED_CURRENT RSI=29.94 liquidity=28307214.0 spike=0.26
- MCQE.CA: score=18.04 buy_ready=False sector_rank=2 price=168.06 support=144.0 resistance=224.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:46 PM market time freshness=DELAYED_CURRENT RSI=35.34 liquidity=30685744.0 spike=0.41
- MCRO.CA: score=12.25 buy_ready=False sector_rank=16 price=1.3 support=1.07 resistance=1.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:45 PM market time freshness=DELAYED_CURRENT RSI=41.67 liquidity=38497612.0 spike=0.83
- MENA.CA: score=12.3 buy_ready=False sector_rank=15 price=5.62 support=5.45 resistance=7.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=29.69 liquidity=33222170.0 spike=12.39
- MEPA.CA: score=7.63 buy_ready=False sector_rank=16 price=1.26 support=1.14 resistance=1.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:44 PM market time freshness=DELAYED_CURRENT RSI=27.38 liquidity=15740651.0 spike=1.19
- MFPC.CA: score=13.19 buy_ready=False sector_rank=17 price=44.02 support=40.66 resistance=47.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:44 PM market time freshness=DELAYED_CURRENT RSI=49.56 liquidity=28194446.0 spike=0.56
- MFSC.CA: score=-1.44 buy_ready=False sector_rank=16 price=32.63 support=28.55 resistance=47.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:43 PM market time freshness=DELAYED_CURRENT RSI=27.44 liquidity=1315531.88 spike=0.66
- MHOT.CA: score=13.82 buy_ready=False sector_rank=1 price=14.77 support=13.0 resistance=16.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:44 PM market time freshness=DELAYED_CURRENT RSI=42.96 liquidity=6779654.0 spike=0.91
- MICH.CA: score=7.2 buy_ready=False sector_rank=16 price=40.62 support=35.5 resistance=44.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:45 PM market time freshness=DELAYED_CURRENT RSI=43.58 liquidity=1955214.5 spike=0.31
- MILS.CA: score=3.07 buy_ready=False sector_rank=16 price=125.16 support=96.02 resistance=195.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:41 PM market time freshness=DELAYED_CURRENT RSI=26.16 liquidity=5824676.5 spike=0.69
- MIPH.CA: score=4.77 buy_ready=False sector_rank=6 price=747.92 support=610.0 resistance=840.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:37 PM market time freshness=DELAYED_CURRENT RSI=40.02 liquidity=504737.19 spike=0.14
- MOED.CA: score=6.88 buy_ready=False sector_rank=16 price=0.46 support=0.39 resistance=0.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:44 PM market time freshness=DELAYED_CURRENT RSI=24.4 liquidity=9632579.0 spike=0.72
- MOIL.CA: score=4.33 buy_ready=False sector_rank=7 price=0.63 support=0.6 resistance=0.71 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:32 PM market time freshness=DELAYED_CURRENT RSI=40.0 liquidity=111096.59 spike=0.55
- MOIN.CA: score=2.67 buy_ready=False sector_rank=16 price=28.38 support=25.7 resistance=37.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:46 PM market time freshness=DELAYED_CURRENT RSI=27.06 liquidity=4421217.0 spike=0.54
- MOSC.CA: score=3.25 buy_ready=False sector_rank=16 price=239.42 support=198.01 resistance=310.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:40 PM market time freshness=DELAYED_CURRENT RSI=38.12 liquidity=999281.0 spike=0.26
- MPCI.CA: score=18.11 buy_ready=False sector_rank=16 price=320.46 support=238.6 resistance=369.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:46 PM market time freshness=DELAYED_CURRENT RSI=48.35 liquidity=138239696.0 spike=1.43
- MPCO.CA: score=6.4 buy_ready=False sector_rank=21 price=1.76 support=1.55 resistance=2.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:45 PM market time freshness=DELAYED_CURRENT RSI=30.95 liquidity=28578350.0 spike=0.35
- MPRC.CA: score=8.35 buy_ready=False sector_rank=16 price=32.77 support=27.0 resistance=41.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:45 PM market time freshness=DELAYED_CURRENT RSI=31.53 liquidity=23176652.0 spike=1.55
- MTIE.CA: score=7.25 buy_ready=False sector_rank=11 price=6.94 support=6.05 resistance=8.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:44 PM market time freshness=DELAYED_CURRENT RSI=38.9 liquidity=4642633.0 spike=0.23
- NAHO.CA: score=3.26 buy_ready=False sector_rank=16 price=0.13 support=0.12 resistance=0.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:42 PM market time freshness=DELAYED_CURRENT RSI=38.1 liquidity=15356.88 spike=0.88
- NCCW.CA: score=7.25 buy_ready=False sector_rank=16 price=5.26 support=4.05 resistance=7.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:46 PM market time freshness=DELAYED_CURRENT RSI=30.68 liquidity=18504440.0 spike=0.98
- NEDA.CA: score=0.43 buy_ready=False sector_rank=16 price=2.47 support=2.47 resistance=2.71 source=Yahoo Finance as_of=2026-10-28T21:00:00+00:00 freshness=FRESH RSI=0.0 liquidity=386769.89 spike=2.4
- NHPS.CA: score=1.36 buy_ready=False sector_rank=16 price=55.74 support=50.0 resistance=77.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:44 PM market time freshness=DELAYED_CURRENT RSI=24.29 liquidity=4110496.5 spike=0.52
- NINH.CA: score=1.53 buy_ready=False sector_rank=16 price=14.91 support=12.36 resistance=20.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:46 PM market time freshness=DELAYED_CURRENT RSI=28.97 liquidity=2281448.25 spike=0.23
- NIPH.CA: score=16.49 buy_ready=False sector_rank=6 price=283.98 support=205.0 resistance=341.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:46 PM market time freshness=DELAYED_CURRENT RSI=45.43 liquidity=141852784.0 spike=1.11
- OBRI.CA: score=3.93 buy_ready=False sector_rank=16 price=22.78 support=18.11 resistance=33.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:44 PM market time freshness=DELAYED_CURRENT RSI=33.07 liquidity=6679654.0 spike=0.46
- OCDI.CA: score=12.3 buy_ready=False sector_rank=15 price=22.8 support=21.0 resistance=28.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:45 PM market time freshness=DELAYED_CURRENT RSI=39.61 liquidity=19624936.0 spike=0.56
- OCPH.CA: score=-1.2 buy_ready=False sector_rank=16 price=183.3 support=147.96 resistance=244.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:42 PM market time freshness=DELAYED_CURRENT RSI=34.18 liquidity=1550145.5 spike=0.48
- ODIN.CA: score=7.93 buy_ready=False sector_rank=16 price=2.04 support=1.7 resistance=2.67 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:46 PM market time freshness=DELAYED_CURRENT RSI=36.62 liquidity=5685058.5 spike=0.94
- OFH.CA: score=7.25 buy_ready=False sector_rank=16 price=0.69 support=0.61 resistance=0.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:46 PM market time freshness=DELAYED_CURRENT RSI=29.74 liquidity=13170720.0 spike=0.47
- OIH.CA: score=10.53 buy_ready=False sector_rank=20 price=1.63 support=1.5 resistance=1.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:44 PM market time freshness=DELAYED_CURRENT RSI=36.0 liquidity=8071711.5 spike=0.17
- OLFI.CA: score=1.5 buy_ready=False sector_rank=9 price=18.98 support=17.86 resistance=22.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:44 PM market time freshness=DELAYED_CURRENT RSI=27.19 liquidity=3572725.25 spike=0.26
- ORAS.CA: score=4.6 buy_ready=False sector_rank=5 price=817.97 support=807.14 resistance=837.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:45 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=147702512.0 spike=1.0
- ORHD.CA: score=9.3 buy_ready=False sector_rank=15 price=9.6 support=8.5 resistance=12.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:45 PM market time freshness=DELAYED_CURRENT RSI=31.29 liquidity=38498448.0 spike=0.33
- ORWE.CA: score=3.6 buy_ready=False sector_rank=12 price=24.99 support=23.34 resistance=25.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:45 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=37256912.0 spike=1.0
- PHAR.CA: score=14.27 buy_ready=False sector_rank=6 price=99.39 support=90.2 resistance=119.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:45 PM market time freshness=DELAYED_CURRENT RSI=37.25 liquidity=53401304.0 spike=0.96
- PHDC.CA: score=3.56 buy_ready=False sector_rank=15 price=10.7 support=10.51 resistance=11.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:45 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=98722888.0 spike=1.13
- PHTV.CA: score=3.57 buy_ready=False sector_rank=16 price=319.1 support=300.0 resistance=360.0 source=Yahoo Finance as_of=2026-10-28T21:00:00+00:00 freshness=FRESH RSI=35.46 liquidity=325801.11 spike=0.35
- POUL.CA: score=14.93 buy_ready=False sector_rank=9 price=9.46 support=8.81 resistance=10.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:44 PM market time freshness=DELAYED_CURRENT RSI=47.52 liquidity=28077230.0 spike=0.49
- PRCL.CA: score=20.44 buy_ready=False sector_rank=2 price=20.13 support=16.65 resistance=27.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:44 PM market time freshness=DELAYED_CURRENT RSI=36.86 liquidity=22640768.0 spike=2.2
- PRDC.CA: score=11.3 buy_ready=False sector_rank=15 price=6.07 support=5.08 resistance=8.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:44 PM market time freshness=DELAYED_CURRENT RSI=38.58 liquidity=6995314.5 spike=0.2
- PRMH.CA: score=7.2 buy_ready=False sector_rank=16 price=1.85 support=1.7 resistance=2.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:41 PM market time freshness=DELAYED_CURRENT RSI=39.1 liquidity=2831524.25 spike=1.06
- RACC.CA: score=1.26 buy_ready=False sector_rank=16 price=7.2 support=6.1 resistance=9.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:42 PM market time freshness=DELAYED_CURRENT RSI=26.97 liquidity=4011500.25 spike=0.56
- RAKT.CA: score=0.56 buy_ready=False sector_rank=16 price=22.35 support=20.4 resistance=25.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=26.11 liquidity=307127.06 spike=0.71
- RAYA.CA: score=7.57 buy_ready=False sector_rank=13 price=5.38 support=5.02 resistance=6.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:45 PM market time freshness=DELAYED_CURRENT RSI=32.86 liquidity=13431368.0 spike=0.67
- RMDA.CA: score=16.27 buy_ready=False sector_rank=6 price=5.07 support=4.5 resistance=5.62 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:45 PM market time freshness=DELAYED_CURRENT RSI=49.05 liquidity=11716337.0 spike=0.49
- ROTO.CA: score=0.18 buy_ready=False sector_rank=16 price=29.94 support=25.0 resistance=42.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:36 PM market time freshness=DELAYED_CURRENT RSI=24.78 liquidity=2928940.75 spike=0.36
- RREI.CA: score=8.37 buy_ready=False sector_rank=16 price=2.68 support=1.96 resistance=4.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:44 PM market time freshness=DELAYED_CURRENT RSI=26.64 liquidity=15865336.0 spike=1.56
- RTVC.CA: score=-0.85 buy_ready=False sector_rank=16 price=2.8 support=2.77 resistance=3.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:42 PM market time freshness=DELAYED_CURRENT RSI=16.81 liquidity=1903396.75 spike=0.68
- RUBX.CA: score=8.25 buy_ready=False sector_rank=16 price=12.79 support=10.51 resistance=19.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:47 PM market time freshness=DELAYED_CURRENT RSI=33.72 liquidity=51292580.0 spike=0.61
- SAUD.CA: score=6.88 buy_ready=False sector_rank=3 price=20.44 support=19.3 resistance=23.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:44 PM market time freshness=DELAYED_CURRENT RSI=32.72 liquidity=7096103.0 spike=0.62
- SCEM.CA: score=19.78 buy_ready=False sector_rank=2 price=85.06 support=73.9 resistance=95.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:45 PM market time freshness=DELAYED_CURRENT RSI=43.59 liquidity=81038032.0 spike=1.37
- SCFM.CA: score=8.3 buy_ready=False sector_rank=16 price=216.38 support=153.02 resistance=259.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:42 PM market time freshness=DELAYED_CURRENT RSI=37.82 liquidity=3930634.5 spike=2.06
- SCTS.CA: score=9.46 buy_ready=False sector_rank=8 price=494.05 support=410.0 resistance=588.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:41 PM market time freshness=DELAYED_CURRENT RSI=43.61 liquidity=3479503.5 spike=0.88
- SDTI.CA: score=16.25 buy_ready=False sector_rank=16 price=83.23 support=75.01 resistance=90.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:44 PM market time freshness=DELAYED_CURRENT RSI=40.42 liquidity=12229295.0 spike=0.71
- SEIG.CA: score=8.25 buy_ready=False sector_rank=16 price=223.68 support=192.0 resistance=223.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:44 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=24195224.0 spike=10.09
- SIPC.CA: score=13.25 buy_ready=False sector_rank=16 price=4.5 support=3.73 resistance=6.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:46 PM market time freshness=DELAYED_CURRENT RSI=38.49 liquidity=20882420.0 spike=0.35
- SKPC.CA: score=14.19 buy_ready=False sector_rank=17 price=15.0 support=14.01 resistance=16.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:44 PM market time freshness=DELAYED_CURRENT RSI=41.16 liquidity=24364114.0 spike=0.42
- SMFR.CA: score=-1.08 buy_ready=False sector_rank=16 price=183.0 support=165.0 resistance=245.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:45 PM market time freshness=DELAYED_CURRENT RSI=27.55 liquidity=1673589.63 spike=0.56
- SNFC.CA: score=5.97 buy_ready=False sector_rank=16 price=10.72 support=10.08 resistance=11.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:41 PM market time freshness=DELAYED_CURRENT RSI=37.45 liquidity=3718472.0 spike=0.48
- SPIN.CA: score=7.94 buy_ready=False sector_rank=12 price=13.66 support=12.0 resistance=17.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:45 PM market time freshness=DELAYED_CURRENT RSI=36.83 liquidity=3341361.25 spike=0.65
- SPMD.CA: score=8.31 buy_ready=False sector_rank=16 price=0.34 support=0.3 resistance=0.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:47 PM market time freshness=DELAYED_CURRENT RSI=42.45 liquidity=4057117.75 spike=0.27
- SUGR.CA: score=7.23 buy_ready=False sector_rank=9 price=48.56 support=44.62 resistance=54.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:46 PM market time freshness=DELAYED_CURRENT RSI=44.41 liquidity=3304034.0 spike=0.37
- SVCE.CA: score=12.25 buy_ready=False sector_rank=16 price=8.54 support=7.01 resistance=11.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:46 PM market time freshness=DELAYED_CURRENT RSI=35.17 liquidity=38979176.0 spike=0.59
- SWDY.CA: score=15.87 buy_ready=False sector_rank=10 price=110.77 support=97.0 resistance=124.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:45 PM market time freshness=DELAYED_CURRENT RSI=49.55 liquidity=21708596.0 spike=0.39
- TALM.CA: score=8.98 buy_ready=False sector_rank=8 price=18.77 support=17.0 resistance=23.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:45 PM market time freshness=DELAYED_CURRENT RSI=29.43 liquidity=10404131.0 spike=0.38
- TMGH.CA: score=12.3 buy_ready=False sector_rank=15 price=78.89 support=79.4 resistance=93.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:45 PM market time freshness=DELAYED_CURRENT RSI=39.08 liquidity=210827072.0 spike=0.82
- TRTO.CA: score=-1.75 buy_ready=False sector_rank=16 price=0.05 support=0.05 resistance=0.07 source=Yahoo Finance as_of=2026-10-28T21:00:00+00:00 freshness=FRESH RSI=0.0 liquidity=187.0 spike=0.03
- UEFM.CA: score=-1.09 buy_ready=False sector_rank=16 price=435.74 support=422.0 resistance=550.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:46 PM market time freshness=DELAYED_CURRENT RSI=23.52 liquidity=1663415.5 spike=0.78
- UEGC.CA: score=14.25 buy_ready=False sector_rank=16 price=1.39 support=1.21 resistance=1.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:44 PM market time freshness=DELAYED_CURRENT RSI=47.22 liquidity=24328378.0 spike=0.52
- UNIP.CA: score=2.52 buy_ready=False sector_rank=16 price=0.28 support=0.25 resistance=0.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:47 PM market time freshness=DELAYED_CURRENT RSI=31.79 liquidity=5267440.5 spike=0.66
- UNIT.CA: score=8.36 buy_ready=False sector_rank=15 price=17.75 support=15.06 resistance=19.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:45 PM market time freshness=DELAYED_CURRENT RSI=51.89 liquidity=1055132.25 spike=0.34
- WCDF.CA: score=-2.1 buy_ready=False sector_rank=16 price=493.78 support=432.5 resistance=639.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:42 PM market time freshness=DELAYED_CURRENT RSI=23.34 liquidity=656638.94 spike=0.32
- WKOL.CA: score=-0.41 buy_ready=False sector_rank=16 price=240.79 support=218.0 resistance=309.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:46 PM market time freshness=DELAYED_CURRENT RSI=34.27 liquidity=2343975.25 spike=0.33
- ZEOT.CA: score=5.19 buy_ready=False sector_rank=16 price=10.47 support=8.0 resistance=13.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:45 PM market time freshness=DELAYED_CURRENT RSI=41.08 liquidity=1946925.88 spike=0.25
- ZMID.CA: score=13.3 buy_ready=False sector_rank=15 price=6.45 support=5.91 resistance=7.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:45 PM market time freshness=DELAYED_CURRENT RSI=38.51 liquidity=21761670.0 spike=0.32

## Backtesting Lite
- CANA.CA: 180d return=13.94%, max drawdown=-36.46%, MA20>MA50 days last20=19, as_of=2026-10-28T21:00:00+00:00
- LCSW.CA: 180d return=53.36%, max drawdown=-17.84%, MA20>MA50 days last20=0, as_of=2026-10-28T21:00:00+00:00
- AMOC.CA: 180d return=109.06%, max drawdown=-16.73%, MA20>MA50 days last20=20, as_of=2026-10-28T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- CANA.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=669 sources=3 expected=Suez Canal Bank summary=Suez Canal Bank delivers EGP 1.6bn profits in Q1-26; Suez Canal Bank unveils details for previous dividends payout; Suez Canal Bank to distribute EGP 5bn bonus shares for 2025
  - Suez Canal Bank delivers EGP 1.6bn profits in Q1-26: https://english.mubasher.info/news/4611255/Suez-Canal-Bank-delivers-EGP-1-6bn-profits-in-Q1-26/
  - Suez Canal Bank unveils details for previous dividends payout: https://english.mubasher.info/news/4586807/Suez-Canal-Bank-unveils-details-for-previous-dividends-payout/
  - Suez Canal Bank to distribute EGP 5bn bonus shares for 2025: https://english.mubasher.info/news/4581661/Suez-Canal-Bank-to-distribute-EGP-5bn-bonus-shares-for-2025/
- LCSW.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Lecico Egypt summary=Evidence rejected for LCSW.CA: source text did not clearly match LCSW.CA / Lecico Egypt.
- AMOC.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Alexandria Mineral Oils summary=AMOC achieves EGP 10.5bn consolidated sales in Q1-26; AMOC studies potential project with Germany’s SULZER; AMOC to pay out EGP 0.4/shr dividends for H2-25
  - AMOC achieves EGP 10.5bn consolidated sales in Q1-26: https://english.mubasher.info/news/4604903/AMOC-achieves-EGP-10-5bn-consolidated-sales-in-Q1-26/
  - AMOC studies potential project with Germany’s SULZER: https://english.mubasher.info/news/4586853/AMOC-studies-potential-project-with-Germany-s-SULZER/
  - AMOC to pay out EGP 0.4/shr dividends for H2-25: https://english.mubasher.info/news/4586775/AMOC-to-pay-out-EGP-0-4-shr-dividends-for-H2-25/
- PRCL.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Ceramic and Porcelain summary=Evidence rejected for PRCL.CA: source text did not clearly match PRCL.CA / Ceramic and Porcelain.
- ADIB.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Abu Dhabi Islamic Bank Egypt summary=ADIB Egypt’s consolidated profits leap to EGP 3.6bn in Q1-26; ADIB Egypt stock approaches breakout above EGP 41; ADIB Egypt’s stock holds uptrend despite corrections
  - ADIB Egypt’s consolidated profits leap to EGP 3.6bn in Q1-26: https://english.mubasher.info/news/4607278/ADIB-Egypt-s-consolidated-profits-leap-to-EGP-3-6bn-in-Q1-26/
  - ADIB Egypt stock approaches breakout above EGP 41: https://english.mubasher.info/news/4591391/ADIB-Egypt-stock-approaches-breakout-above-EGP-41/
  - ADIB Egypt’s stock holds uptrend despite corrections: https://english.mubasher.info/news/4562331/ADIB-Egypt-s-stock-holds-uptrend-despite-corrections/
- SCEM.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=669 sources=3 expected=Sinai Cement summary=Sinai Cement’s consolidated profits fall in 2025; net sales cross EGP 9bn; Upward trend line ends several-day decline for Sinai Cement stock; Sinai Cement reports lower consolidated net profits at EGP 1.5bn in 9M-25
  - Sinai Cement’s consolidated profits fall in 2025; net sales cross EGP 9bn: https://english.mubasher.info/news/4564824/Sinai-Cement-s-consolidated-profits-fall-in-2025-net-sales-cross-EGP-9bn/
  - Upward trend line ends several-day decline for Sinai Cement stock: https://english.mubasher.info/news/4529647/Upward-trend-line-ends-several-day-decline-for-Sinai-Cement-stock/
  - Sinai Cement reports lower consolidated net profits at EGP 1.5bn in 9M-25: https://english.mubasher.info/news/4526073/Sinai-Cement-reports-lower-consolidated-net-profits-at-EGP-1-5bn-in-9M-25/
- AJWA.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=AJWA For Food Industries Co. Egypt summary=Ajwa Egypt&#39;s board approves capital increase to EGP 500m, joins new food venture; AJWA Egypt’s standalone net profits retreat to EGP 14m in 9M-25 amid shift to profitability in Q3; Ajwa Egypt turns to losses in 9M
  - Ajwa Egypt&#39;s board approves capital increase to EGP 500m, joins new food venture: https://english.mubasher.info/news/4532004/Ajwa-Egypt-s-board-approves-capital-increase-to-EGP-500m-joins-new-food-venture/
  - AJWA Egypt’s standalone net profits retreat to EGP 14m in 9M-25 amid shift to profitability in Q3: https://english.mubasher.info/news/4527545/AJWA-Egypt-s-standalone-net-profits-retreat-to-EGP-14m-in-9M-25-amid-shift-to-profitability-in-Q3/
  - Ajwa Egypt turns to losses in 9M: https://english.mubasher.info/news/3883210/Ajwa-Egypt-turns-to-losses-in-9M/
- MPCI.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Memphis Pharmaceuticals & Chemical Industries summary=Evidence rejected for MPCI.CA: source text did not clearly match MPCI.CA / Memphis Pharmaceuticals & Chemical Industries.

## Warnings
- OpenRouter API error: 404
- Evidence for CANA.CA matches the company but appears old; latest detected date is 2025-01-01.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence rejected for LCSW.CA: source text did not clearly match LCSW.CA / Lecico Egypt.
- Evidence for AMOC.CA matches the company but no source/report date was detected.
- Evidence rejected for PRCL.CA: source text did not clearly match PRCL.CA / Ceramic and Porcelain.
- Evidence for ADIB.CA matches the company but no source/report date was detected.
- Evidence for SCEM.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for AJWA.CA matches the company but no source/report date was detected.
- Evidence rejected for MPCI.CA: source text did not clearly match MPCI.CA / Memphis Pharmaceuticals & Chemical Industries.
