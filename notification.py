
import requests

tk = "8067465500:AAE7aFkUXitqIOAqYHCEMcHigxH37YrKK4w"

def enviar(mensaje:str):
    try:
        CHAT_ID = "-4699510072"
        url = f"https://api.telegram.org/bot{tk}/sendMessage"
        params = {"chat_id": CHAT_ID, "text": mensaje,"parse_mode": "HTML"}
        print("monitor super mensaje desde funcion 'enviar': "+mensaje)
        response = requests.post(url,data=params)

        if response.status_code == 200:
            print("Mensaje enviado al grupo.")
        else:
          raise Exception(response.text)
    except Exception as e:
        print(f"Error al enviar el mensaje: {e}")


def enviarUltimaEjecucion(mensaje:str):
    try:
        CHAT_ID = "1031782272"
        url = f"https://api.telegram.org/bot{tk}/sendMessage"
        params = {"chat_id": CHAT_ID, "text": mensaje,"parse_mode": "HTML"}
        print("monitor super mensaje desde funcion 'enviarUltimaEjecucion': "+mensaje)
        response = requests.post(url,data=params)

        if response.status_code == 200:
            print("Mensaje enviado al grupo.")
        else:
            raise Exception(response.text)
    except Exception as e:
        print(f"Error al enviar el mensaje: {e}")
