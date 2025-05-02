from selenium import webdriver
from selenium.webdriver.common.by import By

# запускаем драйвер
driver = webdriver.Chrome()
# устанавливаем ожидание
driver.implicitly_wait(20)

# переходим на страницу http://uitestingplayground.com/textinput
driver.get("http://uitestingplayground.com/textinput")

# находим строку поиска
search_box = driver.find_element(By.CSS_SELECTOR, "#newButtonName")

# вводим в поле ввода текст "SkyPro"
search_box.send_keys("SkyPro")

# нажимаем на синюю кнопку
driver.find_element(By.CSS_SELECTOR, "#updatingButton").click()

# получаем новый текст на кнопке
txt = driver.find_element(By.CSS_SELECTOR, "#updatingButton").text

# выводим текст в консоль ("SkyPro")
print(txt)

driver.quit()
