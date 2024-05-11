import os
import allure
import pytest
from dotenv import load_dotenv
from selene import browser
from selenium import webdriver
from start_project_tests.test_data.constants import web_base_url, WebDriverDefaults, TIMEOUT
from start_project_tests.utils import allure_attach
from start_project_tests.utils.resource import path


@allure.step('Select variables according command line')
def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default='')
    parser.addoption("--browser_version", action="store", default='')
    parser.addoption("--context", action="store", default='')


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


@pytest.fixture
def module_name(request):
    name = request.node.module.__name__
    return name


@pytest.fixture(scope="function", autouse=True)
def browser_config(context, browser_name, browser_version, module_name):
    if 'api' in module_name:
        with allure.step('Api tests - no browser config'):
            yield
    else:
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

        allure_attach.add_screenshot(browser)
        allure_attach.add_html(browser)
        allure_attach.add_logs(browser, browser_name)
        allure_attach.add_video(browser, context)

        browser.quit()
