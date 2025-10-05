from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time

# ✅ ChromeDriver path (update this if needed)
path = "C:/Users/USER/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe"
driver = webdriver.Chrome(service=Service(path))

# ✅ Open About Page
driver.get("http://127.0.0.1:8000/aboutus")
driver.set_window_size(1120, 1000)

try:
    # --- Check if About Us heading is visible ---
    heading = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//h1[text()='About Us']"))
    )
    print("✅ About Us heading found!")

    # --- Check 'Learn More' button ---
    learn_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "learn-btn"))
    )
    print("✅ Learn More button found!")
    learn_btn.click()
    time.sleep(1)
    print("✅ Learn More button clicked successfully!")

    # --- Check footer contact form elements ---
    name_field = driver.find_element(By.NAME, "name")
    email_field = driver.find_element(By.NAME, "email")
    message_field = driver.find_element(By.NAME, "message")

    name_field.send_keys("Test User")
    email_field.send_keys("test@example.com")
    message_field.send_keys("This is a test message.")
    print("✅ Contact form fields filled successfully!")

    # --- Check footer links (Quick Links) ---
    links = driver.find_elements(By.CSS_SELECTOR, ".footer-col.links ul li a")
    print(f"✅ Found {len(links)} quick links in the footer.")
    for link in links:
        print(" -", link.text)

    # --- Check social icons are loaded ---
    social_icons = driver.find_elements(By.CSS_SELECTOR, ".social-icons img")
    if len(social_icons) > 0:
        print(f"✅ Found {len(social_icons)} social icons in the footer.")
    else:
        print("❌ No social icons found!")

except NoSuchElementException as e:
    print("❌ Element not found:", e)

except TimeoutException as e:
    print("❌ Timeout waiting for element:", e)

finally:
    time.sleep(3)
    driver.quit()
    print("🔚 Test Completed!")