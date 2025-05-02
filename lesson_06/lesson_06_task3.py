from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# запускаем драйвер
driver = webdriver.Chrome()

# # устанавливаем ожидание
# waiter = WebDriverWait(driver, 40, 0.01)

# переходим на сайт
driver.get(
    "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html"
    )
waiter = WebDriverWait(driver, 40)

# ждем загрузку img = landscape
element_present = EC.visibility_of_element_located(
    (By.CSS_SELECTOR, "#landscape"))
waiter.until(element_present)

# получаем значение атрибута "src" у 3-й картинки
container = driver.find_element(By.CSS_SELECTOR, "#image-container")
pictures = container.find_elements(By.CSS_SELECTOR, "img")
print(f"Загружено картинок: {len(pictures)}\n")

src_3 = pictures[2].get_attribute("src")

# выводим значение в консоль
print(src_3)

driver.quit()
