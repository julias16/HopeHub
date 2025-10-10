from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import time


path = "C:/Users/hp/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe"

# Browser open
driver = webdriver.Chrome(service=Service(path))
driver.get("http://127.0.0.1:8000/accounts/signup/")
driver.set_window_size(1120, 1000)

try:
    # Wait for page to load fully
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "username"))
    )

    # Fill form fields
    driver.find_element(By.ID, "name").send_keys("Test User")
    driver.find_element(By.ID, "username").send_keys("testuser123")
    driver.find_element(By.ID, "email").send_keys("testuser123@gmail.com")
    driver.find_element(By.ID, "phone").send_keys("01700000000")
    driver.find_element(By.ID, "address").send_keys("Dhaka, Bangladesh")
    driver.find_element(By.ID, "password1").send_keys("TestPass123")
    driver.find_element(By.ID, "password2").send_keys("TestPass123")

    # Click the Sign Up button
    signup_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "btn"))
    )
    signup_button.click()

    time.sleep(3)

    print("✅ Signup form submitted successfully!")

except NoSuchElementException as e:
    print("❌ Element not found:", e)

except ElementClickInterceptedException as e:
    print("❌ Could not click the button:", e)

# Optional: check if redirected to login or home page
try:
    WebDriverWait(driver, 5).until(
        EC.url_contains("login")  # check if redirected to login page
    )
    print("✅ Successfully redirected to the login page after signup.")
except:
    print("⚠ No redirect detected. Please verify manually if the signup was successful.")

driver.quit()
