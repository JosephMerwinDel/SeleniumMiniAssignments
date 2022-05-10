from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(ChromeDriverManager().install())

#Goibibo Logo
driver.find_element(by=By.XPATH, value=".header-sprite.logo")

#Login or Sign Up
driver.find_element(by=By.XPATH, value="div[@class='login__tab_wrapper']")

#Hotels, Flights, Cabs
driver.find_element(by=By.XPATH, value="a[text()='Hotels']")

#Round-trip
driver.find_element(by=By.XPATH, value="//span[.='Round-trip']")

#From
driver.find_element(by=By.XPATH, value="//span[text()='From']//following-sibling::p[text() = 'Enter city or airport']")

#To
driver.find_element(by=By.XPATH, value="//span[text()='To']//following-sibling::p[text() = 'Enter city or airport']")

#Search flights
driver.find_element(by=By.XPATH, value="//span[@class='sc-fHeRUh jHgPBA']")