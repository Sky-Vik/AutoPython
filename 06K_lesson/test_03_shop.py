import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def wait_clickable(element, driver_, waiting):
    return WebDriverWait(driver_, waiting).until(
        EC.element_to_be_clickable(element))


@pytest.mark.lesson6k
def test_cart():
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--incognito')

    driver = webdriver.Chrome(options=options)

    # открываем сайт магазина
    driver.get("https://www.saucedemo.com/")
    wait = 10
    driver.implicitly_wait(wait)

    # авторизация
    username = driver.find_element(By.ID, "user-name")
    password = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")

    username.clear()
    password.clear()
    username.send_keys("standard_user")
    password.send_keys("secret_sauce")
    login_button.click()

    # находим товар и проверяем кликабельность кнопки для добавления в корзину
    backpack_in_cart = driver.find_element(
        By.ID, "add-to-cart-sauce-labs-backpack")
    wait_clickable(backpack_in_cart, driver, wait)

    tshirt_in_cart = driver.find_element(
        By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    wait_clickable(tshirt_in_cart, driver, wait)

    onesie_in_cart = driver.find_element(
        By.ID, "add-to-cart-sauce-labs-onesie")
    wait_clickable(onesie_in_cart, driver, wait)

    driver.implicitly_wait(20)
    # добавляем товары в корзину
    backpack_in_cart.click()
    tshirt_in_cart.click()
    onesie_in_cart.click()

    # Переходим в корзину
    cart_link = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    wait_clickable(cart_link, driver, wait)
    cart_link.click()

    # Нажать Checkout
    driver.find_element(By.ID, "checkout").click()

    # Заполнить форму данными
    driver.find_element(By.ID, 'first-name').send_keys('Виктория')
    driver.find_element(By.ID, 'last-name').send_keys('Кекконен')
    driver.find_element(By.ID, 'postal-code').send_keys("196000")
    driver.find_element(By.ID, 'continue').click()

    # Чтение итоговой стоимости
    total_cost = driver.find_element(By.CLASS_NAME, "summary_total_label").text
    total_cost_value = float(total_cost.split("$")[1])
    print(f"Итоговая сумма {total_cost_value}")
    
    driver.quit()

    # Проверка итоговой суммы
    assert total_cost_value == 58.29, "Итоговая сумма должна быть 58.29"
