import pytest
import time
from Demo_Page.Page_Objects.search_item import SearchItem
from Demo_Page.Constants.constant import Constant
from Demo_Page.Page_Objects.locators import AmazonLocators


@pytest.fixture(scope="module")
def test_base(driver):
    from Demo_Page.Utilities.test_base import TestBase
    return TestBase(driver)


def test_search(driver, test_base):
    search_item = SearchItem(driver)
    search_item.open(Constant.BASE_URL)

    test_base.wait_for_element(AmazonLocators.SEARCH_BAR)
    search_item.set_search_item(Constant.SEARCH_ITEM)
    test_base.wait_for_element(AmazonLocators.SELECT_ITEM)
    search_item.select_item()
    windows_opened = driver.window_handles
    driver.switch_to.window(windows_opened[1])

    text_in_item = (search_item.item_text())
    search_item.add_to_cart()

    test_base.wait_for_element_interactable(AmazonLocators.VIEW_CART_BUTTON)
    search_item.cart_btn()

    text_in_cart = (search_item.item_text_cart())
    assert text_in_item == text_in_cart
    time.sleep(5)
