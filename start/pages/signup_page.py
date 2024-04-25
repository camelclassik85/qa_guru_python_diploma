import allure
from selene import browser, have, be
from start.constants import web_signup_url, web_signup_page_title


class SignupPage:

    def __init__(self):
        self.email_field = browser.element('#signField')
        self.password_field = browser.element('#signPassword')
        self.policy_checkbox = browser.element('[for="agreement"]')
        self.signup_button = browser.element(
            '[class="Button_red-button__GCS4r Button_fullWidth__YUBwh"]')
        self.capcha_input = browser.element('#signFieldCapcha')

    @staticmethod
    def open_signup_page():
        with allure.step("Open SignUp page"):
            browser.open(web_signup_url)

    @staticmethod
    def check_signup_page_title():
        with allure.step("Validate SignUp page title"):
            browser.should(have.title(web_signup_page_title))

    def fill_registration_form(self, email, password):
        with allure.step(f"Fill registration form. Type email: {email} and password: {password}"):
            self.email_field.type(email)
            self.password_field.type(password)

    def accept_policy(self):
        with allure.step("Policy checkbox accept"):
            self.policy_checkbox.click()

    def signup_button_click(self):
        with allure.step("SignUp button click"):
            self.signup_button.click()

    def check_capcha(self):
        with allure.step("Check capcha presence"):
            try:
                self.capcha_input.should(be.visible)
                raise PermissionError('Capcha presence on method, need to wait some time')
            except AssertionError:
                pass
