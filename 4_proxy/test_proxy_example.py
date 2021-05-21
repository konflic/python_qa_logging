import pytest
import urllib.parse
import time
import os

from browsermobproxy import Server, Client
from selenium import webdriver

DRIVERS = os.path.expanduser("~/Downloads/drivers")


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

    driver = webdriver.Chrome(executable_path=f"{DRIVERS}/chromedriver", options=options)

    driver.proxy = proxy_server
    driver.implicitly_wait(5)

    def fin():
        driver.proxy.close()
        driver.quit()

    request.addfinalizer(fin)
    return driver


def test_proxy_login(browser):
    browser.get('https://demo.opencart.com/admin')
    browser.find_element_by_id("input-username").send_keys("admin")
    browser.find_element_by_id("input-password").send_keys("admin")
    browser.find_element_by_tag_name("form").submit()
    har = browser.proxy.har['log']
    with open("open_cart_login.log", "w+") as f:
        for el in har["entries"]:
            f.write(str(el["request"]) + "\n")
    browser.close()


def test_simple_example(browser):
    browser.get("https://konflic.github.io/front_example/pages/ajax.html")
    # Выполняем несколько кликов для ajax запросов
    browser.find_element_by_name("showjsbutton").click()
    time.sleep(1)
    browser.find_element_by_name("showjsbutton").click()
    time.sleep(1)
    browser.find_element_by_name("showjsbutton").click()
    time.sleep(5)

    har = browser.proxy.har['log']

    with open("ajax_requests.log", "w+") as f:
        for el in har["entries"]:
            f.write(str(el["request"]) + "\n")

    browser.close()


def test_proxy_yandex(browser):
    browser.get('https://yandex.ru/')
    browser.find_element_by_id("text").send_keys("test")
    browser.find_element_by_id("text").submit()

    time.sleep(2)
    har = browser.proxy.har['log']

    with open("yandex.log", "w+") as f:
        for el in har["entries"]:
            f.write(str(el["request"]) + "\n")
    browser.close()
