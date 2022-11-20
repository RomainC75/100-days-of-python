from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path="../selenium_driver/chromedriver"
s=Service(chrome_driver_path)
driver = webdriver.Chrome(service=s)
url='https://orteil.dashnet.org/experiments/cookie/'

driver.get(url)

time.sleep(2)

# print("len : ", len(store))

def buy_things (): 
    store = driver.find_elements(By.CSS_SELECTOR,"#store > div")
    store.reverse()
    for item in store:
        color = item.value_of_css_property('color')
        print(color, type(color))
        print("")
        if color == "rgba(0, 0, 0, 1)":
            item.click()
            time.sleep(0.05)
            break

cookie = driver.find_element(By.ID, "cookie")
print(cookie.get_attribute('id'))

money = driver.find_element(By.ID, "money")


for i in range(0,1000000):
    cookie.click()
    time.sleep(0.01)

    if((i+1)%500==0):
        print(money.text)
        buy_things()


while True:
    pass