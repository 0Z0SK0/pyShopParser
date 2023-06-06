from CNetwork import CNetwork
from CConfig import CConfig

from selenium.webdriver.common.by import By

network = CNetwork()
config = CConfig()

def getWomanLamodaItems():
    products = []
        
    try:
        market = config.getMarket("Lamoda")

        items = []
        
        url = market[0][1] + market[2][1]
        items = network.getItems(url, market[3][1], "page", market[10][1], market[11][1])
        for item in items:
            try:
                old_price = item.find_element(By.XPATH, market[4][1]).text
                new_price = item.find_element(By.XPATH, market[5][1]).text
                brand = item.find_element(By.XPATH, market[7][1]).text
                name = item.find_element(By.XPATH, market[8][1]).text

                link = item.find_element(By.XPATH, market[6][1])
                link = link.get_attribute('href')

                products.append([
                    brand,
                    name,
                    old_price,
                    new_price,
                    link
                ])
            except Exception as e:
                pass

        return products
    
    except Exception as e:
        print(e)
        return products
    
p = getWomanLamodaItems()
for i in p:
    print(i)