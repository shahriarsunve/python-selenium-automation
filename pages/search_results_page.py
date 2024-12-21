from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from time import sleep

class SearchResultsPage(BasePage):
    SEARCH_RESULTS = (By.XPATH, "//div[@data-test='resultsHeading']")
    PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='content-wrapper'] h4")
    FAVORITES_BTN = (By.CSS_SELECTOR, "[data-test='FavoritesButton']")
    FAVORITES_TOOLTIP_TXT = (By.XPATH, "//*[text()='Click to sign in and save']")

    def get_product_name(self):
        return self.find_element(*self.PRODUCT_NAME).text

    def hover_favorites_icon(self):
        # fav_icon = self.find_element(*self.FAVORITES_BTN)
        # actions = ActionChains(self.driver)
        # actions.move_to_element(fav_icon)
        # actions.perform()
        self.hover_element(*self.FAVORITES_BTN)

    def verify_search_results(self, product):
        self.verify_partial_text(product, *self.SEARCH_RESULTS)

    def verify_search_url(self, product):
        self.verify_partial_url(product)

    def verify_fav_tooltip(self):
        self.wait_for_element_visible(*self.FAVORITES_TOOLTIP_TXT)

