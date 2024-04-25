import allure
import pytest
from start.data.content import cheburashka
from start.pages.page_factory import pages


@allure.epic('Favorites tests')
@allure.feature('Show popup about registration to virtual user')
@pytest.mark.parametrize('content', [cheburashka.alias])
def test_favorites_show_popup_for_virtual(content):
    pages.content_page.open_content_page(content)
    pages.content_page.click_add_to_favorites()
    pages.registration_popup.check_popup_shows()
