import allure
import jsonschema
from allure_commons._allure import step
from allure_commons.types import Severity

from tests.conftest import get_facts_params, catfacts_api
from utils import load_schema


@allure.title('GET facts: Status code is 200')
@allure.label('owner', 'AngPawl')
@allure.tag('smoke tests')
@allure.severity(Severity.CRITICAL)
def test_get_facts_status_code_is_200():
    response = catfacts_api(url='/facts', method='get', params=get_facts_params)

    with step('Status code is 200'):
        assert (
            response.status_code == 200
        ), f"Status code {response.status_code} is incorrect"


@allure.title('GET facts: Response schema is valid')
@allure.label('owner', 'AngPawl')
@allure.tag('smoke tests')
@allure.severity(Severity.CRITICAL)
def test_get_facts_schema_is_valid():
    schema = load_schema('catfacts', 'get_fact.json')

    response = catfacts_api(url='/facts', method='get', params=get_facts_params)

    with step('Response schema is valid'):
        jsonschema.validate(response.json(), schema)


@allure.title('GET facts: Response time is less than 1 second')
@allure.label('owner', 'AngPawl')
@allure.tag('smoke tests')
@allure.severity(Severity.CRITICAL)
def test_get_facts_response_time_is_valid():
    response = catfacts_api(url='/facts', method='get', params=get_facts_params)

    with step('Response time is less than 1 second'):
        assert (
            response.elapsed.total_seconds() < 1
        ), f"Actual response time {response.elapsed.total_seconds()} is more than 1 second"


@allure.title('GET facts: Response headers are not empty and have correct values')
@allure.label('owner', 'AngPawl')
@allure.tag('smoke tests')
@allure.severity(Severity.CRITICAL)
def test_headers_are_valid():
    response = catfacts_api(url='/facts', method='get', params=get_facts_params)

    with step('Response headers are not empty and have correct values'):
        assert response.headers, "Response headers are empty"
        assert (
            response.headers['Content-Type'] == 'application/json'
        ), f"Header Content-Type value is incorrect: {response.headers['Content-Type']}"
        assert (
            response.headers['Cache-Control'] == 'no-cache, private'
        ), f"Header Cache-Control value is incorrect: {response.headers['Cache-Control']}"
        assert (
            response.headers['Access-Control-Allow-Origin'] == '*'
        ), f"Header Access-Control-Allow-Origin value is incorrect: {response.headers['Access-Control-Allow-Origin']}"
