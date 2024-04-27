import allure
from allure_commons.types import AttachmentType
from curlify import to_curl
import logging
import json
from requests import Response


def add_screenshot(browser):
    png = browser.driver.get_screenshot_as_png()
    allure.attach(body=png, name='screenshot', attachment_type=AttachmentType.PNG, extension='.png')


def add_logs(browser):
    log = "".join(f'{text}\n' for text in browser.driver.get_log(log_type='browser'))
    allure.attach(log, 'browser_logs', AttachmentType.TEXT, '.log')


def add_html(browser):
    html = browser.driver.page_source
    allure.attach(html, 'page_source', AttachmentType.HTML, '.html')


def add_video(browser):
    video_url = "https://selenoid.autotests.cloud/video/" + browser.driver.session_id + ".mp4"
    html = "<html><body><video width='100%' height='100%' controls autoplay><source src='" \
           + video_url \
           + "' type='video/mp4'></video></body></html>"
    allure.attach(html, 'video_' + browser.driver.session_id, AttachmentType.HTML, '.html')


def request_response_logger(response: Response):
    with allure.step(f'{response.request.method} {response.request.url}'):
        curl = to_curl(response.request)
        logging.info(curl)
        logging.info(f'status code: {response.status_code}')
        allure.attach(body=curl, name='curl', attachment_type=allure.attachment_type.TEXT, extension='txt')

        try:
            allure.attach(body=json.dumps(response.json(), indent=4), name='response',
                          attachment_type=allure.attachment_type.JSON, extension='json')
        except json.JSONDecodeError:
            if response.text:
                allure.attach(body=response.text, name='response',
                              attachment_type=allure.attachment_type.TEXT, extension='txt')
            else:
                # allure.attach(body=None, name='response', attachment_type=allure.attachment_type.TEXT, extension='txt')
                pass
        return response
