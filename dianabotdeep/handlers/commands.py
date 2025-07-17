from aiogram import Router, types
from aiogram.filters import Command
from aiogram import F

from utils.keyboards import main_menu_markup

router = Router()

@router.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        " Bot Administrador de Canales\n\n"
        "Selecciona una opción:",
        reply_markup=main_menu_markup()
    )

@router.message(Command("help"))
async def cmd_help(message: types.Message):
    await message.answer(
        " Lista de comandos disponibles:\n\n"
        "/start - Iniciar el bot\n"
        "/help - Mostrar ayuda\n"
        "/my_channels - Mostrar canales administrados"
    )
