import allure
import pytest
from jsonschema import validate
from start.api.api import api_call
from start.test_data.constants import ApiUrl
from start.test_data.content import chyornaya_vesna
from start.schemas.content_series_data_schema import series_schema


@allure.epic('API tests')
@allure.feature('Content page series data')
@allure.story("Checking content page series data")
@pytest.mark.parametrize('series', [chyornaya_vesna])
def test_content_page_series_data_api(series):
    endpoint = "/web/watch/" + series.alias
    params = {"apikey": "a20b12b279f744f2b3c7b5c5400c4eb5",
              "locale": "ru",
              "content_lang": "ru"
              }

    response = api_call.api_request(ApiUrl.base_api_url, endpoint, "GET", params=params)

    with allure.step('Check status code = 200'):
        assert response.status_code == 200
    with allure.step(f'Check title {series.title}'):
        assert response.json()['title'] == series.title
    with allure.step(f'Check {series.cls} type'):
        assert response.json()['_cls'] == series.cls
    with allure.step(f'Check {series.uid} for correctness'):
        assert response.json()['uid'] == series.uid
    with allure.step(f'Check for_kids {series.for_kids} flag'):
        assert response.json()['for_kids'] == series.for_kids
    with allure.step(f'Check seasons  q-ty - {series.items_total}'):
        assert response.json()['items_total'] == series.items_total
    with allure.step('Validate Schema'):
        validate(response.json(), series_schema)
