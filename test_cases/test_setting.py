from pages.home_page import Homepage


class TestSetting:
    def test_open_setting_page(self, driver):
        """
        The method tests that user can go to setting page by clicking setting button.
        :param driver: fixture
        :return: None
        """
        home_page = Homepage(driver)
        home_page.go_to_setting()

        # go to setting page and check elements
        # setting page is not implemented
        assert False, 'setting page is not implemented'
