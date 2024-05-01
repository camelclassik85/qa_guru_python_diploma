import allure
from jsonschema import validate
from start.api.api import api_call
from start.constants import ApiUrl
from start.data.content import lermontov
from start.schemas.search_result_data_schema import search_result


@allure.title("Checking 1 item search result data")
def test_search_one_item_result_data_api():
    endpoint = "/v2/search"
    params = {"apikey": "a20b12b279f744f2b3c7b5c5400c4eb5",
              "locale": "ru",
              "limit": 40,
              "q": lermontov.title.lower(),
              "offset": 0
              }

    response = api_call.api_request(ApiUrl.base_api_url, endpoint, "GET", params=params)

    with allure.step('Check status code = 200'):
        assert response.status_code == 200
    with allure.step(f'Check title {lermontov.title}'):
        assert response.json()['items'][0]['title'] == lermontov.title
    with allure.step(f'Check {lermontov.cls} type'):
        assert response.json()['items'][0]['_cls'] == lermontov.cls
    with allure.step(f'Check {lermontov.uid} for correctness'):
        assert response.json()['items'][0]['uid'] == lermontov.uid
    with allure.step(f'Check original query {params["q"]} for correctness'):
        assert response.json()['original_query'] == params["q"]
    with allure.step(f'Check status FOUND'):
        assert response.json()['status'] == "FOUND"
    with allure.step(f'Check result q-ty 1'):
        assert response.json()['meta']['items_count'] == 1
    with allure.step('Validate Schema'):
        validate(response.json(), search_result)
