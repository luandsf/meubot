import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Configuração de Logs
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Nome do arquivo de imagem que DEVE estar na mesma pasta do main.py no GitHub
PHOTO_FILENAME = "banner.png"

# Link do seu grupo do Telegram
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

    # Tenta enviar a imagem local
    try:
        # os.getcwd() pega o diretório de trabalho atual do bot no Render
        photo_path = os.path.join(os.getcwd(), PHOTO_FILENAME)
        
        if os.path.exists(photo_path):
            with open(photo_path, 'rb') as photo_file:
                # O Telegram trata o envio de arquivo local com mais qualidade do que URL
                await context.bot.send_photo(
                    chat_id=chat_id,
                    photo=photo_file,
                    caption=caption_text,
                    reply_markup=reply_markup
                )
                logging.info("Imagem local enviada com sucesso.")
        else:
            # Se o arquivo não for encontrado, avisa no log e envia só texto
            logging.error(f"Arquivo não encontrado: {photo_path}")
            await context.bot.send_message(
                chat_id=chat_id,
                text=f"{caption_text}\n\n(Erro: Imagem '{PHOTO_FILENAME}' não encontrada no servidor)",
                reply_markup=reply_markup
            )
            
    except Exception as e:
        # Captura qualquer outro erro e envia só texto
        logging.error(f"Erro ao enviar foto: {e}")
        await context.bot.send_message(
            chat_id=chat_id,
            text=f"{caption_text}\n\n(Erro técnico ao carregar imagem)",
            reply_markup=reply_markup
        )

def main():
    # Pega o token da variável de ambiente no Render
    token = os.environ.get("TELEGRAM_TOKEN")
    
    if not token:
        raise ValueError("A variável TELEGRAM_TOKEN não foi encontrada nas Configurações do Render!")

    app = ApplicationBuilder().token(token).build()

    # Registra o comando /start
    app.add_handler(CommandHandler("start", start))

    print("Bot rodando e aguardando /start...")
    # Usa polling para simplificar
    app.run_polling()

if __name__ == '__main__':
    main()
