import allure
import jsonschema
from allure_commons._allure import step
from allure_commons.types import Severity

from tests.conftest import get_list_users_params, reqres_api
from utils import load_schema


@allure.title('GET list_users: Status code is 200')
@allure.label('owner', 'AngPawl')
@allure.tag('smoke tests')
@allure.severity(Severity.CRITICAL)
def test_status_code_is_ok():
    response = reqres_api(url='/users', method='get', params=get_list_users_params)

    with step('Status code is 200'):
        assert (
            response.status_code == 200
        ), f"Status code {response.status_code} is incorrect"


@allure.title('GET list_users: Response schema is valid')
@allure.label('owner', 'AngPawl')
@allure.tag('smoke tests')
@allure.severity(Severity.CRITICAL)
def test_schema_is_valid():
    schema = load_schema('reqres', 'get_users.json')

    response = reqres_api(url='/users', method='get', params=get_list_users_params)

    with step('Response schema is valid'):
        jsonschema.validate(response.json(), schema)


@allure.title('GET list_users: Per_page param returns correct value')
@allure.label('owner', 'AngPawl')
@allure.tag('smoke tests')
@allure.severity(Severity.CRITICAL)
def test_response_with_per_page_param_is_valid():
    response = reqres_api(url='/users', method='get', params=get_list_users_params)

    with step('Per_page param returns correct value'):
        assert (
            response.json()['per_page'] == 1
        ), f"Per page param returned incorrect value: {response.json()['per_page']}"


@allure.title('GET list_users: Response time is less than 1 second')
@allure.label('owner', 'AngPawl')
@allure.tag('smoke tests')
@allure.severity(Severity.CRITICAL)
def test_response_time_is_valid():
    response = reqres_api(url='/users', method='get', params=get_list_users_params)

    with step('Response time is less than 1 second'):
        assert (
            response.elapsed.total_seconds() < 1
        ), f"Actual response time {response.elapsed.total_seconds()} is more than 1 second"


@allure.title('GET list_users: Response headers are not empty and have correct values')
@allure.label('owner', 'AngPawl')
@allure.tag('smoke tests')
@allure.severity(Severity.CRITICAL)
def test_headers_are_valid():
    response = reqres_api(url='/users', method='get', params=get_list_users_params)

    with step('Response headers are not empty and have correct values'):
        assert response.headers, "Response headers are empty"
        assert (
            response.headers['Content-Type'] == 'application/json; charset=utf-8'
        ), f"Header Content-Type value is incorrect: {response.headers['Content-Type']}"
        assert (
            response.headers['Connection'] == 'keep-alive'
        ), f"Header Connection value is incorrect: {response.headers['Connection']}"
        assert (
            response.headers['Cache-Control'] == 'max-age=14400'
        ), f"Header Cache-Control value is incorrect: {response.headers['Cache-Control']}"
        assert (
            response.headers['Access-Control-Allow-Origin'] == '*'
        ), f"Header Access-Control-Allow-Origin value is incorrect: {response.headers['Access-Control-Allow-Origin']}"
