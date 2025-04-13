from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
import os
import time

load_dotenv()

def login_to_erp():
    options = Options()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)

    driver.get("https://erp.silicon.ac.in/estcampus/index.php")
    time.sleep(0)

    # Enter username and password using IDs
    username_input = driver.find_element(By.XPATH, '//*[@id="username"]')
    password_input = driver.find_element(By.XPATH, '//*[@id="password"]')

    username_input.send_keys(os.getenv("ERP_USERNAME"))
    password_input.send_keys(os.getenv("ERP_PASSWORD"))

    # Click the login button using its actual ID
    login_button = driver.find_element(By.XPATH, '//*[@id="btnLogIn"]')
    login_button.click()

    time.sleep(1)  # Wait for redirection after login
    return driver
