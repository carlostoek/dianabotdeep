from aiogram import Router, types
from aiogram.filters import Command

start_router = Router()

# Text constants
WELCOME_TITLE = " <b>¡Bienvenido/a a nuestro exclusivo bot de Telegram!</b>"
FREE_CHANNEL_DESC = " <b>Canal Gratuito:</b> Accede a contenido público y anuncios generales"
VIP_CHANNEL_DESC = " <b>Canal VIP:</b> Contenido premium, acceso prioritario y beneficios exclusivos"
CALL_TO_ACTION = "¡Explora todo lo que tenemos para ofrecerte! Usa los comandos disponibles para interactuar conmigo."

WELCOME_MESSAGE = f"{WELCOME_TITLE}\n\n{FREE_CHANNEL_DESC}\n{VIP_CHANNEL_DESC}\n\n{CALL_TO_ACTION}"

@start_router.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer(WELCOME_MESSAGE)

# REF: bot/handlers/__init__.py > register_handlers