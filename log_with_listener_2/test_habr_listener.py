from log_with_listener_2.HabrObject import HabrObject


def test_post_open(browser):
    page = HabrObject(browser)
    page.open("https://habr.com/en")
    page.click_search()
    page.search('Python')
    page.read_more()
    page.is_present(page.POST_BODY)


def test_hubs_open(browser):
    page = HabrObject(browser)
    page.open("https://habr.com/en")
    page.click_search()
    page.search('Python')
    page.select_hubs()
    page.is_present(page.HUBS)
