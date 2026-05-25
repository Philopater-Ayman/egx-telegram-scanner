import json
import re
from datetime import datetime, timezone
from typing import List, Literal, Optional

import requests
from google import genai
from google.genai import types
from pydantic import BaseModel, Field, ValidationError

from config import (
    GEMINI_API_KEY,
    MAX_WATCHLIST_SIZE,
    MODEL_NAME,
    OPENROUTER_API_KEY,
    OPENROUTER_FALLBACK_MODELS,
    OPENROUTER_MODEL,
    USE_GEMINI_GROUNDING,
    USE_OPENROUTER_NARRATIVE,
    get_company_name_map,
    get_yahoo_symbol_map,
)


class TradeRecommendation(BaseModel):
    action: Literal["BUY", "SELL", "HOLD"]
    ticker: Optional[str] = ""
    entry: float = Field(default=0, ge=0)
    take_profit: float = Field(default=0, ge=0)
    stop_loss: float = Field(default=0, ge=0)
    confidence: Literal["LOW", "MEDIUM", "HIGH"] = "LOW"
    trade_reason: str = ""


class DecisionPayload(BaseModel):
    updated_watchlist: List[str]
    watchlist_changes_reason: str
    trade_recommendation: TradeRecommendation


def _hold_decision(current_watchlist, reason):
    return {
        "updated_watchlist": current_watchlist[:MAX_WATCHLIST_SIZE],
        "watchlist_changes_reason": "No AI update applied.",
        "trade_recommendation": {
            "action": "HOLD",
            "ticker": "",
            "entry": 0,
            "take_profit": 0,
            "stop_loss": 0,
            "confidence": "LOW",
            "trade_reason": reason,
        },
    }


def _extract_grounding_items(response):
    items = []
    metadata = getattr(response.candidates[0], "grounding_metadata", None) if getattr(response, "candidates", None) else None
    chunks = getattr(metadata, "grounding_chunks", None) if metadata else None
    if chunks:
        for chunk in chunks[:8]:
            web = getattr(chunk, "web", None)
            if web and getattr(web, "uri", None):
                items.append(
                    {
                        "title": getattr(web, "title", None) or "Grounded source",
                        "url": web.uri,
                        "source": "Gemini Google Search grounding",
                    }
                )
    return items


def _extract_json_object(text):
    match = re.search(r"\{.*\}", text, re.S)
    if not match:
        return None
    try:
        return json.loads(match.group(0))
    except Exception:
        return None


def _openrouter_models():
    models = []
    if OPENROUTER_MODEL:
        models.append(OPENROUTER_MODEL)
    for model in OPENROUTER_FALLBACK_MODELS:
        if model not in models:
            models.append(model)
    return models[:3]


def _coerce_narrative(content):
    parsed = _extract_json_object(content) or {}
    if parsed:
        bullets = parsed.get("bullets") if isinstance(parsed.get("bullets"), list) else []
        return parsed.get("summary", "").strip(), [str(item).strip() for item in bullets if str(item).strip()]

    summary_match = re.search(r'"summary"\s*:\s*"((?:[^"\\]|\\.)*)"', content, re.S)
    summary = ""
    if summary_match:
        try:
            summary = json.loads(f'"{summary_match.group(1)}"')
        except Exception:
            summary = summary_match.group(1)
    bullet_matches = re.findall(r'"([^"]{20,220})"', content)
    bullets = [item for item in bullet_matches if item != summary and "summary" not in item.lower()]
    return summary or content.strip(), bullets[:5]


def _norm_text(value):
    return re.sub(r"[^A-Z0-9]+", " ", str(value or "").upper()).strip()


def _company_terms(company_name):
    stopwords = {
        "THE",
        "AND",
        "FOR",
        "OF",
        "S",
        "SAE",
        "S A E",
        "EGYPT",
        "EGYPTIAN",
        "COMPANY",
        "CO",
        "GROUP",
        "HOLDING",
        "HOLDINGS",
        "INTERNATIONAL",
        "INVESTMENT",
        "INVESTMENTS",
        "DEVELOPMENT",
    }
    terms = []
    for term in re.findall(r"[A-Z0-9]{3,}", _norm_text(company_name)):
        if term not in stopwords and term not in terms:
            terms.append(term)
    return terms[:5]


def _parse_evidence_dates(text):
    text = str(text or "")
    dates = []
    month_map = {
        "JANUARY": 1,
        "FEBRUARY": 2,
        "MARCH": 3,
        "APRIL": 4,
        "MAY": 5,
        "JUNE": 6,
        "JULY": 7,
        "AUGUST": 8,
        "SEPTEMBER": 9,
        "OCTOBER": 10,
        "NOVEMBER": 11,
        "DECEMBER": 12,
        "JAN": 1,
        "FEB": 2,
        "MAR": 3,
        "APR": 4,
        "JUN": 6,
        "JUL": 7,
        "AUG": 8,
        "SEP": 9,
        "SEPT": 9,
        "OCT": 10,
        "NOV": 11,
        "DEC": 12,
    }
    for year, month, day in re.findall(r"\b(20\d{2})[-/](\d{1,2})[-/](\d{1,2})\b", text):
        try:
            dates.append(datetime(int(year), int(month), int(day), tzinfo=timezone.utc))
        except ValueError:
            pass
    month_pattern = "|".join(month_map)
    for month, day, year in re.findall(rf"\b({month_pattern})\.?\s+(\d{{1,2}}),?\s+(20\d{{2}})\b", text, re.I):
        try:
            dates.append(datetime(int(year), month_map[month.upper().rstrip(".")], int(day), tzinfo=timezone.utc))
        except ValueError:
            pass
    for day, month, year in re.findall(rf"\b(\d{{1,2}})\s+({month_pattern})\.?\s+(20\d{{2}})\b", text, re.I):
        try:
            dates.append(datetime(int(year), month_map[month.upper().rstrip(".")], int(day), tzinfo=timezone.utc))
        except ValueError:
            pass
    for year in re.findall(r"\b(20\d{2})\b", text):
        try:
            dates.append(datetime(int(year), 1, 1, tzinfo=timezone.utc))
        except ValueError:
            pass
    return dates


def _evidence_freshness(evidence_text):
    dates = _parse_evidence_dates(evidence_text)
    if not dates:
        return "ACCEPTED_UNDATED", "", ""
    latest = max(dates)
    now = datetime.now(timezone.utc)
    age_days = max(0, (now - latest).days)
    if age_days <= 365:
        return "RECENT_ACCEPTED", latest.date().isoformat(), age_days
    return "OLD_ACCEPTED", latest.date().isoformat(), age_days


def _validate_evidence_packet(ticker, packet, company_name="", yahoo_symbol=""):
    packet = dict(packet or {})
    items = [item for item in packet.get("items", []) if isinstance(item, dict)]
    summary = str(packet.get("summary") or "")
    evidence_text = " ".join(
        [summary]
        + [
            " ".join(str(item.get(key, "")) for key in ("title", "url", "source"))
            for item in items
        ]
    )
    normalized = _norm_text(evidence_text)
    symbol = ticker.replace(".CA", "").upper()
    yahoo_base = str(yahoo_symbol or ticker).replace(".CA", "").upper()
    company = company_name or get_company_name_map().get(ticker, ticker)
    terms = _company_terms(company)
    matched_symbol = symbol in normalized.split() or yahoo_base in normalized.split()
    matched_terms = [term for term in terms if term in normalized]
    accepted = bool(items) and (matched_symbol or len(matched_terms) >= 2)
    packet["expected_company"] = company
    packet["matched_terms"] = ", ".join(([symbol] if matched_symbol else []) + matched_terms)
    packet.setdefault("warnings", [])
    if accepted:
        freshness, latest_date, age_days = _evidence_freshness(evidence_text)
        packet["items"] = items[:3]
        packet["evidence_status"] = freshness
        packet["evidence_latest_date"] = latest_date
        packet["evidence_age_days"] = age_days
        if freshness == "OLD_ACCEPTED":
            packet["warnings"].append(
                f"Evidence for {ticker} matches the company but appears old; latest detected date is {latest_date}."
            )
        elif freshness == "ACCEPTED_UNDATED":
            packet["warnings"].append(f"Evidence for {ticker} matches the company but no source/report date was detected.")
    else:
        packet["items"] = []
        packet["evidence_status"] = "REJECTED_TICKER_MISMATCH"
        packet["evidence_latest_date"] = ""
        packet["evidence_age_days"] = ""
        reason = f"Evidence rejected for {ticker}: source text did not clearly match {ticker} / {company}."
        packet["summary"] = reason
        if reason not in packet["warnings"]:
            packet["warnings"].append(reason)
    return packet


def evidence_from_market_data(ticker, row):
    items = row.get("News_Items") or []
    headlines = row.get("Recent_Headlines") or []
    warnings = []
    source_mode = "YAHOO_NEWS_FALLBACK"
    if not items and not headlines:
        mubasher = mubasher_stock_evidence(ticker)
        items = mubasher.get("items", [])
        headlines = [item.get("title", "") for item in items]
        warnings.extend(mubasher.get("warnings", []))
        source_mode = mubasher.get("source_mode", "MUBASHER_STOCK_PAGE")
    if not items and not headlines:
        warnings.append(f"No Yahoo or Mubasher evidence found for {ticker}.")
    packet = {
        "ticker": ticker,
        "items": items[:3],
        "summary": "; ".join(headlines[:3]) if headlines else "No public fallback evidence found.",
        "warnings": warnings,
        "source_mode": source_mode,
    }
    return _validate_evidence_packet(
        ticker,
        packet,
        company_name=get_company_name_map().get(ticker, ""),
        yahoo_symbol=get_yahoo_symbol_map().get(ticker, ticker),
    )


def mubasher_stock_evidence(ticker):
    symbol = ticker.replace(".CA", "").upper()
    url = f"https://english.mubasher.info/markets/EGX/stocks/{symbol}"
    try:
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=20)
        response.raise_for_status()
        html = response.text
        items = []
        pattern = r'<a[^>]+class="[^"]*(?:mi-home-media-block__title|market-announcement-list__title)[^"]*"[^>]+href="([^"]+)"[^>]*>(.*?)</a>'
        for href, text in re.findall(pattern, html, re.S):
            title = " ".join(re.sub(r"<.*?>", " ", text).split())
            if not title:
                continue
            full_url = href if href.startswith("http") else f"https://english.mubasher.info{href}"
            items.append({"title": title, "url": full_url, "source": "Mubasher stock page"})
            if len(items) >= 3:
                break
        warnings = []
        if not items:
            warnings.append(f"Mubasher stock page returned no evidence titles for {ticker}.")
        return {
            "ticker": ticker,
            "items": items,
            "summary": "; ".join(item["title"] for item in items) if items else "No Mubasher stock-page evidence found.",
            "warnings": warnings,
            "source_mode": "MUBASHER_STOCK_PAGE",
        }
    except Exception as exc:
        return {
            "ticker": ticker,
            "items": [],
            "summary": "Mubasher stock-page evidence failed.",
            "warnings": [f"Mubasher stock-page evidence failed for {ticker}: {exc}"],
            "source_mode": "MUBASHER_STOCK_PAGE_FAILED",
        }


def gather_evidence(ticker, company_context=""):
    if not GEMINI_API_KEY:
        return {
            "ticker": ticker,
            "items": [],
            "summary": "Gemini key missing; no grounded web evidence collected.",
            "warnings": ["Missing GEMINI_API_KEY blocks web evidence."],
        }
    if not USE_GEMINI_GROUNDING:
        return {
            "ticker": ticker,
            "items": [],
            "summary": "Gemini grounding disabled by USE_GEMINI_GROUNDING=false.",
            "warnings": ["Gemini grounding disabled."],
        }

    try:
        client = genai.Client(api_key=GEMINI_API_KEY)
        grounding_tool = types.Tool(google_search=types.GoogleSearch())
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=(
                f"Find recent, relevant public evidence for EGX stock {ticker}. "
                f"Context: {company_context}. Return concise JSON with summary and up to 3 cited source URLs. "
                "Use evidence from the last 12 months when possible. Include the source/report date in each title or summary. "
                "If evidence is not clearly relevant to this ticker, return an empty items list."
            ),
            config=types.GenerateContentConfig(
                tools=[grounding_tool],
                temperature=0.1,
            ),
        )
        raw = response.text.strip()
        data = _extract_json_object(raw) or {}
        items = data.get("items") if isinstance(data.get("items"), list) else []
        grounded_items = _extract_grounding_items(response)
        if grounded_items:
            seen = {item.get("url") for item in items if isinstance(item, dict)}
            items.extend([item for item in grounded_items if item.get("url") not in seen])
        packet = {
            "ticker": ticker,
            "items": items[:3],
            "summary": data.get("summary") or raw[:600] or "Grounded evidence collected.",
            "warnings": [],
            "source_mode": "GEMINI_GROUNDING",
        }
        return _validate_evidence_packet(ticker, packet, company_name=company_context)
    except Exception as exc:
        return {
            "ticker": ticker,
            "items": [],
            "summary": "Grounded evidence retrieval failed.",
            "warnings": [f"Evidence agent failed for {ticker}: {exc}"],
        }


def gather_batch_evidence(candidate_rows):
    packets = {}
    for row in candidate_rows:
        packets[row["Ticker"]] = evidence_from_market_data(row["Ticker"], row)

    if not GEMINI_API_KEY or not USE_GEMINI_GROUNDING or not candidate_rows:
        return packets

    tickers = [row["Ticker"] for row in candidate_rows]
    company_map = get_company_name_map()
    yahoo_map = get_yahoo_symbol_map()
    context = [
        {
            "ticker": row["Ticker"],
            "company": company_map.get(row["Ticker"], row["Ticker"]),
            "yahoo_symbol": yahoo_map.get(row["Ticker"], row["Ticker"]),
            "sector": row.get("Sector"),
            "price": row.get("Current_Price"),
            "rsi": row.get("RSI"),
            "liquidity": row.get("Daily_Liquidity_EGP"),
        }
        for row in candidate_rows
    ]
    try:
        client = genai.Client(api_key=GEMINI_API_KEY)
        grounding_tool = types.Tool(google_search=types.GoogleSearch())
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=(
                "Search the web for recent, ticker-relevant evidence for these EGX candidates. "
                "Prefer official company, exchange, disclosure, financial news, and market pages. "
                "Each evidence item must clearly match the exact ticker and company name in the candidate object. "
                "Reject similarly named US tickers or other EGX tickers. "
                "Use evidence from the last 12 months when possible and include source/report dates in the summary or item titles. "
                "Return a compact JSON object like {\"evidence\":{\"TICKER.CA\":{\"summary\":\"...\",\"items\":[{\"title\":\"...\",\"url\":\"...\"}]}}}. "
                "If evidence is not clearly about the ticker, leave items empty. Candidates: "
                + json.dumps(context)
            ),
            config=types.GenerateContentConfig(
                tools=[grounding_tool],
                temperature=0.1,
            ),
        )
        raw = response.text.strip()
        data = _extract_json_object(raw) or {}
        evidence = data.get("evidence", {}) if isinstance(data.get("evidence"), dict) else {}
        for ticker in tickers:
            packet = evidence.get(ticker, {}) if isinstance(evidence.get(ticker), dict) else {}
            items = packet.get("items") if isinstance(packet.get("items"), list) else []
            if items:
                candidate_packet = {
                    "ticker": ticker,
                    "items": items[:3],
                    "summary": packet.get("summary") or f"Gemini grounding found public sources for {ticker}.",
                    "warnings": [],
                    "source_mode": "GEMINI_BATCH_GROUNDING",
                }
                validated = _validate_evidence_packet(
                    ticker,
                    candidate_packet,
                    company_name=company_map.get(ticker, ""),
                    yahoo_symbol=yahoo_map.get(ticker, ticker),
                )
                if validated.get("items"):
                    packets[ticker] = validated
                else:
                    packets[ticker].setdefault("warnings", []).extend(validated.get("warnings", []))
                    packets[ticker]["evidence_status"] = "REJECTED_TICKER_MISMATCH"
            elif raw and packets[ticker].get("items"):
                packets[ticker]["summary"] = packets[ticker]["summary"] + " Gemini also reviewed web evidence but did not return ticker-specific citations."
        return packets
    except Exception as exc:
        warning = f"Gemini batch evidence failed: {exc}"
        for packet in packets.values():
            packet.setdefault("warnings", []).append(warning)
        return packets


def build_openrouter_narrative(decision, ranked_rows, sector_scores, evidence_packets, warnings):
    if not USE_OPENROUTER_NARRATIVE:
        return {
            "provider": "OpenRouter",
            "status": "DISABLED",
            "model": "",
            "summary": "OpenRouter narrative disabled by USE_OPENROUTER_NARRATIVE=false.",
            "bullets": [],
            "warnings": [],
        }
    if not OPENROUTER_API_KEY:
        return {
            "provider": "OpenRouter",
            "status": "MISSING_KEY",
            "model": "",
            "summary": "OpenRouter key missing; local scanner summary used.",
            "bullets": [],
            "warnings": ["Missing OPENROUTER_API_KEY."],
        }

    top_rows = [
        {
            "ticker": row.get("Ticker"),
            "rank_score": row.get("Rank_Score"),
            "buy_ready": row.get("Buy_Ready"),
            "outlook": row.get("Outlook_Label"),
            "outlook_score": row.get("Outlook_Score"),
            "liquidity_regime": row.get("Liquidity_Regime"),
            "liquidity": row.get("Daily_Liquidity_EGP"),
            "liquidity_spike": row.get("Liquidity_Spike"),
            "support_20d": row.get("Support_20D"),
            "resistance_20d": row.get("Resistance_20D"),
            "support_distance_pct": row.get("Support_Distance_%"),
            "resistance_distance_pct": row.get("Resistance_Distance_%"),
            "rsi": row.get("RSI"),
            "sector": row.get("Sector"),
            "sector_rank": row.get("Sector_Rank"),
            "risk_notes": row.get("Risk_Notes"),
        }
        for row in ranked_rows[:8]
    ]
    evidence_summary = {
        ticker: {
            "source_mode": packet.get("source_mode"),
            "source_count": len(packet.get("items", [])),
            "summary": packet.get("summary", "")[:350],
        }
        for ticker, packet in (evidence_packets or {}).items()
    }
    payload = {
        "role": "telegram_narrative_only_not_trade_decision",
        "primary_ticket": decision.get("trade_recommendation", {}),
        "tickets": decision.get("trade_recommendations", []) or [decision.get("trade_recommendation", {})],
        "top_scanner_rows": top_rows,
        "top_sectors": sorted((sector_scores or {}).values(), key=lambda row: row.get("Sector_Rank", 99))[:5],
        "evidence": evidence_summary,
        "warnings": warnings[:8],
    }
    prompt = (
        "Write a concise Telegram narrative for a personal EGX stock scanner. "
        "Do not make a new trade decision. Do not invent live data. Do not mention quantities or position sizing. "
        "Explain why the local scanner selected these prioritized tickets, what liquidity/sector/support/resistance/outlook means for the next 1-3 days, "
        "and include uncertainty. Return only valid compact JSON with keys summary and bullets, where bullets is 3 to 5 short strings. "
        f"Scanner payload: {json.dumps(payload, default=str)}"
    )
    models = _openrouter_models()
    try:
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                "Content-Type": "application/json",
                "HTTP-Referer": "https://github.com/",
                "X-OpenRouter-Title": "EGX Telegram Scanner",
            },
            json={
                "models": models,
                "route": "fallback",
                "messages": [
                    {
                        "role": "system",
                        "content": "You summarize deterministic stock-scanner output. You are not the trade decision engine.",
                    },
                    {"role": "user", "content": prompt},
                ],
                "temperature": 0.2,
                "max_tokens": 900,
            },
            timeout=45,
        )
        if response.status_code != 200:
            return {
                "provider": "OpenRouter",
                "status": "ERROR",
                "model": models[0] if models else "",
                "summary": "OpenRouter narrative failed; local scanner summary used.",
                "bullets": [],
                "warnings": [f"OpenRouter API error: {response.status_code}"],
            }
        data = response.json()
        message = (data.get("choices") or [{}])[0].get("message", {})
        content = message.get("content") or ""
        summary, bullets = _coerce_narrative(content)
        return {
            "provider": "OpenRouter",
            "status": "OK",
            "model": data.get("model") or (models[0] if models else ""),
            "summary": summary[:700],
            "bullets": [str(item).strip()[:220] for item in bullets[:5] if str(item).strip()],
            "warnings": [],
        }
    except Exception as exc:
        return {
            "provider": "OpenRouter",
            "status": "ERROR",
            "model": models[0] if models else "",
            "summary": "OpenRouter narrative failed; local scanner summary used.",
            "bullets": [],
            "warnings": [f"OpenRouter narrative failed: {exc}"],
        }


def ask_decision_agent(market_data, current_watchlist, egx30_data, evidence_packets):
    if not GEMINI_API_KEY:
        return _hold_decision(current_watchlist, "Gemini key missing; advisor falls back to HOLD.")

    context = {
        "advisor_mode": "ADVISOR_ONLY_NEVER_EXECUTE",
        "ticket_mode": "SIGNAL_ONLY_NO_QUANTITY",
        "current_watchlist": current_watchlist,
        "egx30": egx30_data,
        "market_data": market_data,
        "evidence_packets": evidence_packets,
    }
    system_rules = f"""
You are an advisor-only EGX trading assistant. You never execute trades.
Create one daily recommendation only. Prefer HOLD unless evidence and data quality are strong.
BUY requires fresh price data, liquidity, clear stop loss, clear take profit, and relevant evidence.
Weak evidence, stale data, missing macro data, or missing citations must become HOLD or low-confidence WATCH-like HOLD.
The watchlist can have at most {MAX_WATCHLIST_SIZE} tickers and should avoid more than 2 tickers in one sector.
Return only JSON with this exact shape:
{{
  "updated_watchlist": ["TICKER.CA"],
  "watchlist_changes_reason": "short reason",
  "trade_recommendation": {{
    "action": "BUY" or "SELL" or "HOLD",
    "ticker": "TICKER.CA",
    "entry": 0,
    "take_profit": 0,
    "stop_loss": 0,
    "confidence": "LOW" or "MEDIUM" or "HIGH",
    "trade_reason": "reason with data source quality and manual Thndr instruction"
  }}
}}
"""
    try:
        client = genai.Client(api_key=GEMINI_API_KEY)
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=json.dumps(context, default=str),
            config=types.GenerateContentConfig(
                system_instruction=system_rules,
                temperature=0.2,
                response_mime_type="application/json",
            ),
        )
        raw = response.text.strip()
        payload = DecisionPayload.model_validate_json(raw)
        return payload.model_dump()
    except (ValidationError, json.JSONDecodeError, Exception) as exc:
        return _hold_decision(current_watchlist, f"AI decision output invalid or unavailable; safe HOLD fallback. Details: {exc}")
