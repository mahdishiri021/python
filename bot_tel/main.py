
import setup  # اجرای اسکریپت نصب اتوماتیک

import asyncio
from datetime import datetime
import pytz
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
from dotenv import load_dotenv
import os

load_dotenv()
bot_token = os.getenv("TELEGRAM_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "سلام! برای دریافت ساعت محلی یک شهر، نام شهر را وارد کنید.\nمثال: London, Tehran, New York"
    )

async def get_time(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    city = update.message.text.strip()
    
    city_mapping = {
        "tehran": "Asia/Tehran",
        "london": "Europe/London",
        "new york": "America/New_York",
        "tokyo": "Asia/Tokyo",
        "paris": "Europe/Paris",
    }

    city = city_mapping.get(city.lower(), city)
    try:
        timezone = pytz.timezone(city)
        local_time = datetime.now(timezone).strftime('%Y/%m/%d %H:%M:%S')
        await update.message.reply_text(f'زمان محلی در {city}: {local_time}')
    except pytz.UnknownTimeZoneError:
        await update.message.reply_text("❌ نام شهر یا منطقه وارد شده صحیح نیست. لطفاً دوباره امتحان کنید.")

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text='''
            ربات ساعت جهانی 
            بر اساس نام شهری که وارد میکنید زمان محلی آن شهر رو به شما نمایش میدهد
            ممنون از اعتمادتون
        '''
    )

if __name__ == '__main__':
    bot = ApplicationBuilder().token(bot_token).build()
    bot.add_handler(CommandHandler('start', start))
    bot.add_handler(CommandHandler('help', help))
    bot.add_handler(CommandHandler('time', get_time))
    bot.run_polling()
