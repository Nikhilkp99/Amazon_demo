
from selenium.webdriver.common.by import By


class AmazonLocators:
    SEARCH_BAR = (By.XPATH, "//*[@placeholder='Search Amazon.in']")
    SEARCH_BUTTON = (By.XPATH, "//*[@id='nav-search-submit-button']")
    SELECT_ITEM = (By.XPATH, "//span[@class='a-size-medium a-color-base a-text-normal']")
    ADD_CART = (By.XPATH, "//*[@id='add-to-cart-button']")
    ITEM_TEXT = (By.XPATH, "//*[@id='productTitle']")
    VIEW_CART_BUTTON = (By.XPATH, "//*[@id='attach-sidesheet-view-cart-button']")

    ITEM_TEXT_CART = (By.XPATH, "//*[@class='a-truncate-cut']")





