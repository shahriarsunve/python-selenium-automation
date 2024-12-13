#
# # Blueprint / abstraction
# class Page:
#
#     def click(self, locator):
#         print(f'Clicking by {locator}')
#
#     def find_element(self, locator):
#         print(f'Searching by {locator}')
#
#     def iput_txt(self, locator, text):
#         print(f'Inputting {text} by {locator}')
#
#
# class LoginPage(Page):
#     def login(self):
#         print('Login...')
#
# class SearchResultsPage(Page):
#     pass
#
#
# page = Page()
# page.click()
#
# login_page = LoginPage()
# login_page.click()
