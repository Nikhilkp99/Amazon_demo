
from selenium.webdriver.common.by import By


class AdminLocators:
    USERNAME_INPUT = (By.XPATH, "//input[@placeholder='Username']")
    PASSWORD_INPUT = (By.XPATH, "//input[@placeholder='Password']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    MAIN_PAGE = (By.XPATH, "//div[@class='orangehrm-login-slot']")
    ASSERT_VALUE = (By.XPATH, "//h6[text()='Dashboard']")
    LOGOUT_DROPDOWN = (By.XPATH, "//*[@class='oxd-icon bi-caret-down-fill oxd-userdropdown-icon']")
    LOGOUT_BUTTON = (By.XPATH, "//a[normalize-space()='Logout']")


class UserLocator:
    PIM_MENU = (By.XPATH, "//*[@href='/web/index.php/pim/viewPimModule']")
