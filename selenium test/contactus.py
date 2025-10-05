from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import time

# ChromeDriver path
path = "C:/Users/USER/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe"
driver = webdriver.Chrome(service=Service(path))

#  Contact Us open
driver.get("http://127.0.0.1:8000/contactus")
driver.set_window_size(1120, 1000)

try:

    name_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "name"))
    )
    name_field.send_keys("Kohinur Hossain Mim")


    email_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "email"))
    )
    email_field.send_keys("mim@example.com")


    message_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "message"))
    )
    message_field.send_keys("This is a test message from Selenium automation.")


    send_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
    )
    send_button.click()
    print("✅ Form submitted successfully!")

    time.sleep(3)

except NoSuchElementException as e:
    print("❌ Element not found:", e)

except ElementClickInterceptedException as e:
    print("❌ Could not click element:", e)

finally:
    print("🧾 Contact Us page testing completed.")
    time.sleep(3)
    driver.quit()