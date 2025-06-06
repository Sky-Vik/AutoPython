import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ShopCart:
    """
    Класс для работы с корзиной выбранных товаров:
    - проверка содержимого (правильно ли отобраны товары)
    """
    @allure.description("Проверка содержимого корзины \
                        на наличие нужных товаров")
    @allure.feature("Работа с корзиной")
    def __init__(self, driver):
        """
        Конструктор класса 'ShopCart'.

        :param driver: WebDriver — объект драйвера Selenium.
        """
        self._driver = driver

    @allure.step("Нажатие кнопки '{id}'.")
    def click_Checkout(self, id: str) -> None:
        """
        Формирует список товаров в корзине и
        переходит на страницу с оформлением заказа с помощью кнопки 'Checkout'.
        Нажимает кнопку 'Checkout' после проверки ее кликабельности.

        :param id: str - id кнопки 'Checkout'.
        """
        WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.ID, id)))
        self._driver.find_element(By.ID, id).click()

    @allure.step("Получение списка товаров из корзины.")
    def product_availability(self) -> list:
        """
        Возвращает содержимое корзины в виде списка.

        :return: list[str] - возвращает список товаров в корзине.
        """
        WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "cart_list")))
        list_availability = self._driver.find_elements(
            By.CLASS_NAME, "inventory_item_name")

        list_availability_text = [list_availability[i].text for i in range(
            0, len(list_availability))]
        print(list_availability_text)

        return list_availability_text
