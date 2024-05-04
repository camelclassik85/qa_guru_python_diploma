import allure
import pytest
from start.api.api import api_call
from start.data.content import cheburashka, syostry
from start.data.users import authorized_user
from start.pages.page_factory import pages


@allure.epic('Favorites tests')
@allure.feature('Shows popup about registration to virtual user')
@pytest.mark.parametrize('content', [cheburashka.alias])
def test_favorites_show_popup_for_virtual(content):
    pages.content_page.open_content_page(content)
    pages.cookie_popup.cookie_accept()
    pages.content_page.click_add_to_favorites()
    pages.registration_popup.check_popup_shows()


@allure.epic('Favorites tests')
@allure.feature('Add to favorites')
@pytest.mark.parametrize('content', [cheburashka, syostry])
def test_add_to_favorites_authorized(content):
    api_call.add_to_favorites(authorized_user, content.uid)
    pages.favorites_page.open_favorites_page_authorized(authorized_user)
    pages.favorites_page.check_favorites_title()
    pages.favorites_page.check_content_presence_in_favorites(content.favs_title)
    api_call.delete_from_favorites(authorized_user, content.uid)
