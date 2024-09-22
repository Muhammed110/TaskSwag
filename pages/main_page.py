from pages.base_page import BasePage
from utils.locators import MainLocators, LoginFormLocators
import allure


class MainPage(BasePage):
    main_locators = MainLocators()
    login_locators = LoginFormLocators()

    @allure.step("Add SAUCE_LABS_BACKPACK to cart and get the COUNT_ITEMS value")
    def add_to_cart(self):
        self.click_on_element(self.main_locators.SAUCE_LABS_BACKPACK)
        value = self.element_is_visible(self.main_locators.COUNT_ITEMS)
        return value

    @allure.step("Remove from cart")
    def remove_from_cart(self):
        self.click_on_element(self.main_locators.REMOVE_SAUCE_LABS_BACKPACK)

    @allure.step("Check the element is not present")
    def check_element_is_not_present(self):
        return self.element_is_not_present(self.main_locators.COUNT_ITEMS)


    def check_card(self, value):
        return self.main_locators.CARD_LAMBDA(value)
