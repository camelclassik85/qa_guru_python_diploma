import allure
from selene import browser, be


class CookiePopup:

    def __init__(self):
        self.cookie1_popup = browser.element('.CookieBanner_banner__d7Vth')
        self.cookie1_accept = browser.element('.CookieBanner_banner__submit-button__zkWN_')
        self.cookie2_popup = browser.element('[name="CybotCookiebotDialog"]')
        self.cookie2_accept = browser.element('button[id = "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"]')

    def check_cookie1_presence(self) -> bool:
        with allure.step("Check 1st type cookie popup presence"):
            try:
                self.cookie1_popup.should(be.visible)
                return True
            except AssertionError:
                return False

    def check_cookie2_presence(self) -> bool:
        with allure.step("Check 2nd type cookie popup presence"):
            try:
                self.cookie2_popup.should(be.visible)
                return True
            except AssertionError:
                return False

    def cookie_accept(self):
        with allure.step("Cookie accept"):
            if self.check_cookie1_presence():
                self.cookie1_accept.click()
            elif self.check_cookie2_presence():
                self.cookie2_accept.click()
