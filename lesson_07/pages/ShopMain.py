from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ShopMain:
    def __init__(self, driver):
        self._driver = driver

    def add_product(self, id_product):   # добавление товаров в корзину
        # находим товар и проверяем кликабельность кнопки для добавления товара
        product_in_cart = self._driver.find_element(By.ID, id_product)
        WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable(product_in_cart))

        # self._driver.implicitly_wait(20)
        # добавляем товары в корзину
        product_in_cart.click()

    def go_to_cart(self, cart_link):
        if cart_link.startswith("https://"):
            self._driver.get(cart_link)
        else:
            cart_link = self._driver.find_element(By.CLASS_NAME, cart_link)
            WebDriverWait(self._driver, 10).until(
                EC.element_to_be_clickable(cart_link))
            cart_link.click()
