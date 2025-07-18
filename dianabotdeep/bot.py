import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import InlineQuery, InlineQueryResultArticle, InputTextMessageContent

from keyboards import main_menu

# Cargar variables de entorno
load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')

# Inicializar bot y dispatcher
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Manejador del comando /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        "🛠️ <b>Menú Principal</b>\n\n"
        "Selecciona una opción del menú inline:",
        reply_markup=main_menu()
    )

# Manejador para el botón de Administración
@dp.callback_query(F.data == "admin_menu")
async def admin_menu_handler(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(
        "⚙️ <b>Menú de Administración</b>\n\n"
        "Funciones disponibles:\n"
        "- Gestionar canales\n"
        "- Moderar usuarios\n"
        "- Estadísticas\n\n"
        "Selecciona una opción:",
        reply_markup=InlineKeyboardMarkup(inline_keyboard=[
            [types.InlineKeyboardButton(text="📊 Canales", callback_data="manage_channels")],
            [types.InlineKeyboardButton(text="👥 Usuarios", callback_data="manage_users")],
            [types.InlineKeyboardButton(text="📈 Estadísticas", callback_data="show_stats")],
            [types.InlineKeyboardButton(text="🔙 Volver", callback_data="main_menu")]
        ])
    )

# Manejador para el botón de Configuración
@dp.callback_query(F.data == "config_menu")
async def config_menu_handler(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(
        "🔧 <b>Menú de Configuración</b>\n\n"
        "Opciones disponibles:\n"
        "- Preferencias\n"
        "- Notificaciones\n"
        "- Privacidad\n\n"
        "Selecciona una opción:",
        reply_markup=InlineKeyboardMarkup(inline_keyboard=[
            [types.InlineKeyboardButton(text="⚡ Preferencias", callback_data="set_preferences")],
            [types.InlineKeyboardButton(text="🔔 Notificaciones", callback_data="set_notifications")],
            [types.InlineKeyboardButton(text="👁️ Privacidad", callback_data="set_privacy")],
            [types.InlineKeyboardButton(text="🔙 Volver", callback_data="main_menu")]
        ])
    )

# Manejador para volver al menú principal
@dp.callback_query(F.data == "main_menu")
async def main_menu_handler(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(
        "🛠️ <b>Menú Principal</b>\n\n"
        "Selecciona una opción del menú inline:",
        reply_markup=main_menu()
    )

# Función principal
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
  
