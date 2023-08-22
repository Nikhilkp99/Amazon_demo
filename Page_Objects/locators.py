
from selenium.webdriver.common.by import By


class AdminLocators:
    USERNAME_INPUT = (By.XPATH, "//input[@placeholder='Username']")
    PASSWORD_INPUT = (By.XPATH, "//input[@placeholder='Password']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    MAIN_PAGE = (By.XPATH, "//div[@class='orangehrm-login-slot']")
    ASSERT_VALUE = (By.XPATH, "//h6[text()='Dashboard']")
    LOGOUT_DROPDOWN = (By.XPATH, "//*[@class='oxd-icon bi-caret-down-fill oxd-userdropdown-icon']")
    LOGOUT_BUTTON = (By.XPATH, "//a[normalize-space()='Logout']")


class UserLocators:
    ADMIN_MENU = (By.XPATH, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a")
    USERADD_BUTTON = (By.XPATH, "//button[normalize-space()='Add']")
    USER_ROLE = (By.XPATH, "(//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow'])[1]")
    ESS_ELEMENT = (By.XPATH, "(//div[@role='listbox']//child::div)[3]")
    STATUS = (By.XPATH, "(//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow'])[2]")
    ENABLED_ELEMENT = (By.XPATH, "(//div[@role='listbox']//child::div)[2]")
    EMPLOYEE_XPATH = (By.XPATH, "//input[@placeholder='Type for hints...']")
    USER_NAME = (By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[2]")
    PASSWORD_FILL = (By.XPATH, "(//input[@type='password'])[1]")
    CONFIRM_PASSWORD = (By.XPATH, "(//input[@type='password'])[2]")
    SAVE_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")







