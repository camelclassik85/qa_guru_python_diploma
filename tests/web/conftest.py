import os
import allure
import pytest
from dotenv import load_dotenv
from selene import browser
from selenium import webdriver
from start.constants import web_base_url, WebDriverDefaults, TIMEOUT
from start.utils import allure_attach
from start.utils.resource import path


@allure.step('Select variables according command line')
def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store")
    parser.addoption("--browser_version", action="store")
    parser.addoption("--context", action="store")


@pytest.fixture(scope='session', autouse=True)
@allure.step('Load env file')
def load_env():
    dotenv_path = path('.env')
    if os.path.exists(dotenv_path):
        load_dotenv(dotenv_path=dotenv_path)
    else:
        load_dotenv()


@pytest.fixture
def context(request):
    context = request.config.getoption("--context")
    context = context if context != '' \
        else WebDriverDefaults.default_context
    return context.lower()


@pytest.fixture
def browser_name(request):
    browser_name = request.config.getoption("--browser_name")
    browser_name = browser_name if browser_name != '' \
        else WebDriverDefaults.default_browser_name
    return browser_name.lower()


@pytest.fixture
def browser_version(request):
    browser_version = request.config.getoption("--browser_version")
    browser_version = browser_version if browser_version != ''\
        else WebDriverDefaults.default_browser_version
    return browser_version


@pytest.fixture(scope="function", autouse=True)
def browser_config(context, browser_name, browser_version):
    with allure.step('Browser driver creation'):
        from config import web_config

        if context == 'web_selenoid':
            with allure.step('Selenoid driver creation'):
                options = web_config.web_driver_options(
                    context=context,
                    browser_name=browser_name,
                    browser_version=browser_version
                    )

                driver = webdriver.Remote(
                    command_executor=f"https://{web_config.selenoid_login}:"
                                     f"{web_config.selenoid_password}"
                                     f"@selenoid.autotests.cloud/wd/hub",
                    options=options)

                browser.config.driver = driver

        elif context == 'web_local':

            if browser_name == 'firefox':
                with allure.step('Firefox local driver options load'):
                    browser.config.driver_options = webdriver.FirefoxOptions()

            else:
                with allure.step('Chrome local driver options will load by default'):
                    pass

        with allure.step('Add base url, resolution and timeout to browser config'):
            browser.config.base_url = web_base_url
            browser.config.window_height = 1080
            browser.config.window_width = 1920
            browser.config.timeout = TIMEOUT

        yield

        with allure.step('Add screenshot'):
            allure_attach.add_screenshot(browser)
        with allure.step('Add html'):
            allure_attach.add_html(browser)

    if browser_name == WebDriverDefaults.default_browser_name:
        with allure.step('Add logs'):
            allure_attach.add_logs(browser)

    if context == WebDriverDefaults.default_context:
        with allure.step('Add video'):
            allure_attach.add_video(browser)

    browser.quit()
