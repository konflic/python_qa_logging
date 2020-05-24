import pytest
import urllib.parse

from helper import chromedriver
from browsermobproxy import Server, Client
from selenium import webdriver


@pytest.fixture
def proxy_server(request):
    server = Server("browsermob-proxy/bin/browsermob-proxy")
    server.start()
    client = Client("localhost:8080")
    server.create_proxy()
    request.addfinalizer(server.stop)
    client.new_har()
    return client


@pytest.fixture
def browser(request, proxy_server):
    options = webdriver.ChromeOptions()
    # Избавляемся от ошибок сертификатов
    # https://stackoverflow.com/questions/24507078/how-to-deal-with-certificates-using-selenium
    options.add_argument('--ignore-certificate-errors')
    # Устанавливаем прокси сервер
    proxy_url = urllib.parse.urlparse(proxy_server.proxy).path
    options.add_argument('--proxy-server=%s' % proxy_url)
    driver = webdriver.Chrome(options=options, executable_path=chromedriver())
    driver.proxy = proxy_server
    driver.implicitly_wait(5)
    request.addfinalizer(driver.quit)
    return driver


def test_proxy(browser):
    browser.get('https://yandex.ru/')
    browser.get('https://demo.opencart.com/')
    browser.get('https://demo.opencart.com/admin')
    browser.find_element_by_id("input-username").send_keys("admin")
    browser.find_element_by_id("input-password").send_keys("admin")
    browser.find_element_by_tag_name("form").submit()
    har = browser.proxy.har['log']
    for el in har:
        print(el)
