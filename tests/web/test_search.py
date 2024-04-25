import allure
import pytest
from start.constants import Search
from start.pages.page_factory import pages


@allure.epic('Search tests')
@allure.feature('Search in header')
def test_search_one_film_result_dropdown(browser_name):
    pages.main_page.open_page_according_browser_name(browser_name=browser_name)
    pages.cookie_popup.cookie_accept()
    pages.main_page.close_exp_tarifficator_on_main()
    pages.header.click_on_search_loupe()
    pages.header.type_text_to_search_filed(text=Search.search_with_one_element_result)
    pages.header.check_one_film_search_result_dropdown()


@allure.epic('Search tests')
@allure.feature('Search on search page')
@pytest.mark.parametrize('text',
                         [Search.search_multiple_element_result_per,
                          Search.search_multiple_element_result_nov])
def test_search_multiple_films_result(text):
    pages.search_page.open_search_page()
    pages.search_page.check_search_title()
    pages.search_page.type_text_to_filed(text=text)
    pages.search_page.check_multiple_film_search_result()


@allure.epic('Search tests')
@allure.feature('Search on search page')
def test_search_empty_result():
    pages.search_page.open_search_page()
    pages.search_page.check_search_title()
    pages.search_page.type_text_to_filed(text=Search.search_no_results)
    pages.search_page.check_empty_search_results()
