from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from scrape import Scrape
import time
FORM = "https://docs.google.com/forms/d/e/1FAIpQLSdtU3ma9fIZw80sYk9ZnZbOBYquNr-NIPdbyku2AwyAy9_7OQ/viewform?usp=sf_link"


class HandelingData(Scrape):
    def __init__(self) -> None:
        super().__init__()
        
    def goto(self):
        self.driver.get(FORM)

        for flat_infos in self.data:
            self.insert_form_data(flat_infos)

    def insert_form_data(self, flat_infos):
        inputs = self.driver.find_elements(By.CSS_SELECTOR, "input:not([type=hidden])")
        print("len : ", len(inputs))
        for i,input in enumerate(inputs):
            print(flat_infos[i])
            input.send_keys(flat_infos[i])
        self.driver.find_element(By.CSS_SELECTOR, "div[role=button]").click()

        super().wait_for_element_with_text('a',"Envoyer une autre réponse")
        self.driver.find_element(By.CSS_SELECTOR, "a").click()
        time.sleep(3)


    
    