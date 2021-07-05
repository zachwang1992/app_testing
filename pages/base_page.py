import logging as logger


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click_by_id(self, locator):
        self.driver.find_element_by_id(locator).click()
        logger.info("Clicking on an Element "+ locator)

    def click_by_class_name(self, locator):
        self.driver.find_element_by_class_name(locator).click()
        logger.info("Clicking on an Element "+ locator)

    def click_index(self, locator, index):
        self.driver.find_elements_by_id(locator)[index].click()
        logger.info("Clicking on an Element " + locator + " with index: " + str(index))

    def type(self, locator, value):
        self.driver.find_element_by_id(locator).send_keys(value)
        logger.info("Typing in an Element "+ locator + " entered the value as: "+ value)