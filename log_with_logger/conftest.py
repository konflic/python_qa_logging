import datetime
import os

import pytest
import logging

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeServise
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.service import Service as FirefoxService


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--executor", action="store", default="127.0.0.1")
    parser.addoption("--log_level", action="store", default="INFO")


# TODO: Задизайнить через общий logger
@pytest.fixture
def browser(request):
    browser = request.config.getoption("--browser")
    log_level = request.config.getoption("--log_level")

    logger = logging.getLogger(request.node.name)
    file_handler = logging.FileHandler(f"logs/{request.node.name}.log", mode="w")
    file_handler.setFormatter(logging.Formatter("%(levelname)s %(message)s"))
    logger.addHandler(file_handler)
    logger.setLevel(level=log_level)

    logger.info("===> Test started at %s" % datetime.datetime.now())

    service = ChromeServise()
    options = Options()
    options.page_load_strategy = 'eager'
    driver = webdriver.Chrome(service=service, options=options)

    driver.log_level = log_level
    driver.logger = logger
    driver.test_name = request.node.name

    logger.info("Browser %s started" % browser)

    def fin():
        driver.quit()
        logger.info("===> Test finished at %s" % datetime.datetime.now())

    request.addfinalizer(fin)
    return driver
