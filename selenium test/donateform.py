from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import os


path = "C:/Users/hp/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe"
service = Service(path)
driver = webdriver.Chrome(service=service)
driver.set_window_size(1440, 1000)
wait = WebDriverWait(driver, 10)

BASE_URL = "http://127.0.0.1:8000"

try:
    #  Login first
    driver.get(f"{BASE_URL}/accounts/login/")
    print("🟢 Login page opened")

    identifier_field = wait.until(EC.presence_of_element_located((By.ID, "identifier")))
    identifier_field.send_keys("mohona")

    password_field = wait.until(EC.presence_of_element_located((By.ID, "password")))
    password_field.send_keys("123")

    login_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn")))
    login_button.click()
    print("🟢 Logged in successfully")
    time.sleep(3)

    #  Open donation page
    driver.get(f"{BASE_URL}/donations/donateform/")
    print("🟢 Donation page opened")
    time.sleep(2)

    #  Fill donation form
    wait.until(EC.presence_of_element_located((By.NAME, "donor_name"))).send_keys("Sadia Afrin Mohona")
    time.sleep(2)
    driver.find_element(By.NAME, "donor_phone").send_keys("01712345678")
    time.sleep(2)
    driver.find_element(By.NAME, "donor_address").send_keys("Dhaka, Bangladesh")
    time.sleep(2)
    print(" Donor details filled")

    # Select item type
    item_type = Select(driver.find_element(By.NAME, "item_type"))
    item_type.select_by_value("clothes")
    time.sleep(2)
    print(" Item type selected: clothes")

    # Quantity
    driver.find_element(By.NAME, "quantity").send_keys("5")
    print(" Quantity added")
    time.sleep(2)

    # Item name / description
    driver.find_element(By.NAME, "item_name").send_keys("Three Piece")
    print(" Item name added")
    time.sleep(2)


    image_path = os.path.abspath("C:/Users/hp/Downloads/threePiece.jpg")
    if os.path.exists(image_path):
        driver.find_element(By.NAME, "file_upload").send_keys(image_path)
        print(" Image uploaded")
        time.sleep(2)
    else:
        print("️ sample.jpg not found — skipping image upload")

    #  Submit form
    submit_btn = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "donate-btn")))
    submit_btn.click()
    print("🟢 Donation form submitted")
    time.sleep(2)

    #  Wait for success message
    try:
        success_message = wait.until(EC.presence_of_element_located((By.XPATH, "//p[contains(text(),'successfully') or contains(text(),'Thank')]")))
        print(" Donation success message found:", success_message.text)
        time.sleep(2)
    except TimeoutException:
        print(" No success message appeared — check form validation or redirect")


    time.sleep(2)
    print("\n Donation form tested successfully!")

except TimeoutException as e:
    print(" Page took too long to load:", e)

finally:
    driver.quit()
    print(" Browser closed")
