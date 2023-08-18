import pytest
from selenium import webdriver
from Demo_Page.Page_Objects.orange_login import LoginPage
import chromedriver_autoinstaller
from Demo_Page.Constants.constant import Constant
from Demo_Page.Utilities.test_base import TestBase
from Demo_Page.Page_Objects.locators import Locators


@pytest.fixture(scope="module")
def driver():
    try:
        chromedriver_autoinstaller.install()
        driver = webdriver.Chrome()
        driver.maximize_window()
        yield driver
    except Exception as e:
        print("An error occurred during driver setup:", e)
    finally:
        driver.quit()


def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.open(Constant.BASE_URL)

    test_base = TestBase(driver)
    test_base.wait_for_element(Locators.MAIN_PAGE)

    login_page.set_username(Constant.USERNAME)
    login_page.set_password(Constant.PASSWORD)
    login_page.click_login()



