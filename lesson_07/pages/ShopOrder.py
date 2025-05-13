from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ShopOrder:

    def __init__(self, driver):
        self._driver = driver

    def fill_data(self, id_element, text_element):
        # заполнение формы данными (имя, фамилия, почтовый индекс)
        WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.ID, id_element)))
        self._driver.find_element(By.ID, id_element).send_keys(text_element)

    def click_continue(self, id):
        WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.ID, id)))
        self._driver.find_element(By.ID, id).click()

    def total_cost(self):   # получение значения итоговой стоимости
        total_cost = self._driver.find_element(
            By.CLASS_NAME, "summary_total_label").text
        total_cost_value = float(total_cost.split("$")[1])
        print(f"Итоговая сумма {total_cost_value}")
        return total_cost_value
