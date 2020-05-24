import pytest
import logging

from helper import chromedriver, geckodriver
from selenium import webdriver

logging.basicConfig(level=logging.INFO, filename="selenium.log")


@pytest.fixture
def chrome(request):
    test_name = request.node.name
    logger = logging.getLogger('chrome_fixture')
    logger.info("Started test {}".format(test_name))
    chrome = webdriver.Chrome(executable_path=chromedriver())
    chrome.maximize_window()
    logger.info("Browser Chrome started with {}".format(chrome.desired_capabilities))

    def fin():
        chrome.quit()
        logger.info("Browser chrome closed")
        logger.info("Test {} finished".format(test_name))

    request.addfinalizer(fin)
    return chrome


@pytest.fixture
def firefox(request):
    firefox = webdriver.Firefox(executable_path=geckodriver())
    firefox.maximize_window()
    request.addfinalizer(firefox.quit)
    return firefox
