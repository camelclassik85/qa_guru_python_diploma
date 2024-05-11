import allure
from selene import browser, have
from start_project_tests.test_data.constants import KIDS_HEADER_SECTION_NAMES


class Header:

    def __init__(self):
        self.search_loupe = browser.element('[data-testid="search_loupe"]')
        self.search_input_text = browser.element(
            '.HeaderSearch_header-search__input-text__F3SjJ')
        self.search_result_films = browser.all('[data-testid="search_result"]')
        self.series_button = browser.element('[data-testid="series_button"]')
        self.start_logo = browser.element('[class="HeaderDesktop_header-desktop__left-section__Xj2yw"]>a')
        self.kids_content_sections = browser.all('.HeaderCatalog_header-catalog__child-link__7VASR')

    def click_on_search_loupe(self):
        with allure.step("Click header search loupe"):
            self.search_loupe.click()

    def type_text_to_search_filed(self, text):
        with allure.step(f"Type text {text} to header search field"):
            self.search_input_text.type(text)

    def check_one_film_search_result_dropdown(self):
        with allure.step("Check one dropdown search result"):
            self.search_result_films.should(have.size(1))

    def click_on_header_start_logo(self):
        with allure.step("Click on Start header logo"):
            self.start_logo.click()

    def check_kids_header_content_sections_name(self):
        with allure.step("Check kids header content sections name"):
            for number, section in enumerate(self.kids_content_sections):
                section.should(have.text(KIDS_HEADER_SECTION_NAMES[number]))
