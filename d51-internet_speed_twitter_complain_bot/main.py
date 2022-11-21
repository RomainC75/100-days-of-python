from InternetSpeedTwitterBot import InternetSpeedTwitterBot
import dotenv 

config = dotenv.dotenv_values('../.env')
PROMISED_DOWN = 1000
PROMISED_UP = 600


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


TWITTER_MAIL = config['TW_MAIL']
TWITTER_PASS = config['TW_PASS']
TWITTER_USERNAME = config['TW_USERNAME']

twitter_Bot = InternetSpeedTwitterBot(PROMISED_DOWN, PROMISED_UP, TWITTER_MAIL, TWITTER_USERNAME, TWITTER_PASS)

twitter_Bot.get_internet_speed()
twitter_Bot.tweet_at_provider()



while True:
    pass
