import json
import time

import pytest
import os

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

DRIVERS = os.path.expanduser("~/Downloads/drivers")
# https://github.com/SeleniumHQ/selenium/wiki/Logging

@pytest.fixture
def driver(request):
    caps = DesiredCapabilities.CHROME
    options = webdriver.ChromeOptions()

    caps['goog:loggingPrefs'] = {
        'browser': 'ALL',
        'performance': 'ALL',
        'driver': 'ALL'
    }

    _driver = webdriver.Chrome(executable_path=f"{DRIVERS}/chromedriver",
                               desired_capabilities=caps,
                               options=options)

    request.addfinalizer(_driver.quit)
    return _driver


def test_logging_browser(driver):
    driver.get('https://yandex.ru/')

    driver.execute_script("console.warn('Here is the WARNING message!')")
    driver.execute_script("console.error('Here is the ERROR message!')")
    driver.execute_script("console.log('Here is the LOG message!')")
    driver.execute_script("console.info('Here is the INFO message!')")

    print(driver.log_types)

    # Логиирование производительности страницы
    with open("performance.json", "w+") as f:
        f.write(json.dumps(driver.get_log("performance"), indent=4, ensure_ascii=False))

    with open("browser.json", "w+") as f:
        f.write(json.dumps(driver.get_log("browser"), indent=4, ensure_ascii=False))

    with open("driver.json", "w+") as f:
        f.write(json.dumps(driver.get_log("driver"), indent=4, ensure_ascii=False))
