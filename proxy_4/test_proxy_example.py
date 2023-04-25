import json

import pytest
import time
import os

from browsermobproxy import Server, Client
from selenium import webdriver
from selenium.webdriver.common.by import By

DRIVERS = os.path.expanduser("~/Downloads/drivers")


@pytest.fixture
def proxy_server(request):
    server = Server("browsermob-proxy/bin/browsermob-proxy")
    server.start()
    client = Client("localhost:8080")

    client.rewrite_url("https://yandex.ru/clck/safeclick.*", "/some/new/path")

    server.create_proxy()
    request.addfinalizer(server.stop)
    client.new_har()
    return client


@pytest.fixture
def browser(request, proxy_server):
    options = webdriver.ChromeOptions()
    # Избавляемся от ошибок сертификатов
    options.accept_insecure_certs = True

    # Устанавливаем прокси сервер
    caps = {}
    proxy_server.add_to_webdriver_capabilities(caps)

    print(caps)

    driver = webdriver.Chrome(
        executable_path=f"{DRIVERS}/chromedriver",
        options=options,
        desired_capabilities=caps
    )

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
        f.write(json.dumps(logs, indent=4, ensure_ascii=False))


def test_proxy_login(browser):
    browser.get('https://demo.opencart.com/admin')
    browser.find_element(value="input-username").send_keys("admin")
    browser.find_element(value="input-password").send_keys("admin")
    browser.find_element(By.TAG_NAME, "form").submit()
    time.sleep(5)
    dump_log_to_json(browser.proxy.har['log'], "open_cart_login.json")
    browser.close()


# def test_simple_example(browser):
#     browser.get("https://konflic.github.io/examples/pages/ajax.html")
#     # Выполняем несколько кликов для ajax запросов
#     browser.find_element(By.NAME, "showjsbutton").click()
#     time.sleep(1)
#     browser.find_element(By.NAME, "showjsbutton").click()
#     time.sleep(1)
#     browser.find_element(By.NAME, "showjsbutton").click()
#     time.sleep(1)
#     dump_log_to_json(browser.proxy.har['log'], "ajax_requests.json")
#     browser.close()


def test_proxy_yandex(browser):
    browser.get('https://ya.ru/')
    browser.find_element(value="text").send_keys("test")
    browser.find_element(value="text").submit()
    time.sleep(5)
    dump_log_to_json(browser.proxy.har['log'], "yandex.json")
    browser.close()
