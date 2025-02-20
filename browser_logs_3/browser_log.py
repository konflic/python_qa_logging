import json

import pytest
import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

DRIVERS = os.path.expanduser("~/Downloads/drivers")
# https://github.com/SeleniumHQ/selenium/wiki/Logging

@pytest.fixture
def driver(request):
    options = webdriver.ChromeOptions()
    options.set_capability('goog:loggingPrefs', {
        'browser': 'ALL',
        'performance': 'ALL',
        'driver': 'ALL'
    })
    service = ChromeService()
    _driver = webdriver.Chrome(service=service, options=options)

    request.addfinalizer(_driver.quit)
    return _driver


def test_logging_browser(driver):
    driver.get('https://demo.opencart.com/')

    driver.execute_script("console.warn('Here is the WARNING message!')")
    driver.execute_script("console.error('Here is the ERROR message!')")
    driver.execute_script("console.log('Here is the LOG message!')")
    driver.execute_script("console.info('Here is the INFO message!')")

    print(driver.log_types)

    # Логиирование производительности страницы
    # with open("logs/performance.json", "w+") as f:
    #     f.write(json.dumps(driver.get_log("performance"), indent=4, ensure_ascii=False))

    # with open("network.json", "w+") as f:
    #     logs = driver.get_log("performance")
    #     data = []
    #     for entry in logs:
    #         log = json.loads(entry["message"])["message"]
    #         if (
    #                 "Network.response" in log["method"]
    #                 or "Network.request" in log["method"]
    #                 or "Network.webSocket" in log["method"]
    #                 or "Network.dataReceived" in log["method"]
    #         ):
    #             data.append(log)
    #     f.write(json.dumps(data, indent=4, ensure_ascii=False))

    with open("browser.json", "w+") as f:
        f.write(json.dumps(driver.get_log("browser"), indent=4, ensure_ascii=False))
