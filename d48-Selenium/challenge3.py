from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path="../selenium_driver/chromedriver"
s=Service(chrome_driver_path)
driver = webdriver.Chrome(service=s)
url='https://secure-retreat-92358.herokuapp.com/'

driver.get(url)

first_name_input = driver.find_element(By.CSS_SELECTOR, "input[name=fName]")
first_name_input.send_keys("Romrom")

last_name_input = driver.find_element(By.CSS_SELECTOR, "input[name=lName]")
last_name_input.send_keys("Cheche")

email_input = driver.find_element(By.CSS_SELECTOR, "input[name=email]")
email_input.send_keys("sponge.bob@gmail.com")

signup_button = driver.find_element(By.CSS_SELECTOR, "button[type=submit]")
signup_button.click()

while True:
    pass