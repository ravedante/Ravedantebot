from keep_alive import keep_alive
keep_alive()

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import os
import asyncio

BOT_TOKEN = "8072106293:AAFZLW8HHoG8qHV9q_9iYzE4etVyVCDKaJM"
WEBHOOK_URL = f"https://ravedantebot.onrender.com/{BOT_TOKEN}"

# /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🤖 Bot online via Webhook!")

# Quando o usuário enviar um vídeo ou documento
async def handle_video(update: Update, context: ContextTypes.DEFAULT_TYPE):
    file = update.message.video or update.message.document
    if file:
        file_name = file.file_name or "sem_nome.mp4"
        file_size = file.file_size / (1024 * 1024)
        await update.message.reply_text(
            f"🎬 Recebi o arquivo:\n📁 Nome: {file_name}\n📦 Tamanho: {file_size:.2f} MB"
        )
    else:
        await update.message.reply_text("❌ Não foi possível processar o arquivo.")

# App
app = ApplicationBuilder().token(BOT_TOKEN).build()

# Handlers
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.VIDEO | filters.Document.VIDEO, handle_video))

# Webhook setup
async def setup():
    await app.bot.set_webhook(WEBHOOK_URL)

asyncio.run(setup())

PORT = int(os.environ.get("PORT", 8080))
app.run_webhook(
    listen="0.0.0.0",
    port=PORT,
    webhook_url=WEBHOOK_URL
)
