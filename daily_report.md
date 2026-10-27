# Telegram-First EGX Scanner Report

Scan phase: Intraday liquidity update
Generated UTC: 2026-10-27T13:58:49.373754+00:00
Generated Cairo: 2026-10-27 16:58
Run timing: target 11:00 Cairo | generated Cairo 2026-10-27 16:58 | cron 0 8 * * 0-4
Trigger: scheduled cron=0 8 * * 0-4 mapped to intraday; Cairo now 2026-10-27 16:51

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 4
- Tradeable price/liquidity tickers: 76/186
- Top sector: Telecommunications

## Market Context
- Market trend: Unavailable
- Source: Market context unavailable
- As of: None
- Freshness: MISSING
- EGX30 regime: BEARISH / above MA20 14.29% / above MA50 14.29%
- EGX70 regime: BEARISH / above MA20 0.0% / above MA50 4.55%
- Sector breadth: 0.0%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- COMI.CA: liquidity=1293849053.36 spike=2.63 score=17.96
- ETEL.CA: liquidity=423965632.0 spike=1.61 score=9.06
- ORAS.CA: liquidity=343100416.0 spike=1.0 score=4.6
- TMGH.CA: liquidity=306956448.0 spike=1.22 score=16.03
- CCAP.CA: liquidity=290514784.0 spike=0.58 score=8.34

## AI Narrative
- Provider: OpenRouter ERROR
- Model: openai/gpt-oss-120b:free
- Summary: OpenRouter narrative failed; local scanner summary used.

## Top Liquidity Spikes
- DEIN.CA: spike=19.95 liquidity=12181.95 outlook=NEUTRAL score=48.64 buy_ready=False
- MEPA.CA: spike=10.45 liquidity=73060744.0 outlook=NEUTRAL score=39.64 buy_ready=False
- EOSB.CA: spike=6.71 liquidity=439274.01 outlook=CONSTRUCTIVE score=61.64 buy_ready=False
- EPCO.CA: spike=3.88 liquidity=17136966.02 outlook=NEUTRAL score=39.64 buy_ready=False
- SPMD.CA: spike=2.88 liquidity=32400078.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False

## Sector Leaderboard
- #1 Telecommunications: score=2.09 5d=0.28% 20d=-1.05% aboveMA50=0.0%
- #2 Basic Resources & Chemicals: score=2.0 5d=0.0% 20d=-0.45% aboveMA50=20.0%
- #3 General / Verified EGX Expansion: score=1.64 5d=0.0% 20d=0.0% aboveMA50=4.9%
- #4 Industrial Goods & Cables: score=1.59 5d=0.0% 20d=0.0% aboveMA50=0.0%
- #5 Industrial Goods & Construction: score=1.5 5d=0.0% 20d=0.0% aboveMA50=0.0%
- #6 Real Estate: score=1.48 5d=0.0% 20d=0.0% aboveMA50=0.0%
- #7 Building Materials: score=1.47 5d=0.0% 20d=0.0% aboveMA50=0.0%
- #8 Healthcare: score=1.37 5d=-1.0% 20d=-1.65% aboveMA50=0.0%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- ABUK.CA: BULLISH_WATCH score=82.0 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- CPCI.CA: BULLISH_WATCH score=75.64 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- MFPC.CA: BULLISH_WATCH score=75.0 liquidity=TRADEABLE sector=LEADING risk=below MA20
- SDTI.CA: CONSTRUCTIVE score=69.64 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; below MA20
- ETRS.CA: CONSTRUCTIVE score=64.64 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=below MA20; below MA50
- RAKT.CA: CONSTRUCTIVE score=64.64 liquidity=THIN sector=LEADING risk=liquidity below minimum
- EOSB.CA: CONSTRUCTIVE score=61.64 liquidity=THIN sector=LEADING risk=liquidity below minimum; momentum is extended
- DEIN.CA: NEUTRAL score=48.64 liquidity=THIN sector=LEADING risk=liquidity below minimum; below MA20
- EPCO.CA: NEUTRAL score=39.64 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=below MA20; below MA50; weak RSI
- MEPA.CA: NEUTRAL score=39.64 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=below MA20; below MA50; weak RSI

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- EKHO.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- SUGR.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ARVA.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=1.75 buy_ready=False sector_rank=3 price=205.64 support=171.02 resistance=208.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=6096374.5 spike=0.68
- ABUK.CA: score=23.8 buy_ready=False sector_rank=2 price=90.76 support=80.5 resistance=95.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=52.37 liquidity=61367904.0 spike=0.78
- ACAMD.CA: score=9.66 buy_ready=False sector_rank=3 price=1.96 support=1.86 resistance=2.16 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=33.33 liquidity=42226848.0 spike=0.96
- ACGC.CA: score=4.09 buy_ready=False sector_rank=15 price=12.96 support=12.25 resistance=12.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=13325431.0 spike=1.3
- ADCI.CA: score=-2.28 buy_ready=False sector_rank=3 price=256.84 support=235.01 resistance=258.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=1807377.25 spike=1.13
- ADIB.CA: score=8.12 buy_ready=False sector_rank=13 price=44.5 support=43.16 resistance=51.87 source=Yahoo Finance as_of=2026-10-25T21:00:00+00:00 freshness=FRESH RSI=34.33 liquidity=92704002.0 spike=1.21
- ADPC.CA: score=1.72 buy_ready=False sector_rank=3 price=2.85 support=2.74 resistance=2.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=6065782.5 spike=0.64
- AFDI.CA: score=-3.25 buy_ready=False sector_rank=3 price=41.5 support=39.96 resistance=41.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=1095126.88 spike=0.25
- AFMC.CA: score=5.66 buy_ready=False sector_rank=3 price=109.83 support=102.0 resistance=112.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=18114832.0 spike=1.0
- AJWA.CA: score=1.81 buy_ready=False sector_rank=3 price=208.22 support=196.0 resistance=208.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=6157796.5 spike=0.18
- ALCN.CA: score=7.67 buy_ready=False sector_rank=20 price=31.15 support=27.11 resistance=36.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=32.21 liquidity=10407863.0 spike=0.48
- ALUM.CA: score=-1.46 buy_ready=False sector_rank=3 price=18.21 support=17.0 resistance=18.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:09 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=2879783.75 spike=0.8
- AMER.CA: score=4.69 buy_ready=False sector_rank=6 price=4.07 support=3.55 resistance=4.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=55269472.0 spike=1.05
- AMES.CA: score=5.66 buy_ready=False sector_rank=3 price=32.48 support=29.51 resistance=32.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=52009636.0 spike=0.89
- AMIA.CA: score=9.23 buy_ready=False sector_rank=3 price=16.92 support=14.0 resistance=19.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=32.15 liquidity=8576823.0 spike=0.53
- AMOC.CA: score=17.44 buy_ready=False sector_rank=9 price=13.08 support=12.18 resistance=14.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=35.6 liquidity=88816376.0 spike=0.69
- APSW.CA: score=1.79 buy_ready=False sector_rank=3 price=7.12 support=7.1 resistance=8.92 source=Yahoo Finance as_of=2026-10-25T21:00:00+00:00 freshness=FRESH RSI=10.0 liquidity=973396.54 spike=1.58
- ARAB.CA: score=14.73 buy_ready=False sector_rank=6 price=0.23 support=0.2 resistance=0.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=38.51 liquidity=120337336.0 spike=1.07
- ARCC.CA: score=4.59 buy_ready=False sector_rank=7 price=64.0 support=60.17 resistance=64.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=37887120.0 spike=0.88
- AREH.CA: score=4.75 buy_ready=False sector_rank=3 price=1.06 support=0.96 resistance=1.06 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=8912434.0 spike=1.09
- ASCM.CA: score=1.08 buy_ready=False sector_rank=3 price=42.91 support=41.01 resistance=43.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=5425728.5 spike=0.62
- ASPI.CA: score=6.44 buy_ready=False sector_rank=3 price=0.3 support=0.28 resistance=0.31 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=26404044.0 spike=1.39
- ATLC.CA: score=5.72 buy_ready=False sector_rank=12 price=4.75 support=4.4 resistance=4.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=13659926.0 spike=1.84
- ATQA.CA: score=6.8 buy_ready=False sector_rank=2 price=9.32 support=8.78 resistance=9.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=32569800.0 spike=0.6
- AXPH.CA: score=-1.04 buy_ready=False sector_rank=3 price=1266.58 support=1185.0 resistance=1287.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=3300734.0 spike=0.59
- BINV.CA: score=10.66 buy_ready=False sector_rank=17 price=53.53 support=52.11 resistance=65.99 source=Yahoo Finance as_of=2026-10-25T21:00:00+00:00 freshness=FRESH RSI=25.17 liquidity=31152906.92 spike=2.16
- BIOC.CA: score=5.66 buy_ready=False sector_rank=3 price=258.24 support=226.3 resistance=260.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=51761400.0 spike=0.47
- BTFH.CA: score=8.44 buy_ready=False sector_rank=12 price=2.26 support=2.05 resistance=2.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=21.43 liquidity=123439040.0 spike=1.2
- CAED.CA: score=6.74 buy_ready=False sector_rank=3 price=79.6 support=69.0 resistance=81.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=13035019.0 spike=1.54
- CANA.CA: score=13.84 buy_ready=False sector_rank=13 price=42.93 support=38.1 resistance=48.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=36.69 liquidity=17547500.0 spike=1.07
- CCAP.CA: score=8.34 buy_ready=False sector_rank=17 price=6.06 support=5.8 resistance=6.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=28.99 liquidity=290514784.0 spike=0.58
- CCRS.CA: score=3.04 buy_ready=False sector_rank=3 price=1.58 support=1.53 resistance=1.62 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=7245409.0 spike=1.07
- CEFM.CA: score=-0.66 buy_ready=False sector_rank=3 price=115.5 support=108.0 resistance=117.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=2826191.75 spike=1.43
- CERA.CA: score=5.66 buy_ready=False sector_rank=3 price=1.04 support=1.0 resistance=1.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=76579384.0 spike=0.63
- CFGH.CA: score=3.07 buy_ready=False sector_rank=3 price=0.1 support=0.1 resistance=0.12 source=Yahoo Finance as_of=2026-10-25T21:00:00+00:00 freshness=FRESH RSI=9.09 liquidity=15859.32 spike=2.7
- CICH.CA: score=-1.35 buy_ready=False sector_rank=12 price=10.7 support=9.63 resistance=12.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=18.93 liquidity=605765.5 spike=0.27
- CIEB.CA: score=7.29 buy_ready=False sector_rank=13 price=21.42 support=21.35 resistance=24.76 source=Yahoo Finance as_of=2026-10-25T21:00:00+00:00 freshness=FRESH RSI=22.6 liquidity=9384894.57 spike=1.1
- CIRA.CA: score=6.39 buy_ready=False sector_rank=19 price=34.32 support=32.01 resistance=41.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=23.29 liquidity=8533742.0 spike=0.51
- CLHO.CA: score=5.53 buy_ready=False sector_rank=8 price=13.8 support=13.0 resistance=13.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=55105032.0 spike=1.49
- CNFN.CA: score=1.64 buy_ready=False sector_rank=12 price=3.82 support=3.6 resistance=3.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=7600189.5 spike=0.81
- COMI.CA: score=17.96 buy_ready=False sector_rank=13 price=120.1 support=118.06 resistance=130.0 source=Yahoo Finance as_of=2026-10-25T21:00:00+00:00 freshness=FRESH RSI=36.48 liquidity=1293849053.36 spike=2.63
- COPR.CA: score=5.66 buy_ready=False sector_rank=3 price=0.4 support=0.37 resistance=0.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=14804712.0 spike=0.91
- COSG.CA: score=5.84 buy_ready=False sector_rank=3 price=1.25 support=1.17 resistance=1.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=12349514.0 spike=1.09
- CPCI.CA: score=14.2 buy_ready=False sector_rank=3 price=597.93 support=502.25 resistance=619.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=44.24 liquidity=3547737.75 spike=0.67
- CSAG.CA: score=0.11 buy_ready=False sector_rank=20 price=32.21 support=30.1 resistance=38.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=24.06 liquidity=3442811.0 spike=0.49
- DAPH.CA: score=5.66 buy_ready=False sector_rank=3 price=76.99 support=69.0 resistance=78.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=20413416.0 spike=0.49
- DEIN.CA: score=13.67 buy_ready=False sector_rank=3 price=10.35 support=10.35 resistance=12.42 source=Yahoo Finance as_of=2026-10-25T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=12181.95 spike=19.95
- DOMT.CA: score=-4.73 buy_ready=False sector_rank=14 price=22.39 support=21.19 resistance=22.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=1697322.88 spike=0.51
- DSCW.CA: score=7.3 buy_ready=False sector_rank=3 price=1.52 support=1.37 resistance=1.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=28602236.0 spike=1.82
- DTPP.CA: score=5.66 buy_ready=False sector_rank=3 price=42.99 support=41.08 resistance=43.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=25323674.0 spike=0.63
- EALR.CA: score=-3.25 buy_ready=False sector_rank=3 price=257.52 support=245.21 resistance=259.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=1092583.75 spike=0.34
- EASB.CA: score=0.08 buy_ready=False sector_rank=3 price=6.07 support=5.5 resistance=6.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=4425512.5 spike=0.9
- EAST.CA: score=16.57 buy_ready=False sector_rank=14 price=31.18 support=27.01 resistance=30.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=56.91 liquidity=27253444.0 spike=0.57
- EBSC.CA: score=0.88 buy_ready=False sector_rank=3 price=1.45 support=1.29 resistance=1.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=3647180.25 spike=1.79
- ECAP.CA: score=0.74 buy_ready=False sector_rank=3 price=26.51 support=24.8 resistance=31.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=17.48 liquidity=1088194.75 spike=0.31
- EDFM.CA: score=1.65 buy_ready=False sector_rank=3 price=366.59 support=335.2 resistance=425.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=23.78 liquidity=989115.44 spike=0.88
- EEII.CA: score=8.4 buy_ready=False sector_rank=3 price=1.64 support=1.55 resistance=1.67 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=15206575.0 spike=2.37
- EFIC.CA: score=6.8 buy_ready=False sector_rank=2 price=139.81 support=129.0 resistance=140.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=14225599.0 spike=0.55
- EFID.CA: score=9.57 buy_ready=False sector_rank=14 price=17.8 support=16.01 resistance=19.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=34.1 liquidity=25787282.0 spike=0.63
- EFIH.CA: score=3.4 buy_ready=False sector_rank=16 price=21.91 support=20.61 resistance=21.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=54070816.0 spike=0.81
- EGAL.CA: score=11.8 buy_ready=False sector_rank=2 price=303.13 support=275.0 resistance=359.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=22.11 liquidity=81821336.0 spike=0.87
- EGAS.CA: score=-2.47 buy_ready=False sector_rank=9 price=47.0 support=44.04 resistance=47.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=3089904.75 spike=0.59
- EGBE.CA: score=-1.25 buy_ready=False sector_rank=13 price=0.5 support=0.47 resistance=0.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=15.66 liquidity=43945.2 spike=0.43
- EGCH.CA: score=11.02 buy_ready=False sector_rank=2 price=10.7 support=10.0 resistance=13.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=20.23 liquidity=66425368.0 spike=1.11
- EGSA.CA: score=10.44 buy_ready=False sector_rank=1 price=8.81 support=8.75 resistance=9.09 source=Yahoo Finance as_of=2026-10-25T21:00:00+00:00 freshness=FRESH RSI=46.05 liquidity=7990.67 spike=1.3
- EGTS.CA: score=4.59 buy_ready=False sector_rank=6 price=12.07 support=10.7 resistance=12.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=10876095.0 spike=0.51
- EHDR.CA: score=4.16 buy_ready=False sector_rank=3 price=1.98 support=1.9 resistance=2.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=8508324.0 spike=0.91
- ELEC.CA: score=4.72 buy_ready=False sector_rank=4 price=1.51 support=1.43 resistance=1.53 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=51834240.0 spike=1.04
- ELKA.CA: score=9.7 buy_ready=False sector_rank=3 price=1.39 support=1.21 resistance=1.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=31.65 liquidity=13163929.0 spike=1.02
- ELNA.CA: score=9.96 buy_ready=False sector_rank=3 price=37.2 support=33.46 resistance=39.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=65.45 liquidity=305714.84 spike=0.62
- ELSH.CA: score=2.92 buy_ready=False sector_rank=3 price=9.61 support=8.9 resistance=9.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=7266957.5 spike=0.39
- ELWA.CA: score=11.66 buy_ready=False sector_rank=3 price=1.65 support=1.43 resistance=1.66 source=Yahoo Finance as_of=2026-10-25T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=1288.65 spike=0.0
- EMFD.CA: score=9.59 buy_ready=False sector_rank=6 price=11.63 support=10.6 resistance=13.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=26.84 liquidity=25521870.0 spike=0.45
- ENGC.CA: score=2.61 buy_ready=False sector_rank=3 price=31.27 support=28.93 resistance=31.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=6954708.0 spike=0.64
- EOSB.CA: score=16.1 buy_ready=False sector_rank=3 price=1.61 support=1.56 resistance=1.72 source=Yahoo Finance as_of=2026-10-25T21:00:00+00:00 freshness=FRESH RSI=70.0 liquidity=439274.01 spike=6.71
- EPCO.CA: score=14.66 buy_ready=False sector_rank=3 price=7.21 support=7.0 resistance=10.4 source=Yahoo Finance as_of=2026-10-25T21:00:00+00:00 freshness=FRESH RSI=18.45 liquidity=17136966.02 spike=3.88
- EPPK.CA: score=-3.92 buy_ready=False sector_rank=3 price=10.29 support=10.29 resistance=10.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=8 September 01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=419183.72 spike=0.28
- ETEL.CA: score=9.06 buy_ready=False sector_rank=1 price=123.95 support=117.8 resistance=127.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=423965632.0 spike=1.61
- ETRS.CA: score=16.8 buy_ready=False sector_rank=3 price=10.37 support=9.51 resistance=11.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=42.86 liquidity=18109074.0 spike=1.57
- EXPA.CA: score=3.7 buy_ready=False sector_rank=13 price=13.96 support=13.07 resistance=14.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=15154290.0 spike=0.4
- FAIT.CA: score=6.64 buy_ready=False sector_rank=13 price=42.54 support=40.0 resistance=45.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=38.3 liquidity=2934673.5 spike=0.99
- FAITA.CA: score=5.71 buy_ready=False sector_rank=13 price=0.99 support=0.98 resistance=1.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=51.97 liquidity=6216.88 spike=0.18
- FERC.CA: score=-0.08 buy_ready=False sector_rank=2 price=57.98 support=56.05 resistance=59.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=3117489.25 spike=0.98
- FWRY.CA: score=7.4 buy_ready=False sector_rank=16 price=17.13 support=16.45 resistance=19.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=26.23 liquidity=86505744.0 spike=0.74
- GBCO.CA: score=6.4 buy_ready=False sector_rank=21 price=23.6 support=22.02 resistance=32.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=12.3 liquidity=60071228.0 spike=0.51
- GDWA.CA: score=4.59 buy_ready=False sector_rank=3 price=0.53 support=0.51 resistance=0.53 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=8935478.0 spike=0.63
- GGCC.CA: score=6.36 buy_ready=False sector_rank=3 price=0.54 support=0.51 resistance=0.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=21647612.0 spike=1.35
- GIHD.CA: score=5.72 buy_ready=False sector_rank=3 price=38.73 support=35.25 resistance=39.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=14221600.0 spike=1.03
- GMCI.CA: score=3.95 buy_ready=False sector_rank=3 price=1.48 support=1.47 resistance=1.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=10.53 liquidity=556110.5 spike=1.87
- GRCA.CA: score=-0.88 buy_ready=False sector_rank=3 price=25.3 support=24.02 resistance=25.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=3459492.0 spike=0.71
- GSSC.CA: score=-3.58 buy_ready=False sector_rank=3 price=244.5 support=234.0 resistance=249.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=761257.5 spike=0.62
- GTWL.CA: score=6.16 buy_ready=False sector_rank=3 price=93.13 support=83.01 resistance=95.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=218386240.0 spike=1.25
- HDBK.CA: score=8.96 buy_ready=False sector_rank=13 price=95.91 support=83.01 resistance=112.4 source=Yahoo Finance as_of=2026-10-25T21:00:00+00:00 freshness=FRESH RSI=33.91 liquidity=36018618.24 spike=1.63
- HELI.CA: score=9.93 buy_ready=False sector_rank=6 price=6.39 support=5.72 resistance=7.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=26.37 liquidity=80956352.0 spike=1.17
- HRHO.CA: score=8.04 buy_ready=False sector_rank=12 price=24.04 support=22.8 resistance=27.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=34.17 liquidity=38642496.0 spike=0.3
- ICID.CA: score=0.01 buy_ready=False sector_rank=3 price=16.93 support=15.6 resistance=16.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=4349223.5 spike=0.62
- IDRE.CA: score=6.61 buy_ready=False sector_rank=3 price=32.02 support=30.1 resistance=34.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=9555244.0 spike=1.7
- IFAP.CA: score=0.9 buy_ready=False sector_rank=18 price=16.72 support=15.51 resistance=19.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=14.98 liquidity=3832910.0 spike=0.74
- INFI.CA: score=5.66 buy_ready=False sector_rank=3 price=107.92 support=103.51 resistance=109.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=10419770.0 spike=0.51
- IRON.CA: score=6.52 buy_ready=False sector_rank=2 price=24.92 support=23.53 resistance=32.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=28.16 liquidity=5724836.5 spike=0.54
- ISMA.CA: score=7.26 buy_ready=False sector_rank=3 price=18.55 support=16.33 resistance=18.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=12442040.0 spike=1.8
- ISMQ.CA: score=4.76 buy_ready=False sector_rank=2 price=6.74 support=6.28 resistance=6.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=7958915.5 spike=0.46
- ISPH.CA: score=8.55 buy_ready=False sector_rank=8 price=10.05 support=9.14 resistance=12.03 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=20.97 liquidity=43963600.0 spike=0.95
- JUFO.CA: score=4.73 buy_ready=False sector_rank=14 price=23.3 support=21.91 resistance=23.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=26127482.0 spike=1.58
- KABO.CA: score=9.35 buy_ready=False sector_rank=15 price=6.73 support=5.58 resistance=9.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=31.42 liquidity=44556732.0 spike=1.93
- KWIN.CA: score=1.06 buy_ready=False sector_rank=3 price=52.68 support=49.5 resistance=53.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=5265760.0 spike=1.07
- KZPC.CA: score=-0.23 buy_ready=False sector_rank=3 price=12.75 support=12.1 resistance=12.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=4117385.25 spike=0.56
- LCSW.CA: score=7.23 buy_ready=False sector_rank=7 price=33.49 support=31.2 resistance=33.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=46142168.0 spike=2.32
- LUTS.CA: score=5.86 buy_ready=False sector_rank=3 price=0.59 support=0.53 resistance=0.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=61812808.0 spike=1.1
- MAAL.CA: score=2.22 buy_ready=False sector_rank=3 price=6.25 support=5.65 resistance=6.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=6564155.5 spike=0.46
- MASR.CA: score=10.32 buy_ready=False sector_rank=3 price=6.18 support=5.6 resistance=8.0 source=Yahoo Finance as_of=2026-10-25T21:00:00+00:00 freshness=FRESH RSI=28.05 liquidity=66244549.1 spike=1.33
- MBSC.CA: score=4.59 buy_ready=False sector_rank=7 price=306.42 support=285.5 resistance=309.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=56515964.0 spike=0.53
- MCQE.CA: score=4.59 buy_ready=False sector_rank=7 price=164.34 support=150.0 resistance=165.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=59403456.0 spike=0.84
- MCRO.CA: score=5.92 buy_ready=False sector_rank=3 price=1.23 support=1.17 resistance=1.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=51411312.0 spike=1.13
- MENA.CA: score=1.32 buy_ready=False sector_rank=6 price=5.83 support=5.45 resistance=7.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=25.93 liquidity=2626099.75 spike=1.05
- MEPA.CA: score=14.66 buy_ready=False sector_rank=3 price=1.25 support=1.14 resistance=1.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=17.44 liquidity=73060744.0 spike=10.45
- MFPC.CA: score=21.8 buy_ready=False sector_rank=2 price=45.18 support=40.66 resistance=47.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=45.06 liquidity=39546956.0 spike=0.8
- MFSC.CA: score=-2.46 buy_ready=False sector_rank=3 price=33.22 support=31.02 resistance=33.67 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=1888186.0 spike=0.84
- MHOT.CA: score=0.43 buy_ready=False sector_rank=11 price=14.37 support=13.16 resistance=14.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=6044059.5 spike=0.64
- MICH.CA: score=-1.5 buy_ready=False sector_rank=3 price=40.75 support=39.45 resistance=41.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=2843941.75 spike=0.37
- MILS.CA: score=6.28 buy_ready=False sector_rank=3 price=118.9 support=107.01 resistance=119.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=10158610.0 spike=1.31
- MIPH.CA: score=14.87 buy_ready=False sector_rank=8 price=751.35 support=610.0 resistance=879.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=37.34 liquidity=8103759.5 spike=2.11
- MOED.CA: score=6.06 buy_ready=False sector_rank=3 price=0.45 support=0.41 resistance=0.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=15351919.0 spike=1.2
- MOIL.CA: score=-0.38 buy_ready=False sector_rank=9 price=0.65 support=0.6 resistance=0.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=21.97 liquidity=188892.25 spike=0.87
- MOIN.CA: score=1.87 buy_ready=False sector_rank=3 price=27.89 support=26.4 resistance=28.21 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=6212817.0 spike=0.73
- MOSC.CA: score=4.69 buy_ready=False sector_rank=3 price=234.93 support=221.11 resistance=243.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=6931487.5 spike=2.05
- MPCI.CA: score=5.66 buy_ready=False sector_rank=3 price=275.0 support=256.0 resistance=278.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=90856088.0 spike=0.95
- MPCO.CA: score=3.07 buy_ready=False sector_rank=18 price=1.83 support=1.72 resistance=1.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=80345760.0 spike=0.87
- MPRC.CA: score=5.78 buy_ready=False sector_rank=3 price=31.98 support=28.06 resistance=33.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=17607240.0 spike=1.06
- MTIE.CA: score=2.82 buy_ready=False sector_rank=21 price=7.16 support=6.68 resistance=7.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=25457174.0 spike=1.21
- NAHO.CA: score=-4.33 buy_ready=False sector_rank=3 price=0.13 support=0.12 resistance=0.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=12447.38 spike=0.73
- NCCW.CA: score=5.66 buy_ready=False sector_rank=3 price=5.08 support=4.49 resistance=5.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=14173980.0 spike=0.57
- NEDA.CA: score=2.72 buy_ready=False sector_rank=3 price=2.6 support=2.47 resistance=2.71 source=Yahoo Finance as_of=2026-10-25T21:00:00+00:00 freshness=FRESH RSI=0.0 liquidity=66674.4 spike=0.33
- NHPS.CA: score=2.97 buy_ready=False sector_rank=3 price=54.47 support=51.2 resistance=55.67 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=7315166.0 spike=0.87
- NINH.CA: score=3.25 buy_ready=False sector_rank=3 price=14.01 support=12.92 resistance=14.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=7592513.0 spike=0.75
- NIPH.CA: score=4.55 buy_ready=False sector_rank=8 price=241.81 support=229.0 resistance=243.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=101775232.0 spike=0.84
- OBRI.CA: score=5.66 buy_ready=False sector_rank=3 price=21.41 support=19.91 resistance=21.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=11014135.0 spike=0.75
- OCDI.CA: score=4.59 buy_ready=False sector_rank=6 price=24.0 support=22.09 resistance=24.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=29245978.0 spike=0.79
- OCPH.CA: score=0.7 buy_ready=False sector_rank=3 price=169.47 support=153.88 resistance=170.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=4203421.5 spike=1.42
- ODIN.CA: score=-0.38 buy_ready=False sector_rank=3 price=1.91 support=1.81 resistance=1.92 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=3962114.0 spike=0.67
- OFH.CA: score=5.66 buy_ready=False sector_rank=3 price=0.7 support=0.66 resistance=0.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=24119184.0 spike=0.62
- OIH.CA: score=3.34 buy_ready=False sector_rank=17 price=1.66 support=1.54 resistance=1.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=41914448.0 spike=0.71
- OLFI.CA: score=7.16 buy_ready=False sector_rank=14 price=19.34 support=17.86 resistance=22.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=17.9 liquidity=9590502.0 spike=0.62
- ORAS.CA: score=4.6 buy_ready=False sector_rank=5 price=818.86 support=780.0 resistance=830.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=343100416.0 spike=1.0
- ORHD.CA: score=5.21 buy_ready=False sector_rank=6 price=9.68 support=9.15 resistance=10.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=155435056.0 spike=1.31
- ORWE.CA: score=8.65 buy_ready=False sector_rank=15 price=24.01 support=22.62 resistance=28.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=22.61 liquidity=41809648.0 spike=1.08
- PHAR.CA: score=10.81 buy_ready=False sector_rank=8 price=97.1 support=90.2 resistance=119.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=17.65 liquidity=95138176.0 spike=1.63
- PHDC.CA: score=8.59 buy_ready=False sector_rank=6 price=11.79 support=11.0 resistance=13.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=25.63 liquidity=57043692.0 spike=0.6
- PHTV.CA: score=1.61 buy_ready=False sector_rank=3 price=322.68 support=300.0 resistance=360.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=33.19 liquidity=958309.38 spike=0.99
- POUL.CA: score=9.77 buy_ready=False sector_rank=14 price=9.03 support=8.81 resistance=10.81 source=Yahoo Finance as_of=2026-10-25T21:00:00+00:00 freshness=FRESH RSI=31.72 liquidity=62778770.49 spike=1.1
- PRCL.CA: score=4.75 buy_ready=False sector_rank=7 price=20.01 support=18.38 resistance=20.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=10489108.0 spike=1.08
- PRDC.CA: score=4.59 buy_ready=False sector_rank=6 price=6.25 support=5.7 resistance=6.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=16987526.0 spike=0.48
- PRMH.CA: score=-2.24 buy_ready=False sector_rank=3 price=1.87 support=1.78 resistance=1.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=2103026.5 spike=0.69
- RACC.CA: score=9.97 buy_ready=False sector_rank=3 price=7.16 support=6.1 resistance=9.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=21.15 liquidity=9596348.0 spike=1.36
- RAKT.CA: score=13.55 buy_ready=False sector_rank=3 price=22.5 support=20.26 resistance=25.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=53.67 liquidity=655919.31 spike=1.62
- RAYA.CA: score=4.38 buy_ready=False sector_rank=10 price=5.57 support=5.28 resistance=5.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=15549582.0 spike=0.64
- RMDA.CA: score=5.17 buy_ready=False sector_rank=8 price=5.08 support=4.8 resistance=5.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=33585028.0 spike=1.31
- ROTO.CA: score=10.28 buy_ready=False sector_rank=3 price=29.29 support=25.0 resistance=42.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=22.34 liquidity=10515284.0 spike=1.31
- RREI.CA: score=7.34 buy_ready=False sector_rank=3 price=2.44 support=2.29 resistance=2.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=14865112.0 spike=1.84
- RTVC.CA: score=3.09 buy_ready=False sector_rank=3 price=3.02 support=2.89 resistance=3.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=11.11 liquidity=2997590.5 spike=1.22
- RUBX.CA: score=5.66 buy_ready=False sector_rank=3 price=12.91 support=11.59 resistance=13.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=74822120.0 spike=0.9
- SAUD.CA: score=6.7 buy_ready=False sector_rank=13 price=20.02 support=19.3 resistance=23.95 source=Yahoo Finance as_of=2026-10-25T21:00:00+00:00 freshness=FRESH RSI=20.96 liquidity=8995146.37 spike=0.77
- SCEM.CA: score=5.81 buy_ready=False sector_rank=7 price=83.26 support=77.01 resistance=83.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=92056336.0 spike=1.61
- SCFM.CA: score=-0.94 buy_ready=False sector_rank=3 price=188.22 support=168.5 resistance=195.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=2581742.25 spike=1.41
- SCTS.CA: score=16.12 buy_ready=False sector_rank=19 price=519.98 support=410.0 resistance=588.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=39.73 liquidity=8147731.0 spike=2.56
- SDTI.CA: score=17.23 buy_ready=False sector_rank=3 price=81.09 support=75.01 resistance=94.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=43.77 liquidity=8577843.0 spike=0.41
- SEIG.CA: score=-3.32 buy_ready=False sector_rank=3 price=161.52 support=155.5 resistance=164.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=1025068.44 spike=0.49
- SIPC.CA: score=5.66 buy_ready=False sector_rank=3 price=4.44 support=4.11 resistance=4.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=31417288.0 spike=0.54
- SKPC.CA: score=10.8 buy_ready=False sector_rank=2 price=14.71 support=14.01 resistance=16.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=27.59 liquidity=54483100.0 spike=0.88
- SMFR.CA: score=-2.53 buy_ready=False sector_rank=3 price=181.36 support=169.0 resistance=188.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=1815470.38 spike=0.61
- SNFC.CA: score=4.61 buy_ready=False sector_rank=3 price=10.71 support=10.08 resistance=11.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=28.57 liquidity=4951690.0 spike=0.63
- SPIN.CA: score=7.21 buy_ready=False sector_rank=15 price=14.32 support=12.0 resistance=17.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=29.34 liquidity=8582543.0 spike=1.57
- SPMD.CA: score=9.42 buy_ready=False sector_rank=3 price=0.34 support=0.32 resistance=0.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=32400078.0 spike=2.88
- SVCE.CA: score=5.66 buy_ready=False sector_rank=3 price=8.66 support=8.01 resistance=8.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=55575088.0 spike=0.79
- SWDY.CA: score=4.8 buy_ready=False sector_rank=4 price=109.03 support=103.4 resistance=110.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=66326280.0 spike=1.08
- TALM.CA: score=7.86 buy_ready=False sector_rank=19 price=18.03 support=17.0 resistance=23.5 source=Yahoo Finance as_of=2026-10-25T21:00:00+00:00 freshness=FRESH RSI=6.11 liquidity=16952509.82 spike=0.6
- TMGH.CA: score=16.03 buy_ready=False sector_rank=6 price=82.67 support=80.01 resistance=93.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=35.92 liquidity=306956448.0 spike=1.22
- TRTO.CA: score=1.02 buy_ready=False sector_rank=3 price=0.06 support=0.05 resistance=0.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=27.78 liquidity=8364.05 spike=1.18
- UEFM.CA: score=1.23 buy_ready=False sector_rank=3 price=446.64 support=407.57 resistance=550.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=23.58 liquidity=1571237.13 spike=0.55
- UEGC.CA: score=5.66 buy_ready=False sector_rank=3 price=1.4 support=1.32 resistance=1.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=37773132.0 spike=0.83
- UNIP.CA: score=4.11 buy_ready=False sector_rank=3 price=0.28 support=0.27 resistance=0.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=8372512.0 spike=1.04
- UNIT.CA: score=5.47 buy_ready=False sector_rank=6 price=16.69 support=15.06 resistance=19.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=35.8 liquidity=874179.44 spike=0.22
- WCDF.CA: score=0.63 buy_ready=False sector_rank=3 price=480.22 support=432.5 resistance=652.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=13.93 liquidity=975116.25 spike=0.39
- WKOL.CA: score=2.9 buy_ready=False sector_rank=3 price=235.0 support=225.01 resistance=236.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=7241543.0 spike=0.97
- ZEOT.CA: score=0.86 buy_ready=False sector_rank=3 price=10.25 support=9.7 resistance=10.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=5199648.5 spike=0.64
- ZMID.CA: score=4.59 buy_ready=False sector_rank=6 price=6.41 support=6.05 resistance=6.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=67384584.0 spike=0.99

## Backtesting Lite
- ABUK.CA: 180d return=44.57%, max drawdown=-26.86%, MA20>MA50 days last20=20, as_of=2026-10-25T21:00:00+00:00
- MFPC.CA: 180d return=46.58%, max drawdown=-26.33%, MA20>MA50 days last20=20, as_of=2026-10-25T21:00:00+00:00
- COMI.CA: 180d return=-5.14%, max drawdown=-18.04%, MA20>MA50 days last20=0, as_of=2026-10-25T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- ABUK.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Abu Qir Fertilizers summary=Abu Qir Fertilizers generates EGP 5.6bn net profits in Q1-26 unaudited results; Abu Qir Fertilizers&#39; board approves $5.6m coated urea project; Abu Qir Fertilizers&#39; profits exceed EGP 5.1bn in H1-25/26
  - Abu Qir Fertilizers generates EGP 5.6bn net profits in Q1-26 unaudited results: https://english.mubasher.info/news/4604919/Abu-Qir-Fertilizers-generates-EGP-5-6bn-net-profits-in-Q1-26-unaudited-results/
  - Abu Qir Fertilizers&#39; board approves $5.6m coated urea project: https://english.mubasher.info/news/4585599/Abu-Qir-Fertilizers-board-approves-5-6m-coated-urea-project/
  - Abu Qir Fertilizers&#39; profits exceed EGP 5.1bn in H1-25/26: https://english.mubasher.info/news/4554415/Abu-Qir-Fertilizers-profits-exceed-EGP-5-1bn-in-H1-25-26/
- MFPC.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Misr Fertilizers Production summary=Evidence rejected for MFPC.CA: source text did not clearly match MFPC.CA / Misr Fertilizers Production.
- COMI.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Commercial International Bank Egypt summary=Evidence rejected for COMI.CA: source text did not clearly match COMI.CA / Commercial International Bank Egypt.
- AMOC.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Alexandria Mineral Oils summary=AMOC achieves EGP 10.5bn consolidated sales in Q1-26; AMOC studies potential project with Germany’s SULZER; AMOC to pay out EGP 0.4/shr dividends for H2-25
  - AMOC achieves EGP 10.5bn consolidated sales in Q1-26: https://english.mubasher.info/news/4604903/AMOC-achieves-EGP-10-5bn-consolidated-sales-in-Q1-26/
  - AMOC studies potential project with Germany’s SULZER: https://english.mubasher.info/news/4586853/AMOC-studies-potential-project-with-Germany-s-SULZER/
  - AMOC to pay out EGP 0.4/shr dividends for H2-25: https://english.mubasher.info/news/4586775/AMOC-to-pay-out-EGP-0-4-shr-dividends-for-H2-25/
- SDTI.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=SHARM DREAMS Co. for Touristic Investment S.A.E summary=Sharm Dreams stock maintains strong uptrend - Analysis; Sharm Dreams stock is experiencing sideways movement amid anticipation of next trend – Analysis; Sharm Dreams stock hits historic level halting driving buying force
  - Sharm Dreams stock maintains strong uptrend - Analysis: https://english.mubasher.info/news/4577977/Sharm-Dreams-stock-maintains-strong-uptrend-Analysis/
  - Sharm Dreams stock is experiencing sideways movement amid anticipation of next trend – Analysis: https://english.mubasher.info/news/4547831/Sharm-Dreams-stock-is-experiencing-sideways-movement-amid-anticipation-of-next-trend-Analysis/
  - Sharm Dreams stock hits historic level halting driving buying force: https://english.mubasher.info/news/4529096/Sharm-Dreams-stock-hits-historic-level-halting-driving-buying-force/
- ETRS.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Egyptian Transport and Commercial Services Company S.A.E. summary=Evidence rejected for ETRS.CA: source text did not clearly match ETRS.CA / Egyptian Transport and Commercial Services Company S.A.E..
- EAST.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Eastern Company summary=Evidence rejected for EAST.CA: source text did not clearly match EAST.CA / Eastern Company.
- SCTS.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Suez Canal Company for Technology Settling summary=Suez Canal Technology’s consolidated net profits cross EGP 1.5bn in H1-25/26; Suez Canal Technology’s shareholders greenlight EGP 11/shr dividends; Suez Canal Technology logs EGP 1.3bn consolidated profits in FY23/24
  - Suez Canal Technology’s consolidated net profits cross EGP 1.5bn in H1-25/26: https://english.mubasher.info/news/4600018/Suez-Canal-Technology-s-consolidated-net-profits-cross-EGP-1-5bn-in-H1-25-26/
  - Suez Canal Technology’s shareholders greenlight EGP 11/shr dividends: https://english.mubasher.info/news/4463096/Suez-Canal-Technology-s-shareholders-greenlight-EGP-11-shr-dividends/
  - Suez Canal Technology logs EGP 1.3bn consolidated profits in FY23/24: https://english.mubasher.info/news/4366060/Suez-Canal-Technology-logs-EGP-1-3bn-consolidated-profits-in-FY23-24/

## Warnings
- OpenRouter API error: 404
- Evidence for ABUK.CA matches the company but no source/report date was detected.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence rejected for MFPC.CA: source text did not clearly match MFPC.CA / Misr Fertilizers Production.
- Evidence rejected for COMI.CA: source text did not clearly match COMI.CA / Commercial International Bank Egypt.
- Evidence for AMOC.CA matches the company but no source/report date was detected.
- Evidence for SDTI.CA matches the company but no source/report date was detected.
- Evidence rejected for ETRS.CA: source text did not clearly match ETRS.CA / Egyptian Transport and Commercial Services Company S.A.E..
- Evidence rejected for EAST.CA: source text did not clearly match EAST.CA / Eastern Company.
- Evidence for SCTS.CA matches the company but no source/report date was detected.
