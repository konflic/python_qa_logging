import logging

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:

    def __init__(self, driver, wait=3):
        self.driver = driver
        self.wait = WebDriverWait(driver, wait)
        self.logger = logging.getLogger(type(self).__name__)
        self.action = ActionChains(driver)

    def open(self, url):
        self.logger.info("Opening url: {}".format(url))
        self.driver.get(url)

    def click(self, locator):
        self.logger.info("Clicking element: {}".format(locator))
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def input_and_submit(self, locator, value):
        self.logger.info("Input {} in input {}".format(value, locator))
        find_field = self.wait.until(EC.presence_of_element_located(locator))
        find_field.click()
        find_field.clear()
        find_field.send_keys(value)
        find_field.send_keys(Keys.ENTER)

    def is_present(self, locator):
        self.logger.info("Check if element {} is present".format(locator))
        return self.wait.until(EC.visibility_of_element_located(locator))
