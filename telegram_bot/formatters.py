def safe(value, default="—"):
    return value if value not in [None, "", []] else default


def format_lead_card(lead: dict) -> str:
    return f"""
Лид #{lead.get("id")}

{safe(lead.get("title"))}

Регион: {safe(lead.get("region"))}
Score: {safe(lead.get("score"))}
Статус: {safe(lead.get("status"))}
Источник: {safe(lead.get("source"))}
URL: {safe(lead.get("source_url"))}
""".strip()


def format_pipeline_summary(data: dict) -> str:
    return f"""
CRM Brain & Analytics

Всего лидов: {data.get("total_leads", 0)}
Новые: {data.get("new", 0)}
Contacted: {data.get("contacted", 0)}
Qualified: {data.get("qualified", 0)}
Proposal prepared: {data.get("proposal_prepared", 0)}
Proposal sent: {data.get("proposal_sent", 0)}
Won: {data.get("won", 0)}
Lost: {data.get("lost", 0)}

Горячие лиды: {data.get("high_score_leads", 0)}
Средний score: {data.get("average_score", 0)}
""".strip()


def format_market_signal(signal: dict) -> str:
    return f"""
Market Intelligence AI

Сигнал #{signal.get("id")}

{safe(signal.get("title"))}

Регион: {safe(signal.get("region"))}
Ниша: {safe(signal.get("niche"))}
Тип сигнала: {safe(signal.get("signal_type"))}
Score: {safe(signal.get("opportunity_score"))}

Описание:
{safe(signal.get("description"))}

Источник:
{safe(signal.get("source_url"))}
""".strip()


def format_content_item(item: dict) -> str:
    return f"""
Content AI Engine

Материал #{item.get("id")}

Тип: {safe(item.get("content_type"))}
Тема: {safe(item.get("topic"))}
Статус: {safe(item.get("status"))}

Текст:
{safe(item.get("text"))}
""".strip()


def format_proposal(proposal: dict) -> str:
    return f"""
Proposal & Sales AI

КП #{proposal.get("id")}

Лид: #{proposal.get("lead_id")}
Название: {safe(proposal.get("title"))}
Статус: {safe(proposal.get("status"))}

Pricing:
{safe(proposal.get("pricing"))}

Roadmap:
{safe(proposal.get("roadmap"))}

ROI Analysis:
{safe(proposal.get("roi_analysis"))}

Текст КП:
{safe(proposal.get("full_text"))}
""".strip()


def format_outreach_sequence(items: list[dict]) -> str:
    text = "Outreach AI\n\n"

    for item in items:
        text += f"Шаг {item.get('step_number')} | {item.get('channel')}\n"

        if item.get("subject"):
            text += f"Тема: {item.get('subject')}\n"

        text += f"{safe(item.get('message'))}\n\n"

    return text.strip()


def format_ai_error(text: str) -> str:
    if "insufficient_quota" in text or "429" in text:
        return "AI-сервис временно недоступен. Функция запущена, данные сохранены, но текст AI не сформирован из-за ограничения API."

    return text