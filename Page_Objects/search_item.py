import time
from Demo_Page.Page_Objects.locators import AmazonLocators
from Demo_Page.Utilities.test_base import TestBase


class SearchItem(TestBase):
    def __init__(self, driver):
        super().__init__(driver)    # used to call the __init__ method of the parent class TestBase
        self.driver = driver

    def open(self, url):
        self.driver.get(url)
        self.wait_for_element(AmazonLocators.SEARCH_BAR)

    def wait_for_main_page(self):
        self.wait_for_element(AmazonLocators.SEARCH_BAR)

    def set_search_item(self, item):
        self.driver.find_element(*AmazonLocators.SEARCH_BAR).send_keys(item)
        self.driver.find_element(*AmazonLocators.SEARCH_BUTTON).click()

    def select_item(self):
        self.driver.find_element(*AmazonLocators.SELECT_ITEM).click()

    def item_text(self):
        text_item = self.driver.find_element(*AmazonLocators.ITEM_TEXT).text
        return text_item

    def add_to_cart(self):
        self.driver.find_element(*AmazonLocators.ADD_CART).click()

    def cart_btn(self):
        self.driver.find_element(*AmazonLocators.VIEW_CART_BUTTON).click()

    def item_text_cart(self):
        text_cart = self.driver.find_element(*AmazonLocators.ITEM_TEXT_CART).text
        return text_cart


