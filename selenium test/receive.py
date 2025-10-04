from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

# ChromeDriver path
path = "C:/Users/hp/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe"
service = Service(path)
driver = webdriver.Chrome(service=service)
driver.set_window_size(1440, 1000)
wait = WebDriverWait(driver, 5)

try:
    # 1️ Login
    driver.get("http://127.0.0.1:8000/accounts/login/")
    print(" Login page opened")

    identifier_field = wait.until(EC.presence_of_element_located((By.ID, "identifier")))
    identifier_field.send_keys("mohona")

    password_field = wait.until(EC.presence_of_element_located((By.ID, "password")))
    password_field.send_keys("123")

    login_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn")))
    login_button.click()
    print(" Logged in successfully")
    time.sleep(3)

    # 2️ Category first pages
    categories = ["foodfirst", "clothsfirst", "furniturefirst"]

    for cat in categories:
        first_page_url = f"http://127.0.0.1:8000/{cat}"
        driver.get(first_page_url)
        print(f"\n Category first page opened: {cat}")
        time.sleep(2)

        # Click "Receive" button on the first page
        try:
            receive_btn = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Receive")))
            receive_btn.click()
            time.sleep(2)
            print(f" '{cat}' Receive page opened → Title: {driver.title}")
        except TimeoutException:
            print(f" Receive button not found for category: {cat}")
            continue

        # Loop through all items on Receive page
        items = driver.find_elements(By.CSS_SELECTOR, ".item-card a")
        print(f"Found {len(items)} items in {cat} receive page.")

        for index, item in enumerate(items, start=1):
            try:
                # Scroll to item
                driver.execute_script("arguments[0].scrollIntoView({behavior:'smooth', block:'center'});", item)
                time.sleep(1)

                # Click item
                item.click()
                time.sleep(2)

                # Verify item detail page
                print(f" {cat} item {index} detail page → Title: {driver.title}")

                # Go back to Receive page
                driver.back()
                time.sleep(2)

                # Re-fetch items after going back
                items = driver.find_elements(By.CSS_SELECTOR, ".item-card a")

            except Exception as e:
                print(f" {cat} item {index} test failed:", e)

    print("\n All categories and items tested successfully!")

except TimeoutException as e:
    print(" Page took too long to load:", e)

finally:
    driver.quit()
