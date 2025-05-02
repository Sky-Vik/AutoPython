from selenium import webdriver
from selenium.webdriver.common.by import By

# запускаем драйвер
driver = webdriver.Chrome()
# устанавливаем ожидание
driver.implicitly_wait(20)

# переходим на страницу http://uitestingplayground.com/ajax
driver.get("http://uitestingplayground.com/ajax")

# нажимаем на синюю кнопку
driver.find_element(By.CSS_SELECTOR, "#ajaxButton").click()

# собираем элемент из зеленой плашки
content = driver.find_element(By.CSS_SELECTOR, "#content")
green_element = content.find_element(By.CSS_SELECTOR, "p.bg-success")

# текст из зеленой плашки
# выводим текст в консоль ("Data loaded with AJAX get request.")
print(green_element.text)

driver.quit()
