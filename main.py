import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Configuração de Logs
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Caminho do arquivo da imagem salva na raiz do GitHub
PHOTO_PATH = "banner.png"

# Link do seu grupo
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

    # Abre o arquivo de imagem do próprio servidor (sem depender de URL)
    if os.path.exists(PHOTO_PATH):
        with open(PHOTO_PATH, 'rb') as photo_file:
            await context.bot.send_photo(
                chat_id=update.effective_chat.id,
                photo=photo_file,
                caption=caption_text,
                reply_markup=reply_markup
            )
    else:
        # Se por algum motivo o arquivo não estiver lá, envia o texto com o botão
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=caption_text,
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
