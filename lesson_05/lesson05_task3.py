from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/inputs")

# Найти строку поиска
search_loc = "input"

search_box = driver.find_element(By.CSS_SELECTOR, search_loc)

# ввести "Sky"
search_box.send_keys("Sky")
sleep(2)   # пауза
# очистить поле
search_box.clear()
sleep(2)   # пауза
# ввести "Pro"
search_box.send_keys("Pro")
sleep(2)   # пауза

driver.quit()
