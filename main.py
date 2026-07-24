import os
import uuid
from threading import Thread
from http.server import HTTPServer, BaseHTTPRequestHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, InlineQueryResultPhoto
from telegram.ext import Application, InlineQueryHandler

# Servidor simples para o Render aceitar o plano Free
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot Ativo!")

def run_server():
    port = int(os.environ.get("PORT", 8080))
    server = HTTPServer(('0.0.0.0', port), SimpleHTTPRequestHandler)
    server.serve_forever()

TOKEN = os.environ.get("TELEGRAM_TOKEN")
LINK_DO_GRUPO = "https://t.me/tipslucrativas1"
URL_DA_IMAGEM = "https://i.imgur.com/vH9XgGj.png"

async def inline_query(update, context):
    keyboard = [
        [
            InlineKeyboardButton(
                "CLIQUE AQUI E ACESSE O GRUPO GRATUITO", 
                url=LINK_DO_GRUPO
            )
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    results = [
        InlineQueryResultPhoto(
            id=str(uuid.uuid4()),
            photo_url=URL_DA_IMAGEM,
            thumbnail_url=URL_DA_IMAGEM,
            caption="",
            reply_markup=reply_markup
        )
    ]

    await update.inline_query.answer(results, cache_time=1)

def main():
    if not TOKEN:
        raise ValueError("O token do Telegram nao foi configurado.")

    Thread(target=run_server, daemon=True).start()

    app = Application.builder().token(TOKEN).build()
    app.add_handler(InlineQueryHandler(inline_query))

    print("Bot rodando em modo inline...")
    app.run_polling()

if __name__ == "__main__":
    main()
