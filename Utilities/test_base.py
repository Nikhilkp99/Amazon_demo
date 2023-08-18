from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestBase:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, locator, timeout=20):
        wait = WebDriverWait(self.driver, timeout)
        wait.until(EC.presence_of_element_located(locator))
