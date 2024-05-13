import allure
from selene import browser, have
from start_project_tests.test_data.constants import web_favorites_title, web_favorites_url
from start_project_tests.test_data.users import User
from start_project_tests.utils.cookie import add_auth_cookie_to_browser


class FavoritesPage:

    def __init__(self):
        self.favorites_content_list = browser.all(
            '[class="VideoList_videoCatalog-item-wrapper__MXO94'
            ' VideoList_videoCatalog-item-wrapper-catalog__Kgg4T"]>a')

    @staticmethod
    def open_favorites_page():
        with allure.step("Open Favorites page"):
            browser.open(web_favorites_url)

    @staticmethod
    def open_favorites_page_authorized(user: User):
        add_auth_cookie_to_browser(user, web_favorites_url)

    @staticmethod
    def check_favorites_title():
        with allure.step("Validate Favorites page title"):
            browser.should(have.title(web_favorites_title))

    def check_content_presence_in_favorites(self, content: str):
        with allure.step("Validate Favorites q-ty more than 0"):
            self.favorites_content_list.should(have.size_greater_than(0))
        with allure.step(f"Check content title({content}) presence"):
            browser.element(content)
