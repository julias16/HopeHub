from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

# ChromeDriver path
path = "C:/Users/USER/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe"

service = Service(path)
driver = webdriver.Chrome(service=service)
driver.set_window_size(1440, 1000)
wait = WebDriverWait(driver, 10)

try:
    # 1️⃣ LOGIN
    driver.get("http://127.0.0.1:8000/accounts/login/")
    print("🔹 Login page opened")

    identifier = wait.until(EC.presence_of_element_located((By.ID, "identifier")))
    password = wait.until(EC.presence_of_element_located((By.ID, "password")))
    login_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn")))

    identifier.send_keys("mohona")   # তোমার username
    password.send_keys("123")     # তোমার password
    login_button.click()
    print("✅ Logged in successfully")
    time.sleep(3)

    # 2️⃣ DONATION FORM PAGE OPEN
    driver.get("http://127.0.0.1:8000/donations/donateform/")
    print("🔹 Donation form page opened")
    time.sleep(2)

    # 3️⃣ FORM FILL-UP
    wait.until(EC.presence_of_element_located((By.NAME, "donor_name"))).send_keys("Kohinur Hossain Mim")
    driver.find_element(By.NAME, "donor_phone").send_keys("01737465097")
    driver.find_element(By.NAME, "donor_address").send_keys("Farmgate, Dhaka")
    driver.find_element(By.NAME, "item_type").send_keys("food")
    driver.find_element(By.NAME, "quantity").send_keys("5")
    driver.find_element(By.NAME, "item_name").send_keys("Rice, Dal, Vegetables")

    print("✅ Form fields filled successfully")

    # 4️⃣ FILE UPLOAD (optional)
    try:
        file_input = driver.find_element(By.NAME, "file_upload")
        file_input.send_keys(r"C:/Users/USER/Downloads/test_image.jpg")  # test image path
        print("✅ File uploaded successfully")
    except:
        print("⚠ File upload not found (optional).")

    # 5️⃣ SUBMIT FORM
    donate_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.donate-btn")))
    donate_button.click()
    print("✅ Donate button clicked")

    time.sleep(3)

    # 6️⃣ CHECK SUCCESS MESSAGE
    try:
        success_msg = driver.find_element(By.XPATH, "//p[contains(text(), 'success') or contains(text(), 'Thank')]")
        print("🎉 Donation submitted successfully →", success_msg.text)
    except:
        print("⚠ No visible success message found (may still have submitted).")

except TimeoutException as e:
    print("❌ Page load timeout:", e)

except Exception as e:
    print("❌ Unexpected error:", e)

finally:
    time.sleep(2)
    driver.quit()
    print("🔚 Test full completed.")