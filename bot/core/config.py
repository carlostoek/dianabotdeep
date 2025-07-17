import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
    if not BOT_TOKEN:
        raise ValueError("No BOT_TOKEN found in environment variables")

# REF: bot/core/bot.py > Bot initialization