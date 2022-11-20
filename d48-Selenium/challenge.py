from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path="../selenium_driver/chromedriver"
# driver = webdriver.Chrome(executable_path=chrome_driver_path)
s=Service(chrome_driver_path)
driver = webdriver.Chrome(service=s)
url='https://www.python.org/'
driver.get(url)


schedule = driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/div/section/div[3]/div[2]/div/ul')

lis = schedule.find_elements(By.TAG_NAME,"li")

events = []

for li in lis :
    date = li.find_element(By.TAG_NAME,"time")
    date_text = date.get_attribute("datetime")

    event = li.find_element(By.TAG_NAME,'a')

    events.append({
        'time': date_text.split("T")[0],
        'name':event.text
    })

print(events)