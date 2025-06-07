from keep_alive import keep_alive
keep_alive()

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os
import asyncio

BOT_TOKEN = "8072106293:AAFZLW8HHoG8qHV9q_9iYzE4etVyVCDKaJM"
WEBHOOK_URL = f"https://ravedantebot.onrender.com/{BOT_TOKEN}"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🤖 Bot online via Webhook!")

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))

async def setup():
    await app.bot.set_webhook(WEBHOOK_URL)

asyncio.run(setup())

PORT = int(os.environ.get("PORT", 8080))
app.run_webhook(
    listen="0.0.0.0",
    port=PORT,
    webhook_url=WEBHOOK_URL
)
