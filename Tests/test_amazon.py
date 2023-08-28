import pytest
import time
from Demo_Page.Page_Objects.search_item import SearchItem
from Demo_Page.Constants.constant import Constant
from Demo_Page.Page_Objects.locators import AmazonLocators
from Demo_Page.Utilities.test_base import TestBase


@pytest.fixture(scope="module")
def test_base(driver):
    return TestBase(driver)


@pytest.mark.usefixtures("test_base")
def test_search(driver, test_base):
    logger = test_base.get_logger()
    logger.info("Starting the test_search function")

    search_item = SearchItem(driver)
    logger.info("Opening URL: %s", Constant.BASE_URL)
    search_item.open(Constant.BASE_URL)

    test_base.wait_for_element(AmazonLocators.SEARCH_BAR)
    logger.info("Searched item: %s", Constant.SEARCH_ITEM)
    search_item.set_search_item(Constant.SEARCH_ITEM)
    test_base.wait_for_element(AmazonLocators.SELECT_ITEM)
    search_item.select_item()
    windows_opened = driver.window_handles
    driver.switch_to.window(windows_opened[1])

    text_in_item = (search_item.item_text())
    logger.info("Text in the item: %s", text_in_item)
    search_item.add_to_cart()

    test_base.wait_for_element_interactable(AmazonLocators.VIEW_CART_BUTTON)
    search_item.cart_btn()

    text_in_cart = (search_item.item_text_cart())
    logger.info("Text in the cart: %s", text_in_cart)

    assert text_in_item == text_in_cart
    time.sleep(5)
    logger.info("Finishing the test_search function")

    if __name__ == "__main__":
        pytest.main(["-v", "--html=reports/test_report.html"])

