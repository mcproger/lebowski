import json

import httpx
import pytest

from tinkoff.http_client import TinkoffHttpClient, USER_AGENT, TinkoffAPIRequestError


@pytest.fixture()
def client(mocker):
    return TinkoffHttpClient()


@pytest.fixture()
def mocked_httpx(mocker):
    return mocker.patch('tinkoff.http_client.httpx.request')


@pytest.mark.parametrize(
    ('headers', 'expected_value'),
    [
        (
            None,
            {
                'authority': 'www.tinkoff.ru',
                'user-agent': USER_AGENT,
                'content-type': 'application/x-www-form-urlencoded',
                'accept': '*/*',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-mode': 'cors',
                'sec-fetch-dest': 'empty',
                'referer': 'https://www.tinkoff.ru/login/',
                'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8,ru;q=0.7',
            },
        ),
        (
            {'X-CUSTOME-HEADER': 'TEST'},
            {
                'authority': 'www.tinkoff.ru',
                'user-agent': USER_AGENT,
                'content-type': 'application/x-www-form-urlencoded',
                'accept': '*/*',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-mode': 'cors',
                'sec-fetch-dest': 'empty',
                'referer': 'https://www.tinkoff.ru/login/',
                'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8,ru;q=0.7',
                'X-CUSTOME-HEADER': 'TEST',
            },
        ),
    ],
)
def test_properly_make_request_call(client, mocked_httpx, headers, expected_value):
    client.make_request('GET', url='https://test.com', headers=headers)

    mocked_httpx.assert_called_once_with(
        'get',
        'https://test.com',
        headers=expected_value,
        data=None,
    )


def test_handle_tinkoff_error_response(client, httpx_mock):
    def error_response(request, ext):
        raise httpx.RequestError(message='Error from service', request=request)

    httpx_mock.add_callback(error_response)

    with pytest.raises(TinkoffAPIRequestError):
        client.make_request('GET', url='https://test.com')


def test_handle_invalid_json_response_from_tinkoff(client, httpx_mock):
    def invalid_response(request, ext):
        raise json.JSONDecodeError(msg='', doc='', pos=1)

    httpx_mock.add_callback(invalid_response)

    with pytest.raises(TinkoffAPIRequestError):
        client.make_request('GET', url='https://test.com')
