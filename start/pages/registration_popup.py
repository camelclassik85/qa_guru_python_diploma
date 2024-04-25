import allure
from selene import browser, be


class RegistrationPopup:

    def __init__(self):
        self.registration_popup = browser.element('[class="popups_nalp__wrapper__dyHzJ"]')

    def check_popup_shows(self):
        with allure.step("Check registration popup shows"):
            self.registration_popup.should(be.visible)
