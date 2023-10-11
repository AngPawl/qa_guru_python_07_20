import json
import allure
from allure_commons._allure import step
from allure_commons.types import AttachmentType
from curlify import to_curl
from requests import sessions

get_list_users_params = {'page': 1, 'per_page': 1}
post_new_user_params = {"name": "John Doe", "job": "developer"}
register_new_valid_user_params = {"email": "eve.holt@reqres.in", "password": "pistol"}
register_new_invalid_user_params = {"email": "sydney@fife"}
get_facts_params = {'max_length': 1, 'limit': 1}


def retrieve_request(full_url, method, **kwargs):
    with sessions.Session() as session:
        response = session.request(method=method, url=full_url, **kwargs)

        message = to_curl(response.request)
        allure.attach(
            body=message.encode('utf8'),
            name='Request cURL',
            attachment_type=AttachmentType.TEXT,
            extension='txt',
        )
        try:
            allure.attach(
                body=json.dumps(response.json(), indent=4).encode('utf8'),
                name='Response JSON',
                attachment_type=AttachmentType.JSON,
                extension='json',
            )
        except:
            allure.attach(
                body=response.content,
                name='Response',
                attachment_type=AttachmentType.TEXT,
                extension='txt',
            )
    return response


def reqres_api(url, method, **kwargs):
    base_url = 'https://reqres.in/api'
    full_url = base_url + url

    with step(f'Send request {method.upper()} {full_url}'):
        response = retrieve_request(full_url, method, **kwargs)

    return response


def catfacts_api(url, method, **kwargs):
    base_url = 'https://catfact.ninja'
    full_url = base_url + url

    with step(f'Send request {method.upper()} {full_url}'):
        response = retrieve_request(full_url, method, **kwargs)

    return response
