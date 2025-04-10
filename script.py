from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = Options()

service = Service('/usr/bin/chromedriver')
driver = webdriver.Chrome(service=service, options=chrome_options)

# Maximize the window after initializing the driver
driver.maximize_window()

try:
    driver.get('https://www.intervue.io')

    # Click "Login" in the header
    login_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="iv-homepage-login"]/div/a[2]'))
    )
    login_btn.click()

    WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))

    # Store the original window handle (before the new tab opens)
    original_window = driver.current_window_handle

    # Switch to the new tab (which should be the second window)
    for window_handle in driver.window_handles:
        if window_handle != original_window:
            driver.switch_to.window(window_handle)
            break

    # Click "Login for Companies" from the modal
    company_login_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/section[1]/div/div/div[1]/div/div/a"))
    )
    company_login_btn.click()


    # # Wait for email input and enter email
    email_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="login_email"]'))
    )
    email_input.send_keys("neha@intervue.io")

    
    # Enter password
    password_input = driver.find_element(By.XPATH, '//*[@id="login_password"]')
    password_input.send_keys("Ps@neha@123")

    # Press enter to login
    password_input.send_keys(Keys.RETURN)

finally:
    driver.quit()