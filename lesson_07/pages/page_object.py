from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PageObject:

    def __init__(self, driver):
        self._driver = driver
        self._driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/"
            "slow-calculator.html")
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

    def set_delay(self, wait):        # установка времени ожидания

        # проверка поля на доступность к вводу
        WebDriverWait(self._driver, wait).until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "#delay")))

        # установка значения ожидания
        delay = "delay"
        self._driver.find_element(By.ID, delay).clear()
        self._driver.find_element(By.ID, delay).send_keys(wait)

    def calculate(self, list_calc, wait):
        # Нажимаем кнопки из списка
        for button in list_calc:
            str = "//span[text()='" + button + "']"
            button_click = self._driver.find_element(By.XPATH, str)
            WebDriverWait(self._driver, wait).until(EC.element_to_be_clickable(
                button_click))
            button_click.click()

    def rezult_calc(self, rez, wait):
        # получаем результат
        WebDriverWait(self._driver, wait).until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, '[class="screen"]'), rez))

        val = self._driver.find_element(
            By.CSS_SELECTOR, '[class="screen"]')
        rezult = float(val.text)
        return rezult
