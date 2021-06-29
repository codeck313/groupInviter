import csv
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.common.exceptions import UnexpectedAlertPresentException

dataBaseName = 'dataV1.csv'
nameRow = 2
numberRow = 3

msg1 = "I am"
msg2 = "Lazy"
delayTime = 15

driver = webdriver.Chrome(executable_path="./chromedriver")

with open(dataBaseName, 'r') as file:
    reader = csv.reader(file)
    driver.get('https://web.whatsapp.com')

    # Scan the code before proceeding further
    input('Ready?(Press Enter to Continue)')
    for row in reader:
        print("Sending to", row[nameRow])
        try:
            driver.execute_script("window.open();")
            driver.switch_to_window(driver.window_handles[1])
            driver.get(
                'https://web.whatsapp.com/send?phone=+91{}'.format(row[numberRow]))
            timeout = 5

            try:
                element_present = EC.presence_of_element_located(
                    (By.CLASS_NAME, '_2A8P4'))
                WebDriverWait(driver, timeout).until(element_present)

            except TimeoutException:
                print("Timed out waiting for page to load")

            WebDriverWait(driver, delayTime)
            msg_box = driver.find_element_by_class_name('_2A8P4')

            ActionChains(driver).key_down(
                Keys.SHIFT).key_down(Keys.ENTER).perform()
            ActionChains(driver).key_up(
                Keys.SHIFT).key_up(Keys.ENTER).perform()
            msg_box.send_keys(msg1)
            ActionChains(driver).key_down(
                Keys.SHIFT).key_down(Keys.ENTER).perform()
            ActionChains(driver).key_up(
                Keys.SHIFT).key_up(Keys.ENTER).perform()
            msg_box.send_keys(msg2)

            input('Confirm?')
            driver.find_element_by_class_name('_1E0Oz').click()
            driver.close()
            driver.switch_to_window(driver.window_handles[0])
        except UnexpectedAlertPresentException:
            driver.close()
            driver.switch_to_window(driver.window_handles[1])
            pass
