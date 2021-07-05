import logging as logger

import pytest

from pages.home_page import Homepage
from pages.product_page import ProductPage


class TestReviews:
    def test_add_review_with_message_and_rate(self, driver):
        """
        The method tests that user can add review to a product and review is shown in product page immediately after
        being saved.
        :param driver: fixture
        :return: None
        """
        home_page = Homepage(driver)
        review_page = home_page.select_a_product().add_review()
        review_page.fill_and_save_review()
        product_page = ProductPage(driver)
        review_message = f'{review_page.review} {review_page.rating}'

        assert product_page.search_for_review(review_message), \
            'newly added review is not shown in product page without resetting app'

    @pytest.mark.flaky(reruns=1)
    def test_review_is_saved_after_resetting_app(self, driver):
        """
        The method tests that user can add review to a product and review is shown in product page after app is
        relaunched.
        :param driver: fixture
        :return: None
        """
        home_page = Homepage(driver)
        review_page = home_page.select_a_product().add_review()
        review_page.fill_and_save_review()
        review_message = f'{review_page.review} {review_page.rating}'

        driver.reset()
        logger.info('relaunching the app')
        home_page = Homepage(driver)
        product_page = home_page.select_a_product()
        assert product_page.search_for_review(review_message), \
            'newly added review is not shown in product page after resetting app'

    @pytest.mark.flaky(reruns=1)
    def test_add_review_with_only_rating(self, driver):
        """
        The method tests that user can add review with only rating and without a message.
        :param driver:
        :return: None
        """
        home_page = Homepage(driver)
        review_page = home_page.select_a_product().add_review()
        review_page.fill_and_save_review_with_only_rating()


