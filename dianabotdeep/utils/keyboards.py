from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup

def main_menu_markup() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    builder.button(text=" Mis Canales")
    builder.button(text="⚙️ Configuración")
    builder.button(text="ℹ️ Ayuda")
    builder.adjust(2)
    return builder.as_markup(resize_keyboard=True)

def channel_actions_markup(channel_id: int) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(text=" Suscriptores", callback_data=f"subs:{channel_id}")
    builder.button(text=" Publicar", callback_data=f"post:{channel_id}")
    builder.button(text="⚙️ Configurar", callback_data=f"config:{channel_id}")
    builder.button(text="❌ Eliminar", callback_data=f"delete:{channel_id}")
    builder.adjust(2)
    return builder.as_markup()