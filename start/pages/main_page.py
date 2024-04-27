import allure
from selene import browser, have, be
from start.constants import web_main_page_title, web_kids_main_page_title


class MainPage:

    def __init__(self):
        self.exp_tarifficator_header = browser.element('.Header_header__6eZSK')
        self.tarifficator_header_logo = browser.element('[class="Header_header__logo__xv0aB"]')
        self.google_account_popup = browser.element('iframe[src*="google.com"]')
        self.header_films_button = browser.element('[data-testid="movies_button"]')

    @staticmethod
    def open_main_page():
        with allure.step("Open Main page"):
            browser.open('/')

    @staticmethod
    def open_kids_main_page():
        with allure.step("Open kids main page"):
            browser.open('/kids')

    @staticmethod
    def check_kids_main_page_title():
        with allure.step("Validate Kids main page title"):
            browser.should(have.title(web_kids_main_page_title))

    @staticmethod
    def open_film_page():
        with allure.step("Open Movies page"):
            browser.open('/movies')

    @staticmethod
    def check_main_page_title():
        with allure.step("Validate Main page title"):
            browser.should(have.title(web_main_page_title))

    def close_exp_tarifficator_on_main(self):
        with allure.step("Close exp tarifficator on main if presence"):
            try:
                self.exp_tarifficator_header.should(be.visible)
                self.tarifficator_header_logo.click()
            except AssertionError:
                pass

    def open_page_according_browser_name(self, browser_name):
        """Сделано так, потому что в firefox не закрывается iframe по командам selene"""

        if browser_name == 'firefox':
            self.open_film_page()
        else:
            self.open_main_page()
            self.check_main_page_title()
