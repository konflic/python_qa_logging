import pytest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


# https://github.com/SeleniumHQ/selenium/wiki/Logging

@pytest.fixture
def driver(request):
    d = DesiredCapabilities.CHROME
    opt = webdriver.ChromeOptions()
    opt.add_experimental_option('w3c', False)
    d['loggingPrefs'] = {'performance': 'ALL', 'browser': 'ALL'}
    wd = webdriver.Chrome(desired_capabilities=d, options=opt)
    request.addfinalizer(wd.quit)
    return wd


def test_logging_browser(driver):
    driver.get('https://ya.ru/')

    driver.execute_script("console.warn('Here is the WARNING message!')")
    driver.execute_script("console.error('Here is the ERROR message!')")
    driver.execute_script("console.log('Here is the LOG message!')")

    print(driver.log_types)

    # Логиирование производительности страницы
    # performance = driver.get_log("performance")
    # for l in performance:
    #     print(l)

    # Логи консоли браузера собирает WARNINGS, ERRORS
    # browser = driver.get_log("browser")
    # for l in browser:
    #     print(l)

    # Тоже какое-то логгирование драйвера :)
    # driver = driver.get_log("driver")
    # for l in driver:
    #     print(l)
