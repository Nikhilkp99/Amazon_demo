import pytest
from selenium import webdriver
from Demo_Page.Page_Objects.orange_login import LoginPage
import chromedriver_autoinstaller


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
    login_page.open("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    login_page.wait_for_main_page()
    login_page.set_username("Admin")
    login_page.set_password("admin123")
    login_page.click_login()



