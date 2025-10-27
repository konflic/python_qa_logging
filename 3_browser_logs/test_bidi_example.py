import json

import pytest
import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService


@pytest.fixture
def driver(request):
    options = webdriver.ChromeOptions()
    options.enable_bidi = True
    service = ChromeService()
    _driver = webdriver.Chrome(service=service, options=options)

    console_log_entries = []

    _driver.script.add_console_message_handler(console_log_entries.append)

    yield _driver

    _driver.quit()

    for el in console_log_entries:
        if el.level == "error":
            raise AssertionError(f"Found js error '{el.text}'")


def test_logging_browser(driver):
    driver.get("https://konflic.github.io/examples/")
    driver.execute_script("console.warn('Here is the WARNING message!')")
    driver.execute_script("console.error('Here is the ERROR message!')")
    driver.execute_script("console.log('Here is the LOG message!')")
    driver.execute_script("console.info('Here is the INFO message!')")
