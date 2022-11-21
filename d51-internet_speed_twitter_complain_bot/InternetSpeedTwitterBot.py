from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
chrome_driver_path="../selenium_driver/chromedriver"
import time
import re

import csv
SPEED_TEST_URL = "https://www.speedtest.net/fr"
TWITTER_LOGIN_URL = "https://twitter.com/i/flow/login"

class InternetSpeedTwitterBot:
    def __init__(self, down, up, twitter_mail, twitter_username, twitter_pass) -> None:
        
        self.s=Service(chrome_driver_path)
        self.driver = webdriver.Chrome(service=self.s)

        self.down=down
        self.up=up
        self.twitter_mail = twitter_mail
        self.twitter_pass = twitter_pass
        self.twitter_username = twitter_username
        self.current_down_speed=0
        self.current_up_speed=0

    def get_internet_speed(self):
        self.driver.get(SPEED_TEST_URL)
        accept_cookie_btn = self.driver.find_element(By.CSS_SELECTOR,'#onetrust-accept-btn-handler')
        accept_cookie_btn.click()
        time.sleep(0.5)
        go_btn = self.driver.find_element(By.CSS_SELECTOR, ".start-text")
        go_btn.click()

        url_not_changed = True
        while url_not_changed:
            current_url = self.driver.current_url
            if len(re.findall(r'[0-9]',current_url)):
                url_not_changed = False
            time.sleep(1)

        down_speed = float(self.driver.find_element(By.CSS_SELECTOR, '.download-speed').text)
        self.current_down_speed = down_speed
        up_speed = float(self.driver.find_element(By.CSS_SELECTOR, '.upload-speed').text)
        self.current_up_speed = up_speed
        print("-->",down_speed, up_speed)

    def tweet_at_provider(self):
        self.connect_to_twitter()
        
        text = f'I pay an Internet connection for down:{self.down}/up{self.up} and I have down:{self.current_down_speed}/up{self.current_up_speed}'

        self.wait_for_selector("a[aria-label=Tweet]")
        new_tweet_button = self.driver.find_element(By.CSS_SELECTOR, "a[aria-label=Tweet]")
        new_tweet_button.click()

        self.wait_for_selector('div[aria-label="Tweet text"]')
        new_tweet_button = self.driver.find_element(By.CSS_SELECTOR, 'div[aria-label="Tweet text"]')
        new_tweet_button.send_keys(text)

        add_tweet_button = self.driver.find_element(By.CSS_SELECTOR, 'div[data-testid="tweetButton"]')
        add_tweet_button.click()



    def connect_to_twitter(self):
        self.driver.get(TWITTER_LOGIN_URL)
        self.wait_for_selector("input[type=text]")
        print("==> handeling email ....")
        input=self.driver.find_element(By.CSS_SELECTOR, 'input[type=text]')
        input.send_keys(self.twitter_mail)

        self.click_on_button_with_text('div[role=button]', "Next")

        self.wait_for_selector("input[type=text]")
        print("==> handeling username ....")
        username_input=self.driver.find_element(By.CSS_SELECTOR, 'input[type=text]')
        username_input.send_keys(self.twitter_username)

        self.click_on_button_with_text('div[role=button]', "Next")
        
        self.wait_for_selector('input[name="password"]')
        print("==> handeling password ...")
        username_input=self.driver.find_element(By.CSS_SELECTOR, 'input[name="password"]')
        username_input.send_keys(self.twitter_pass)
        
        self.click_on_button_with_text('div[role=button]', "Log in")


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

    def click_on_button_with_text(self,css_selector, text):
        buttons=self.driver.find_elements(By.CSS_SELECTOR, css_selector)
        for button in buttons :
            if button.text==text:
                button.click()
                break

    
            