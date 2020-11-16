from HabrObject import HabrObject


def test_post_open(browser):
    page = HabrObject(browser)
    page.open("https://habr.com/en")
    page.click_search()
    page.search('Python')
    page.filter_by_rating()
    page.read_more()
    page.is_present(page.POST_BODY)


def test_hubs_open(browser):
    page = HabrObject(browser)
    page.open("https://habr.com/en")
    page.click_search()
    page.search('Python')
    page.select_hubs_and_companies()
    page.is_present(page.HUBS)
