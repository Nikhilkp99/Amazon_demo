import pytest
import time
from Demo_Page.Page_Objects.orange_login import LoginPage
from Demo_Page.Constants.constant import Constant
from Demo_Page.Constants.constant import UserDATA
from Demo_Page.Page_Objects.locators import AdminLocators, UserLocators
from Demo_Page.Page_Objects.users_login import UserLogin


@pytest.fixture(scope="module")
def test_base(driver):
    from Demo_Page.Utilities.test_base import TestBase
    return TestBase(driver)


def test_valid_login(driver, test_base):
    login_page = LoginPage(driver)
    login_page.open(Constant.BASE_URL)

    test_base.wait_for_element(AdminLocators.MAIN_PAGE)

    login_page.set_username(Constant.USERNAME)
    login_page.set_password(Constant.PASSWORD)
    login_page.click_login()
    test_base.wait_for_element(AdminLocators.ASSERT_VALUE)
    login_page.assert_dashboard_title()


def test_user_login(driver, test_base):
    user_page = UserLogin(driver)
    user_page.access_system_users_menu()
    test_base.wait_for_element(UserLocators.USERADD_BUTTON)
    user_page.user_add_btn()
    test_base.wait_for_element(UserLocators.USER_ROLE)

    user_page.user_role()
    user_page.user_status()
    user_page.add_employee(UserDATA.EMPLOYEE_NAME)
    user_page.add_username(UserDATA.MY_USER)
    user_page.add_password(UserDATA.MY_PASSWORD)
    user_page.confirm_password(UserDATA.MY_PASSWORD)
    user_page.save_btn()
    time.sleep(20)
