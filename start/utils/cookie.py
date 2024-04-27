import logging
from selene import browser
from start.data.users import User


def add_auth_cookie_to_browser(user: User, url: str = '/'):
    browser.open(url)
    browser.driver.add_cookie({"name": "auth", "value": user.auth})
    # logging.info(browser.driver.get_cookie('auth'))
    browser.driver.refresh()
