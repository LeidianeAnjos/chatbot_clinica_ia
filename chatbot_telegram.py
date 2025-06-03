from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from chatbot_motor import responder  # Certifique-se de que o nome do arquivo é chatbot_motor.py

TOKEN = "7062908060:AAE356yc0yV70ZuwKSDvusiLViGb0eJPYtc"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    from chatbot_motor import teclado_opcoes
    await update.message.reply_text(
        "Olá! Eu sou a assistente da Clínica. Como posso ajudar?",
        reply_markup=teclado_opcoes
    )

async def responder_mensagem(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto_usuario = update.message.text
    resposta, teclado = responder(texto_usuario)
    await update.message.reply_text(resposta, reply_markup=teclado)

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, responder_mensagem))
    print("Bot rodando...")
    app.run_polling()

if __name__ == "__main__":
    main()
