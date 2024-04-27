import allure
from start.pages.page_factory import pages


@allure.epic('Header tests')
@allure.feature('Start Logo clink')
def test_logo_start_should_open_main_page():
    pages.series_page.open_series_page()
    pages.series_page.check_series_page_title()
    pages.header.click_on_header_start_logo()
    pages.main_page.check_main_page_title()


@allure.epic('Header tests')
@allure.feature('Kids header content sections')
def test_kids_header_content_sections_name():
    pages.main_page.open_kids_main_page()
    pages.main_page.check_kids_main_page_title()
    pages.header.check_kids_header_content_sections_name()
