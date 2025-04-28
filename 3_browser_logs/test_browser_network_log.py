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
        'performance': 'ALL',
    })
    service = ChromeService()
    _driver = webdriver.Chrome(service=service, options=options)

    yield _driver

    _driver.quit()



def test_logging_browser(driver):
    driver.get('https://dzen.ru')

    with open("logs/network.json", "w+") as f:
        logs = driver.get_log("performance")
        data = []
        for entry in logs:
            log = json.loads(entry["message"])["message"]
            if (
                    "Network.response" in log["method"]
                    or "Network.request" in log["method"]
                    or "Network.webSocket" in log["method"]
                    or "Network.dataReceived" in log["method"]
            ):
                data.append(log)
        f.write(json.dumps(data, indent=4, ensure_ascii=False))
