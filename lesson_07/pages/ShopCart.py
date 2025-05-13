from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ShopCart:
    def __init__(self, driver):
        self._driver = driver

    def click_Checkout(self, id):
        # нажатие кнопки Checkout
        WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.ID, id)))
        self._driver.find_element(By.ID, id).click()

    def product_availability(self):
        # содержимое корзины
        WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "cart_list")))
        list_availability = self._driver.find_elements(
            By.CLASS_NAME, "inventory_item_name")

        list_availability_text = [list_availability[i].text for i in range(
            0, len(list_availability))]
        print(list_availability_text)

        return list_availability_text
