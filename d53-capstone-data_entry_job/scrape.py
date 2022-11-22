from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
chrome_driver_path="../selenium_driver/chromedriver"
import time
import re
MAX_WAITING_CYCLES = 20

ZILLOW_URL = "https://www.zillow.com/san-francisco-ca/rentals/?itc=_zw_zh_homepage-renter_btn_find-rentals-v1-property-types&searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.61632052783203%2C%22east%22%3A-122.25033847216797%2C%22south%22%3A37.46283218401745%2C%22north%22%3A38.08643671580814%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22mp%22%3A%7B%22min%22%3A1400%2C%22max%22%3A3500%7D%2C%22price%22%3A%7B%22min%22%3A283114%2C%22max%22%3A707785%7D%2C%22beds%22%3A%7B%22min%22%3A2%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A11%7D"

array_test = [
    ["57 Elmhurst LLC, 94-25 57th Ave, Elmhurst, NY 11373","2,699","https://www.zillow.com/homedetails/94-25-57th-Ave-48EB0198D-Elmhurst-NY-11373/2066695920_zpid/"],
    ["Park Haven Place, 88 153rd St, Jamaica, NY 11432", "2,599","https://www.zillow.com/homedetails/88-153rd-St-1696887-Jamaica-NY-11432/2098522443_zpid/"],
    ["140-60 Beech LLC, 140-60 Beech Ave, Flushing, NY 11355","2,599","https://www.zillow.com/homedetails/140-60-Beech-Ave-BF63C0FB9-Flushing-NY-11355/2066682511_zpid/" ]
]

class Scrape():
    def __init__(self) -> None:
        self.s=Service(chrome_driver_path)
        self.driver = webdriver.Chrome(service=self.s)        
        self.data=[]
        self.max_waiting_cycles=MAX_WAITING_CYCLES

    def get_infos_on_page(self):
        self.driver.get(ZILLOW_URL)
        time.sleep(2)
        try:
            self.scroll_down_to_bottom()
            self.infos_is_here()
            lis = self.driver.find_elements(By.CSS_SELECTOR,".photo-cards.with_constellation > li")
            for li in lis:
                infos = self.get_infos_of_flat_with_li(li)
                if infos:
                    self.data.append(infos)
                    print("=====> len : ",len(self.data))
        except Exception as e:
            print("error : ", e)


    def scroll_down_to_bottom(self):
        window = self.driver.find_element(By.CSS_SELECTOR,".photo-cards.with_constellation")
        # self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);", window)
        for i in range(20):
            self.driver.execute_script(f"window.scrollTo(0, 500*{i});", window)
            time.sleep(0.4)
        # self.driver.execute_script("arguments[0].scrollIntoView(true);", window)
        print("text : ", window.text)


    def infos_is_here(self):
        lis = self.driver.find_elements(By.CSS_SELECTOR,".photo-cards.with_constellation > li")
        time.sleep(1)
        for li in lis:
            print("text test : ", li.text)
            if li.text=="" and li.get_attribute("data-test")!="search-list-first-ad" and self.max_waiting_cycles>0:
                self.max_waiting_cycles-=1
                return self.infos_is_here()
        self.max_waiting_cycles=MAX_WAITING_CYCLES
        return True



    def next_page(self):
        self.driver.find_element(By.CSS_SELECTOR,".search-pagination").click()
        time.sleep(0.2)
        self.wait_for_selector(".search-pagination")


    def get_infos_of_flat_with_li(self, li):
        try:
            address = li.find_element(By.CSS_SELECTOR,"address[data-test=property-card-addr]").text
            price = li.find_element(By.CSS_SELECTOR,"span[data-test=property-card-price]").text
            price = re.findall(r"[0-9,]+", price)[0]
            link = li.find_element(By.CSS_SELECTOR,"a").get_attribute("href")
            print(f"==>{address}///{price}///{link}")
            return {
                address:address,
                price: price,
                link: link
            }
        except:
            return False
        

    def wait_for_selector(self, css_selector):
        not_found=True
        while not_found:
            time.sleep(0.5)
            try:
                self.driver.find_element(By.CSS_SELECTOR, css_selector)
            except:
                pass
            else:
                not_found=False


    def wait_for_element_with_text(self, css_selector, text):
        not_found=True
        print("entered")
        while not_found:
            time.sleep(0.5)
            try:
                buttons = self.driver.find_elements(By.CSS_SELECTOR, css_selector)
                for button in buttons :
                    print("button text : ", button.text)
                    if(button.text==text):
                        print("FOUND ! ")
                        not_found=False
            except:
                pass
    