import requests
from bs4 import BeautifulSoup
from telegram.ext import Updater, CommandHandler

# Define la función para procesar el comando "/tabla"
def tabla_command(update, context):
    # Obtener el texto del mensaje
    text = update.message.text.lower()

    # Verificar si el mensaje comienza con el prefijo del comando "/tabla"
    if text.startswith("/tabla"):
        # Realiza una solicitud GET a la página web de la Serie Nacional de Béisbol de Cuba
        response = requests.get("http://www.beisbolencuba.com/series-nacionales/")

        # Analiza el contenido HTML de la página web utilizando BeautifulSoup
        soup = BeautifulSoup(response.content, "html.parser")

        # Encuentra la tabla de posiciones en la página web
        tabla = soup.find("table", {"class": "tabla"})

        # Crea una respuesta de mensaje con la tabla de posiciones
        response_message = f"<b>Tabla de posiciones:</b>n{tabla}"

        # Envía la respuesta de mensaje al chat
        context.bot.send_message(chat_id=update.effective_chat.id, text=response_message, parse_mode="HTML")

# Define la función para procesar el comando "/resultados"
def resultados_command(update, context):
    # Obtener el texto del mensaje
    text = update.message.text.lower()

    # Verificar si el mensaje comienza con el prefijo del comando "/resultados"
    if text.startswith("/resultados"):
        # Realiza una solicitud GET a la página web de la Serie Nacional de Béisbol de Cuba
        response = requests.get("http://www.beisbolencuba.com/series-nacionales/")

        # Analiza el contenido HTML de la página web utilizando BeautifulSoup
        soup = BeautifulSoup(response.content, "html.parser")

        # Encuentra la tabla de resultados en la página web
        tabla = soup.find("table", {"class": "tabla"})

        # Crea una respuesta de mensaje con la tabla de resultados
        response_message = f"<b>Resultados:</b>n{tabla}"

        # Envía la respuesta de mensaje al chat
        context.bot.send_message(chat_id=update.effective_chat.id, text=response_message, parse_mode="HTML")

# Crea una instancia del updater y pasa el token del bot
updater = Updater(token="5635481710:AAEme7XW_45c69YpUV0RS9ip2p2QjTIl47o", use_context=True)

# Obtén el dispatcher para registrar los manejadores de comandos
dispatcher = updater.dispatcher

# Registra los manejadores de comandos
dispatcher.add_handler(CommandHandler("tabla", tabla_command))
dispatcher.add_handler(CommandHandler("resultados", resultados_command))

# Inicia el bot
updater.start_polling()
