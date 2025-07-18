from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardMarkup

def main_menu() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(text="⚙️ Administración", callback_data="admin_menu")
    builder.button(text="🔧 Configuración", callback_data="config_menu")
    builder.adjust(2)
    return builder.as_markup()
