import allure
from selene import browser


class ContentPage:

    def __init__(self):
        self.add_to_favorites_image = browser.element('[src="/static/images/product/favorites.svg"]')

    @staticmethod
    def open_content_page(alias):
        with allure.step(f'Open content: {alias} page'):
            browser.open('/watch/' + alias)

    def click_add_to_favorites(self):
        with allure.step("Click add to favorites icon"):
            self.add_to_favorites_image.click()
