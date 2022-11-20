from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path="../selenium_driver/chromedriver"
# driver = webdriver.Chrome(executable_path=chrome_driver_path)
s=Service(chrome_driver_path)
driver = webdriver.Chrome(service=s)

url="https://en.wikipedia.org/wiki/Main_Page"
id="articlecount"

driver.get(url)

count = driver.find_element(By.CSS_SELECTOR, "#articlecount > a")
print("count : ", count.text)
count.click()

while(True):
    pass