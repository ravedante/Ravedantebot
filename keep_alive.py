from flask import Flask, request
import threading

# Substitua esse token pelo mesmo que você usa em bot.py
BOT_TOKEN = "8072106293:AAFZLW8HHoG8qHV9q_9iYzE4etVyVCDKaJM"

app = Flask('')

# Página raiz, usada pelo UptimeRobot para manter o bot vivo
@app.route('/')
def home():
    return "✅ Bot está vivo!"

# Rota onde o Telegram envia as atualizações (webhook)
@app.route(f'/{BOT_TOKEN}', methods=['POST'])
def webhook():
    return "📬 Webhook recebido com sucesso", 200

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = threading.Thread(target=run)
    t.start()
