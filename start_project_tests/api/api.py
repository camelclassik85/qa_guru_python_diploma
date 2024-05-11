import allure
import requests
from start_project_tests.test_data.constants import ApiUrl, web_apikey
from start_project_tests.test_data.users import User
from start_project_tests.utils.allure_attach import request_response_logger


class ApiCall:

    @staticmethod
    def api_request(base_api_url, endpoint, method, json=None, params=None, headers=None, cookies=None):
        url = f"{base_api_url}{endpoint}"
        response = requests.request(method, url, json=json, params=params, headers=headers, cookies=cookies)
        request_response_logger(response)
        return response

    def add_to_favorites(self, user: User, content_uid: str):
        with allure.step(f'Add to favorites content {content_uid}'):
            params = {"apikey": web_apikey}
            endpoint = ApiUrl.favorites_endpoint + '/' + user.default_profile_id
            json = {"product_id": content_uid}
            cookies = {"auth": user.auth}
            self.api_request(
                base_api_url=ApiUrl.base_api_url,
                endpoint=endpoint,
                method="POST",
                json=json,
                params=params,
                cookies=cookies)

    def delete_from_favorites(self, user: User, content_uid: str):
        with allure.step(f'Delete from favorites content {content_uid}'):
            params = {"apikey": web_apikey}
            endpoint = ApiUrl.favorites_endpoint + '/' + user.default_profile_id
            json = {"product_id": content_uid}
            cookies = {"auth": user.auth}
            self.api_request(
                base_api_url=ApiUrl.base_api_url,
                endpoint=endpoint,
                method="DELETE",
                json=json,
                params=params,
                cookies=cookies)


api_call = ApiCall()
