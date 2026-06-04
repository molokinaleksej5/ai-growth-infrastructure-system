import requests
from app.config import settings
class TelegramNotifyService:
    def send_message(self, text: str):
        if not settings.telegram_bot_token or not settings.telegram_admin_chat_id or settings.telegram_bot_token == 'your_telegram_bot_token': return False
        url=f"https://api.telegram.org/bot{settings.telegram_bot_token}/sendMessage"
        try:
            requests.post(url,json={"chat_id":settings.telegram_admin_chat_id,"text":text,"parse_mode":"HTML"},timeout=10)
            return True
        except Exception: return False
    def notify_new_lead(self, lead_title: str, score: float, source_url: str|None=None):
        return self.send_message(f"<b>New AI Lead</b>\n\nLead: {lead_title}\nScore: {score}\nSource: {source_url or 'not provided'}")
