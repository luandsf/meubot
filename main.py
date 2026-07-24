import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Configuração de Logs
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

PHOTO_FILENAME = "banner.png"
GROUP_LINK = "https://t.me/tipslucrativas1"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    
    caption_text = (
        "Parabéns!! Você foi selecionado para acessar o grupo gratuito, "
        "clique abaixo e aproveite!! ⬇️"
    )

    keyboard = [
        [InlineKeyboardButton("ENTRAR NO GRUPO GRATUITO 🚀", url=GROUP_LINK)]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    try:
        base_path = os.path.dirname(os.path.abspath(__file__))
        photo_path = os.path.join(base_path, PHOTO_FILENAME)

        if os.path.exists(photo_path):
            with open(photo_path, 'rb') as photo_file:
                # send_photo envia como imagem visualizável no chat
                await context.bot.send_photo(
                    chat_id=chat_id,
                    photo=photo_file,
                    caption=caption_text,
                    reply_markup=reply_markup
                )
                logging.info("Banner enviado como imagem com sucesso!")
        else:
            logging.error(f"Arquivo não encontrado no caminho: {photo_path}")
            await context.bot.send_message(
                chat_id=chat_id,
                text=caption_text,
                reply_markup=reply_markup
            )

    except Exception as e:
        logging.error(f"Erro ao enviar a foto: {e}")
        await context.bot.send_message(
            chat_id=chat_id,
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
