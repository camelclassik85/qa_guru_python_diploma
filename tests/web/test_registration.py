import allure
from start.models.page_factory import pages
from start.utils.generators import random_email_generate, random_password_generate


@allure.epic('Registration tests')
@allure.feature('Registration by email')
def test_registration_email():
    email = random_email_generate()
    password = random_password_generate()
    pages.signup_page.open_signup_page()
    pages.signup_page.check_signup_page_title()
    pages.cookie_popup.cookie_accept()
    pages.signup_page.fill_registration_form(email=email, password=password)
    pages.signup_page.accept_policy()
    pages.signup_page.signup_button_click()
    pages.signup_page.check_capcha()
    pages.account_page.open_account_page()
    pages.account_page.check_user_email(email=email)
