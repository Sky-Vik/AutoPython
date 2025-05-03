import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.lesson6k
def test_fill_form():
    driver = webdriver.Chrome()
    # Открытие страницы
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    # Ожидание появления кнопки Submit
    WebDriverWait(driver, 30).until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, "form")))

    fields = (["first-name", "last-name", "address", "city", "country",
               "e-mail", "phone", "job-position", "company"])

    # Заполнение формы
    driver.find_element(By.NAME, fields[0]).send_keys("Иван")
    driver.find_element(By.NAME, fields[1]).send_keys("Петров")
    driver.find_element(By.NAME, fields[2]).send_keys("Ленина, 55-3")
    driver.find_element(By.NAME, fields[3]).send_keys("Москва")
    driver.find_element(By.NAME, fields[4]).send_keys("Россия")
    driver.find_element(By.NAME, fields[5]).send_keys("test@skypro.com")
    driver.find_element(By.NAME, fields[6]).send_keys("+7985899998787")
    driver.find_element(By.NAME, fields[7]).send_keys("QA")
    driver.find_element(By.NAME, fields[8]).send_keys("SkyPro")

    # Нажатие кнопки "Submit"
    submit = "button[type='submit']"
    driver.find_element(By.CSS_SELECTOR, submit).click()

    # Ждем загрузки последнего элемента формы
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, "#company")))

    waiter = WebDriverWait(driver, 20)

    # Проверка подсветки поля Zip code
    zip_code = waiter.until(
        EC.visibility_of_element_located((By.ID, "zip-code")))
    zip_code = driver.find_element(By.ID, "zip-code")
    background_color = zip_code.value_of_css_property(
        "background-color")
    assert [background_color == "rgb(248 215 218 1)",
            "Поле 'Zip code' не подсвечено красным"]

    # Проверка подсветки остальных полей
    for field_id in fields:
        field_element = waiter.until(
            EC.visibility_of_element_located((By.ID, field_id)))
        background_color = field_element.value_of_css_property(
            "background-color")
        print(f"{field_id} - {background_color}")
        assert [background_color == "rgb(209 231 221 1)",
                f"Поле {field_id} не подсвечено зеленым"]

    driver.quit()
