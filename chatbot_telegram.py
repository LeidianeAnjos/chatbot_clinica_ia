from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from chatbot_motor import responder

TOKEN = "7062908060:AAE356yc0yV70ZuwKSDvusiLViGb0eJPYtc"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Olá! Eu sou a assistente da Clínica. Como posso ajudar?")

async def responder_mensagem(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto_usuario = update.message.text
    resposta = responder(texto_usuario)
    await update.message.reply_text(resposta, reply_markup=teclado)
def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, responder_mensagem))
    print("Bot rodando...")
    app.run_polling()

if __name__ == "__main__":
    main()

