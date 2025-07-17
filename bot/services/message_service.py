# REF: handlers/start_handler.py > /start command response
from bot.config import FREE_CHANNEL_LINK, VIP_CHANNEL_LINK

def get_welcome_message(name: str) -> str:
    """
    Genera mensaje de bienvenida profesional con explicación de canales
    """
    return (
        f" ¡Hola {name}! Bienvenido/a al gestor oficial de contenidos exclusivos.\n\n"
        " **Nuestros canales:**\n"
        f"• Canal GRATUITO: Acceso a contenido básico ({FREE_CHANNEL_LINK})\n"
        f"• Canal VIP: Contenido premium, análisis exclusivos y ventajas ({VIP_CHANNEL_LINK})\n\n"
        " **¿Por qué unirte al VIP?**\n"
        "- Acceso 24/7 a materiales exclusivos\n"
        "- Análisis de mercado en tiempo real\n"
        "- Soporte prioritario\n\n"
        "¡Usa los comandos del bot para explorar todas las funcionalidades! "
    )
