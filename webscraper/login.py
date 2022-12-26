from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import csv
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
import time

def RequestRide(url):


    # Get WebDriver
    driver = webdriver.Chrome(executable_path="chromedriver_win32/chromedriver.exe", chrome_options=chrome_options)
    driver.maximize_window()
    driver.get(url)

    # Finding elements on request ride page
    driver.find_element(By.XPATH, "//button[@class='d0 bp c1 d1 ae c0 aj d2 d3 bz d4 d5 c3 d6 d7 d8 bx d9 da db dc ao']").click()

    waited = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//input[@data-inputkey='pickup']"))
    )

    driver.get("https://m.uber.com/looking?drop%5B0%5D=%7B%22latitude%22%3A33.9450646%2C%22longitude%22%3A-118.4055151%2C%22addressLine1%22%3A%22Los%20Angeles%20International%20Airport%20%28LAX%29%22%2C%22addressLine2%22%3A%221%20World%20Way%2C%20Los%20Angeles%22%2C%22id%22%3A%22c2523974-0f10-358d-8de9-8de58a6abcd1%22%2C%22provider%22%3A%22uber_places%22%2C%22index%22%3A0%7D&pickup=%7B%22latitude%22%3A34.0687758%2C%22longitude%22%3A-118.4439306%2C%22addressLine1%22%3A%22UCLA%22%2C%22addressLine2%22%3A%22405%20Hilgard%20Ave%2C%20Los%20Angeles%22%2C%22id%22%3A%2217035f06-801f-3cfb-87b7-365e04a5e5db%22%2C%22provider%22%3A%22uber_places%22%2C%22index%22%3A0%7D&vehicle=125")
    
    cnt = 0
    while True:
        time.sleep(10)
        driver.refresh()

        findPrice = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//p[@class='_css-bDzehI']"))
        )

        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        current_price = driver.find_element(By.XPATH, "//p[@class='_css-bDzehI']").text
        info = [current_time, current_price[1:]]

        file = open("data.csv", 'a')
        writer = csv.writer(file)
        writer.writerow(info)

        cnt+=1
    
    
    
    

RequestRide("https://m.uber.com/looking")


