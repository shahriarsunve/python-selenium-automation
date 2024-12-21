from pages.base_page import BasePage
from pages.cart_page import CartPage
from pages.header import Header
from pages.help_page import HelpPage
from pages.main_page import MainPage
from pages.privacy_policy_page import PrivacyPolicyPage
from pages.search_results_page import SearchResultsPage
from pages.target_app_page import TargetAppPage


class Application:

    def __init__(self, driver):
        self.driver = driver

        self.base_page = BasePage(driver)
        self.cart_page = CartPage(driver)
        self.header = Header(driver)
        self.help_page = HelpPage(driver)
        self.main_page = MainPage(driver)
        self.privacy_policy_page = PrivacyPolicyPage(driver)
        self.search_results_page = SearchResultsPage(driver)
        self.target_app_page = TargetAppPage(driver)
