import allure
from selenium.webdriver.common.by import By


class ShopAutorization:

    def __init__(self, driver):
        """
        Конструктор класса 'ShopAutorization'.

        :param driver: WebDriver - объект драйвера Selenium.
        """
        self._driver = driver
        self._driver.get("https://www.saucedemo.com/")

    @allure.description("Авторизация пользователя на сайте \
                https://www.saucedemo.com/")
    @allure.feature("Авторизация")
    @allure.step("Ввод логина '{login}' и пароля '{passw}'.")
    def set_login_pass(self, login: str, passw: str):
        """
        Осуществляет ввод логина и пароля в соответствующие поля формы
        для авторизации пользователя.

        :param login: str - логин пользователя,
        :param passw: str - пароль пользователя.
        """
        username = self._driver.find_element(By.ID, "user-name")
        password = self._driver.find_element(By.ID, "password")
        username.clear()
        password.clear()
        username.send_keys(login)
        password.send_keys(passw)

    @allure.step("Нажатие кнопки входа для авторизации.")
    def login_button_click(self):
        """
        Нажимает кнопку для залогинивания на сайте.
        """
        self._driver.find_element(By.ID, "login-button").click()
