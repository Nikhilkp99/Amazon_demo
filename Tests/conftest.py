# conftest.py
import pytest
import chromedriver_autoinstaller
from selenium import webdriver


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
