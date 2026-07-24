import os
from threading import Thread
from http.server import HTTPServer, BaseHTTPRequestHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Servidor simples para manter o Render Free ativo
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot esta ativo!")

def run_server():
    port = int(os.environ.get("PORT", 8080))
    server = HTTPServer(('0.0.0.0', port), SimpleHTTPRequestHandler)
    server.serve_forever()

# Dados do bot
TOKEN = os.environ.get("TELEGRAM_TOKEN")
LINK_DO_GRUPO = "https://t.me/tipslucrativas1"

# Link permanente da imagem hospedada no Telegram
URL_DA_IMAGEM = "https://t.me/imagembott/2?single"

# Função acionada quando o usuário envia /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton(
                "CLIQUE AQUI E ACESSE O GRUPO GRATUITO ↗️", 
                url=LINK_DO_GRUPO
            )
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Enviando a foto com o botão embutido
    await context.bot.send_photo(
        chat_id=update.effective_chat.id,
        photo=URL_DA_IMAGEM,
        caption="",
        reply_markup=reply_markup
    )

def main():
    if not TOKEN:
        raise ValueError("O token do Telegram nao foi configurado.")

    Thread(target=run_server, daemon=True).start()

    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))

    print("Bot rodando e aguardando /start...")
    app.run_polling()

if __name__ == "__main__":
    main()
