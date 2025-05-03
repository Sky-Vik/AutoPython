import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.lesson6k
def test_calc():
    driver = webdriver.Chrome()
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    # проверка поля на доступность к вводу

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "#delay")))

    # установка значения ожидания
    delay = "delay"
    wait = "45"
    driver.find_element(By.ID, delay).clear()
    driver.find_element(By.ID, delay).send_keys(wait)

    for button in (["7", "+", "8", "="]):
        str = "//span[text()='" + button + "']"
        button_click = driver.find_element(By.XPATH, str)
        WebDriverWait(driver, wait).until(EC.element_to_be_clickable(
            button_click))
        button_click.click()
        print(str)

    element = driver.find_element(By.CSS_SELECTOR, '[class="screen"]')
    print(element.text)

    WebDriverWait(driver, wait).until(
        EC.text_to_be_present_in_element(
          (By.CSS_SELECTOR, '[class="screen"]'), "15"))

    element = driver.find_element(By.CSS_SELECTOR, '[class="screen"]')
    print(element.text)

    driver.quit()
