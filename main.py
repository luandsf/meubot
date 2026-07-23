import os
import uuid
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, InlineQueryResultPhoto
from telegram.ext import Application, InlineQueryHandler

# Pega o token configurado no Render / Servidor
TOKEN = os.environ.get("TELEGRAM_TOKEN")

# Link do seu grupo no Telegram
LINK_DO_GRUPO = "https://t.me/tipslucrativas1"

# Link direto da sua imagem no Imgur
URL_DA_IMAGEM = "https://i.imgur.com/vH9XgGj.png"

async def inline_query(update, context):
    # Criando o botão interativo
    keyboard = [
        [
            InlineKeyboardButton(
                "CLIQUE AQUI E ACESSE O GRUPO GRATUITO", 
                url=LINK_DO_GRUPO
            )
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Montando a resposta inline com a foto e o botão
    results = [
        InlineQueryResultPhoto(
            id=str(uuid.uuid4()),
            photo_url=URL_DA_IMAGEM,
            thumbnail_url=URL_DA_IMAGEM,
            caption="",  # Legenda vazia para manter o visual limpo
            reply_markup=reply_markup
        )
    ]

    await update.inline_query.answer(results, cache_time=1)

def main():
    if not TOKEN:
        raise ValueError("O token do Telegram não foi configurado nas variáveis de ambiente.")

    app = Application.builder().token(TOKEN).build()
    app.add_handler(InlineQueryHandler(inline_query))

    print("Bot rodando em modo inline...")
    app.run_polling()

if __name__ == "__main__":
    main()
