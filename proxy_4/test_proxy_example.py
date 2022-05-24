import json

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
    options.add_argument(f'--proxy-server={proxy_url}')
    driver = webdriver.Chrome(executable_path=f"{DRIVERS}/chromedriver", options=options)
    driver.proxy = proxy_server
    driver.implicitly_wait(5)

    def fin():
        driver.proxy.close()
        driver.quit()

    request.addfinalizer(fin)
    return driver


def dump_log_to_json(har_log, file_name):
    logs = []
    with open(file_name, "w+") as f:
        for i, el in enumerate(har_log["entries"], start=1):
            logs.append({i: {"request": el["request"], "response": el["response"]}})
        f.write(json.dumps(logs))


def test_proxy_login(browser):
    browser.get('https://demo.opencart.com/admin')
    browser.find_element_by_id("input-username").send_keys("admin")
    browser.find_element_by_id("input-password").send_keys("admin")
    browser.find_element_by_tag_name("form").submit()
    dump_log_to_json(browser.proxy.har['log'], "open_cart_login.json")
    browser.close()


def test_simple_example(browser):
    browser.get("https://konflic.github.io/examples/pages/ajax.html")
    # Выполняем несколько кликов для ajax запросов
    browser.find_element_by_name("showjsbutton").click()
    time.sleep(1)
    browser.find_element_by_name("showjsbutton").click()
    time.sleep(1)
    browser.find_element_by_name("showjsbutton").click()
    time.sleep(5)
    dump_log_to_json(browser.proxy.har['log'], "ajax_requests.json")
    browser.close()


def test_proxy_yandex(browser):
    browser.get('https://yandex.ru/')
    browser.find_element_by_id("text").send_keys("test")
    browser.find_element_by_id("text").submit()
    time.sleep(2)
    dump_log_to_json(browser.proxy.har['log'], "yandex.json")
    browser.close()
