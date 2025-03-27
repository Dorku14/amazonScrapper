tk = "8067465500:AAE7aFkUXitqIOAqYHCEMcHigxH37YrKK4w"

import requests


def enviar(mensaje:str):
    # ID del chat o grupo
    CHAT_ID = "-4699510072"



    # URL de la API de Telegram


    url = f"https://api.telegram.org/bot{tk}/sendMessage"
    params = {"chat_id": CHAT_ID, "text": mensaje,"parse_mode": "HTML"}

    response = requests.post(url,data=params)

    if response.status_code == 200:
        print("Mensaje enviado al grupo.")
    else:
        print(f"Error al enviar el mensaje: {response.text}")

def enviarUltimaEjecucion(mensaje:str):
    CHAT_ID = "1031782272"
    url = f"https://api.telegram.org/bot{tk}/sendMessage"
    params = {"chat_id": CHAT_ID, "text": mensaje,"parse_mode": "HTML"}

    response = requests.post(url,data=params)

    if response.status_code == 200:
        print("Mensaje enviado al grupo.")
    else:
        print(f"Error al enviar el mensaje: {response.text}")

