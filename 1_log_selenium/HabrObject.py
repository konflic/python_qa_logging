from BasePage import BasePage
from selenium.webdriver.common.by import By


class HabrObject(BasePage):
    SEARCH_BTN = (By.CSS_SELECTOR, ".tm-header-user-menu__search")
    SEARCH_FILED = (By.CSS_SELECTOR, "input[name='q']")
    READ_MORE = (By.CSS_SELECTOR, ".tm-article-snippet__readmore")
    FILTERS_DROPDOWN = (By.CSS_SELECTOR, ".tm-navigation-dropdown__button")
    FILTER_BY_RATING = (By.XPATH, "//li[contains(text(), 'rating')]")
    POST_BODY = (By.CSS_SELECTOR, ".tm-page-article__body")
    TAB_HUBS = (By.XPATH, "//a[contains(text(), 'Hubs')]")
    HUBS = (By.CSS_SELECTOR, ".tm-hubs-list")

    def search(self, request):
        self.input_and_submit(self.SEARCH_FILED, request)

    def read_more(self):
        self.click(self.READ_MORE)

    def click_search(self):
        self.click(self.SEARCH_BTN)

    def select_hubs(self):
        self.click(self.TAB_HUBS)
