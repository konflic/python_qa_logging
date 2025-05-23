import os
import pytest
import logging
import uuid

from selenium import webdriver
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener

DRIVERS = os.path.expanduser("~/Downloads/drivers")


# Конфигурируем логгер глобально и наблюдаем сайдэффект
# logging.basicConfig(level=logging.INFO, filename="logs/test.log")


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--executor", action="store", default="127.0.0.1")
    parser.addoption("--log_level", action="store", default="INFO")

log_map = {
    "DEBUG": logging.DEBUG,
    "INFO": logging.INFO
}

@pytest.fixture
def browser(request):
    browser = request.config.getoption("--browser")
    executor = request.config.getoption("--executor")
    log_level = request.config.getoption("--log_level")

    class MyListener(AbstractEventListener):
        logger = logging.getLogger(request.node.name)
        logger.setLevel(logging.INFO)
        ch = logging.FileHandler(filename=f"logs/{request.node.name}.log")
        ch.setFormatter(logging.Formatter('%(name)s:%(levelname)s %(message)s'))
        ch.setLevel(log_map[log_level])
        logger.addHandler(ch)

        def before_navigate_to(self, url, driver):
            self.logger.info(f"I'm navigating to {url}")

        def after_navigate_to(self, url, driver):
            self.logger.info(f"I'm on {url}")

        def before_navigate_back(self, driver):
            self.logger.info(f"I'm navigating back")

        def after_navigate_back(self, driver):
            self.logger.info(f"I'm back!")

        def before_find(self, by, value, driver):
            self.logger.info(f"I'm looking for '{value}' with '{by}'")

        def after_find(self, by, value, driver):
            self.logger.info(f"I've found '{value}' with '{by}'")

        def before_click(self, element, driver):
            self.logger.info(f"I'm clicking found element")

        def after_click(self, element, driver):
            self.logger.info(f"I've clicked {element}")

        def before_execute_script(self, script, driver):
            self.logger.info(f"I'm executing '{script}'")

        def after_execute_script(self, script, driver):
            self.logger.info(f"I've executed '{script}'")

        def before_quit(self, driver):
            self.logger.info(f"I'm getting ready to terminate {driver}")

        def after_quit(self, driver):
            self.logger.info(f"Driver Quit")

        def on_exception(self, exception, driver):
            self.logger.error(f'Oooops i got: {exception}')
            driver.save_screenshot(f'logs/{uuid.uuid4()}.png')

    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()

    driver = EventFiringWebDriver(driver, MyListener())
    driver.test_name = request.node.name
    driver.log_level = log_level

    def fin():
        driver.quit()

    request.addfinalizer(fin)
    return driver
