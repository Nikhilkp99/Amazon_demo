from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Demo_Page.Page_Objects.locators import Locators
from Demo_Page.Utilities.test_base import TestBase


class LoginPage(TestBase):
    def __init__(self, driver):
        super().__init__(driver)    # used to call the __init__ method of the parent class TestBase
        self.driver = driver

    def open(self, url):
        self.driver.get(url)
        self.wait_for_element(Locators.USERNAME_INPUT)

    def set_username(self, username):
        self.driver.find_element(*Locators.USERNAME_INPUT).send_keys(username)

    def set_password(self, password):
        self.driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)

    def click_login(self):
        self.driver.find_element(*Locators.LOGIN_BUTTON).click()

    def wait_for_main_page(self):
        self.wait_for_element(Locators.MAIN_PAGE)
