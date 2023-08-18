
from selenium.webdriver.common.by import By


class Locators:
    USERNAME_INPUT = (By.XPATH, "//input[@placeholder='Username']")
    PASSWORD_INPUT = (By.XPATH, "//input[@placeholder='Password']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    MAIN_PAGE = (By.XPATH, "//div[@class='orangehrm-login-slot']")
