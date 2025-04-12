from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import notification
def orchestrator(price,priceDecimals):
    priceConcat =  price + priceDecimals
    priceFloat = float(priceConcat)

    print(priceFloat)

def scrapOtherVendorsSection(driver:webdriver,url:str,precioInteres:float,tienePrioridad:int):
    mensaje = "\n"
    mensajeLocal = ""
    encontroPrecioInteres = False
    try:
        WebDriverWait(driver, 2).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#buybox-see-all-buying-choices .a-button-inner"))
        ).click()

        elementos = WebDriverWait(driver, 5).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#aod-offer"))
        )
        titulo = driver.find_element(By.CSS_SELECTOR, "#productTitle")
        print(titulo.text)
        mensajeLocal += "\n "
        mensajeLocal += f'<u><a href="{url}">{titulo.text}</a></u>'
        for elemento in elementos:
            precio = elemento.find_element(By.CSS_SELECTOR,'#aod-offer .a-price-whole').text
            vendidoPor = elemento.find_element(By.CSS_SELECTOR,'#aod-offer #aod-offer-soldBy').text
            enviadoPor = elemento.find_element(By.CSS_SELECTOR,'#aod-offer #aod-offer-shipsFrom').text
            precio_float = float(precio.replace(",",""))

            if float(precio_float) <= precioInteres:
                encontroPrecioInteres = True
                mensajeLocal += "\n"
                mensajeLocal += f" El precio es de <b>${precio}</b> "
                if 'amazon' in vendidoPor.lower():
                    mensajeLocal += f" Es vendido por amazon "
                else:
                    mensajeLocal += f" No es vendido por amazon "

                if 'amazon' in enviadoPor.lower():
                    mensajeLocal += f" Es enviado por amazon "
                else:
                    mensajeLocal += f" No es enviado por amazon"
                mensajeLocal += "\n"

                if "" in mensajeLocal:
                    print("no hay ofertas de interes")
                print(mensajeLocal)
    except  Exception as e:
        print(e)


    if tienePrioridad == 1 and encontroPrecioInteres:
        notification.enviar(mensajeLocal)
    elif tienePrioridad == 0 and encontroPrecioInteres:
        mensaje += mensajeLocal + "\n"


    return mensaje

def scrapOtherCompareSection(driver:webdriver,url:str,precioInteres:float,tienePrioridad:int):
    mensaje = "\n"
    mensajeLocal = ""
    encontroPrecioInteres = False
    try:
        vendorSection = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#corePriceDisplay_desktop_feature_div .a-price-whole"))
        ).click()

        precio = driver.find_element(By.CSS_SELECTOR,'#corePriceDisplay_desktop_feature_div:has(.priceToPay) .a-price-whole')
        titulo = driver.find_element(By.CSS_SELECTOR,'#productTitle')
        print(titulo.text)
        precio_float = float(precio.text.replace(",",""))

        if float(precio_float) <= precioInteres:
            encontroPrecioInteres = True
            mensajeLocal += "\n "
            mensajeLocal = f' <u><a href="{url}">{titulo.text}</a></u>\n '
            mensajeLocal += f"el precio es de <b>${precio.text}</b>"

            if "Amazon México".lower() in vendorSection.text.lower():
                mensajeLocal += " y es de amazon mexico"
            print(mensajeLocal)
    except  Exception as e:
        print(e)


    if tienePrioridad == 1 and encontroPrecioInteres:
        notification.enviar(mensajeLocal)
    elif tienePrioridad == 0 and encontroPrecioInteres:
        mensaje += mensajeLocal + "\n"


    return mensaje