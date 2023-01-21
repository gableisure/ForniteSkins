from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import dotenv_values
from time import sleep
import pandas as pd

class Scraping:
    
    def __init__(self):
        self.env = dotenv_values('.env')
        self.driver = webdriver.Chrome()
        
        
    def run(self):
        self.driver.get(self.env.get('URL'))    
        skins = self.driver.find_element(By.XPATH, '//*[@id="main"]/div/div[4]/div').find_elements(By.CLASS_NAME, 'skin-caption-info')
        for skin in skins:
            """ print(skin.find_element(By.TAG_NAME, 'strong').get_attribute('innerHTML')) """
            
            # TODO: O código abaixo está dando erro
            
            """ print(skin.find_element(By.CLASS_NAME, 'text-small text-center').get_attribute('innerHTML')) """
        
        sleep(2)


