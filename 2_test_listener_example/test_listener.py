import pytest
import logging
import time
from selenium import webdriver
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener
from selenium.webdriver.common.keys import Keys

logging.basicConfig(level=logging.INFO, filename="test.log")


class MyListener(AbstractEventListener):

    def before_navigate_to(self, url, driver):
        logging.info(f"I'm navigating to {url}")

    def after_navigate_to(self, url, driver):
        logging.info(f"I'm on {url}")

    def before_navigate_back(self, driver):
        logging.info(f"I'm navigating back")

    def after_navigate_back(self, driver):
        logging.info(f"I'm back!")

    def before_find(self, by, value, driver):
        logging.info(f"I'm looking for '{value}' with '{by}'")

    def after_find(self, by, value, driver):
        logging.info(f"I've found '{value}' with '{by}'")

    def before_click(self, element, driver):
        logging.info(f"I'm clicking {element}")

    def after_click(self, element, driver):
        logging.info(f"I've clicked {element}")

    def before_execute_script(self, script, driver):
        logging.info(f"I'm executing '{script}'")

    def after_execute_script(self, script, driver):
        logging.info(f"I've executed '{script}'")

    def before_quit(self, driver):
        logging.info(f"I'm getting ready to terminate {driver}")

    def after_quit(self, driver):
        logging.info(f"WASTED!!!")

    def on_exception(self, exception, driver):
        logging.error(f'Oooops i got: {exception}')
        driver.save_screenshot(f'{exception}.png')


@pytest.fixture
def driver(request):
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    wd = EventFiringWebDriver(webdriver.Chrome(), MyListener())
    request.addfinalizer(wd.quit)
    return wd


def test_logging(driver):
    driver.get('https://habr.com/en/')
    driver.find_element_by_id('search-form-btn').click()
    find_field = driver.find_element_by_id('search-form-field')
    find_field.send_keys('Python')
    find_field.send_keys(Keys.ENTER)
    driver.back()
    driver.execute_script("console.log('Wooooohooooo');")
    driver.save_screenshot('finish_test.png')
