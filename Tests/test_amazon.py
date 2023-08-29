import pytest
import time
import os
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

    screenshot_counter = 1

    search_item = SearchItem(driver)

    logger.info("Opening URL: %s", Constant.BASE_URL)
    search_item.open(Constant.BASE_URL)

    logger.info("Capturing screenshot: After opening website")
    test_base.capture_screenshot(f"website_opened_{screenshot_counter}")
    screenshot_counter += 1

    test_base.wait_for_element(AmazonLocators.SEARCH_BAR)
    logger.info("Searched item: %s", Constant.SEARCH_ITEM)
    search_item.set_search_item(Constant.SEARCH_ITEM)
    test_base.wait_for_element(AmazonLocators.SELECT_ITEM)
    search_item.select_item()

    windows_opened = driver.window_handles
    driver.switch_to.window(windows_opened[1])

    text_in_item = (search_item.item_text())
    logger.info("Text in the item: %s", text_in_item)

    logger.info("Capturing screenshot: After selecting an item")
    test_base.capture_screenshot(f"item_selected_{screenshot_counter}")
    screenshot_counter += 1

    search_item.add_to_cart()

    test_base.wait_for_element_interactable(AmazonLocators.VIEW_CART_BUTTON)
    search_item.cart_btn()

    text_in_cart = (search_item.item_text_cart())
    logger.info("Text in the cart: %s", text_in_cart)

    assert text_in_item == text_in_cart

    logger.info("Capturing screenshot: After adding item to cart")
    test_base.capture_screenshot(f"item_added_to_cart_{screenshot_counter}")
    screenshot_counter += 1

    time.sleep(5)
    logger.info("Finishing the test_search function")

    if __name__ == "__main__":
        report_dir = os.path.join(os.getcwd(), "..", "Reports")
        test_report_path = os.path.join(report_dir, "test_report.html")
        pytest.main(["-v", f"--html={test_report_path}"])


