from cmath import log
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import os
import time 

load_dotenv()
driver = webdriver.Chrome()

driver.get(os.environ['URL'])

element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "email")))

username_input = driver.find_element(By.ID, value='email')
password_input = driver.find_element(By.ID, value='password')

username_input.send_keys(os.environ['USERNAME'])
password_input.send_keys(os.environ['PASSWORD'])

driver.find_element(By.XPATH, value='//form[@class="auth-form"]/div[@class="margin-top-1x flow flow-3 divided"]/button').click()

element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, f"user-dossier-cntn-{os.environ['CLIENT_ID']}")))

# scroll!
wait = WebDriverWait(driver, 10)
find_elem = None
scroll_from = 0
scroll_limit = 3000
while not find_elem:
    time.sleep(2)
    driver.execute_script("window.scrollTo(%d, %d);" %(scroll_from, scroll_from+scroll_limit))
    scroll_from += scroll_limit
    try:
        find_elem = wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Dicembre 2020')]")))
    except TimeoutException:
        pass

elements: list[WebElement] = driver.find_element(By.ID, value=f"user-dossier-cntn-{os.environ['CLIENT_ID']}").find_elements(By.XPATH, value='//button[@class="button button-compact button-primary button-reverse dossier-download-item"]')

for el in elements:
    driver.execute_script("arguments[0].click();", el)
    time.sleep(30)

driver.close()