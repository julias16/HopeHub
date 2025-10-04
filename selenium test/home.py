from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException
import time


# ChromeDriver path

path = "C:/Users/hp/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe"
service = Service(path)
driver = webdriver.Chrome(service=service)
driver.set_window_size(1440, 1000)
wait = WebDriverWait(driver, 5)

try:

    # Login

    driver.get("http://127.0.0.1:8000/accounts/login/")
    print(" Login page opened")

    identifier_field = wait.until(EC.presence_of_element_located((By.ID, "identifier")))
    identifier_field.send_keys("mohona")

    password_field = wait.until(EC.presence_of_element_located((By.ID, "password")))
    password_field.send_keys("123")

    login_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn")))
    login_button.click()
    print(" Logged in successfully")
    time.sleep(2)


    # Go to Home page explicitly

    driver.get("http://127.0.0.1:8000/")
    print(" Home page opened:", driver.title)
    hero_heading = wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
    print(" Hero heading:", hero_heading.text)


    # Navbar links test

    navbar_links = ["Home", "About", "Donate", "Blog", "Contact"]
    for link_text in navbar_links:
        try:
            link = driver.find_element(By.LINK_TEXT, link_text)
            link.click()
            time.sleep(2)
            print(f" Navbar '{link_text}' page loaded → Title: {driver.title}")

        except Exception as e:
            print(f" Navbar '{link_text}' test failed:", e)


    #  Category pages test (sequential automatic)

    driver.get("http://127.0.0.1:8000/")
    time.sleep(2)
    categories = {
        "Food": "http://127.0.0.1:8000/foodfirst",
        "Clothes": "http://127.0.0.1:8000/clothsfirst",
        "Furniture": "http://127.0.0.1:8000/furniturefirst"
    }

    for cat, url in categories.items():
        driver.get(url)
        time.sleep(2)
        print(f" {cat} page loaded → Title: {driver.title}")
        driver.get("http://127.0.0.1:8000/")  # back to home automatically
        time.sleep(2)


    #Donate button test

    try:
        donate_btn = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn-donate")))
        donate_btn.click()
        time.sleep(2)
        print(" Donate Now page loaded → Title:", driver.title)
        driver.get("http://127.0.0.1:8000/")  # back to home automatically
    except Exception as e:
        print(" Donate button test failed:", e)




    # Scroll to footer

    total_height = driver.execute_script("return document.body.scrollHeight")
    current_pos = 0
    step = 100
    print(" Scrolling gradually to footer...")

    while current_pos < total_height:
        driver.execute_script(f"window.scrollBy(0, {step});")
        current_pos += step
        time.sleep(0.1)

    print(" Reached footer")


    # Footer elements test

    # Social icons
    social_icons = ["facebook.png", "whatsapp.png", "gmail.png"]
    for icon in social_icons:
        try:
            img = driver.find_element(By.XPATH, f"//img[contains(@src,'{icon}')]")
            img.click()
            time.sleep(2)
            driver.switch_to.window(driver.window_handles[-1])
            print(f" Social icon '{icon}' opened → URL: {driver.current_url}")
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
        except Exception as e:
            print(f" Social icon '{icon}' test failed:", e)

    # Footer quick links
    footer_links = [
        # Quick Links
        "Home", "About Us", "Donate", "Contact Us",
        # Resources
        "FAQ", "Blog", "Trams & Conditions", "Privacy Policy"
    ]

    for f_link in footer_links:
        # Scroll to footer
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)

        try:
            link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, f_link)))
            link.click()
            time.sleep(2)
            print(f" Footer link '{f_link}' page loaded → Title: {driver.title}")
        except Exception as e:
            print(f" Footer link '{f_link}' test failed:", e)


    # Back to home page and scroll
    driver.get("http://127.0.0.1:8000/")
    time.sleep(2)
    total_height = driver.execute_script("return document.body.scrollHeight")
    current_pos = 0
    step = 100
    print(" Scrolling gradually to footer...")

    while current_pos < total_height:
        driver.execute_script(f"window.scrollBy(0, {step});")
        current_pos += step
        time.sleep(0.1)

    print(" Reached footer")


    # Contact form
    try:
        # Name
        name_input = wait.until(EC.presence_of_element_located((By.NAME, "name")))
        name_input.send_keys("Test User")

        # Email
        email_input = driver.find_element(By.NAME, "email")
        email_input.send_keys("test@example.com")

        # Message
        message_input = driver.find_element(By.NAME, "message")
        message_input.send_keys("This is a test message.")

        # Submit
        submit_btn = driver.find_element(By.XPATH, "//button[text()='Send Message']")
        submit_btn.click()
        print(" Footer contact form submitted (check Web3Forms)")

        time.sleep(3)
    except Exception as e:
        print(" Footer contact form test failed:", e)
    # Optional: scroll up a little after checking
    driver.execute_script("window.scrollTo(0, 0);")

    print("\n Footer test completed successfully!")

except TimeoutException as e:
    print(" Page took too long to load:", e)

finally:
    time.sleep(3)
    driver.quit()