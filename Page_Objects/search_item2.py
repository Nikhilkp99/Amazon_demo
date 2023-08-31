from Demo_Page.Page_Objects.locators2 import AmazonLocators2
from Demo_Page.Utilities.test_base import TestBase


class SearchItem2(TestBase):
    def __init__(self, driver):
        super().__init__(driver)    # used to call the __init__ method of the parent class TestBase
        self.driver = driver

    def open(self, url):
        self.driver.get(url)
        self.wait_for_element(AmazonLocators2.SEARCH_BAR)

    def wait_for_main_page(self):
        self.wait_for_element(AmazonLocators2.SEARCH_BAR)

    def set_search_item(self, item):
        self.driver.find_element(*AmazonLocators2.SEARCH_BAR).send_keys(item)
        self.driver.find_element(*AmazonLocators2.SEARCH_BUTTON).click()

    def price_of_search_item(self):
        price_in_search = self.driver.find_element(*AmazonLocators2.PRICE_OF_SEARCH_ITEM).text
        return price_in_search

    def select_item(self):
        self.driver.find_element(*AmazonLocators2.SELECT_ITEM).click()

    def price_of_selected_item(self):
        price_in_selected = self.driver.find_element(*AmazonLocators2.PRICE_OF_SELECTED_ITEM).text
        return price_in_selected

    def add_to_cart(self):
        self.driver.find_element(*AmazonLocators2.ADD_CART).click()

    def cart_btn(self):
        self.driver.find_element(*AmazonLocators2.VIEW_CART_BUTTON).click()

    def price_of_cart_item(self):
        price_in_cart = self.driver.find_element(*AmazonLocators2.PRICE_OF_CART_ITEM).text
        return price_in_cart
