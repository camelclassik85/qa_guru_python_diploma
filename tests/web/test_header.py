import allure
from start.pages.page_factory import pages


@allure.epic('Header tests')
@allure.feature('Start Logo clink')
def test_logo_start_should_open_main_page():
    pages.series_page.open_series_page()
    pages.series_page.check_series_page_title()
    pages.header.click_on_header_start_logo()
    pages.main_page.check_main_page_title()
