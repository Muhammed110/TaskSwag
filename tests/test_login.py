import pytest
from selenium import webdriver
from utils.data import Login
from utils.locators import MainLocators
from pages.login_page import LoginPage
from utils.data import MainData
import allure
import os
from dotenv import load_dotenv

load_dotenv()
base_url = os.getenv("BASE_URL")

@allure.epic("Testing login page")
class TestLogin:
    main_locators = MainLocators()
    data = MainData()

    @allure.title("test login with page title check")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_login1_positive(self, driver):
        page = LoginPage(driver, base_url)
        page.open()
        page.login()
        header_title = page.get_text(self.main_locators.TITLE)
        expected_header_title = self.data.header_title
        assert (
            header_title == expected_header_title
        ), f"Unexpected text. Expected: {expected_header_title}, Actual: {header_title}"

