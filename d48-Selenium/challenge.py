from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path="../selenium_driver/chromedriver"
# driver = webdriver.Chrome(executable_path=chrome_driver_path)
s=Service(chrome_driver_path)
driver = webdriver.Chrome(service=s)
url='https://www.python.org/'
driver.get(url)

# find_element-S-
# find_element(By.ID, "id")
# find_element(By.NAME, "name")
# find_element(By.XPATH, "xpath")
# find_element(By.LINK_TEXT, "link text")
# find_element(By.PARTIAL_LINK_TEXT, "partial link text")
# find_element(By.TAG_NAME, "tag name")
# find_element(By.CLASS_NAME, "class name")
# find_element(By.CSS_SELECTOR, "css selector")

# element.text
# element.get_attribute("value")
# element.value_of_css_property('color')
# coords
# element.rect

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