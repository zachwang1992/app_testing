from pathlib import Path
import logging as logger

import pytest

from appium import webdriver
from appium.webdriver.connectiontype import ConnectionType

from utilities.generic_utilities import get_appium_server_address


@pytest.fixture(scope="function")
def driver():
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['deviceName'] = 'Android'
    desired_caps['app'] = str(Path().absolute()) + r'\app\app-debug.apk'

    logger.info('launching the app')
    driver = webdriver.Remote(get_appium_server_address(), desired_caps)
    driver.implicitly_wait(10)
    yield driver
    driver.set_network_connection(ConnectionType.ALL_NETWORK_ON)
    logger.info('quiting the app')
    driver.quit()
