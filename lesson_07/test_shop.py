from selenium import webdriver
# Импотируем классы из папки pages:
from pages.ShopAutorization import ShopAutorization
from pages.ShopMain import ShopMain
from pages.ShopCart import ShopCart
from pages.ShopOrder import ShopOrder


def test_shop():
    # Задаем настройки браузера
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--incognito')

    browser = webdriver.Chrome(options=options)
    wait = 10  # время ожидания
    browser.implicitly_wait(wait)

    # 1. Создаем экземпляр класса PageObject - Авторизация
    page_auto = ShopAutorization(browser)
    # логинимся
    page_auto.set_login_pass("standard_user", "secret_sauce")
    page_auto.login_button_click()

    # 2. Создаем экземпляр класса PageObject - Главная страница
    page_main = ShopMain(browser)
    # Добавляем товары по ID
    list_id_product = ["add-to-cart-sauce-labs-backpack",
                       "add-to-cart-sauce-labs-bolt-t-shirt",
                       "add-to-cart-sauce-labs-onesie"
                       ]
    for prod in list_id_product:
        page_main.add_product(prod)

    # Переходим в корзину
    # вариант а) - по URL
    # page_main.go_to_cart("https://www.saucedemo.com/cart.html")
    # вариант б) - по атрибуту класса
    page_main.go_to_cart("shopping_cart_link")

    # 3. Работа с корзиной

    page_cart = ShopCart(browser)
    # проверка содержимого корзины
    list_product = ["Sauce Labs Backpack",
                    "Sauce Labs Bolt T-Shirt",
                    "Sauce Labs Onesie"
                    ]
    list_cart = page_cart.product_availability()
    for product in list_cart:
        txt = product
        print(product)
        assert txt in list_product, f"{txt} отсутствует в корзине"
    # Нажать Checkout
    page_cart.click_Checkout("checkout")

    # 4. Заполнить форму данными
    page_order = ShopOrder(browser)
    page_order.fill_data('first-name', 'Виктория')
    page_order.fill_data('last-name', 'Кекконен')
    page_order.fill_data('postal-code', '196000')
    # переходим на итог по заказу
    page_order.click_continue('continue')

    # Чтение итоговой стоимости
    to_be = 58.29
    as_is = page_order.total_cost()

    browser.quit()

    # 5. Проверка итоговой суммы
    assert as_is == 58.29, f"Итоговая сумма должна быть {to_be}"
