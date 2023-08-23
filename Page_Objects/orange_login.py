import time
from Demo_Page.Page_Objects.locators import AdminLocators
from Demo_Page.Utilities.test_base import TestBase


class LoginPage(TestBase):
    def __init__(self, driver):
        super().__init__(driver)    # used to call the __init__ method of the parent class TestBase
        self.driver = driver

    def open(self, url):
        self.driver.get(url)
        self.wait_for_element(AdminLocators.USERNAME_INPUT)

    def set_username(self, username):
        self.driver.find_element(*AdminLocators.USERNAME_INPUT).send_keys(username)

    def set_password(self, password):
        self.driver.find_element(*AdminLocators.PASSWORD_INPUT).send_keys(password)

    def click_login(self):
        self.driver.find_element(*AdminLocators.LOGIN_BUTTON).click()

    def assert_dashboard_title(self):
        assert self.driver.find_element(*AdminLocators.ASSERT_VALUE).text == "Dashboard", "Dashboard title not found"

    def wait_for_main_page(self):
        self.wait_for_element(AdminLocators.MAIN_PAGE)

    def click_logout(self):
        self.driver.find_element(*AdminLocators.LOGOUT_DROPDOWN).click()
        time.sleep(1)
        self.driver.find_element(*AdminLocators.LOGOUT_BUTTON).click()
