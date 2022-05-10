from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as waitime


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/")
driver.implicitly_wait(2)

driver.find_element(by=By.XPATH, value="//a[text() = 'JavaScript Alerts']").click()
ele = driver.find_element(by=By.XPATH, value="//button[text() = 'Click for JS Prompt']")
driver.execute_script("arguments[0].click();", ele)

alert = driver.switch_to.alert
print(alert.text)
time.sleep(2)
alert.send_keys("Test")
alert.dismiss()
time.sleep(5)