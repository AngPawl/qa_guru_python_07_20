import allure
import jsonschema
from allure_commons._allure import step
from allure_commons.types import Severity

from tests.conftest import (
    register_new_valid_user_params,
    register_new_invalid_user_params,
    reqres_api,
)
from utils import load_schema


@allure.title('Register user: Request returns correct response')
@allure.label('owner', 'AngPawl')
@allure.tag('smoke tests')
@allure.severity(Severity.CRITICAL)
def test_successful_registration():
    schema = load_schema('reqres', 'register_user.json')

    response = reqres_api(
        url='/register',
        method='post',
        json=register_new_valid_user_params,
    )

    with step('Response schema is valid'):
        jsonschema.validate(response.json(), schema)

    with step('Status code is 200'):
        assert (
            response.status_code == 200
        ), f"Status code {response.status_code} is incorrect"


@allure.title('Register user: Request raises an error')
@allure.label('owner', 'AngPawl')
@allure.tag('smoke tests')
@allure.severity(Severity.CRITICAL)
def test_unsuccessful_registration():
    response = reqres_api(
        url='/register',
        method='post',
        json=register_new_invalid_user_params,
    )

    with step('Status code is 400'):
        assert (
            response.status_code == 400
        ), f"Status code {response.status_code} is incorrect"

    with step('Error message is correct'):
        assert (
            response.json()['error'] == 'Missing password'
        ), f"Error message {response.json()['error']} is incorrect"
