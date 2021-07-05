import time
import logging as logger

import pytest
from appium.webdriver.connectiontype import ConnectionType

from pages.home_page import Homepage
from pages.product_page import ProductPage


class TestCornerCases:
    @pytest.mark.flaky(reruns=1)
    def test_launching_app_during_internet_disconnection(self, driver):
        """
        The method tests that elements are not shown in the homepage when app is launched during internet disconnection.
        :param driver: fixture
        :return: None
        """
        driver.set_network_connection(ConnectionType.NO_CONNECTION)
        logger.info('stopping internet connection')
        time.sleep(2)

        driver.reset()
        logger.info('relaunching the app')
        home_page = Homepage(driver)

        assert not home_page.product_elements, 'elements are still shown during internet disconnection'

    @pytest.mark.flaky(reruns=1)
    def test_add_review_during_internet_disconnection(self, driver):
        """
        The method tests that the added review during internet disconnection is not saved and will not be shown in
        product page when internet is reconnected.
        :param driver: fixture
        :return: None
        """
        home_page = Homepage(driver)
        driver.set_network_connection(ConnectionType.NO_CONNECTION)
        logger.info('stopping internet connection')
        review_page = home_page.select_a_product().add_review()
        review_page.fill_and_save_review()
        product_page = ProductPage(driver)
        review_message = f'{review_page.review} {review_page.rating}'

        assert not product_page.search_for_review(review_message), 'review is saved during internet disconnection'

        driver.set_network_connection(ConnectionType.ALL_NETWORK_ON)
        logger.info('starting internet connection')
        time.sleep(3)
        driver.reset()
        logger.info('relaunching the app')
        home_page = Homepage(driver)
        product_page = home_page.select_a_product()
        assert not product_page.search_for_review(review_message), 'review is saved during internet disconnection'


