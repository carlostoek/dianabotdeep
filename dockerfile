# Usa la imagen oficial de Python
FROM python:3.11-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos necesarios
COPY . .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Crea un usuario no root para mayor seguridad
RUN useradd -m botuser && \
    chown -R botuser:botuser /app
USER botuser

# Variables de entorno (opcional, puedes pasarlas al ejecutar)
# ENV BOT_TOKEN=tu_token_aqui
# ENV ADMIN_IDS=123456789,987654321

# Puerto expuesto (para métricas/health checks si las agregas después)
EXPOSE 8080

# Comando para ejecutar el bot
CMD ["python", "bot.py"]
