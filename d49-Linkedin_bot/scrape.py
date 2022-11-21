import time 
import dotenv 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import csv
import re
config = dotenv.dotenv_values('../.env')
chrome_driver_path="../selenium_driver/chromedriver"

class Scrape:
    def __init__(self) -> None:
        self.s=Service(chrome_driver_path)
        self.driver = webdriver.Chrome(service=self.s)
        self.base_url='https://www.linkedin.com'
        self.driver.get(self.base_url)
        self.offers_in_the_page = None

    def connect(self):
        email_input = self.driver.find_element(By.ID,"session_key")
        print("email : ", email_input)
        email_input.send_keys(config['LI_MAIL'])
        pass_input = self.driver.find_element(By.ID,"session_password")
        pass_input.send_keys(config['LI_PASS'])
        submit_button = self.driver.find_element(By.CSS_SELECTOR, "button.sign-in-form__submit-button")
        submit_button.click()

    def analyse(self):
        state=True
        start=0
        while state:
            print("start : ", start)
            jobs_url = f'https://www.linkedin.com/jobs/search/?currentJobId=3009054686&f_AL=true&f_E=2&f_PP=101240143&f_TPR=r2592000&f_WT=2%2C3&geoId=105015875&sortBy=R&start={start}'
            self.driver.get(jobs_url)
            time.sleep(1)
            self.get_offers_block()
            self.handle_offers_in_page()
            time.sleep(1)
            for i in range(5):
                self.driver.find_element(By.CLASS_NAME,'scaffold-layout__list').send_keys(Keys.END)
                time.sleep(0.5)
            start+=25
    
    def get_offers_block(self):
        try:
            offers_in_the_page = self.driver.find_elements(By.CSS_SELECTOR,".scaffold-layout__list-container > li")
            print('lis len : ', len(offers_in_the_page))
            self.offers_in_the_page = offers_in_the_page
        except:
            self.offers_in_the_page = None

    def handle_offers_in_page(self):    
        i=0
        if not self.get_offers_block:
            return
        for offer in self.offers_in_the_page:
            f=open('offers.csv','a')
            writer = csv.writer(f)
            print(f'+++{i}+++')
            try:
                time.sleep(2)
                role = offer.find_element(By.CSS_SELECTOR,"div > div > div > div:nth-child(2) > div > a")
                role.click()
                time.sleep(2.5)
                offer_link = role.get_attribute('href')
                enterprise_name = offer.find_element(By.CSS_SELECTOR,"div > div > div > div:nth-child(2) > div:nth-child(2) > a")
                print("====> role : ", role.text)
                print("offer_link : ", offer_link)
                print("enteprise : ", enterprise_name.text)
                job_description = self.driver.find_element( By.CLASS_NAME, "jobs-description" )
                # print( "job_description : ", job_description.text )
                res = re.findall(r'(fullstack|backend|node|react)',job_description.text, flags=re.IGNORECASE)
                
                if len(res)>0 :
                    time.sleep(1)
                    print("interesting !!  <======")
                    row = [role.text, enterprise_name.text, offer_link]
                    print("==> ROW : ", row)
                    writer.writerow(row)
                    res = self.send_appliance()
            except Exception as e:
                print("!!!!!!!",e)
            f.close()
            i+=1
        return True

    def send_appliance(self):
        print("==> applying....")
        try:
            button = self.driver.find_element(By.CSS_SELECTOR, '.jobs-details__main-content button.jobs-apply-button')
            button.click()
            time.sleep(1)
            button_send = self.driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Envoyer la candidature"]')
            button_send.click()
            time.sleep(1)
            #=================
            #......
            dismiss_button = self.driver.find_element(By.CSS_SELECTOR,'.artdeco-modal__dismiss')
            dismiss_button.click()
            #=================
            print("===> Applied !!!! ^^^^^^")
            return True
        except :
            self.escape()
            print("===> Error : applying ... :-(")
            return False

    def escape(self):
        try:
            print("==>clicking overlay")
            overlay = self.driver.find_element(By.CSS_SELECTOR,'.artdeco-modal__dismiss')
            overlay.click()
            time.sleep(0.5)
            print("==>clicking supprimer")
            escape_button = self.driver.find_element(By.CSS_SELECTOR,'button[data-control-name="discard_application_confirm_btn"]')
            escape_button.click()
        except:
            pass