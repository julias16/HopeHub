from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import time

path = "C:/Users/hp/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe"

driver=webdriver.Chrome(service=Service(path))
driver.get('http://127.0.0.1:8000/accounts/login/')
driver.set_window_size(1120, 1000)

try:
    identifier_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "identifier"))
    )
    identifier_field.send_keys("mohona")

    password_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "password"))
    )
    password_field.send_keys("123")

    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "btn"))
    )
    login_button.click()

    time.sleep(3)

except NoSuchElementException as e:
    print("Element not found:", e)

except ElementClickInterceptedException as e:
    print("Could not click element:", e)


# exceptional (if password or username is wrong then it will go to the signup page)
try:
    signup_link = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Sign up"))
    )
    signup_link.click()
    time.sleep(2)
except NoSuchElementException:
    print("Signup link not found")

driver.quit()
