from telegram.ext import Application, CommandHandler, CallbackQueryHandler
from config import BOT_TOKEN
from handlers import start, button_handler
def main():
    if not BOT_TOKEN or BOT_TOKEN == 'your_telegram_bot_token':
        print('TELEGRAM_BOT_TOKEN is not configured. Bot is disabled.'); return
    app=Application.builder().token(BOT_TOKEN).build(); app.add_handler(CommandHandler('start',start)); app.add_handler(CallbackQueryHandler(button_handler)); app.run_polling()
if __name__=='__main__': main()
