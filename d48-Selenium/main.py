from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path="../selenium_driver/chromedriver"
# driver = webdriver.Chrome(executable_path=chrome_driver_path)
s=Service(chrome_driver_path)
driver = webdriver.Chrome(service=s)
url='https://www.amazon.fr/dp/B004Y6AJP2/ref=syn_sd_onsite_desktop_254?ie=UTF8&psc=1&pd_rd_plhdr=t'
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

# element.click()
# element.send_keys("")
# element.send_keys(Keys.ENTER)

result = driver.find_element(By.XPATH, '//*[@id="productOverview_feature_div"]/div/table/tbody/tr[1]/td[2]/span')
print("result : ", result.text)


while(True):
    pass

# driver.close()
# driver.quit()