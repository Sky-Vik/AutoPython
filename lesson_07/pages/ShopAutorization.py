from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC


class ShopAutorization:

    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://www.saucedemo.com/")
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

    def set_login_pass(self, login, passw):
        # ввод логина и пароля
        username = self._driver.find_element(By.ID, "user-name")
        password = self._driver.find_element(By.ID, "password")
        username.clear()
        password.clear()
        username.send_keys(login)
        password.send_keys(passw)

    def login_button_click(self):
        # нажатие кнопки входа
        self._driver.find_element(By.ID, "login-button").click()
