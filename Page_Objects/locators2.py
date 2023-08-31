from selenium.webdriver.common.by import By


class AmazonLocators2:
    SEARCH_BAR = (By.XPATH, "//*[@placeholder='Search Amazon.in']")
    SEARCH_BUTTON = (By.XPATH, "//*[@id='nav-search-submit-button']")
    SELECT_ITEM = (By.XPATH, "//span[@class='a-size-medium a-color-base a-text-normal']")
    PRICE_OF_SEARCH_ITEM = (By.XPATH, "(//span[@class='a-price-whole'])[1]")
    PRICE_OF_SELECTED_ITEM = (By.XPATH, "(//span[normalize-space()='1,07,990'])[1]")
    ADD_CART = (By.XPATH, "//*[@id='add-to-cart-button']")

    VIEW_CART_BUTTON = (By.XPATH, "//*[@id='attach-sidesheet-view-cart-button']")

    PRICE_OF_CART_ITEM = (By.XPATH, "(//span[@class='a-size-medium a-color-base sc-price sc-white-space-nowrap sc-product-price a-text-bold'])[1]")

