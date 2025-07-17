import asyncio
from bot.core.bot import bot, dp
from bot.handlers import register_handlers

async def main():
    register_handlers(dp)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

# REF: bot/core/bot.py > bot, dp
# REF: bot/handlers/__init__.py > register_handlers