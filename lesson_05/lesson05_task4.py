from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

driver.get("http://the-internet.herokuapp.com/login")
# В поле username ввести значение tomsmith.
element_login = driver.find_element(By.ID, "username")
element_login.send_keys("tomsmith")

# В поле password ввести значение SuperSecretPassword!
element_pass = driver.find_element(By.ID, "password")
element_pass.send_keys("SuperSecretPassword!")

sleep(3)   # пауза

# Нажать кнопку Login
search_field = "i.fa-sign-in"
search_input = driver.find_element(By.CSS_SELECTOR, search_field).click()

# Вывести текст с зеленой плашки в консоль.
search_green = "#flash"
search_input = driver.find_element(By.CSS_SELECTOR, search_green).text
print(search_input)

sleep(3)   # пауза

# Закрыть браузер
driver.quit()
