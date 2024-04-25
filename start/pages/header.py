import allure
from selene import browser, have


class Header:

    def __init__(self):
        self.search_loupe = browser.element('[data-testid="search_loupe"]')
        self.search_input_text = browser.element(
            '.HeaderSearch_header-search__input-text__F3SjJ')
        self.search_result_films = browser.all('[data-testid="search_result"]')

    def click_on_search_loupe(self):
        with allure.step("Click header search loupe"):
            self.search_loupe.click()

    @allure.step("Type text {text} to header search field")
    def type_text_to_search_filed(self, text):
        self.search_input_text.type(text)

    def check_one_film_search_result_dropdown(self):
        with allure.step("Check one dropdown search result"):
            self.search_result_films.should(have.size(1))
