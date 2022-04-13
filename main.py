from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

load_dotenv()
driver = webdriver.Chrome()

driver.get(os.environ['URL'])

element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "email")))

username_input = driver.find_element(By.ID, value='email')
password_input = driver.find_element(By.ID, value='password')

username_input.send_keys(os.environ['USERNAME'])
password_input.send_keys(os.environ['PASSWORD'])

driver.find_element(By.XPATH, value='//form[@class="auth-form"]/div[@class="margin-top-1x flow flow-3 divided"]/button').click()

element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "user-dossier-cntn-sc159b8dae2c3226")))

clickable_buttons = driver.find_element(By.ID, value='user-dossier-cntn-sc159b8dae2c3226').find_element(By.XPATH, value='//button[@class="button button-compact button-primary button-reverse dossier-download-item"]')

print(clickable_buttons)