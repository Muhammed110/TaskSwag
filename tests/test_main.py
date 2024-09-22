from pages.main_page import MainPage
from utils.data import MainData
import allure
import os
import random
from dotenv import load_dotenv


load_dotenv()


@allure.epic("Testing main page")
class TestMainPage:
    base_url = os.getenv("BASE_URL")
    main_url = os.getenv("MAIN_URL")
    about_url = os.getenv("ABOUT_URL")
    main_data = MainData()


    @allure.title("test of adding a product to cart")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_add_item_to_cart(self, driver):
        expected_value = "1"
        page = MainPage(driver, self.base_url)
        page.open()
        page.login()
        value = page.add_to_cart()
        assert (
            value.text == expected_value
        ), f"Number of added products does not match {expected_value}"

    @allure.title("test for removing a product from cart")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_remove_item_from_cart(self, driver):
        page = MainPage(driver, self.base_url)
        page.open()
        page.login()
        page.add_to_cart()
        page.remove_from_cart()
        value = page.check_element_is_not_present()
        assert value is True, "The element is present in the DOM tree"


