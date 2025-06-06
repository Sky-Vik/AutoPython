import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PageObject:

    def __init__(self, driver):
        """
        Конструктор класса 'PageObject'.

        :param driver: WebDriver - объект драйвера Selenium.
        """
        self._driver = driver
        self._driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/"
            "slow-calculator.html")
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

    @allure.step("Установка задержки ожидания {wait} секунд")
    def set_delay(self, wait: int) -> None:
        """
        Метод устанавливает задержку для выполнения операций на калькуляторе,
        предварительно проверяя доступность поля на ввод.

        :param wait: int - время задержки операции (в секундах).
        """
        # проверка поля на доступность к вводу
        WebDriverWait(self._driver, wait).until(EC.element_to_be_clickable(
            (By.ID, "delay")))

        # установка значения ожидания
        delay_input = self._driver.find_element(By.ID, "delay")
        delay_input.clear()
        delay_input.send_keys(wait)

    @allure.step("Нажатие на кнопки: {list_calc}")
    def calculate(self, list_calc: list, wait: int) -> None:
        """
        Метод имитирует нажатие на кнопоки калькулятора.
        Порядок нажатия на кнопки определяется в списке {list_calc},
        переданном в метод как параметр.

        :param list_calc: list[str] - список текстов на кнопках,
                            которые надо нажать на калькуляторе.
        :param wait: int - время задержки операции (в секундах).
        """
        for button in list_calc:
            str = "//span[text()='" + button + "']"
            button_click = self._driver.find_element(By.XPATH, str)
            WebDriverWait(self._driver, wait).until(EC.element_to_be_clickable(
                button_click))
            button_click.click()

    @allure.step("Получение результата '{result}' с экрана калькулятора")
    def rezult_calc(self, result: str, wait: int) -> float:
        """
        Метод ожидает появления результата на экране калькулятора
        и возвращает полученный результат.

        :param result: str - ожидаемый результат.
        :param wait: int - время задержки в секундах.
        :return: float - возвращает результат расчета с экрана калькулятора.
        """
        WebDriverWait(self._driver, wait).until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, '[class="screen"]'), result))

        value = self._driver.find_element(
            By.CSS_SELECTOR, '[class="screen"]')
        rezult = float(value.text)
        return rezult
