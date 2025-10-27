from log_with_logger.BasePage import BasePage
from selenium.webdriver.common.by import By


class HabrObject(BasePage):
    SEARCH_ICON = (
        By.CSS_SELECTOR,
        ".tm-header-user-menu__search .tm-header-user-menu__icon_search",
    )
    SEARCH_FILED = (By.CSS_SELECTOR, "input[name='q']")
    READ_MORE = (By.CSS_SELECTOR, ".tm-article-snippet__readmore")
    FILTERS_DROPDOWN = (By.CSS_SELECTOR, ".tm-navigation-dropdown__button")
    FILTER_BY_RATING = (By.XPATH, "//li[contains(text(), 'rating')]")
    POST_BODY = (By.CSS_SELECTOR, ".tm-article-body")
    TAB_HUBS = (By.XPATH, "//a[contains(text(), 'Hubs')]")
    HUBS = (By.CSS_SELECTOR, ".tm-hubs-list")
    TAB_HUBS_AND_COMPANIES = (By.XPATH, "//h3[contains(text(), 'Hubs')]")

    def search(self, request):
        self.logger.info(f"{self.class_name}: Search for {request}")
        self.input_and_submit(self.SEARCH_FILED, request)

    def read_more(self):
        self.logger.info(f"{self.class_name}: Click 'READ MORE' link")
        self.click(self.READ_MORE)

    def click_search(self):
        self.logger.info(f"{self.class_name}: Click 'SEARCH' element")
        self.click(self.SEARCH_ICON)

    def select_hubs(self):
        self.logger.info(f"{self.class_name}: Selecting Hubs tab")
        self.click(self.TAB_HUBS)

    def filter_by_rating(self):
        self.logger.info(f"{self.class_name}: Filtering search result by rating")
        self.click(self.FILTERS_DROPDOWN)
        self.click(self.FILTER_BY_RATING)
