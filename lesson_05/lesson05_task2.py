from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')

driver = webdriver.Chrome(options=options)

driver.get("http://uitestingplayground.com/dynamicid")
search_field = "button.btn-primary"
search_input = driver.find_element(By.CSS_SELECTOR, search_field).click()

sleep(3)
