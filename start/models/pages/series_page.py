import allure
from selene import browser, have
from start.test_data.constants import web_series_page_title, web_series_url


class SeriesPage:

    def __init__(self):
        self.series_page_h1_text = browser.element('[class="Catalog_catalog__Gjv4a"]')

    @staticmethod
    def open_series_page():
        with allure.step("Open series page"):
            browser.open(web_series_url)

    @staticmethod
    def check_series_page_title():
        with allure.step("Check series page title"):
            browser.should(have.title(web_series_page_title))
