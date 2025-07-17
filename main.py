# main.py
import os
import logging
from dotenv import load_dotenv
from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Configuración inicial
load_dotenv()
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
PORT = int(os.environ.get("PORT", 5000))

# Configurar logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Teclado con un solo botón
START_KEYBOARD = ReplyKeyboardMarkup(
    [["👋 ¡Saludar!"]], 
    resize_keyboard=True,
    one_time_keyboard=True
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Maneja el comando /start"""
    user = update.effective_user
    await update.message.reply_html(
        rf"Hola {user.mention_html()}! Pulsa el botón para saludar:",
        reply_markup=START_KEYBOARD
    )

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Responde al botón de saludo"""
    await update.message.reply_text("¡Hola! ¿Cómo estás? 😊")

def main() -> None:
    """Inicia el bot"""
    application = Application.builder().token(TOKEN).build()

    # Handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, button_handler))

    # Modo producción (para servicios como Heroku)
    if "DYNO" in os.environ:
        application.run_webhook(
            listen="0.0.0.0",
            port=PORT,
            url_path=TOKEN,
            webhook_url=f"https://{os.environ.get('APP_NAME')}.onrender.com/{TOKEN}"
        )
    else:
        # Modo desarrollo local
        application.run_polling()

if __name__ == "__main__":
    main()
