import pytest


@pytest.fixture()
def tinkoff_http_client_factory(mocker):
    def _with_response(response):
        http_client = mocker.MagicMock()
        http_client.make_request.return_value = response
        return http_client
    return _with_response
