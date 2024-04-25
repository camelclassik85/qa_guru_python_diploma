import allure
from selene import browser, have, be
from start.constants import Search, web_search_url, web_search_title


class SearchPage:

    def __init__(self):
        self.search_output_lines = browser.all(
            '[class="VideoUnit_vline__TljVd    VideoUnit_noPadding__oqnkQ"]')
        self.search_field = browser.element('#search')
        self.search_film_results = browser.all('[class="VideoUnit_vline__slider__card__dIGe3"]')
        self.search_empty_results_block = browser.element(
            '[class="Search_search__empty__5m3TS"]')
        self.search_recommendation_title = browser.element(
            '[class="Search_search__recommendation__title__AENpp"]')
        self.search_recommendation_desc = browser.element(
            '[class="Search_search__recommendation__desc__Jb8qW"]')

    @staticmethod
    def open_search_page():
        with allure.step("Open Search page"):
            browser.open(web_search_url)

    @staticmethod
    def check_search_title():
        with allure.step("Validate Search page title"):
            browser.should(have.title(web_search_title))

    @allure.step("Type text {text} to search field")
    def type_text_to_filed(self, text):
        self.search_field.type(text)

    def check_multiple_film_search_result(self):
        with allure.step("Check more than 1 search film results"):
            self.search_film_results.should(have.size_greater_than(1))

    def check_empty_search_results(self):
        with allure.step("Check empty search result block"):
            self.search_empty_results_block.should(be.visible)
        with allure.step("Check empty search result recommendation title"):
            self.search_recommendation_title.should(have.text(
                Search.search_recommendation_title_text))
        with allure.step("Check empty search result recommendation description"):
            self.search_recommendation_desc.should(have.text(
                Search.search_recommendation_desc_text))
