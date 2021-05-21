import os
import pytest
import logging

from selenium import webdriver

DRIVERS = os.path.expanduser("~/Downloads/drivers")

logging.basicConfig(level=logging.INFO, filename="logs/selenium.log")


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--executor", action="store", default="127.0.0.1")


@pytest.fixture
def browser(request):
    browser = request.config.getoption("--browser")
    executor = request.config.getoption("--executor")
    logger = logging.getLogger('BrowserLogger')
    test_name = request.node.name

    logger.info("===> Test {} started".format(test_name))

    if browser == "chrome":
        driver = webdriver.Chrome(executable_path=f"{DRIVERS}/chromedriver")
    elif browser == "firefox":
        driver = webdriver.Firefox(executable_path=f"{DRIVERS}/geckodriver")
    else:
        driver = webdriver.Remote(
            command_executor="http://{}:4444/wd/hub".format(executor),
            desired_capabilities={"browserName": browser}
        )

    logger.info("Browser {} started with {}".format(browser, driver.desired_capabilities))

    def fin():
        driver.quit()
        logger.info("===> Test {} finished".format(test_name))

    request.addfinalizer(fin)
    return driver
