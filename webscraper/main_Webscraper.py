from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

import time
from datetime import datetime
import csv, os

# CONSTANTS
DRIVER_PATH = "chromedriver_win32/chromedriver.exe"
UBER_WEBSITE = "https://m.uber.com/looking?drop%5B0%5D=%7B%22latitude%22%3A33.9450646%2C%22longitude%22%3A-118.4055151%2C%22addressLine1%22%3A%22Los%20Angeles%20International%20Airport%20%28LAX%29%22%2C%22addressLine2%22%3A%221%20World%20Way%2C%20Los%20Angeles%22%2C%22id%22%3A%22c2523974-0f10-358d-8de9-8de58a6abcd1%22%2C%22provider%22%3A%22uber_places%22%2C%22index%22%3A0%7D&pickup=%7B%22latitude%22%3A34.0687758%2C%22longitude%22%3A-118.4439306%2C%22addressLine1%22%3A%22UCLA%22%2C%22addressLine2%22%3A%22405%20Hilgard%20Ave%2C%20Los%20Angeles%22%2C%22id%22%3A%2217035f06-801f-3cfb-87b7-365e04a5e5db%22%2C%22provider%22%3A%22uber_places%22%2C%22index%22%3A0%7D&vehicle=125"
EMAIL = "speedsayssuii" # YOUR OWN EMAIL
PASSWORD = "smokeweedeveryday" # YOUR OWN PASSWORD TO GMAIL
DATA_FILE = "data.csv"

def RequestRide(url):

    # Get WebDriver.
    driver = webdriver.Chrome(executable_path=DRIVER_PATH, chrome_options=chrome_options)
    driver.maximize_window()
    driver.get(url)

    # Clicks to login via Google.
    driver.find_element(By.XPATH, "//button[@class='d9 bp cb da ae ca aj bw db c9 dc dd cd de df dg c1 dh di dj dk ao']").click()

    # Switch to the Google Auth pop-up.
    driver.switch_to.window(driver.window_handles[1])

    print(driver.current_url)

    # Enters in gmail.
    waited = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@type='email']")),
        EC.presence_of_element_located((By.XPATH, "//span[text()='Next']"))
    )
    driver.find_element(By.XPATH, "//input[@type='email']").send_keys(EMAIL)
    driver.find_element(By.XPATH, "//span[text()='Next']").click()

    # Enters in password.
    waited = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@name='password']")),
        EC.presence_of_element_located((By.XPATH, "//span[text()='Next']"))
    )
    driver.refresh()
    driver.find_element(By.XPATH, "//input[@name='password']").send_keys(PASSWORD)
    driver.find_element(By.XPATH, "//span[text()='Next']").click()

    # After Google Auth closes, need to switch back to original window.
    driver.switch_to.window(driver.window_handles[0])

    # Waits until there is a field to enter in location.
    waited = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//input[@data-inputkey='pickup']"))
    )
    
    # Infinite loop to gather data and write to data.csv.
    while True:

        # Refresh and relaod
        time.sleep(60)
        driver.get(UBER_WEBSITE)

        # Sometimes the website crashes from reloading or accessing it a lot so idea is to try to get a price 
        # but if there is no price to get, reload the window.
        findPrice = None
        try:
            findPrice = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//p[@class='_css-bDzehI']"))
            )
        except:
            # check_label = WebDriverWait(driver, 10).until(
            #     EC.presence_of_element_located((By.XPATH, "//button[text()='Change']"))
            # )
            # check_label.click()
            continue

        # Get current time and price
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        current_price = findPrice.text
        info = [current_time, current_price[1:]]

        # Write to data.csv with the current time and price.
        file = open(DATA_FILE, 'a')
        writer = csv.writer(file)
        writer.writerow(info)
    
    
    
    

RequestRide("https://m.uber.com/looking")


