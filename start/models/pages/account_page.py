import allure
from selene import browser, have
from start.test_data.constants import web_account_url


class AccountPage:

    def __init__(self):
        self.user_email = browser.element('[data-testid="email"]')

    @staticmethod
    def open_account_page():
        with allure.step("Open account page"):
            browser.open(web_account_url)

    def check_user_email(self, email):
        with allure.step("Check user email"):
            self.user_email.should(have.text(email))
