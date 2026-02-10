import time

import pytest
import os

from seleniumwire import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

DRIVERS = os.path.expanduser("~/Downloads/drivers")
# https://github.com/SeleniumHQ/selenium/wiki/Logging


@pytest.fixture
def driver(request):
    options = webdriver.ChromeOptions()
    service = ChromeService()
    _driver = webdriver.Chrome(
        service=service, options=options, seleniumwire_options={"enable_har": True}
    )

    request.addfinalizer(_driver.quit)
    return _driver


def test_logging_browser(driver):
    driver.get("https://www.google.com/search?q=lk")

    with open("logs/network.json", "w+") as f:
        f.write(driver.har)
