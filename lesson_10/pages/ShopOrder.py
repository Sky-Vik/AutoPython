import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ShopOrder:
    """
    Класс для работы с заказом:
    - заполнение формы,
    - получение рассчитанной стоимости заказа.
    """

    @allure.description("Заполнение формы заказа \
                        и получение итоговой стоимости")
    @allure.feature("Оформление заказа")
    def __init__(self, driver):
        """
        Конструктор класса 'ShopOrder'.

        :param driver: WebDriver - объект драйвера Selenium.
        """
        self._driver = driver

    @allure.step(
            "Заполнение формы заказа данными: {id_element} - {text_element}.")
    def fill_data(self, id_element: str, text_element: str):
        """
        Осуществляет поэлементное заполнение формы данными:
        - имя,
        - фамилия,
        - почтовый индекс.
        Заполняет после проверки на готовность поля ко вводу данных.

        :param id_element: str - id элемента формы заказа,
        :param text_element: str - данные для заполнения элемента формы.
        """
        WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.ID, id_element)))
        self._driver.find_element(By.ID, id_element).send_keys(text_element)

    @allure.step("Нажатие кнопки '{id}' для продолжения оформления заказа.")
    def click_continue(self, id: str):
        """
        Нажимает кнопку 'Continue' для продолжения оформления заказа
        после проверки ее на кликабельность.

        :param id: str - id кнопки 'Continue'
        """
        WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.ID, id)))
        self._driver.find_element(By.ID, id).click()

    @allure.step("Получение значения итоговой стоимости заказа.")
    def total_cost(self) -> float:
        """
        Получает итоговую стоимость заказа, рассчитанную на сайте.

        :return: float - сумма заказа.
        """
        total_cost = self._driver.find_element(
            By.CLASS_NAME, "summary_total_label").text
        total_cost_value = float(total_cost.split("$")[1])
        print(f"Итоговая сумма {total_cost_value}")
        return total_cost_value
