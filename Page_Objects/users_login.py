import time
from Demo_Page.Page_Objects.locators import UserLocators
from Demo_Page.Utilities.test_base import TestBase
from Demo_Page.Page_Objects.locators import UserLocators
from selenium.webdriver.support.select import Select
from Demo_Page.Constants.constant import UserDATA


class UserLogin(TestBase):

    # def __init__(self, driver):
    #     super().__init__(driver)
    #     self.driver = driver
    def __init__(self, driver):
        super().__init__(driver)

    def access_system_users_menu(self):
        self.driver.find_element(*UserLocators.ADMIN_MENU).click()

    def user_add_btn(self):
        self.driver.find_element(*UserLocators.USERADD_BUTTON).click()

    def user_role(self):
        self.driver.find_element(*UserLocators.USER_ROLE).click()
        self.driver.find_element(*UserLocators.ESS_ELEMENT).click()

    def user_status(self):
        self.driver.find_element(*UserLocators.STATUS).click()
        self.driver.find_element(*UserLocators.ENABLED_ELEMENT).click()

    def add_employee(self, employee):
        self.driver.find_element(*UserLocators.EMPLOYEE_XPATH).send_keys(employee)

    def add_username(self, user_name):
        self.driver.find_element(*UserLocators.USER_NAME).send_keys(user_name)

    def add_password(self, paswrd):
        self.driver.find_element(*UserLocators.PASSWORD_FILL).send_keys(paswrd)

    def confirm_password(self, confirmpaswrd):
        self.driver.find_element(*UserLocators.CONFIRM_PASSWORD).send_keys(confirmpaswrd)

    def save_btn(self):
        self.driver.find_element(*UserLocators.SAVE_BUTTON).click()







