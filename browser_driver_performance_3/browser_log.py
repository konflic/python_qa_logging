import pytest
import os

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

DRIVERS = os.path.expanduser("~/Downloads/drivers")


# https://github.com/SeleniumHQ/selenium/wiki/Logging

@pytest.fixture
def chrome(request):
    caps = DesiredCapabilities.CHROME
    options = webdriver.ChromeOptions()
    options.add_experimental_option('w3c', False)
    caps['loggingPrefs'] = {'performance': 'ALL', 'browser': 'ALL', 'driver': 'ALL'}
    wd = webdriver.Chrome(executable_path=f"{DRIVERS}/chromedriver",
                          desired_capabilities=caps,
                          options=options)

    request.addfinalizer(wd.quit)
    return wd


def test_logging_browser(chrome):
    driver = chrome
    driver.get('https://ya.ru/')
    driver.execute_script("console.warn('Here is the WARNING message!')")
    driver.execute_script("console.error('Here is the ERROR message!')")
    driver.execute_script("console.log('Here is the LOG message!')")
    driver.execute_script("console.info('Here is the INFO message!')")
    print(driver.log_types)

    # Логиирование производительности страницы
    with open("performance.log", "w+") as f:
        for line in driver.get_log("performance"):
            f.write(str(line))
            f.write("\n")

    # Логи консоли браузера собирает WARNINGS, ERRORS
    with open("browser.log", "w+") as f:
        for line in driver.get_log("browser"):
            f.write(str(line))
            f.write("\n")

    # Локальное логированеи драйвера
    with open("driver.log", "w+") as f:
        for line in driver.get_log("driver"):
            f.write(str(line))
            f.write("\n")
