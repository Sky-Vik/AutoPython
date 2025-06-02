import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.description("Добавление заказов в корзину")
@allure.feature("Страница товаров")
class ShopMain:
    """
    Класс для работы на главной странице сайта:
    - выбор товара,
    - добавление товара в корзину.
    """

    def __init__(self, driver):
        """
        Конструктор класса 'ShopMain'.

        :param driver: WebDriver - объект драйвера Selenium.
        """
        self._driver = driver

    @allure.step("Добавление товара с id = '{id_product}' в корзину.")
    def add_product(self, id_product: str):
        """
        Находит товар с указанным id и добавляет его в корзину.

        :param id_product: str - id товара для добавления в корзину.
        """
        # находим товар и проверяем кликабельность кнопки для добавления товара
        product_in_cart = self._driver.find_element(By.ID, id_product)
        WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable(product_in_cart))

        # добавляем товары в корзину
        product_in_cart.click()

    @allure.step("Переход в корзину по URL='{cart_link}'.")
    def go_to_cart(self, cart_link: str):
        """
        Переход в корзину по указаннойму URL.

        :param cart_link: str - URL для перехода в корзину.
        """
        self._driver.get(cart_link)
