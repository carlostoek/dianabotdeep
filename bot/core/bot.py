from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from .config import Config

# Initialize bot and dispatcher
storage = MemoryStorage()
bot = Bot(token=Config.BOT_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher(storage=storage)

# REF: bot/handlers/__init__.py > register_handlers