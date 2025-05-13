from selenium import webdriver

# Импотируем классы из папки pages:
from pages.page_object import PageObject


def test_calc():
    # Задаем браузер
    browser = webdriver.Chrome()
    waiter = 45
    # Создаем экземпляр класса PageObject
    page_object = PageObject(browser)
    # Устанавливаем время ожидания
    page_object.set_delay(waiter)
    # задаем параметры для расчета
    to_be = "15"
    list_buttons = ["7", "+", "8", "="]
    page_object.calculate(list_buttons, waiter)
    # смотрим результат
    as_is = page_object.rezult_calc(to_be, waiter)
    # Проверка результата ожидаемому
    assert as_is == float(to_be), (
        f"Результат должен быть равен {float(to_be)}, а равен {as_is}")

    browser.quit()
