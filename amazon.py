import error
import utils
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from datetime import datetime
import bd
import notification
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from logging.handlers import TimedRotatingFileHandler
import logging
import logging.handlers
import time

while True:
    logger = logging.getLogger("AmazonScrapper")
    logger.setLevel(logging.ERROR)  # Nivel de error

    event_handler = logging.handlers.NTEventLogHandler("AmazonScrapper")
    logger.addHandler(event_handler)

    handler = TimedRotatingFileHandler("AmazonScrapper.log", when="midnight", interval=1, backupCount=7)
    handler.suffix = "%Y-%m-%d" 
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    # aod-offer-shipsFrom enviado por
    # aod-offer-soldBy vendido por
    # #aod-offer seccion donde está las ofertas
    # buybox-see-all-buying-choices id del boton para ver todos los vendedores
    chrome_options = Options()
    chrome_options.add_argument(r"--user-data-dir=C:\Users\super\AppData\Local\Google\Chrome\User Data")
    chrome_options.add_argument(r"--profile-directory=alexisDO.ku")
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')
    chrome_options.add_argument('--log-level=1')
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0"
    }
    options = webdriver.ChromeOptions()
    options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0")
    productos = bd.obtenerRegistrosProductos()
    fechaInicio = " \n la ejecución comenzó a las " + datetime.now().strftime("%d/%m/%Y %H:%M:%S") + " \n"
    superMensaje = "\n"
    for producto in productos:
        driver = webdriver.Chrome(options=chrome_options)

        url = producto["url"]
        precioInteres = producto["precioInteres"]
        tienePrioridad = producto["tienePrioridad"]
        urlCorta = producto["UrlCorta"]
        page = driver.get(url) 
        existeEscenario = False

        if not existeEscenario:
            try:
                print("se inicia el proceso de buscar boton de vendedores")
                existe = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "#buybox-see-all-buying-choices .a-button-inner"))
                ) 
                existe.text
                existeEscenario = True
                superMensaje += utils.scrapOtherVendorsSection(driver,urlCorta,precioInteres,tienePrioridad)
            except  Exception as e:
                print('El producto no tiene el boton de otros vendedores')
                existeEscenario = False
                logger.error(f"Ocurrió un error inesperado: {str(e)}", exc_info=True)

        if not existeEscenario:
            try:
                existe = WebDriverWait(driver, 5).until(
                                    EC.presence_of_element_located((By.CSS_SELECTOR, "#availability"))
                                ) 
                text = existe.text

                if "No disponible por el momento".lower() in text.lower():
                    print('texto "No disponible por el momento." encontrado')
                    existeEscenario = True
                else:
                    raise Exception("")
            except  Exception as e:
                print('El producto no tiene el texto de "No disponible por el momento." ')
                logger.error(f"Ocurrió un error inesperado: {str(e)}", exc_info=True)
                existeEscenario = False





        if not existeEscenario:
            try:
                print("se intenta buscar el precio en la pagina principal")
                existe = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "#corePriceDisplay_desktop_feature_div .a-price-whole"))
                ) 
                existeEscenario = True
                titulo = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "#productTitle"))
                )
                print(titulo)
                superMensaje += utils.scrapOtherCompareSection(driver,urlCorta,precioInteres,tienePrioridad)
            except  Exception as e:
                print('el producto no tiene el precio en la pagina principal')
                existeEscenario = False
                logger.error(f"Ocurrió un error inesperado: {str(e)}", exc_info=True)

        driver.quit()

    fechaFinalizacion = " \n la ejecución terminó a las " + datetime.now().strftime("%d/%m/%Y %H:%M:%S") + " \n"
    notification.enviar(superMensaje.replace("-","\-"))

    logger.setLevel(logging.INFO) 

    logger.info(fechaFinalizacion)

    notificacionMonitoreoAutomatico = fechaInicio + "\n"+fechaFinalizacion
    print(superMensaje)
    notification.enviarUltimaEjecucion(notificacionMonitoreoAutomatico)
    # time.sleep(10)

