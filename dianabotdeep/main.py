import logging
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from loguru import logger

from config import Config
from handlers import commands, callbacks, admin, errors
from utils.middlewares import AdminMiddleware

async def setup_bot():
    bot = Bot(token=Config.BOT_TOKEN, parse_mode=ParseMode.HTML)
    dp = Dispatcher(storage=MemoryStorage())
    
    # Middlewares
    dp.message.middleware(AdminMiddleware())
    dp.callback_query.middleware(AdminMiddleware())
    
    # Handlers
    dp.include_router(commands.router)
    dp.include_router(callbacks.router)
    dp.include_router(admin.router)
    dp.include_router(errors.router)
    
    return bot, dp

async def main():
    bot, dp = await setup_bot()
    
    # Eliminar webhook si existe y empezar polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    import asyncio
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())