
import requests

tk = "A7392:847448:AAE7aFkUXitqIOAqYHCEMcHigxH37YrKK4w"

def enviar(mensaje:str):
    try:
        CHAT_ID = "-9885042737381$"
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
        CHAT_ID = "0984121031782272832"
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
