import os
import re
import math
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select

class CNetwork():
    def __init__(self):
        path_to_browser = os.path.abspath(os.getcwd()) + "\\driver\\chromedriver"
        service = Service(executable_path=path_to_browser)
        self.browser = webdriver.Chrome(service=service)

    def getItems(self, url, xpath, page_params=None, items_count=None, items_per_page=None):
        items = []

        if not page_params:
            self.browser.get(url)
            
            # wait until page is succesfully loaded
            WebDriverWait(self.browser, 10)

            items = self.browser.find_elements(By.XPATH, xpath)

        else:
            self.browser.get(url + "&" + page_params + "=" + str(1))

            # wait until page is succesfully loaded
            WebDriverWait(self.browser, 30)
            
            items_count = self.browser.find_element(By.XPATH, items_count).text        
            items_count = re.findall(r'\d+', items_count)
            items_count = int(items_count[0])

            page_count = math.floor(items_count / items_per_page)

            for i in range(1,2):
                self.browser.get(url + "&" + page_params + "=" + str(i))

                # wait until page is succesfully loaded
                WebDriverWait(self.browser, 30)

                items = items + self.browser.find_elements(By.XPATH, xpath)

        return items