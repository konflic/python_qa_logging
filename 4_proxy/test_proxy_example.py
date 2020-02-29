from browsermobproxy import Server, Client
import pytest
import pprint
import time
import urllib.parse
from selenium import webdriver

server = Server("browsermob-proxy/bin/browsermob-proxy")
server.start()
client = Client("localhost:8080")
proxy = server.create_proxy()
client.new_har()


@pytest.fixture
def browser(request):
    chrome_options = webdriver.ChromeOptions()
    url = urllib.parse.urlparse(client.proxy).path
    chrome_options.add_argument('--proxy-server=%s' % url)
    driver = webdriver.Chrome(options=chrome_options)
    request.addfinalizer(driver.quit)
    return driver


def test_proxy(browser):
    browser.get('http://localhost/opencart/')
    browser.get('http://localhost/opencart/admin')
    browser.find_element_by_id("input-username").send_keys("admin")
    browser.find_element_by_id("input-password").send_keys("admin")
    browser.find_element_by_tag_name("form").submit()
    pprint.pprint(client.har)
    server.stop()
