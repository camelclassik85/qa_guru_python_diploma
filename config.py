import os
from pydantic import BaseModel
from start.constants import TIMEOUT


class WebConfig(BaseModel):
    timeout: float = TIMEOUT
    selenoid_login: str = os.getenv('SELENOID_LOGIN')
    selenoid_password: str = os.getenv('SELENOID_PASSWORD')

    @staticmethod
    def web_driver_options(context, browser_name, browser_version):
        if browser_name == 'chrome':
            from selenium.webdriver.chrome.options import Options
        elif browser_name == 'firefox':
            from selenium.webdriver.firefox.options import Options
        else:
            raise ValueError("Absent driver browser_name")

        options = Options()

        if context == 'web_selenoid':
            selenoid_capabilities = {
                "browserName": browser_name,
                "browserVersion": browser_version,
                "selenoid:options": {
                    "enableVNC": True,
                    "enableVideo": True
                }
            }
            options.capabilities.update(selenoid_capabilities)

        return options


web_config = WebConfig()
