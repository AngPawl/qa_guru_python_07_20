import allure
import jsonschema
from allure_commons._allure import step
from allure_commons.types import Severity

from tests.conftest import post_new_user_params, reqres_api
from utils import load_schema


@allure.title('POST user: Status code is 201')
@allure.label('owner', 'AngPawl')
@allure.tag('smoke tests')
@allure.severity(Severity.CRITICAL)
def test_status_code_is_ok():
    response = reqres_api(url='/users', method='post', json=post_new_user_params)

    with step('Status code is 201'):
        assert (
            response.status_code == 201
        ), f"Status code {response.status_code} is incorrect"


@allure.title('POST user: Response schema is valid')
@allure.label('owner', 'AngPawl')
@allure.tag('smoke tests')
@allure.severity(Severity.CRITICAL)
def test_schema_is_valid():
    schema = load_schema('reqres', 'post_user.json')

    response = reqres_api(url='/users', method='post', json=post_new_user_params)

    with step('Response schema is valid'):
        jsonschema.validate(response.json(), schema)


@allure.title('POST user: Response data contains correct values')
@allure.label('owner', 'AngPawl')
@allure.tag('smoke tests')
@allure.severity(Severity.CRITICAL)
def test_response_data_is_valid():
    response = reqres_api(url='/users', method='post', json=post_new_user_params)

    with step('Response data contains correct values'):
        assert (
            response.json()['name'] == post_new_user_params['name']
        ), f"Response data contains incorrect value: {response.json()['name']}"
        assert (
            response.json()['job'] == post_new_user_params['job']
        ), f"Response data contains incorrect value: {response.json()['job']}"
