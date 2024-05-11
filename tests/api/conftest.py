import pytest


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default='')
    parser.addoption("--browser_version", action="store", default='')
    parser.addoption("--context", action="store", default='')


@pytest.fixture()
def base_api_url():
    return 'https://api.start.ru'
