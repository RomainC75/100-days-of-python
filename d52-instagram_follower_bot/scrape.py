from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
chrome_driver_path="../selenium_driver/chromedriver"
import time
import re

INSTA_URL = "https://www.instagram.com"
clickable_blue = "0, 149, 246"


class Scrape:
    def __init__(self, insta_mail, insta_pass) -> None:
        self.s=Service(chrome_driver_path)
        self.driver = webdriver.Chrome(service=self.s)
        self.insta_mail = insta_mail
        self.insta_pass = insta_pass

    def login(self):
        self.driver.get(INSTA_URL)
        time.sleep(2)
        print("==> handeling cookies ....")
        self.click_on_button_with_text("button","Allow essential and optional cookies")
        print("==> handeling credentials...")
        time.sleep(1)
        user_input=self.driver.find_element(By.CSS_SELECTOR,"input[name=username]")
        user_input.send_keys(self.insta_mail)
        time.sleep(1)
        user_input=self.driver.find_element(By.CSS_SELECTOR,'input[name="password"]')
        user_input.send_keys(self.insta_pass)
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR,"#loginForm > div > div:nth-child(3)").click()
        
        self.wait_for_element_with_text("button", "Not Now")
        self.click_on_button_with_text('button', "Not Now")

    def find_followers(self, target_account):
        self.driver.get(f"{INSTA_URL}/{target_account}/followers")
        self.wait_for_selector("div[role=dialog]")
        # self.wait_for_selector("button[type=button]")
        self.wait_for_element_with_text("div[role=dialog] button[type=button]", "Follow")
        
        follower_window = self.driver.find_element(By.CSS_SELECTOR,"div[role=dialog]  > div > div:nth-child(2) > div > div > div:nth-child(2)")
        print("text : ", follower_window.text)
        for i in range(15):
            self.driver.execute_script("arguments[0].scrollIntoView(true);", follower_window);
            time.sleep(0.1)
        #==>follow
        self.click_on_buttons_with_text(follower_window, "button", "Follow")

 
                
    def click_on_button_with_text(self,css_selector, text):
        buttons=self.driver.find_elements(By.CSS_SELECTOR, css_selector)
        for button in buttons :
            if button.text==text:
                button.click()
                break
    
    def click_on_buttons_with_text(self, element, css_selector, text):
        buttons=element.find_elements(By.CSS_SELECTOR, css_selector)
        for button in buttons :
            if button.text==text and button.value_of_css_property("background-color") == "rgba(0, 149, 246, 1)":
                button.click()
                time.sleep(2)
        if self.still_users_to_follow(element, css_selector, text):
            self.click_on_buttons_with_text(element, css_selector, text)

    def still_users_to_follow(self, element, css_selector, text):
        buttons=element.find_elements(By.CSS_SELECTOR, css_selector)
        for button in buttons :
            if button.text==text and button.value_of_css_property("background-color") == "rgba(0, 149, 246, 1)":
                return True
        return False