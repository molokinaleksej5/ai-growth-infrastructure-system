from telegram import Update
from telegram.ext import ContextTypes

from api_client import BackendClient
from keyboards import *
from formatters import (
    format_lead_card,
    format_pipeline_summary,
    format_market_signal,
    format_content_item,
    format_proposal,
    format_outreach_sequence,
    format_ai_error,
)

client = BackendClient()


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "AI Growth Infrastructure System\n\nCRM-панель управления:",
        reply_markup=main_menu_keyboard()
    )


async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query
    await q.answer()
    data = q.data

    if data == "menu":
        await q.message.reply_text(
            "Главное меню:",
            reply_markup=main_menu_keyboard()
        )
        return

    if data == "leads:list":
        leads = client.get_leads()

        if not leads:
            await q.message.reply_text("Лидов пока нет.")
            return

        await q.message.reply_text(
            "Lead Hunter AI\n\nПоследние лиды:",
            reply_markup=leads_list_keyboard(leads)
        )
        return

    if data.startswith("lead:view:"):
        lead_id = int(data.split(":")[2])
        leads = client.get_leads()
        lead = next((x for x in leads if x["id"] == lead_id), None)

        if not lead:
            await q.message.reply_text("Лид не найден.")
            return

        await q.message.reply_text(
            format_lead_card(lead),
            reply_markup=lead_card_keyboard(lead_id)
        )
        return

    if data.startswith("lead:status:"):
        _, _, lead_id, status = data.split(":")
        result = client.update_lead_status(int(lead_id), status)

        await q.message.reply_text(
            f"Lead Hunter AI\n\nСтатус лида #{lead_id}: {result.get('status')}"
        )
        return

    if data == "hunt:menu":
        await q.message.reply_text(
            "Lead Hunter AI\n\nВыберите сценарий поиска:",
            reply_markup=hunt_menu_keyboard()
        )
        return

    if data.startswith("hunt:run:"):
        _, _, search_query, region = data.split(":", 3)

        await q.message.reply_text(
            f"Lead Hunter AI\n\nЗапущен поиск.\nЗапрос: {search_query}\nРегион: {region}"
        )

        leads = client.hunt_leads(search_query, region)

        await q.message.reply_text(
            f"Lead Hunter AI\n\nПоиск завершен.\nНайдено лидов: {len(leads)}"
        )
        return

    if data == "outreach:menu":
        await q.message.reply_text(
            "Outreach AI:",
            reply_markup=outreach_menu_keyboard()
        )
        return

    if data == "outreach:create_default":
        campaign = client.create_campaign(
            "Default AI Automation Outreach",
            "We help B2B companies automate sales, operations and client acquisition using AI agents.",
            "USA / Europe / UAE",
            "B2B SaaS, IT services, startups"
        )

        context.user_data["campaign_id"] = campaign["id"]

        await q.message.reply_text(
            f"Outreach AI\n\nКампания создана.\nID: #{campaign['id']}\nНазвание: {campaign.get('name')}"
        )
        return

    if data.startswith("outreach:generate:"):
        _, _, lead_id, channel = data.split(":")

        sequence = client.generate_sequence(
            context.user_data.get("campaign_id", 1),
            int(lead_id),
            channel
        )

        for item in sequence:
            item["message"] = format_ai_error(item.get("message", ""))

        await q.message.reply_text(
            format_outreach_sequence(sequence)[:3900]
        )
        return

    if data == "outreach:sequences":
        sequences = client.get_sequences()

        if not sequences:
            await q.message.reply_text("Outreach AI\n\nСообщений пока нет.")
            return

        for item in sequences:
            item["message"] = format_ai_error(item.get("message", ""))

        await q.message.reply_text(
            format_outreach_sequence(sequences[:5])[:3900]
        )
        return

    if data == "market:menu":
        await q.message.reply_text(
            "Market Intelligence AI:",
            reply_markup=market_menu_keyboard()
        )
        return

    if data == "market:create:usa_ai":
        watch = client.create_market_watch(
            "USA AI Automation Market Watch",
            "USA",
            "AI automation and software outsourcing",
            "AI automation, software outsourcing, contractors, B2B SaaS"
        )

        signals = client.run_market_watch(watch["id"])

        await q.message.reply_text(
            f"Market Intelligence AI\n\nWatch создан.\nID: #{watch['id']}\nСигналов: {len(signals)}"
        )
        return

    if data == "market:signals":
        signals = client.get_market_signals()

        if not signals:
            await q.message.reply_text("Market Intelligence AI\n\nСигналов пока нет.")
            return

        text = "Market Intelligence AI\n\n"

        for signal in signals[:5]:
            text += format_market_signal(signal)
            text += "\n\n"

        await q.message.reply_text(text[:3900])
        return

    if data == "content:menu":
        await q.message.reply_text(
            "Content AI Engine:",
            reply_markup=content_menu_keyboard()
        )
        return

    if data == "content:create_plan":
        plan = client.create_content_plan(
            "AI Automation B2B Content Plan",
            "B2B founders, CEOs, sales leaders",
            "AI automation and software outsourcing",
            "USA / Europe / UAE",
            "Generate trust and attract B2B leads."
        )

        context.user_data["content_plan_id"] = plan["id"]

        topics = format_ai_error(plan.get("topics", ""))

        await q.message.reply_text(
            f"Content AI Engine\n\nКонтент-план создан.\nID: #{plan['id']}\nНазвание: {plan.get('name')}\n\nТемы:\n{topics[:2500]}"
        )
        return

    if data.startswith("content:generate:"):
        content_type = data.split(":")[2]

        item = client.generate_content(
            context.user_data.get("content_plan_id", 1),
            content_type,
            "Why B2B companies should automate lead qualification with AI"
        )

        item["text"] = format_ai_error(item.get("text", ""))

        await q.message.reply_text(
            format_content_item(item)[:3900]
        )
        return

    if data == "content:items":
        items = client.get_content_items()

        if not items:
            await q.message.reply_text("Content AI Engine\n\nМатериалов пока нет.")
            return

        text = ""

        for item in items[:5]:
            item["text"] = format_ai_error(item.get("text", ""))
            text += format_content_item(item)
            text += "\n\n"

        await q.message.reply_text(text[:3900])
        return

    if data == "analytics:menu":
        await q.message.reply_text(
            "CRM Brain & Analytics:",
            reply_markup=analytics_menu_keyboard()
        )
        return

    if data == "analytics:summary":
        analytics = client.get_analytics()

        await q.message.reply_text(
            format_pipeline_summary(analytics)[:3900]
        )
        return

    if data == "analytics:recommendations":
        recommendations = client.get_recommendations()

        if not recommendations:
            await q.message.reply_text("CRM Brain & Analytics\n\nРекомендаций пока нет.")
            return

        text = "CRM Brain & Analytics\n\nAI-рекомендации:\n\n"

        for item in recommendations[:7]:
            text += f"Лид #{item.get('lead_id')}\n"
            text += f"{item.get('title')}\n"
            text += f"Score: {item.get('score')}\n"
            text += f"Статус: {item.get('status')}\n"
            text += f"Приоритет: {item.get('priority')}\n"
            text += f"Следующее действие: {item.get('next_action')}\n"
            text += f"Причина: {item.get('reason')}\n\n"

        await q.message.reply_text(text[:3900])
        return

    if data == "analytics:report":
        report = client.get_management_report().get("report", "")
        report = format_ai_error(report)

        await q.message.reply_text(
            f"CRM Brain & Analytics\n\nManagement Report:\n\n{report[:3500]}"
        )
        return

    if data.startswith("proposal:generate:"):
        lead_id = int(data.split(":")[2])
        proposal = client.generate_proposal(lead_id)

        proposal["roi_analysis"] = format_ai_error(proposal.get("roi_analysis", ""))
        proposal["full_text"] = format_ai_error(proposal.get("full_text", ""))

        await q.message.reply_text(
            format_proposal(proposal)[:3900]
        )
        return

    if data == "proposal:list":
        proposals = client.get_proposals()

        if not proposals:
            await q.message.reply_text("Proposal & Sales AI\n\nКоммерческих предложений пока нет.")
            return

        text = "Proposal & Sales AI\n\nПоследние КП:\n\n"

        for proposal in proposals[:5]:
            proposal["roi_analysis"] = format_ai_error(proposal.get("roi_analysis", ""))
            proposal["full_text"] = format_ai_error(proposal.get("full_text", ""))
            text += format_proposal(proposal)
            text += "\n\n"

        await q.message.reply_text(text[:3900])
        return