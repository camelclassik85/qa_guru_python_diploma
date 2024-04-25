import allure
from selene import browser, have, be
from start.constants import web_signin_url, web_signin_page_title


class SigninPage:

    def __init__(self):
        self.email_field = browser.element('#signField')
        self.password_field = browser.element('#signPassword')
        self.signin_button = browser.element(
            '[class="Button_red-button__GCS4r Button_fullWidth__YUBwh"]')
        self.capcha_input = browser.element('#signFieldCapcha')

    @staticmethod
    def open_signin_page():
        with allure.step("Open SignIn page"):
            browser.open(web_signin_url)

    @staticmethod
    def check_signin_page_title():
        with allure.step("Validate SignIn page title"):
            browser.should(have.title(web_signin_page_title))

    def fill_authorization_form(self, email, password):
        with allure.step(f"Fill registration form. Type email: {email} and password: {password}"):
            self.email_field.type(email)
            self.password_field.type(password)

    def signin_button_click(self):
        with allure.step("SignIn button click"):
            self.signin_button.click()

    def check_capcha(self):
        with allure.step("Check capcha presence"):
            try:
                self.capcha_input.should(be.visible)
                raise PermissionError('Capcha presence on method, need to wait some time')
            except AssertionError:
                pass
