# REF: main.py > Router registration
# REF: services/message_service.py > get_welcome_message()

from aiogram import Router, types
from aiogram.filters import Command
from services.message_service import get_welcome_message

# Inicializar router para manejo de comandos
start_router = Router()

@start_router.message(Command("start"))
async def start_command(message: types.Message):
    """
    Maneja el comando /start enviando mensaje de bienvenida
    Preserva contexto de usuario para personalización
    """
    user_name = message.from_user.full_name
    welcome_text = get_welcome_message(user_name)
    
    # Envía mensaje con formato Markdown
    await message.answer(
        text=welcome_text,
        parse_mode="Markdown",
        disable_web_page_preview=True
    )