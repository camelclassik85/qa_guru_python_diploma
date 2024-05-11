import allure
from start_project_tests.test_data.users import authorized_user
from start_project_tests.models.page_factory import pages


@allure.epic('Authorization tests')
@allure.feature('Authorization by email')
def test_authorization_email():
    pages.signin_page.open_signin_page()
    pages.signin_page.check_signin_page_title()
    pages.cookie_popup.cookie_accept()
    pages.signin_page.fill_authorization_form(
        email=authorized_user.email,
        password=authorized_user.password
        )
    pages.signin_page.signin_button_click()
    pages.signin_page.check_capcha()
    pages.account_page.open_account_page()
    pages.account_page.check_user_email(email=authorized_user.email)
