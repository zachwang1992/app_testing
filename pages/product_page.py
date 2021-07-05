from locators.product_page import ProductPageLocators
from pages.base_page import BasePage
from pages.review_page import ReviewPage
from utilities.scroll_utilities import ScrollUtil
import logging as logger


class ProductPage(BasePage):
    def add_review(self):
        self.click_by_id(ProductPageLocators.ADD_REVIEW_BUTTON_BY_ID)
        return ReviewPage(self.driver)

    def search_for_review(self, text):
        logger.info(f'searching for text: {text}')
        return ScrollUtil.scroll_to_search_for_review(text, self.driver)
