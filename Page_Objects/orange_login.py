from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.XPATH, "//input[@placeholder='Username']")
        self.password_input = (By.XPATH, "//input[@placeholder='Password']")
        self.login_button = (By.CSS_SELECTOR, "button[type='submit']")
        self.main_page = (By.XPATH, "//div[@class='orangehrm-login-slot']")

    def open(self, url):
        self.driver.get(url)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.username_input))

    def set_username(self, username):
        self.driver.find_element(*self.username_input).send_keys(username)

    def set_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()

    def wait_for_main_page(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.visibility_of_element_located(self.main_page))
