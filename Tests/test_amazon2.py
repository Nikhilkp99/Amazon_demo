import pytest
import time
import os
import math
from Demo_Page.Page_Objects.search_item2 import SearchItem2
from Demo_Page.Constants.constant import Constant2
from Demo_Page.Page_Objects.locators2 import AmazonLocators2
from Demo_Page.Utilities.test_base import TestBase


@pytest.fixture(scope="module")
def test_base(driver):
    return TestBase(driver)


@pytest.mark.usefixtures("test_base")
def test_search_2(driver, test_base):
    search_item = SearchItem2(driver)

    logger = test_base.get_logger("test_amazon2")
    logger.info("Starting the test_search_2 function")
    screenshot_counter = 1

    search_item.open(Constant2.BASE_URL)

    logger.info("Capturing screenshot: After opening website")
    test_base.capture_screenshot(f"website_opened_{screenshot_counter}", "test_search2")
    screenshot_counter += 1

    test_base.wait_for_element(AmazonLocators2.SEARCH_BAR)
    logger.info("Searched item: %s", Constant2.SEARCH_ITEM)
    search_item.set_search_item(Constant2.SEARCH_ITEM)
    test_base.wait_for_element(AmazonLocators2.SELECT_ITEM)

    price_in_search = (search_item.price_of_search_item())
    logger.info("Price in the search item: %s", price_in_search)
    print(price_in_search)

    search_item.select_item()

    windows_opened = driver.window_handles
    driver.switch_to.window(windows_opened[1])

    price_in_selected_item = search_item.price_of_selected_item()
    logger.info("Price in the selected item: %s", price_in_selected_item)
    print(price_in_selected_item)

    assert price_in_search == price_in_selected_item

    logger.info("Capturing screenshot: After selecting an item")
    test_base.capture_screenshot(f"item_selected_{screenshot_counter}", "test_search2")
    screenshot_counter += 1

    search_item.add_to_cart()

    test_base.wait_for_element_interactable(AmazonLocators2.VIEW_CART_BUTTON)
    search_item.cart_btn()

    price_in_cart_item = search_item.price_of_cart_item()

    price = (price_in_cart_item[:-3])
    price_in_cart = price.strip()
    logger.info("Price in the cart: %s", price_in_cart)

    assert price_in_selected_item == price_in_cart

    logger.info("Capturing screenshot: After adding item to cart")
    test_base.capture_screenshot(f"item_added_to_cart_{screenshot_counter}", "test_search2")
    screenshot_counter += 1
    time.sleep(2)
    logger.info("Finishing the test_search_2 function")

    if __name__ == "__main__":
        # report_dir = os.path.join(os.getcwd(), "..", "Reports")
        # test_report_path = os.path.join(report_dir, "test_report.html")
        test_report_path = os.path.join(os.getcwd(), "..", "Reports", "test_report.html")

        # Delete existing HTML report if it exists
        if os.path.exists(test_report_path):
            os.remove(test_report_path)
        pytest.main(["-v", f"--html={test_report_path}"])

