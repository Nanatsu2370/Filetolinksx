from pyrogram import Client, filters
import requests
from bs4 import BeautifulSoup

api_id = 9548711 # Reemplaza con tu api_id
api_hash = "4225fbfa50c5ac44194081a0f114bdd1" # Reemplaza con tu api_hash
bot_token = "5635481710:AAFCFnhjfDFW6G5sm9E5o48-9Bm1MBuXB8w" # Reemplaza con tu token de bot

app = Client("my_bot", api_id, api_hash, bot_token=bot_token)

# Define la función para procesar los mensajes
@app.on_message(filters.private)
def process_message(client, message):
    # Obtener el texto del mensaje
    text = message.text.lower()

    # Verificar si el mensaje comienza con el prefijo del comando "/tabla"
    if text.startswith("/tabla"):
        # Realiza una solicitud GET a la página web de la Serie Nacional de Béisbol de Cuba
        response = requests.get("http://www.beisbolencuba.com/series-nacionales/")

        # Analiza el contenido HTML de la página web utilizando BeautifulSoup
        soup = BeautifulSoup(response.content, "html.parser")

        # Encuentra la tabla de posiciones en la página web
        tabla = soup.find("table", {"class": "tabla"})

        # Crea una respuesta de mensaje con la tabla de posiciones
       response_message = "Here's the table of positions:n" + table
       client.send_message(message.chat.id, response_message, parse_mode="markdown")

    # Verificar si el mensaje comienza con el prefijo del comando "/resultados"
    elif text.startswith("/resultados"):
        # Realiza una solicitud GET a la página web de la Serie Nacional de Béisbol de Cuba
        response = requests.get("http://www.beisbolencuba.com/series-nacionales/")

        # Analiza el contenido HTML de la página web utilizando BeautifulSoup
        soup = BeautifulSoup(response.content, "html.parser")

        # Encuentra la tabla de resultados en la página web
        tabla = soup.find("table", {"class": "tabla"})

        # Crea una respuesta de mensaje con la tabla de resultados
        response_message = f"<b>Resultados:</b>n{tabla}"

        # Envía la respuesta de mensaje al chat
        client.send_message(message.chat.id, response_message, parse_mode="html")

# Inicia el cliente de Pyrogram
app.run()
