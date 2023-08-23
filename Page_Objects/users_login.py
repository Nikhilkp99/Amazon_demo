import time
from Demo_Page.Utilities.test_base import TestBase
from Demo_Page.Page_Objects.locators import UserLocator
# from selenium.webdriver.support.select import Select
# from Demo_Page.Constants.constant import UserDATA


class UserLogin(TestBase):

    # def __init__(self, driver):
    #     super().__init__(driver)
    #     self.driver = driver
    def __init__(self, driver):
        super().__init__(driver)

    def access_system_users_menu(self):
        self.driver.find_element(*UserLocator.PIM_MENU).click()

