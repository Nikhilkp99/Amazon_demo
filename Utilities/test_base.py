from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


class TestBase:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def wait_for_element(self, locator, timeout=20):
        wait = WebDriverWait(self.driver, timeout)
        wait.until(EC.presence_of_element_located(locator))

    # def select_option(self, *locator, option):
    #     select = Select(self.driver.find_element(*locator))
    #     select.select_by_visible_text(option)
