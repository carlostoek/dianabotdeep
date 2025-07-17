# REF: handlers/start_handler.py > start_router
# REF: config.py > BOT_TOKEN

import asyncio
from aiogram import Bot, Dispatcher
from bot.handlers import start_handler
from bot.config import BOT_TOKEN

async def main():
    # Inicialización del bot con token
    bot = Bot(token=BOT_TOKEN, parse_mode="HTML")
    dp = Dispatcher()
    
    # Registro de routers (manejadores de comandos)
    dp.include_router(start_handler.start_router)
    # FUTURO: Aquí se agregarán más routers
    
    # Iniciar polling para recibir actualizaciones
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())