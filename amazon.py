import requests
import utils
import error
from bs4 import BeautifulSoup

url = 'https://www.amazon.com.mx/Pok%C3%A9mon-TCG-Scarlet-Violet-Surging-Booster/dp/B0DDYZX1TB/ref=sr_1_2?crid=34IQR1XK9F75D&dib=eyJ2IjoiMSJ9.zZQjagXiNQg889IP5BEyuV3c-FtVYgpKY2Ka51G9LGshrXyuPsDMNCxlIILXVMKuRCLZ-QwGr-xB2td1KgmFJB8Tn4sj-gFagdfqEYLPssttiYYZYPsA35hYwPXRs-UQUaExXIKZMlpKPJ8xQ3whYv1mdhi6xqZ3ZnNpihFVcTbyduRnLjJbhKZ7CDRxMWE4DbOY73UGrkoS8FJTxl_j_yxlalVh9ytOuKTWAAs8nDTjl99lEWcVwivQI6JSs3nox-ds12OPoEJ0jI98tYlmB9jHMCnORbQBEOnhhT27JzTavMIek5m0G1qZ2QX5FZ7G-beZlbbHaa4wedTy1V2m57FwIa4l7Yt-BYYx0VlNui3Unn6s1wesyx3dH7u5Kr38yZlwjo3BsZjaFyDoN_kwsNlGhAzXiCW5_NCQUL6cN500Kw67kbW2r_oWW6b5CaWH.l3QSh7Ab2TZnAgnMW4r994x_g38XNfwUHiXUDCvxa-Y&dib_tag=se&keywords=pokemon+tcg&qid=1742244648&sprefix=pokemon%2Caps%2C123&sr=8-2&ufe=app_do%3Aamzn1.fos.de93fa6a-174c-4df7-be7c-5bc8e9c5a71b'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'lxml')

title_element =  soup.select_one('#productTitle')
price_element =  soup.select_one('.a-price-whole')
price_e_decimals =  soup.select_one('.a-price-fraction')

if price_element is not None and price_e_decimals is not None and title_element is not None:
    utils.orchestrator(price_element.text,price_e_decimals.text,title_element.text)
else :
    error.writeLog()

