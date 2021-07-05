from locators.home_page import HomePageLocators
from pages.base_page import BasePage
from pages.product_page import ProductPage


class Homepage(BasePage):
    def select_a_product(self):
        self.click_index(HomePageLocators.PRODUCT_BY_ID, 1)
        return ProductPage(self.driver)

    def go_to_setting(self):
        self.click_by_class_name(HomePageLocators.ELLIPSIS_BUTTON_BY_CLASS_NAME)
        self.click_by_id(HomePageLocators.SETTING_BUTTON_BY_ID)

    @property
    def product_elements(self):
        return self.driver.find_elements_by_id(HomePageLocators.PRODUCT_BY_ID)
