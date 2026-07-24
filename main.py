import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Configuração de Logs
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Link direto da imagem
PHOTO_URL = "https://i.im.ge/2026/07/23/QMbyySK.983f7348-d9bf-4ed7-8258-f540bd437f8c.png"

# Link do seu grupo do Telegram
GROUP_LINK = "https://t.me/tipslucrativas1"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    caption_text = (
        "Parabéns!! Você foi selecionado para acessar o grupo gratuito, "
        "clique abaixo e aproveite!! ⬇️"
    )

    keyboard = [
        [InlineKeyboardButton("ENTRAR NO GRUPO GRATUITO 🚀", url=GROUP_LINK)]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await context.bot.send_photo(
        chat_id=update.effective_chat.id,
        photo=PHOTO_URL,
        caption=caption_text,
        reply_markup=reply_markup
    )

def main():
    token = os.environ.get("TELEGRAM_TOKEN")
    
    if not token:
        raise ValueError("A variável TELEGRAM_TOKEN não foi encontrada!")

    app = ApplicationBuilder().token(token).build()

    app.add_handler(CommandHandler("start", start))

    print("Bot rodando e aguardando /start...")
    app.run_polling()

if __name__ == '__main__':
    main()
