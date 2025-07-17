from .start import start_router

def register_handlers(dp):
    dp.include_router(start_router)
    # Se pueden agregar más routers aquí
    # REF: bot/core/bot.py > dp