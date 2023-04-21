from pyrogram import Client, filters
import requests
from bs4 import BeautifulSoup

api_id = 9548711 # Reemplaza con tu api_id
api_hash = "4225fbfa50c5ac44194081a0f114bdd1" # Reemplaza con tu api_hash
bot_token = "5635481710:AAFCFnhjfDFW6G5sm9E5o48-9Bm1MBuXB8w" # Reemplaza con tu token de bot

app = Client("my_bot", api_id, api_hash, bot_token=bot_token)

# Define el comando "/tabla" para obtener la tabla de posiciones
@app.on_message(filters.command("tabla"))
def tabla_command(client, message):
    # Realiza una solicitud GET a la página web de la Serie Nacional de Béisbol de Cuba
    response = requests.get("http://www.beisbolencuba.com/series-nacionales/")

    # Analiza el contenido HTML de la página web utilizando BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    # Encuentra la tabla de posiciones en la página web
    tabla = soup.find("table", {"class": "tabla"})

    # Crea una respuesta de mensaje con la tabla de posiciones
    response_message = f"<b>Tabla de posiciones:</b>n{tabla}"

    # Envía la respuesta de mensaje al chat
    client.send_message(message.chat.id, response_message, parse_mode="html")

# Define el comando "/resultados" para obtener los resultados de los juegos
@app.on_message(filters.command("resultados"))
def resultados_command(client, message):
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
print("Bot iniciado")
