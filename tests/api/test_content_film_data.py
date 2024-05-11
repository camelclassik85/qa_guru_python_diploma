import allure
import pytest
from jsonschema import validate
from start.api.api import api_call
from start.test_data.constants import ApiUrl
from start.test_data.content import cheburashka
from start.schemas.content_film_data_schema import film_schema


@allure.epic('API tests')
@allure.feature('Content page film data')
@allure.story("Checking content page film data")
@pytest.mark.parametrize('film', [cheburashka])
def test_content_page_film_data_api(film):
    endpoint = "/web/watch/" + film.alias
    params = {"apikey": "a20b12b279f744f2b3c7b5c5400c4eb5",
              "locale": "ru",
              "content_lang": "ru"
              }

    response = api_call.api_request(ApiUrl.base_api_url, endpoint, "GET", params=params)

    with allure.step('Check status code = 200'):
        assert response.status_code == 200
    with allure.step(f'Check title {film.title}'):
        assert response.json()['title'] == film.title
    with allure.step(f'Check {film.cls} type'):
        assert response.json()['_cls'] == film.cls
    with allure.step(f'Check {film.uid} for correctness'):
        assert response.json()['uid'] == film.uid
    with allure.step(f'Check for_kids {film.for_kids} flag'):
        assert response.json()['for_kids'] == film.for_kids
    with allure.step('Validate Schema'):
        validate(response.json(), film_schema)
