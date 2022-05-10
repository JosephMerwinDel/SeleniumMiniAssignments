from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as waitime

def launch_browser():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.get("http://webdriveruniversity.com/")
    driver.implicitly_wait(2)
    return driver

def check_buttons(driver):
    driver.find_element(by=By.XPATH, value="//h1[text() = 'BUTTON CLICKS']").click()
    print("Parent window title: " + driver.title)
    print(driver.window_handles)
    print(driver.current_window_handle)
    driver.switch_to.window(driver.window_handles[1])
    ele = WebDriverWait(driver, 10).until(waitime.presence_of_element_located((By.XPATH, "//p[text()='CLICK ME!']")))
    ele.click()
    time.sleep(3)
    driver.find_element(by = By.XPATH, value="//button[text() = 'Close']").click()
    time.sleep(4)
    driver.quit

def dropdowns(driver):
    driver.find_element(by=By.XPATH, value="//h1[text() = 'DROPDOWN, CHECKBOXE(S) & RADIO BUTTON(S)']").click()
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(3)
    driver.find_element(by=By.XPATH, value="//input[@value = 'option-1']").click()
    select = Select(driver.find_element(by=By.XPATH, value="//select[@id = 'dropdowm-menu-1']"))
    select.select_by_visible_text("C#")
    driver.quit

def autocomplete(driver):
    driver.find_element(by=By.XPATH, value="//h1[text() = 'AUTOCOMPLETE TEXTFIELD']").click()
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(3)
    driver.find_element(by=By.XPATH, value="//input[@id = 'myInput']").send_keys("Apple")
    time.sleep(3)
    driver.find_element(by=By.XPATH, value="//input[@id = 'submit-button']").click()

def scroll(driver):
    driver.find_element(by=By.XPATH, value="//h1[text() = 'SCROLLING AROUND']").click()
    time.sleep(2)
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(3)
    driver.find_element(by=By.XPATH, value="//div[text() = 'Well done for scrolling to me!']")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()

def 

driver = launch_browser()
check_buttons(driver)
driver = launch_browser()
dropdowns(driver)
driver = launch_browser()
autocomplete(driver)
driver = launch_browser()
scroll(driver)

'''try:
    wait(browser, 10).until(EC.element_to_be_clickable((By.xp, "shopping-selector-parent-process-modal-close-click"))).click()
except TimeoutException:
    print("No popup...")'''






