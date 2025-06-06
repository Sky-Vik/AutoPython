# import pytest
import allure
from selenium import webdriver
# Импотируем классы из папки pages:
from pages.ShopAutorization import ShopAutorization
from pages.ShopMain import ShopMain
from pages.ShopCart import ShopCart
from pages.ShopOrder import ShopOrder


@allure.title("Проверка функциональности интернет-магазина:\
              - Авторизация,\
              - Главная страница сайта,\
              - Корзина,\
              - Заказ.")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("Проверка работы сайта интернет-магазина.")
@allure.feature("Интернет-магазин")
def test_shop():
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--incognito')
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(3)
    driver.maximize_window()
    # "Создание экземпляра класса для авторизации"
    page_auto = ShopAutorization(driver)

    with allure.step("Ввод данных пользователя"):
        login = "standard_user"
        password = "secret_sauce"
        page_auto.set_login_pass(login, password)

    with allure.step("Отправка введенных данных - нажатие на 'Login'"):
        page_auto.login_button_click()

    # "Создание экземпляра класса Главная страница"
    page_main = ShopMain(driver)

    with allure.step("Добавляем товары по ID"):
        list_id_product = ["add-to-cart-sauce-labs-backpack",
                           "add-to-cart-sauce-labs-bolt-t-shirt",
                           "add-to-cart-sauce-labs-onesie"
                           ]
        for prod in list_id_product:
            page_main.add_product(prod)

    with allure.step("Переходим в корзину"):
        page_main.go_to_cart("https://www.saucedemo.com/cart.html")

    # "Создание экземпляра класса для работы с корзиной"
    page_cart = ShopCart(driver)

    with allure.step("Проверка содержимого корзины"):
        list_product = ["Sauce Labs Backpack",
                        "Sauce Labs Bolt T-Shirt",
                        "Sauce Labs Onesie"
                        ]
        list_cart = page_cart.product_availability()
        for product in list_cart:
            txt = product
            print(product)
            assert txt in list_product, f"{txt} отсутствует в корзине"

    with allure.step("Переход к оформлению заказа - нажатие 'Checkout'"):
        page_cart.click_Checkout("checkout")

    # "Создание экземпляра класса для работы с заказом"
    page_order = ShopOrder(driver)

    with allure.step("Ввод данных в форму заказа"):
        page_order.fill_data('first-name', 'Виктория')
        page_order.fill_data('last-name', 'Кекконен')
        page_order.fill_data('postal-code', '196000')

    with allure.step("Получение итоговой стоимости"):
        page_order.click_continue('continue')
        to_be = 58.29
        as_is = page_order.total_cost()

    with allure.step("Проверка итоговой стоимости товаров"):
        try:
            assert as_is == 58.29, f"Итоговая сумма должна быть {to_be}"
        finally:
            driver.close()
