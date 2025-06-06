import allure
from selenium import webdriver
from pages.page_object import PageObject


@allure.title("Тестирование калькулятора (операция сложения)")
@allure.description("Тест проверяет корректность работы калькулятора\
                 c операцией сложения.")
@allure.feature("Калькулятор (сложение)")
@allure.severity(allure.severity_level.CRITICAL)
def test_calc():
    """
    Тест проверяет работу калькулятора с операцией сложения.
    """
    waiter = 5
    list_buttons = ["7", "+", "8", "="]
    to_be = "15"
    with allure.step("Подключение браузера."):
        browser = webdriver.Chrome()

    with allure.step("Создание экземпляра класса 'PageObject'."):
        page_object = PageObject(browser)

    with allure.step(f"Установка задержки ожидания {waiter} секунд."):
        page_object.set_delay(waiter)

    with allure.step(f"Нажатие на кнопки: {list_buttons}"):
        page_object.calculate(list_buttons, waiter)

    with allure.step("Получение результата с экрана калькулятора."):
        as_is = page_object.rezult_calc(to_be, waiter)

    with allure.step(f"Проверка результата {as_is} ожидаемому {float(to_be)}"):
        assert as_is == float(to_be), (
            f"Результат должен быть равен {float(to_be)}, а равен {as_is}")

    browser.quit()
